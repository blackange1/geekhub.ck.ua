"""
Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )
"""
class Calc(object):
    """
    Class used to represent a mathematical operation
    """
    def __init__(self) -> None:
        # saved last operation
        self.duble_last_result = None
        self.last_result = None

    def add(self, a, b):
        """
        Parameters
        ----------
        a : float or int
            first number
        b : str
            second number
        Return
        ----------
        a + b : float or int
        """
        self.duble_last_result = self.last_result
        self.last_result = a + b
        return self.last_result

    def sub(self, a, b):
        """
        Parameters
        ----------
        a : float or int
            first number
        b : str
            second number
        Return
        ----------
        a - b : float or int
        """
        self.duble_last_result = self.last_result
        self.last_result = a - b
        return self.last_result

    def mult(self, a, b):
        """
        Parameters
        ----------
        a : float or int
            first number
        b : str
            second number
        Return
        ----------
        a * b : float or int
        """
        self.duble_last_result = self.last_result
        self.last_result = a * b
        return self.last_result

    def div(self, a, b) -> float:
        """
        Parameters
        ----------
        a : float or int
            first number
        b : str
            second number
        Return
        ----------
        a / b : float or None if b == 0
        """
        if b == 0:
            print('Zero Division')
            return None
        self.duble_last_result = self.last_result
        self.last_result = a / b
        return self.last_result


# test
tmp = Calc()
print(tmp.add(5, 2))
print(tmp.sub(5, 2))
print(tmp.mult(5, 2))
print(tmp.div(5, 2))
print(tmp.last_result)
print(tmp.duble_last_result)