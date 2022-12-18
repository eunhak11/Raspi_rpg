import PIL
from PIL import Image, ImageDraw, ImageFont
import os
import time
import random
import cv2 as cv
import numpy as np
from colorsys import hsv_to_rgb
from Enemy import Enemy
from Bullet import Bullet
from Character import Character
from Joystick import Joystick
import ImgRss as rss 

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)
    # 잔상이 남지 않는 코드 & 대각선 이동 가능
    
    my_turret = Character(joystick.width, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
    
    enemys_list = []
    bullets = []
    start_time = time.time()   # 게임을 시작하는 순간 부터 시간을 기록.
    count = 0
    while True:
        # enemy_list의 인자 개수가 5개보다 작은 경우 계속 새로운 enemy를 생성.
        if len(enemys_list) < 5:
            enemys_list.append(Enemy((240, random.randrange(80,220,10)), random.randint(0,2)))
        
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True

        if not joystick.button_A.value: # A pressed
            bullet = Bullet(my_turret.center, command)
            bullets.append(bullet)

        if not joystick.button_B.value: # A pressed
            bullet = Bullet(my_turret.center, command)
            bullets.append(bullet)

        my_turret.move(command)
        for bullet in bullets:
            bullet.collision_check(enemys_list)
            bullet.move()

            
        # 배경 그리기
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 0, 100))
        # 아군 터렛 그리기
        my_draw.rectangle(tuple(my_turret.position), outline = my_turret.outline, fill = (0, 0, 0))
        
        # 적 구현
        i=0
        for enemy in enemys_list:
            if enemy.state != 'die':    # 적이 살아있는 경우

                my_draw.rectangle(tuple(enemy.position), outline = enemy.outline, fill = (255, 0, 0))

                if enemy.position[0] < 40:  # 적이 살아서 목표 지점에 도달한 경우
                    count += enemy.damage   # 점수에서 적의 타입 별로 점수 차감
                    print(count)
                    del enemys_list[i]      # 적 객체를 삭제한다.

                Enemy.enemy_move(enemys_list[i])    # Enemy의 move 메소드를 구현해 적들을 움직인다.
                i += 1
            else:                       # 적이 죽은 경우
                del enemys_list[i]
            

        j = 0
        for bullet in bullets:
            if bullet.state != 'hit':
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0, 0, 255))
            elif bullet.position[0] > 240:
                del bullets[j]
        #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        joystick.disp.image(my_image)
        

if __name__ == '__main__':
    main()