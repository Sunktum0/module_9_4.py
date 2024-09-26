# first = 'Мама мыла раму'
# second = 'Рамена мало было'
#
# my_func = list(map(lambda x, y: True if x == y else False, first, second))
# print(list(my_func))
import random
# def get_advanced_writer(file_name):
#     def write_everything(*data_set):
#         with open(file_name, 'a', encoding='utf-8') as f:
#             for item in data_set:
#                 f.write(f"{item}\n")  # Записываем каждый элемент в новой строке
#
#     return write_everything
#
# # Пример использования
# write = get_advanced_writer('example.txt')
# write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


from random import choice
class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

if __name__ == '__main__':
    first_ball = MysticBall(['пРИВЕТ','пока','добрый вечер!','добрый день!'])
    print(first_ball())
    print(first_ball())
    print(first_ball())


