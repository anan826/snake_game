import pygame
import random
import time

speeddifferent = 10  # global函數的初始化
pygame.init()  # 初始功能
score = 0  # 總分歸零
score_font = pygame.font.SysFont("bahnschrift", 15)  # 調用字型
Greenfont = (0, 255, 0)  # 綠字
SFont = (0, 255, 0)

width, height = 600, 600  # 設定螢幕寬,高
x, y = 300, 300  # 蛇的初始位置
delta_x, delta_y = 0, 10  # 初始移動輛,x方向
food_x, food_y = random.randrange(
    0, width)//10*10, random.randrange(0, height)//10*10  # 創造食物30(整除3*10)

clock = pygame.time.Clock()  # 時間
body_list = [(x, y)]  # 用tuple list放入list蛇身
game_over = False  # 蛇自撞觸發

font = pygame.font.SysFont("bahnschrift", 30)  # 呈現結束畫面

game_screen = pygame.display.set_mode(
    (width, height))  # 將螢幕大小傳入setmode中,視為蛇的活動範圍
pygame.display.set_caption("貪食蛇期中作業")  # 遊戲標題
pygame.time.delay(500)


def snake():
    # 全域變數設定speedifferent為難易度選項越大越難
    global x, y, food_x, food_y, game_over, speeddifferent, score
    x = (x + delta_x) % width  # 循環邊界
    y = (y + delta_y) % height  # x=0,y=10往上10個單位200y+10
    if ((x, y) in body_list):  # 失敗的條件
        game_over = True
        return
    body_list.append((x, y))  # snake body append列表

    if (food_x == x and food_y == y):
        speeddifferent += 1  # 當蛇吃掉蘋果增加速度
        score += 10
        while ((food_x, food_y) in body_list):  # 吃到蘋果
            food_x, food_y = random.randrange(
                0, width)//10*10, random.randrange(0, height)//10*10  # 隨機生成的蘋果賦值
    else:
        del body_list[0]  # 刪除第一個單位，意味有吃到就不刪第0個單位
    game_screen.fill((0, 0, 0))  # 黑色
    score_sur = score_font.render(
        "player1_score:%s" % str(score), True, Greenfont)
    game_screen.blit(score_sur, (5, 5))
    score_sur = score_font.render("snake_head_position:%s" % str(
        body_list[-1]), True, SFont)  # bodyhead
    game_screen.blit(score_sur, (5, 20))
    pygame.draw.rect(game_screen, (255, 0, 0), [food_x, food_y, 10, 10], 0)
    for (i, j) in body_list:
        pygame.draw.rect(game_screen, (0, 255, 0), [
                         i, j, 10, 10], 0)  # 劃一小方塊[bodyLx,bodyLy,10,10]
    pygame.display.update()


while True:
    print('body_list = ', body_list)  # 將蛇身列表印出來
    if game_over == True:
        game_screen.fill((0, 0, 0))  # 螢幕變黑色
        msg = font.render("GAME OVER !!", True, (255, 255, 255))
        game_screen.blit(msg, [width//3, height//3])
        pygame.display.update()
        time.sleep(5)
        pygame.quit()  # 退出pygame
        quit()
    events = pygame.event.get()
    for event in events:  # 建立事件 滑鼠移動、鍵盤上下左右都可稱為事件
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if (event.type == pygame.KEYDOWN):  # 鍵盤向下鍵
            if (event.key == pygame.K_LEFT):  # K_按鈕名稱
                delta_y = 0
                if (delta_x != 10):  # !not
                    delta_x = -10  # 非右才符合向左條件，非現況右才能左
            elif (event.key == pygame.K_RIGHT):
                delta_y = 0
                if (delta_x != -10):
                    delta_x = 10

            elif (event.key == pygame.K_UP):
                delta_x = 0
                if (delta_y != 10):
                    delta_y = -10
            elif (event.key == pygame.K_DOWN):
                delta_x = 0
                if (delta_y != -10):
                    delta_y = 10
            else:
                continue
            snake()
    if (not events):
        snake()
    clock.tick(speeddifferent)  # 每幀應該調用一次
    print("speeddifferent", speeddifferent)

pygame.quit()
