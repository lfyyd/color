import pygame


def main():
    pygame.init()
    pygame.display.set_caption('未闻Code：青南做的游戏')  # 游戏标题
    win = pygame.display.set_mode((800, 600))  # 窗口尺寸，宽800高600
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击左上角或者右上角的x关闭窗口时，停止程序
                running = False
