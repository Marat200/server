# 3. Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе.
#    Для проверки правильности работы кода используйте значения: «attribute», «класс», «функция», «type»

TEST_LIST = [
    'attribute',
    'класс',
    'функция',
    'type'
]

for word in TEST_LIST:
    try:
        eval(f'b"{word}"')
    except SyntaxError as err:
        print(f'"{word}" cannot be written in byte type.')
