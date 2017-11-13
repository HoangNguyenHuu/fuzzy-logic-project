from defuzzification.speed_calculator import calculate_speed
from fuzzification.fuzzy_dependency import cal_angle_dependencies, cal_distance_dependencies
from fuzzy_rule_base.read_rule import read_impediment_rule


class ImpedimentDeductive:
    def __init__(self):
        self.rules = read_impediment_rule()

    def find_light_rule(self, distance_dependency, angle_dependency):
        for rule in self.rules:
            if distance_dependency[0] == rule[0] and angle_dependency[0] == rule[1]:
                return [distance_dependency, angle_dependency, rule[2]]
        return None

    # calculate arguments for integral function
    def cal_function_arguments(self, distance_dependency, angle_dependency):
        for rule in self.rules:
            if distance_dependency[0] == rule[0] and angle_dependency[0] == rule[1]:
                dependencies = [distance_dependency[1], angle_dependency[1]]
                min_arg = min(dependencies)
                label = rule[2]
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

        return [0, "Stop", 1]

    def fuzzy_deductive(self, distance, angle):
        distance_dependencies = cal_distance_dependencies(distance)
        angle_dependencies = cal_angle_dependencies(angle)
        speed_total = 0
        weight_total = 0
        for distance_dependency in distance_dependencies:
            for angle_dependency in angle_dependencies:
                # dis_label = distance_dependency[0]
                # lig_label = light_dependency[0]
                # ang_label = angle_dependency[0]
                # rule_found = self.find_light_rule(distance_dependency, light_dependency, angle_dependency)
                # print("Rule found: ", rule_found)
                arguments_func = self.cal_function_arguments(distance_dependency, angle_dependency)
                # print("Argument function: ", arguments_func)
                speed, weight = calculate_speed(arguments_func)
                # print("Integrate: ", integrate)
                speed_total += speed * weight
                weight_total += weight
                # print()

        speed_average = round(speed_total / weight_total, 2)
        return speed_average
