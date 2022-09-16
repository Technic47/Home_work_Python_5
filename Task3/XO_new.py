import pygame
import sys


class Player:
    def __init__(self, name: str, sign: str) -> None:
        self.name = name
        self.sign = sign


class Game:
    def __init__(self, player1_sign: str, player2_sign: str) -> None:
        self.player1_sign = player1_sign
        self.player2_sign = player2_sign
        self.game_over = False
        self.mas = [[0] * 3 for i in range(3)]
        self.query = 0
        # self.query = [self.player1_sign, self.player2_sign]

    def check_win(self, mas, sign: str):
        zeros = 0
        for row in self.mas:
            zeros += row.count(0)
            if row.count(sign) == 3:
                return sign
        for col in range(3):
            if self.mas[0][col] == sign and self.mas[1][col] == sign and self.mas[2][col] == sign:
                return sign
        if self.mas[0][0] == sign and self.mas[1][1] == sign and self.mas[2][2] == sign:
            return sign
        if self.mas[2][0] == sign and self.mas[1][1] == sign and self.mas[2][0] == sign:
            return sign
        if zeros == 0:
            return "Piece"
        return False

    def start(self):
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

        while True:
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


def main() -> None:
    player1_sign = input("Choose sign for player 1 (X or O):")
    player2_sign = ''
    if player1_sign == 'X':
        player2_sign = 'O'
    elif player1_sign == 'O':
        player2_sign = 'X'
    game = Game(player1_sign, player2_sign)
    game.start()


if __name__ == '__main__':
    main()
