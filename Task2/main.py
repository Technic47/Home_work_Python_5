# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


from random import randint


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.sweets = 0

    def take_sweets(self):
        number = int(input(f"{self.name}, how many sweets will you take from the table? "))
        if number < 1 or number > 28:
            number = int(input(f"{self.name}, you enter wrong number, try again: "))
        self.sweets += number
        return number


class Bot:
    def __init__(self, name: str) -> None:
        self.name = name
        self.sweets = 0

    def take_sweets(self, maxx: int = 28):
        number = randint(1, maxx)
        self.sweets += number
        print(f'Bot took {number} sweets')
        return number


class Game:
    def __init__(self, player1, player2, game_mode) -> None:
        self.table_sweets = 100
        self.game_mode = game_mode
        self.player1 = Player(name=player1)
        if self.game_mode == 0:
            self.player2 = Player(name=player2)
        elif self.game_mode == 1:
            self.player2 = Bot(name=player2)
        elif self.game_mode == 2:
            self.player2 = Bot(name=player2)
        self.players = [self.player1, self.player2]
        self.index0 = 0
        self.index1 = 0

    def print_sweets_count(self) -> None:
        print(
            f'Sweets on the table: {self.table_sweets}, {self.player1.name} has {self.player1.sweets} sweets, {self.player2.name} has {self.player2.sweets} sweets\n')

    def lottery(self) -> None:
        print('Lottery for first start begins!')
        points_player1 = 0
        points_player2 = 0
        while points_player2 == points_player1:
            points_player1 = randint(1, 6)
            points_player2 = randint(1, 6)
            if points_player1 > points_player2:
                self.index0 = 0
                self.index1 = 1
                print(f'{self.player1.name} starts first!')
                break
            else:
                self.index0 = 1
                self.index1 = 0
                print(f'{self.player2.name} starts first!')
                break

    def player_turn(self, index):
        if self.players[index].__class__ == Bot:
            if self.table_sweets < 28 and self.table_sweets != 0:
                number = self.player2.take_sweets(self.table_sweets)
            else:
                number = self.player2.take_sweets()
            self.table_sweets -= number
            self.print_sweets_count()
            if self.table_sweets == 0:
                print(f'Bot wins!!!')
                quit()
        elif self.players[index].__class__ == Player:
            number = self.players[index].take_sweets()
            while self.table_sweets - number < 0:
                print(f'You want to take too many sweets! Take less. Only {self.table_sweets} left.\n')
                number = self.players[index].take_sweets()
            self.table_sweets -= number
            self.print_sweets_count()
            if self.table_sweets == 0:
                print(f'You win!!! All these sweeeeety sweets are yours, fatass!')
                quit()

    def start(self) -> None:
        if self.game_mode == 0:
            self.lottery()
            self.print_sweets_count()
            while self.table_sweets > 0:
                self.player_turn(self.index0)
                self.player_turn(self.index1)
        elif self.game_mode == 1:
            self.lottery()
            self.print_sweets_count()
            while self.table_sweets > 0:
                self.player_turn(self.index0)
                self.player_turn(self.index1)


def main() -> None:
    game_mode = input('How would you like to play? pvp or bot or cheetbot? ')
    if game_mode == 'pvp':
        player1_name = input("Enter Player1 name: ")
        player2_name = input("Enter Player2 name: ")
        game = Game(player1_name, player2_name, 0)
        game.start()
    elif game_mode == 'bot':
        player1_name = input("Enter Player1 name: ")
        player2_name = 'Bot'
        game = Game(player1_name, player2_name, 1)
        game.start()
    elif game_mode == 'botcheet':
        player1_name = input("Enter Player1 name: ")
        player2_name = '!CheetBot!'
        game = Game(player1_name, player2_name, 2)
        game.start()


if __name__ == '__main__':
    main()
