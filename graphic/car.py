import math

import inference_engine.light_deductive as light_deductive
import graphic.maps as maps
import pygame
from graphic.maps import MAP_NAVS, TRAFFIC_LAMP_POS

from graphic.loader import load_image
from inference_engine import impediment_deductive

PI = math.pi
max_a = 0.1


# Rotate car.
def rot_center(image, rect, angle):
    """rotate an image while keeping itscenter"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


def calculate_angle(point_x, point_y, target_x, target_y):
    neg_dir = math.atan2(point_y - target_y, target_x - point_x) * 180 / PI
    if neg_dir < 0:
        neg_dir += 360
    if neg_dir < 90:
        dir = neg_dir + 360 - 90
    else:
        dir = neg_dir - 90
    return dir


def calculate_abs_angle(point_x, point_y, target_x, target_y):
    dir = math.atan2(point_y - target_y, target_x - point_x) * 180 / PI
    return dir


# define car as Player
class Car(pygame.sprite.Sprite):
    # init_x, init_y: center of image
    def __init__(self, init_x, init_y, init_dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("car_player.png")
        self.rect = self.image.get_rect()
        self.rect_w = self.rect.size[0]
        self.rect_h = self.rect.size[1]
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.x = init_x
        self.y = init_y
        self.rect.topleft = 600 - self.rect_w / 2, 300 - self.rect_h / 2

        self.dir = init_dir
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)
        self.speed = 0.0

        self.maxspeed = 3
        self.minspeed = -1.85
        self.acceleration = 0.095
        self.deacceleration = 0.12
        self.softening = 0.04
        self.steering = 1.60
        self.dir_factor = 0.05
        self.current_nav_index = 0
        self.current_lamp_pos = 0
        self.light_deductive = light_deductive.LightDeductive()
        self.impediment_deductive = impediment_deductive.ImpedimentDeductive()

    # def impact(self):
    #     if self.speed > 0:
    #         self.speed = self.minspeed

    def accelerate(self):
        if self.speed < self.maxspeed:
            self.speed = self.speed + self.acceleration

    def stop(self):
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed

    # def set_dir(self, way_dir):
    #     self.dir = way_dir
    #     self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

    def deaccelerate(self):
        if self.speed > self.minspeed:
            self.speed > self.speed - self.deacceleration

    def steerleft(self):
        self.dir = self.dir + self.steering
        if self.dir > 360:
            self.dir = 0
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

    def steerright(self):
        self.dir = self.dir - self.steering
        if self.dir < 0:
            self.dir = 360
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

    def find_way_direction(self):
        next_nav_index = self.current_nav_index + 1
        next_nav_x, next_nav_y = MAP_NAVS[next_nav_index][0], MAP_NAVS[next_nav_index][1]
        return calculate_angle(self.x, self.y, next_nav_x, next_nav_y)

    def calculate_distance_lamp(self):
        for i in range(len(TRAFFIC_LAMP_POS)):
            pos = TRAFFIC_LAMP_POS[i]
            if self.current_nav_index < pos:
                distance_to_lamp = math.hypot(MAP_NAVS[pos][0] - self.x, MAP_NAVS[pos][1] - self.y)
                if self.current_lamp_pos != i:
                    self.current_lamp_pos = i

                return distance_to_lamp
        return 2000

    def calculate_distance_impediment(self, stone_status):
        if stone_status[0] == 0:
            return 2000
        pos = stone_status[1]
        distance_to_impediment = math.hypot(MAP_NAVS[pos][0] - self.x, MAP_NAVS[pos][1] - self.y)
        return distance_to_impediment

    def calculator_car_angle(self):
        current_dir = self.dir
        way_dir = self.find_way_direction()
        # print(current_dir, " :: ", way_dir)
        return abs(current_dir - way_dir)

    def update_map_nav_index(self):
        next_nav_index = self.current_nav_index + 1
        next_nav_x, next_nav_y = MAP_NAVS[next_nav_index][0], MAP_NAVS[next_nav_index][1]

        if math.hypot(self.x - next_nav_x, self.y - next_nav_y) < self.maxspeed:
            self.current_nav_index = next_nav_index

    def change_dir(self, target_dir):
        if abs(self.dir - target_dir) > 2:
            if self.dir > target_dir:
                angle = self.dir_factor * float(self.dir - target_dir)
                change_dir = angle if angle < 2 else 2
                self.dir -= change_dir
            else:
                angle = self.dir_factor * float(target_dir - self.dir)
                change_dir = angle if angle < 2 else 2
                self.dir += change_dir
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

    def update_acceleration(self, speed):
        off_set = speed - self.speed
        self.acceleration = off_set/10.0
        # if speed < 0.1:
        #     self.speed = speed
        #     return
        # if off_set > 0.1:
        #     self.speed += 0.1
        # elif off_set < -0.2:
        #     self.speed -= 0.2
        # else:
        #     self.speed = speed

    def update_speed(self):
        self.speed += self.acceleration

    def update(self, last_x, last_y, traffic_lamp_status, stone_status, flag):
        self.update_map_nav_index()
        # print("Current index: ", self.current_nav_index)
        if self.current_nav_index < maps.FINISH_INDEX:
            way_dir = self.find_way_direction()
            self.change_dir(way_dir)

            if (flag % 10) == 0:
                # distance_stone = self.calculate_distance_impediment(stone_status)
                angle_tmp = self.calculator_car_angle()

                stone_hide_view = stone_status[0]
                stone_pos = stone_status[1]
                if stone_hide_view == 1 and stone_pos <= TRAFFIC_LAMP_POS[self.current_lamp_pos]:
                    distance_stone = self.calculate_distance_impediment(stone_status)
                    speed_new = self.impediment_deductive.fuzzy_deductive(distance_stone, angle_tmp)
                    # print("Distance to Stone: ", distance_stone)

                    # self.speed = speed_new
                    # self.update_speed(speed_new)
                    self.update_acceleration(speed_new)
                    print("Stone - Speed: ", self.speed)
                    print("--------------------------------------------------------------------------")
                elif stone_hide_view == 1 and self.current_nav_index > TRAFFIC_LAMP_POS[self.current_lamp_pos]:
                    distance_stone = self.calculate_distance_impediment(stone_status)
                    speed_new = self.impediment_deductive.fuzzy_deductive(distance_stone, angle_tmp)
                    # print("Distance to Stone: ", distance_stone)
                    # self.speed = speed_new
                    # self.update_speed(speed_new)
                    self.update_acceleration(speed_new)
                    print("Stone - Speed: ", self.speed)
                    print("--------------------------------------------------------------------------")
                else:
                    distance_tmp = self.calculate_distance_lamp()

                    lamp_status_tmp = traffic_lamp_status[self.current_lamp_pos]
                    # print("current lamp pos: ", self.current_lamp_pos, ", status: ", lamp_status_tmp)
                    # print(distance_tmp, " - ", cal_distance_dependencies(distance_tmp))
                    # print(angle_tmp, " - ", cal_angle_dependencies(angle_tmp))
                    # print(lamp_status_tmp, " - ", cal_lamp_dependencies(lamp_status_tmp))

                    # light = "red"
                    # if lamp_status_tmp[1] == 1:
                    #     light = "green"

                    # print("lamp status: ", light, " - ", lamp_status_tmp[0], "s")
                    speed_new = self.light_deductive.fuzzy_deductive(distance_tmp, lamp_status_tmp, angle_tmp)
                    # self.speed = speed_new
                    # self.update_speed(speed_new)
                    self.update_acceleration(speed_new)
                    print("Traffic Lamp - Speed: ", self.speed)
                    print("--------------------------------------------------------------------------")
            self.update_speed()

        else:
            self.set_speed(0)
        self.x = self.x + self.speed * math.cos(math.radians(270 - self.dir))
        self.y = self.y + self.speed * math.sin(math.radians(270 - self.dir))
