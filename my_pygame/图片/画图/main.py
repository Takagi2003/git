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

# -------画圆------
pygame.draw.circle(window, (255, 0, 0), (100, 100), 30, 0)
#  在哪个表面画这个圆（很明显我们定义的是window）。
#  用什么颜色来画（在这里用的红色，对应值为(255, 0, 0)）。
#  在什么位置画（在这里位于(100, 100)，这里表示从左上角向下100像素再向右100像素的位置）。
#  圆的大小（这里是30，这是圆的半径，单位是像素）。
#  线宽（如果width = 0，圆完全是填充的，这里就采用了完全填充）。


# -------画矩形------
pygame.draw.rect(window, (250, 0, 0), (100, 100, 300, 200), 0)
# 这会创建一个矩形。它的左上角距离左边界250像素，距离窗口上边界150像素，宽为300像素，高为200像素

# -------画直线-----
pygame.draw.line(window, (250, 0, 0), (10, 10), (100, 10), 3)
# Surface: Surface对象
# color: 线段颜色
# start_pos: 线段的起点坐标, 一个二元组(x,y)
# end_pos: 线段的终点坐标, 一个二元组(x,y)
# width: 线条的宽度,默认值为1

# ----画折线----
# pygame.draw.lines(Surface, color, closed, pointlist, width)
pygame.draw.lines(window, (150, 150, 150), True, ((10, 20), (30, 90), (90, 30)), 3)
# Surface: Surface对象
# color: 线条颜色
# closed: 是否封闭图形,布尔型.True:起点与终点会连起来成为一个封闭图形 ,False:起点与终点不会连起来
# pointlist: 折线各个节点的坐标列表. 元素是二元组的列表
# width: 线宽.默认值为1

# 进行刷新，不然不会显示，第一次进行刷新使用这个，后面的都使用pygame.display.update()
pygame.display.flip()


while True:
    # 对输入或者操作的任何一个事件进行循环
    for event in pygame.event.get():
        # 如果检测到按下左上角叉，这结束此程序，exit()只会退出一个线程，如后面添加更过模块exit()可能会导致无法退出
        if event.type ==pygame.QUIT:
            exit()
    # 进行刷新
    pygame.display.update()