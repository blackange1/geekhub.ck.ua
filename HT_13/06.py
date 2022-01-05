# 6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class Demo(object):
    count = 0

    def __init__(self) -> None:
        Demo.count += 1

    @classmethod
    def print_count_of_instances(cls):
        print(cls.count)


# test
a = Demo()
b = Demo()
c = Demo()

a.print_count_of_instances()
