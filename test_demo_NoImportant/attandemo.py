from fuzzification.fuzzy_dependency import *

PI = math.pi

MAP_NAVS = [(600, 350), (690, 370), (810, 385), (910, 380), (1030, 345),
            (1120, 315), (1385, 325), (1540, 375), (1740, 450), (1890, 520),
            (2035, 565), (2230, 640), (2435, 685), (2585, 730), (2735, 790),
            (2840, 890), (2840, 1030), (2748, 1134), (2610, 1110),
            (2455, 1050),
            (2332, 1034), (2140, 1076), (1970, 1125), (1698, 1166),
            (1476, 1138),
            (1256, 1115), (1000, 1130), (756, 1205), (544, 1282), (458, 1398),
            (404, 1540), (410, 1585)]

FINISH_INDEX = 30

TRAFFIC_LAMP_POS = [6, 12, 23, 29]


def calculate_angle(point_x, point_y, target_x, target_y):
    neg_dir = math.atan2(point_y - target_y, target_x - point_x) * 180 / PI
    # if neg_dir < 0:
    #     neg_dir += 360
    # if neg_dir < 90:
    #     dir = neg_dir + 360 - 90
    # else:
    #     dir = neg_dir - 90
    return neg_dir


my_dir = calculate_angle(1, 1, 1, 2)
print(my_dir)

# print(distance_near_dependency(300))
# print(distance_medium_dependency(350))
# print(distance_far_dependency(250))
# print(angle_small_dependency(9))
# print(angle_medium_dependency(9))
# print(angle_big_dependency(16))

# print(lamp_red_dependency(8))
# print(lamp_less_red_dependency(8))
# print(lamp_green_dependency(8))
# print(lamp_less_green_dependency(5))

# print(cal_distance_dependencies(380))
# print(cal_angle_dependencies(12))
# print(cal_lamp_dependencies((8, 2)))

rule_found = [('Far', 1.0), ('Green', 0.8), ('Small', 1.0), 'Fast']
arguments = rule_found[0:(len(rule_found) - 1)]
m = [x[1] for x in arguments]
print (m)
print (min(m))