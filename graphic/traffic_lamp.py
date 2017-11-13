import random

import pygame

from graphic.loader import load_image


class TrafficLamp(pygame.sprite.Sprite):
    # Lamp status
    GREEN = 1
    RED = 2

    # time out for lamp switch from GREEN to RED and backward
    TIMEOUT = 600
    LAMP_RED_IMG = "traffic_lamp_red.png"
    LAMP_GREEN_IMG = "traffic_lamp_green.png"

    def __init__(self, init_x, init_y, dir, numberical_order, status=None, remaining_time=None):
        pygame.sprite.Sprite.__init__(self)

        if status is None:
            status = random.randint(1, 2)
        if remaining_time is None:
            remaining_time = random.randint(5, 15) * 60

        print(status, " - ", int(remaining_time / 60))
        # current status of traffic lamp
        self.status = status
        # time remaining before traffic lamp change status
        self.remaining_time = remaining_time
        print(self.remaining_time)
        # traffic lamp position
        self.x = init_x
        self.y = init_y
        # traffic lamp direction (0, 90, 180, 270)
        self.dir = dir
        self.image = self.set_traffic_lamp_img()
        self.rect = self.image.get_rect()
        self.rect_w = self.rect.size[0]
        self.rect_h = self.rect.size[1]
        self.rect.center = self.x, self.y
        self.numberical_order = numberical_order

    def __init__(self, traffic_coordinates, status=None, remaining_time=None):
        pygame.sprite.Sprite.__init__(self)

        if status is None:
            status = random.randint(1, 2)
        if remaining_time is None:
            remaining_time = random.randint(5, 15) * 60

        print(status, " - ", int(remaining_time / 60))
        # current status of traffic lamp
        self.status = status
        # time remaining before traffic lamp change status
        self.remaining_time = remaining_time
        print(self.remaining_time)
        # traffic lamp position
        self.x = traffic_coordinates[0]
        self.y = traffic_coordinates[1]
        # traffic lamp direction (0, 90, 180, 270)
        self.dir = traffic_coordinates[2]
        self.image = self.set_traffic_lamp_img()
        self.rect = self.image.get_rect()
        self.rect_w = self.rect.size[0]
        self.rect_h = self.rect.size[1]
        self.rect.center = self.x, self.y
        self.numberical_order = traffic_coordinates[3]


    def set_traffic_lamp_img(self):
        if self.status == TrafficLamp.RED:
            return load_image(TrafficLamp.LAMP_RED_IMG)
        elif self.status == TrafficLamp.GREEN:
            return load_image(TrafficLamp.LAMP_GREEN_IMG)

    def switch_status(self):
        if self.status == TrafficLamp.RED:
            self.pre_status = TrafficLamp.RED
            self.status = TrafficLamp.GREEN
            self.remaining_time = 900
        elif self.status == TrafficLamp.GREEN:
            self.pre_status = TrafficLamp.GREEN
            self.status = TrafficLamp.RED
            self.remaining_time = 1200
        self.image = self.set_traffic_lamp_img()
        self.rect = self.image.get_rect()
        pass

    # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.center = self.x - cam_x + 600, self.y - cam_y + 300
        self.remaining_time -= 1
        if self.remaining_time == 0:
            self.switch_status()

    def render(self, screen):
        lamp_font = pygame.font.SysFont(None, 25)
        # render text
        label = lamp_font.render(str(int(self.remaining_time / 60)), 1, (255, 255, 255))
        screen.blit(label, (self.rect.center[0] + 30, self.rect.center[1]))

        return int(self.remaining_time / 60), self.status, self.numberical_order
