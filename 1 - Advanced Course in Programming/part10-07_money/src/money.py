# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        if cents >= 100:
            euros += cents // 100
            cents = cents % 100
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents

    def __lt__(self, another):
        return (self.__euros, self.__cents) < (another.__euros, another.__cents)

    def __gt__(self, another):
        return (self.__euros, self.__cents) > (another.__euros, another.__cents)

    def __ne__(self, another):
        return not self.__eq__(another)

    def __add__(self, another):
        total_euros = self.__euros + another.__euros
        total_cents = self.__cents + another.__cents
        return Money(total_euros, total_cents)

    def __sub__(self, another):
        total_cents_self = self.__euros * 100 + self.__cents
        total_cents_another = another.__euros * 100 + another.__cents
        
        if total_cents_self < total_cents_another:
            raise ValueError("a negative result is not allowed")
        
        result_cents = total_cents_self - total_cents_another
        return Money(result_cents // 100, result_cents % 100)

if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)
    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)