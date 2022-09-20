# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from random import randint
from itertools import groupby


def generate_text(path: str, size: int = 10000) -> None:
    """Generates random string with size = size and saves it in file Generated_text.txt"""
    text = ''.join(str(randint(0, 1)) for i in range(size))
    with open(path, 'w') as data:
        data.write(text)


def copy_text(path: str) -> str:
    """Copies file from path"""
    with open(path, 'r') as data:
        text = data.read()
    return text


def write_text(path, text) -> None:
    """Writes text to file"""
    with open(path, 'a') as data:
        data.writelines(f'\n{text}')


def zipp(text: str) -> str:
    """Encodes with LRE"""
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
        data_str += str(size)
        data_str += text[i]

        i += size
    return data_str


def unzipp(text: str) -> str:
    """Decodes LRE text"""
    data_str = ""
    i = 0
    while i <= len(text) - 1:
        count = int(text[i])
        word = text[i + 1]
        for j in range(count):
            data_str += word
            j += 1
        i += 2
    return data_str


def zipp_groupby(text: str) -> str:
    """Encodes with LRE using groupby"""
    return "".join(f"{sum(1 for _ in x)}{y}" for y, x in groupby(text))


path = r'Generated_text.txt'
generate_text(path, 20)
text = copy_text(path)
print(text)

data = zipp(text)
write_text(path, data)
print(data)
data = unzipp(data)
print(data)

data1 = zipp_groupby(text)
write_text(path, data1)
print(data1)
data1 = unzipp(data1)
print(data1)
