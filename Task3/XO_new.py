import pygame
import sys

objects = []
pygame.init()
size_block = 100
margin = 15
width = heigth = size_block * 3 + margin * 4

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики - нолики')
font = pygame.font.SysFont('Arial', 40)


class Button:
    def __init__(self, x, y, width, height, buttonText, onclickFunction, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2])
        screen.blit(self.buttonSurface, self.buttonRect)


class Player:
    def __init__(self, sign: str) -> None:
        self.sign = sign


class Game:
    def __init__(self, player1_sign, player2_sign) -> None:
        self.player1_sign = player1_sign
        self.player2_sign = player2_sign
        self.game_over = False
        self.mas = [[0] * 3 for i in range(3)]
        self.query = 0

    def check_win(self, mas, sign: str):
        zeros = 0
        for row in self.mas:
            zeros += row.count(0)
            if row.count(sign) == 3:
                return sign + ' Wins'
        for col in range(3):
            if self.mas[0][col] == sign and self.mas[1][col] == sign and self.mas[2][col] == sign:
                return sign + ' Wins'
        if self.mas[0][0] == sign and self.mas[1][1] == sign and self.mas[2][2] == sign:
            return sign + ' Wins'
        if self.mas[2][0] == sign and self.mas[1][1] == sign and self.mas[2][0] == sign:
            return sign
        if zeros == 0:
            return "Piece"
        return False

        # self.start()

    # def prerare(self):
    # while True:
    #     screen.fill((20, 20, 20))
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #     for object in objects:
    #         object.process()
    #     pygame.display.flip()

    def start(self):
        while True:
            black = (0, 0, 0)
            red = (225, 0, 0)
            green = (0, 255, 0)
            white = (255, 255, 255)
            pygame.init()
            size_block = 100
            margin = 15
            width = heigth = size_block * 3 + margin * 4

            size_window = (width, heigth)
            screen = pygame.display.set_mode(size_window)
            pygame.display.set_caption('Крестики - нолики')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    col = x_mouse // (size_block + margin)
                    row = y_mouse // (size_block + margin)
                    if self.mas[row][col] == 0:
                        if self.query % 2 == 0:
                            self.mas[row][col] = self.player1_sign
                        else:
                            self.mas[row][col] = self.player2_sign
                        self.query += 1

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.mas = [[0] * 3 for i in range(3)]
                    self.game_over = False
                    screen.fill(black)

            if not self.game_over:
                for row in range(3):
                    for col in range(3):
                        if self.mas[row][col] == 'X':
                            color = red
                        elif self.mas[row][col] == 'O':
                            color = green
                        else:
                            color = white
                        x = col * size_block + (col + 1) * margin
                        y = row * size_block + (row + 1) * margin
                        pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                        if color == red:
                            pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5),
                                             10)
                            pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5),
                                             10)
                        elif color == green:
                            pygame.draw.circle(screen, white,
                                               (x + size_block // 2, y + size_block // 2),
                                               size_block // 2 - 3, 10)

            if (self.query - 1) % 2 == 0:
                self.game_over = self.check_win(self.mas, self.player1_sign)
            else:
                self.game_over = self.check_win(self.mas, self.player2_sign)

            if self.game_over:
                screen.fill(black)
                font = pygame.font.SysFont('stxingkai', 80)
                text1 = font.render(self.game_over, True, white)
                text_rect = text1.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                screen.blit(text1, [text_x, text_y])

            pygame.display.update()


def main():
    while True:
        screen.fill((20, 20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for object in objects:
            object.process()
        pygame.display.flip()


def set_player_sign1():
    signs[0] = 'X'
    signs[1] = 'O'
    print(signs)


def set_player_sign2():
    signs[0] = 'O'
    signs[1] = 'X'
    print(signs)


signs = ['0', '0']
game = Game(signs[0], signs[1])

Button(30, 30, size_block, size_block, 'X', set_player_sign1())
Button(30, 140, size_block, size_block, 'O', set_player_sign2())

if __name__ == '__main__':
    main()
