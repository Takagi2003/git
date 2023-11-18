import pygame   # 导入pygame模块
from pygame.locals import *     # 导入这个完成对键盘event.key == K_w 之类的操作，否则需要使用event.key == pygame.K_w
# 设置需要的模块大小
HIGHT = 600
WIGHT = 800
# 初始化
pygame.init()
# 创建一个window对象
window = pygame.display.set_mode((WIGHT, HIGHT))
# 该程序框显示的名字
pygame.display.set_caption("这是一个pygame程序")
# 对window对象进行颜色的填充，格式是R G B，现在是进行白色的填充
window.fill((255, 255, 255))

# 创建一个image对象并且在0，0显示
image = pygame.image.load('背景.png')
window.blit(image, (0, 0))
# 进行刷新，不然不会显示，第一次进行刷新使用这个，后面的都使用pygame.display.update()
# 创建对象image_gaomu
image_gaomu = pygame.image.load('高木头像(1).png')
# 得到对象image_gaomu的尺寸，为一元组
size = image_gaomu.get_size()
# 在左边的中间画
window.blit(image_gaomu, (0, HIGHT/2-size[1]/2))
pygame.display.flip()
bw =HIGHT / 2 - size[1]/2   # y 坐标轴
bt = 0  # x 坐标轴
speed =0    # 初始y
spend =0    # 初始x
speed_1 = 10  # 移动的速度

while True:
    # 重新刷新屏幕
    window.blit(image, (0, 0))
    # 使用 bt bw来控制图片的打印位置
    window.blit(image_gaomu, (bt, bw))

    # 对输入或者操作的任何一个事件进行循环
    for event in pygame.event.get():
        # 如果检测到按下左上角叉，这结束此程序，exit()只会退出一个线程，如后面添加更过模块exit()可能会导致无法退出
        if event.type ==pygame.QUIT:
            exit()

        # -------对于键盘鼠标进行判断
        # ---对鼠标的操作
        # 如果鼠标按下
        if event.type == MOUSEBUTTONDOWN:
            # print("鼠标已按下")
            pass
        # 如果鼠标松开
        if event.type == MOUSEBUTTONUP:
            # print('鼠标已松开')
            pass

        # ---对键盘的操作
        # ****这里一定要注意切换英文输入，不然可能输出不了****
        # 按下有速度，松开速度为0
        elif event.type == KEYDOWN:
            if event.key == K_w:
                speed =-1*speed_1
            elif event.key == K_s:
                speed = 1*speed_1
            elif event.key ==K_a:
                spend = -1*speed_1
            elif event.key == K_d:
                spend = 1*speed_1
        elif event.type == KEYUP:
            if event.key ==K_w:
                speed = 0
            elif event.key == K_s:
                speed =0
            elif event.key == K_a:
                spend =0
            elif event.key == K_d:
                spend =0
        bw = bw + speed
        bt = bt + spend
    # 进行刷新
    pygame.display.update()