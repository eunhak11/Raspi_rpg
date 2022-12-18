import numpy as np

# Character class를 정의한 파일
class Character:
    def __init__(self, width, height):  # 생성할 때 너비와 높이를 정해준다.
        self.appearance = 'rectangle'   # 사각형 모형으로 정의할 것   
        self.state = None           
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        # 총알 발사를 위한 캐릭터 중앙 점 추가
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#FFFFFF"        # 윤곽선

    def move(self, command = None):     # Character의 움직임을 정의하는 함수
        if command['move'] == False:    # move 상태가 아닌 경우
            self.state = None
            self.outline = "#FFFFFF" #검정색상 코드!
        
        else:
            self.state = 'move'         # move 상태인 경우 경우
            self.outline = "#FF0000" #빨강색상 코드!

            if command['up_pressed']:   # up 조이스틱이 눌려있으면
                self.position[1] -= 5
                self.position[3] -= 5

            if command['down_pressed']: # down 조이스틱이 눌려있으면
                self.position[1] += 5
                self.position[3] += 5

            if command['left_pressed']: # left 조이스틱이 눌려있으면
                self.position[0] -= 5
                self.position[2] -= 5
                
            if command['right_pressed']: # right 조이스틱이 눌려있으면
                self.position[0] += 5
                self.position[2] += 5
                
        #center update
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2]) 