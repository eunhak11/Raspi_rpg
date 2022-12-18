import numpy as np

class Bullet:
    def __init__(self, position, command):  # Bullet class는 생성시 시작점과, 움직임 커맨드를 준다.
        self.appearance = 'rectangle'       # 모양은 사각형으로 정의
        self.speed = 10                     # 총알의 속도
        self.damage = 10                    # 총알의 피해량
        self.position = np.array([position[0]-3, position[1]-3, position[0]+3, position[1]+3])
        self.direction = {'up' : False, 'down' : False, 'left' : False, 'right' : False}        # 발사 방향
        self.state = None
        self.outline = "#0000FF"
        self.direction['right'] = True      # 총알은 오른쪽으로만 나갈 것이다.

        

    def move(self):                         # 총알의 움직임 정의
        if self.direction['up']:            # up 조이스틱이 눌려있으면
            self.position[1] -= self.speed  
            self.position[3] -= self.speed

        if self.direction['down']:          # down 조이스틱이 눌려있으면
            self.position[1] += self.speed
            self.position[3] += self.speed

        if self.direction['left']:          # left 조이스틱이 눌려있으면
            self.position[0] -= self.speed
            self.position[2] -= self.speed
            
        if self.direction['right']:         # right 조이스틱이 눌려있으면
            self.position[0] += self.speed
            self.position[2] += self.speed
            
    def collision_check(self, enemys):      # 충돌 판정!
        for enemy in enemys:                # 현재 필드에 있는 적의 리스트를 인자로 받는다.
            collision = self.overlap(self.position, enemy.position)     # 충돌을 정의하는 overlap 함수로 판별
            
            if collision:                   # 충돌인 경우
                enemy.state = 'die'         # 총알과 충돌한 적은 die
                self.state = 'hit'          # 총알은 hit 상태로 설정

    def overlap(self, ego_position, other_position):    # 충돌을 정의하는 overlap 함수로 boolean 값을 return
        '''
        두개의 사각형(bullet position, enemy position)이 겹치는지 확인하는 함수
        좌표 표현 : [x1, y1, x2, y2]
        
        return :
            True : if overlap
            False : if not overlap
        '''
        return ego_position[0] > other_position[0] and ego_position[1] > other_position[1] \
                 and ego_position[2] < other_position[2] and ego_position[3] < other_position[3]