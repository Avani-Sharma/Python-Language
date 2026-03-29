# type error
# a = '10'
# b = 20
# c = a+b
def add(a, b):
    try:
        result = a+b
        return result
    except TypeError as e:
        return ("Some thing has occured!", e)
print(add('10',10))