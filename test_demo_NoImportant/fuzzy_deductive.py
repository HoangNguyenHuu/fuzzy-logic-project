import xlrd

from defuzzification.speed_calculator import calculate_speed
from fuzzification.fuzzy_dependency import *


# read light rule
def read_light_rule():
    light_rule = []
    with xlrd.open_workbook('media/fuzzy_rule.xlsx') as book:
        sheet = book.sheet_by_index(1)

        distance = [x for x in sheet.col_values(1)]
        light_status = [y for y in sheet.col_values(2)]
        angle = [z for z in sheet.col_values(3)]
        speed = [t for t in sheet.col_values(4)]

        for i in range(1, len(distance)):
            light_rule.append((distance[i].strip(), light_status[i].strip(), angle[i].strip(), speed[i].strip()))

    return light_rule


light_rules = read_light_rule()


# find rule fit with distance, light_status, angle
def find_light_rule(distance_dependency, light_dependency, angle_dependency):
    for rule in light_rules:
        if distance_dependency[0] == rule[0] and light_dependency[0] == rule[1] and angle_dependency[0] == rule[2]:
            return [distance_dependency, light_dependency, angle_dependency, rule[3]]
    return None


# calculate arguments for integral function
def cal_function_arguments(rule_found):
    min_arg = min(rule_found[0][1], rule_found[1][1], rule_found[2][1])
    label = rule_found[3]
    new_arguments = []
    if label == "Fast":
        if min_arg == 1:
            new_arguments.append(1.5)
        elif 0 < min_arg < 1:
            new_arguments.append(0.5 * min_arg + 1)
    if label == "Slower":
        if min_arg == 1:
            new_arguments.append(1)
        elif 0 < min_arg < 1:
            new_arguments.append(0.5 * min_arg + 0.5)
            new_arguments.append(1.5 - 0.5 * min_arg)
    if label == "Slow":
        if min_arg == 1:
            new_arguments.append(0.5)
        elif 0 < min_arg < 1:
            new_arguments.append(0.5 * min_arg)
            new_arguments.append(1 - 0.5 * min_arg)
    if label == "Stop":
        if min_arg == 1:
            new_arguments.append(0)
        elif 0 < min_arg < 1:
            new_arguments.append(0.01 - 0.01 * min_arg)
    return [new_arguments, label, min_arg]


# def fuzzy_deductive(distance, light_status, angle):
#     distance_dependencies = cal_distance_dependencies(distance)
#     light_dependencies = cal_lamp_dependencies(light_status)
#     angle_dependencies = cal_angle_dependencies(angle)
#     speed_total = 0
#     number_rule = 0
#     for distance_dependency in distance_dependencies:
#         for light_dependency in light_dependencies:
#             for angle_dependency in angle_dependencies:
#                 # dis_label = distance_dependency[0]
#                 # lig_label = light_dependency[0]
#                 # ang_label = angle_dependency[0]
#                 rule_found = find_light_rule(distance_dependency, light_dependency, angle_dependency)
#                 # print("Rule found: ", rule_found)
#                 arguments_func = cal_function_arguments(rule_found)
#                 # print("Argument function: ", arguments_func)
#                 integrate = calculate_integrate(arguments_func)
#                 # print("Integrate: ", integrate)
#                 speed_total += integrate
#                 number_rule += 1
#                 # print()
#
#     speed_average = round(speed_total / number_rule, 2)
#     return speed_average
