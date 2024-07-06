class Example:
    def __init__(self) -> None:
        self.__value = 1

e = Example()
print(dir(e))
print(e._Example__value)