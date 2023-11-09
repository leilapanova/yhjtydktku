from dataclasses import dataclass

@dataclass
class GoodIfrit:
        high: int
        name: str
        goodness: int
        def change_goodness(self,mood):
            c = self.goodness + mood
            if c < 0:
                c = 0
            self.goodness = c
        def __add__(self, other):
            if not isinstance(other, int):
                raise TypeError
            return (GoodIfrit(self.high + other,self.name,self.goodness))

        def argument(self,param):
            return f'Аргумент: {param * self.goodness // self.high}'
        def __str__(self):
            return f'Good Ifrit {self.name}, height {self.high}, goodness {self.goodness}'

        def __eq__(self, other):
            if not isinstance(other, GoodIfrit):
                raise TypeError('tdfjygjfy')
            return (self.goodness, self.high,self.high) == (other.goodness,other.high,other.high)

        def __lt__(self, other):
            if not isinstance(other, GoodIfrit):
                raise TypeError('tdfjygjfy')
            return (self.goodness, self.high,self.high) < (other.goodness,other.high,other.high)

        def __le__(self, other):
            if not isinstance(other, GoodIfrit):
                raise TypeError('tdfjygjfy')
            return (self.goodness, self.high,self.high) <= (other.goodness,other.high,other.high)


gi = GoodIfrit(10,'Vasya',5)
gi2 = GoodIfrit(10,'Petya',5)
gi.change_goodness(50)
print(gi)
print(gi != gi2)
print(gi.argument(1000))