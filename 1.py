from dataclasses import dataclass


class AirCastle:
    def __init__(self,high,clouds,color):
        self.high = high
        self.clouds = clouds
        self.color = color

@dataclass
class AirData:
    high: int
    clouds: int
    color: str

    def change_height(self,value):
        c = self.clouds + value
        if c < 0:
            c = 0
        self.clouds = c
    def __add__(self, other):
        if not isinstance(other,int):
            raise TypeError('E{QE{QE{{QE{QEQE{{WD{AS{D{W{ASD{WASD{AW')
        self.clouds += other
        self.high += other // 5
        return AirData(self.high, self.clouds,self.color)
    def opacity(self,degree):
        self.degree = self.high // degree * self.clouds
        print(f'Значение видимости замка: {self.degree} ')
    def __str__(self):
        return f'The AirCastle at an altitude of {self.high} meters is {self.color} with {self.clouds} clouds'
    def __eq__(self, other):
        if not isinstance(other,AirData):
            raise TypeError('oejfhgvoure')
        return self.clouds == other.clouds
    def __lt__(self, other):
        if not isinstance(other,AirData):
            raise TypeError('oejfhgvoure')
        return self.clouds < other.clouds
    def __le__(self,other):
        if not isinstance(other,AirData):
            raise TypeError('oejfhgvoure')
        return self.clouds <= other.clouds


air = AirData(1,3,"blue")
air2 = AirData(1,3,"blue")
print(air)
air.change_height(10)
print(air)
air = air + 100
print(air)
air.opacity(1)
print(air == air2)
print(air < air2)