import pygame

from graphic.loader import load_image


class Stone(pygame.sprite.Sprite):
    STONE_IMG = "stone3.png"
    HIDE = 0
    VIEW = 1

    def __init__(self, init_x, init_y, dir, status):
        pygame.sprite.Sprite.__init__(self)

        self.status = status

        self.x = init_x
        self.y = init_y

        self.dir = dir
        self.image = self.set_stone_img()
        self.rect = self.image.get_rect()
        self.rect_w = self.rect.size[0]
        self.rect_h = self.rect.size[1]
        self.rect.center = self.x, self.y

    @staticmethod
    def set_stone_img():
        return load_image(Stone.STONE_IMG)

    def switch_status(self, x, y):
        if self.status == Stone.HIDE:
            self.status = Stone.VIEW
            self.x = x
            self.y = y
        elif self.status == Stone.VIEW:
            self.status = Stone.HIDE
            self.x = 200
            self.y = 200
        pass

    # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.center = self.x - cam_x + 600, self.y - cam_y + 300
