#  Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'

text = 'Мы неабв очень любим Питон иабв Джавабв'

text_find = 'абв'
index = 0

list1 = text.split(' ')

print(list1)

list2 = [item for item in list1 if text_find not in item]

print(list2)
