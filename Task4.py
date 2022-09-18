# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from random import randint


def generate_text(size: int = 10000) -> None:
    text = ''.join(str(randint(0, 1)) for i in range(size))
    with open(r'Generated_text.txt', 'w') as data:
        data.write(text)


def copy_text(path: str) -> str:
    with open(path, 'r') as data:
        text = data.read()
    return text

def write_text(text) -> None:
    with open(r'Generated_text.txt', 'a') as data:
        data.writelines(f'\n{text}')


def zipp(text: str) -> str:
    # data = []
    data_str = ''
    i = 0
    while i < len(text):
        size = 0
        j = i
        while text[j] == text[i]:
            size += 1
            j += 1
            if j == len(text):
                break
        # block = [size, int(text[i])]
        # data.append(block)
        data_str += str(size)
        data_str += text[i]
        i += size
    # data_str = str(data)
    return data_str


generate_text(100)
path = r'Generated_text.txt'
text = copy_text(path)
print(text)
data = zipp(text)
print(data)
print(len(text), len(data))

write_text(data)
