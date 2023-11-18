import pygame   # 导入pygame模块
# 设置需要的模块大小
HIGHT = 400
WIGHT = 300
# 初始化，一定不能忘记
pygame.init()
# 创建一个window对象
window = pygame.display.set_mode((WIGHT, HIGHT))
# 该程序框显示的名字
pygame.display.set_caption("这是一个pygame程序")
# 对window对象进行颜色的填充，格式是R G B，现在是进行白色的填充
window.fill((255, 255, 255))


# ------------第一种 使用系统字体 --------------
# 列举一些可以使用的字体，如FangSong,使用照片保存在目录中,照片名font_s
# 获得文件字体
font = pygame.font.match_font('FangSong')
# 获取fonts对象
fonts = pygame.font.Font(font, 30)
# 将文字生成text对象
text=fonts.render('你好', True, (255, 0, 0))
# 将text对象放在window上
window.blit(text, (0, 100))
# 刷新可以写在步骤操作之后
pygame.display.flip()


# ------------第二种 匹配字体文件的字体 --------------

# 操作基本都是差不多的，没有ttf文件，这里就不演示了
# font_1=pygame.font.Font("simhei.ttf", 30)
# text_1=font_1.render('你好', True, (255, 0, 0))
# # 将text对象放在window上
# window.blit(text_1, (0, 100))

while True:
    # 对输入或者操作的任何一个事件进行循环
    for event in pygame.event.get():
        # 如果检测到按下左上角叉，这结束此程序，exit()只会退出一个线程，如后面添加更过模块exit()可能会导致无法退出
        if event.type ==pygame.QUIT:
            exit()
    # 进行刷新
    pygame.display.update()