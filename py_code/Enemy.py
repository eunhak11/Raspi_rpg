import numpy as np

class Enemy:
    def __init__(self, spawn_position, type):
        self.appearance = 'rectangle'
        self.state = 'alive'

        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.direction = {'up' : False, 'down' : False, 'left' : False, 'right' : False}
        self.outline = "#00FF00"

        if type == 0:       # 타입에 따른 속도, 데미지 정의
            self.speed = 4
            self.damage = 2
        else:
            self.speed = 2
            self.damage = 6

        self.direction['left'] = True

    def enemy_move(self):
        self.position[0] -= self.speed
        self.position[2] -= self.speed