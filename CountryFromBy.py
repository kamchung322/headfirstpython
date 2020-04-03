class CountryFromBy:
    def __init__(self, v: int=0, i: int=1)-> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr


a = CountryFromBy(100,20)
b = CountryFromBy()
print(a.val)
print(b.val)
print(a)