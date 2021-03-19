# Errors and Exceptions
try:
    a = 5 /1
except Exception as e :
    print(e)


try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e :
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up...')


class valueTooHighError(Exception):
    pass

class valueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise valueTooHighError('value is too high')
    if x < 5:
        raise valueTooSmallError('value is too small', x)

try:
    test_value(1)
except valueTooHighError as e:
    print(e)
except valueTooSmallError as e:
    print(e.message, e.value)