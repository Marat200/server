# 2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это небходимо в автоматическом,
#    а не ручном режиме с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя
#    методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

TEST_LIST = [
    'class',
    'function',
    'method'
]

for i, word in enumerate(TEST_LIST):
    TEST_LIST[i] = eval(f'b"{word}"')
    print(f'"{word}" => \n    '
          f'type: {type(TEST_LIST[i])}\n    '
          f'value: {TEST_LIST[i]}\n    '
          f'length: {len(TEST_LIST[i])}\n')
