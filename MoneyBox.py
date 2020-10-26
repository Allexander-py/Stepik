class MoneyBox:
    def __init__(self, capacity: int, current_value=0):
        """Создает копилку с именем self и вместимостью capacity"""
        self.capacity = capacity
        self.current_value = current_value

    def can_add(self, quantity: int):
        if self.capacity >= self.current_value + quantity:
            print('Можно добавить ' + str(quantity))
            return True
        else:
            print('Можно добавить не больше : ' + str(self.capacity - self.current_value))
            return False
    def add(self, quantity: int):
        if self.can_add(quantity) == True:
            self.current_value += quantity
        else:
            print('Можно добавить не больше : ' + str(self.capacity - self.current_value))

x = MoneyBox(9)
x.add(5)
x.can_add(2)
x.add(9)
