class LimitedList:

    def __init__(self, count):
        self.__count = count
        self.__limited_list = [None] * count

    def __setitem__(self, key, value):
        if 0 <= key < self.__count:
            self.__limited_list[key] = value
        else:
            raise IndexError("Index out of range")

    def __getitem__(self, item):
        if 0 <= item < self.__count:
            return self.__limited_list[item]
        else:
            raise IndexError("Wrong index")



l1 = LimitedList(2)
l1[0] = 0
l1[1] = 1

print(l1[2])