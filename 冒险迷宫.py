import turtle as t
import random
import time

mz = t.Screen()
mz.setup(700, 700)
mz.bgcolor('black')
mz.title('冒险迷宫')
mz.register_shape('wall.gif')
mz.register_shape('pr.gif')
mz.register_shape('pl.gif')
mz.register_shape('e.gif')
mz.register_shape('gold.gif')
mz.tracer(0)

levels = []
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXX   XXXXX   XXXXXXXXXXX",
    "XXXP XXXXX    XXXXXXXXXXX",
    "XXX  XXXXXXX  XXXGXXXXXXX",
    "XXX                  XXXX",
    "XXXXXXX XXXX  XXXXX  XXXX",
    "XXXXXXXGXXXX  XXXXXE  EXX",
    "XXXXXXXXXX    XXXXX   XXX",
    "XXXXXXXXXXXX  XXXXX    XX",
    "XX                     XX",
    "XXXX  XXXXXX  XXGX  EXXXX",
    "XXXX  XXXXXX  XXXXXXXXXXX",
    "XXXXE            XXXXXXXX",
    "XXXXXXXXXXEXXXG  XXXXXXXX",
    "XXXXXXXXXXXXXXX  XXXXXXXX",
    "XXX    XXXXXXXX  XXEXXXXX",
    "XX               XXXXXXXX",
    "XX   XXXXXX    XXX    XXX",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX     XXXXXXXXXXX  XXXXX",
    "XX            XXXX      X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXX   XXXXXX  XXXXXXXXXXX",
    "XXX  XXXXXXXP XXXXXXXXXXX",
    "XXX  XXXXXXX  XXXXXXXXXXX",
    "XXX                  XXXX",
    "XXX  XX XXXX  XXXXX  XXXX",
    "XXX  XXGXXXX  XXXXXE  EXX",
    "XXX  XXXXXXX  XXXXX   XXX",
    "XXX  XXXXXXX  XXXXX    XX",
    "XX                     XX",
    "XXXX  XXXXXX  XGXX   XXXX",
    "XXXX  XXXXXX  XXXXXXXXXXX",
    "XXXXE            XXX XXXX",
    "XXXXXXX  XEXXXX  XXXXXXXX",
    "XXXXXXXX  XXXXXX  GXXXXXX",
    "XXXXXXX  XXXXXX  XXEXXXXX",
    "XX               XXXXXXXX",
    "XX   XX  XXXXXXXXXXXXXXXX",
    "XX   XX  X              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX     XXXXGXXXXXX  XXXXX",
    "XX            XXXX      X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_3 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXX   XXXXXX  XXXXXXXXXXX",
    "XXXX XXXXXXX  XXXXXXXXXXX",
    "XXX  XXXXGXX  XXX   XXXXX",
    "XXX                  XXXX",
    "XXXXXXX XXXX  XXXXX  XXXX",
    "XXXXXXXGXXXX  XXXXXE  EXX",
    "XXX   XXXXXX  XXXXX   XXX",
    "XXXXGXXXXXXX  XXXXX    XX",
    "XX                     XX",
    "XXXX  XXXEXX  XXXX  EXXXX",
    "XXXX  XXXXXX  XXXXXXXXXXX",
    "XXXXE            XXXXXXXX",
    "XXXX XXXXXEXXXX  XXXXXXXX",
    "XXXX  XXXXXXXXX  XXXXXXXX",
    "XXXX  XXXXXXXXX  XXEXXXXX",
    "XX               XXXXXXXX",
    "XX   XXPXX    XGXXXXEXXXX",
    "XX   XXXXX              X",
    "XX   XXXXXXXEXXXXX  XXXXX",
    "XX     XXXXXXXXXXX  XXXXX",
    "XX            XXXX      X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXEXXXXXXX"
]
level_4 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXX   XXXXXX  GXXXXXXXXXX",
    "XXX  GXXXXXXX XXXXXXXXXXX",
    "XXX  XXXXXXX  XXXXEXXXXXX",
    "XXX                  XXXX",
    "XXX  XX XXEE  XXXXX  XXXX",
    "XXX  XXGXXXX  XXXXXE  EXX",
    "XXX  XXXXXXX  XXXXX   XXX",
    "XXX  XXXXXXX  XXGXX    XX",
    "XX                     XX",
    "XXXX  XXXXXX  XXXG   XXXX",
    "XXXX  XXXXXX  XXXXXXGXXXX",
    "XXXXE            XXX XXXX",
    "XXXXXXX  XEXXXX  XXXXXXXX",
    "XXXXXXXX  XXXXXX  GXXXXXX",
    "XXPXXEX  XXXXEX  XXEXXXXX",
    "XX               XXXXXXXX",
    "XX   XX  XXXXXXXEXXXXXXXX",
    "XX   XX  X              X",
    "XX   XXXXXXXXXEXXX  XGXXX",
    "XX     XXXXGXXXXXX  XXXXX",
    "XX            XXXX      X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)


class Enemy(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('e.gif')
        self.speed(0)
        self.penup()

    def move(self):
        self.turn()
        if self.fx == 'U':
            go_x = self.xcor()
            go_y = self.ycor() + 24
        elif self.fx == 'D':
            go_x = self.xcor()
            go_y = self.ycor() - 24
        elif self.fx == 'R':
            go_x = self.xcor() + 24
            go_y = self.ycor()
        elif self.fx == 'L':
            go_x = self.xcor() - 24
            go_y = self.ycor()
        if (go_x, go_y) in maps:
            self.goto(go_x, go_y)
        #else:
            #print('monster hitting wall')             #检测恶魔撞墙（测试用）
        t.ontimer(self.move, random.randint(100, 400))

    def turn(self):
        # 跟随功能
        if self.distance(player) < 48:
            if self.xcor() < player.xcor():
                self.fx = 'R'
            elif self.xcor() > player.xcor():
                self.fx = 'L'
            elif self.ycor() > player.ycor():
                self.fx = 'D'
            elif self.ycor() < player.ycor():
                self.fx = 'U'

        else:
            self.fx = random.choice(['U', 'D', 'R', 'L'])

    # def attack_player(self):
    # global player_live
    # global monster_damage
    # if self.distance(player) < 48:
    #     player_live -= monster_damage
    #     print(player_live)
    # if player_live == 0:
    #     print('hi')


class Gold(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('gold.gif')
        self.speed(0)
        self.penup()


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('pr.gif')
        self.speed(0)
        self.penup()

    def go_right(self):
        print('Going Right')
        go_x = self.xcor() + 24
        go_y = self.ycor()
        self.shape('pr.gif')
        self.move(go_x, go_y)

    def go_left(self):
        print('Going Left')
        go_x = self.xcor() - 24
        go_y = self.ycor()
        self.shape('pl.gif')
        self.move(go_x, go_y)

    def go_up(self):
        print('Going Up')
        go_x = self.xcor()
        go_y = self.ycor() + 24
        self.move(go_x, go_y)

    def go_down(self):
        print('Going Down')
        go_x = self.xcor()
        go_y = self.ycor() - 24
        self.move(go_x, go_y)

    def move(self, go_x, go_y):
        if (go_x, go_y) not in walls:
            self.goto(go_x, go_y)
            self.look_for_gold(go_x, go_y)
        else:
            print('撞到墙了')

    def look_for_gold(self, go_x, go_y):
        global score
        for g in golds:
            if g.distance(player) == 0:
                score += 1
                print(f"current score is {score}")
                g.ht()
                golds.remove(g)
        if not golds:
            print("金币吃完啦！")
            success()


class Pen(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('wall.gif')
        self.speed(0)
        self.penup()

    def make_maze(self):
        level = levels[current_level - 1]
        for i in range(len(level)):
            row = level[i]
            for j in range(len(row)):
                screen_x = -288 + 24 * j
                screen_y = 288 - 24 * i
                maps.append((screen_x, screen_y))
                char = row[j]
                if char == 'X':
                    self.goto(screen_x, screen_y)
                    self.stamp()
                    walls.append((screen_x, screen_y))  # tuple
                elif char == 'P':
                    player.goto(screen_x, screen_y)
                    player.st()
                elif char == 'G':
                    gold = Gold()
                    golds.append(gold)
                    gold.goto(screen_x, screen_y)
                    gold.st()
                elif char == 'E':
                    ene = Enemy()
                    enemies.append(ene)
                    ene.goto((screen_x, screen_y))
                    ene.st()


# 进入下一关 start
current_level = 1


def success():
    if (current_level == len(levels)):
        print('你已通过全部关卡！')
        show_success_msg('你已通过全部关卡！', '按回车键重新开始')
    else:
        print('成功过关，按回车键进入下一关')
        show_success_msg('成功过关', '按回车键进入下一关')


success_pen = t.Turtle()  # 用来写成功消息的画笔


def show_success_msg(title, msg):
    success_pen.ht()
    success_pen.speed(0)
    success_pen.penup()
    success_pen.goto(-100, -100)
    success_pen.fillcolor('green')  # 设置填充色
    success_pen.begin_fill()  # 开始填充
    for i in range(4):
        success_pen.fd(200)
        success_pen.left(90)
    success_pen.end_fill()  # 结束填充
    success_pen.goto(-80, 30)
    success_pen.color('yellow')
    success_pen.write(title, align='left', font=('Arial', 15, 'bold'))
    success_pen.goto(-80, -30)
    success_pen.write(msg, align='left', font=('Arial', 15, 'bold'))


player_live = 100
monster_damage = 1

pen1 = t.Turtle()
pen1.ht()
pen1.speed(0)
pen1.up()
pen1.goto(-300, 310)
pen1.color('white')
text = f'命数: {player_live}'
font = ('Arial', 20, 'bold')
pen1.write(text, align='left', font=font)


# 进入下一关
def next_level():
    global current_level,walls
    if (current_level == len(levels)):
        current_level = 1
    else:
        current_level = current_level + 1

    # 清楚提示信息
    success_pen.clear()

    # 隐藏并清空敌人
    for e in enemies:
        e.ht()
    enemies.clear()

    # 清除迷宫的砖墙

    pen.reset()
    walls = []

    # 重建迷宫
    pen.make_maze()

    # 给恶魔加定时器，让他动起来
    for e in enemies:
        t.ontimer(e.move, random.randint(100, 300))


# end

score = 0
pen = Pen()
player = Player()
maps = []
walls = []
golds = []
enemies = []

pen.make_maze()

mz.listen()
mz.onkey(player.go_right, 'Right')
mz.onkey(player.go_left, 'Left')
mz.onkey(player.go_up, 'Up')
mz.onkey(player.go_down, 'Down')
mz.onkey(next_level, 'Return')  # 回车键
#walls = []

for e in enemies:
    t.ontimer(e.move, random.randint(100, 300))

gameover = False
while True:
    if gameover:
        break
    mz.update()
    for e in enemies:
        if e.distance(player) == 0:
            player_live = player_live - monster_damage
            time.sleep(0.1)
            if player_live == 0:
                print(f'Player live = {player_live}')
                gameover = True
                pen2 = t.Turtle()
                pen2.ht()
                pen2.speed(0)
                pen2.goto(-50, 0)
                pen2.color('BLUE')
                text = ' 游戏结束'
                font = ('Arial', 20, 'bold')
                pen2.write(text, align='left', font=font)
            pen1.clear()
            pen1.write(f'命数：{player_live}', align='left', font=font)
            pen1.clear()
            pen1.write(f'命数：{player_live}', align='left', font=font)

mz.mainloop()