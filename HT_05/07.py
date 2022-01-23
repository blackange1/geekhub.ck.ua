"""
7. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.
   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   >>>for elem in generator([1, 2, 3]):
   ...    print(elem)
   ...
   1
   2
   3
   1
   2
   3
   1
   .......
"""
def generator(elements, repeat=2):
   flag = True
   while flag:
      iter_element = iter(elements)
      try:
         while True:
            yield next(iter_element)
      except StopIteration:
         repeat -= 1
         if repeat < 1:
            flag = False


# test
for elem in generator([1, 2, 3]):
   print(elem)

print()

for elem in generator('abcd-', repeat=3):
   print(elem)
