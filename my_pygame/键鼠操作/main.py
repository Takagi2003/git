import pygame  # 导入pygame模块
from pygame.locals import *  # 导入这个完成对键盘event.key == K_w 之类的操作，否则需要使用event.key == pygame.K_w
import os
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
image = pygame.image.load('背景.png')
clock = pygame.time.Clock()
window.fill((255, 255, 255))
pygame.display.flip()


def load_animations(name):
    images = []
    i = 0
    while True:
        i += 1
        filename = name.format(i)
        if os.path.exists(filename):
            images.append(pygame.image.load(filename))
        else:
            break
    return images


class Takagi:
    def __init__(self):
        self.images = load_animations('files/pary{}.png')
        self.image = self.images[0]
        self.rect = self.image.get_rect(bottomleft=(0, HIGHT))
        self.move = [0, 0]

    def dray(self, windows):
        windows.blit(self.image, self.rect)

        self.rect.x += self.move[0]
        self.rect.y += self.move[1]

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIGHT:
            self.rect.right = WIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HIGHT:
            self.rect.bottom = HIGHT



def main():
    takagi=Takagi()
    speed = 5

    while True:
        # 重新刷新屏幕
        window.blit(image, (0, 0))
        # 使用 bt bw来控制图片的打印位置
        takagi.dray(window)

        # 对输入或者操作的任何一个事件进行循环
        for event in pygame.event.get():
            # 如果检测到按下左上角叉，这结束此程序，exit()只会退出一个线程，如后面添加更过模块exit()可能会导致无法退出
            if event.type == pygame.QUIT:
                exit()

            # ****这里一定要注意切换英文输入，不然可能输出不了****
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    takagi.move[1] = -speed
                elif event.key == K_s:
                    takagi.move[1] = speed
                elif event.key == K_a:
                    takagi.move[0] = -speed
                elif event.key == K_d:
                    takagi.move[0] = speed
            elif event.type == KEYUP:
                if event.key == K_w:
                    takagi.move[1] = 0
                elif event.key == K_s:
                    takagi.move[1] = 0
                elif event.key == K_a:
                    takagi.move[0] = 0
                elif event.key == K_d:
                    takagi.move[0] = 0

        # 进行刷新
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()