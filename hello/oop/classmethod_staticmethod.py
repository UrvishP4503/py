class Player:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def player_details(self):
        print(f"Name = {self.name} and age = {self.age}")

    @classmethod
    def add_somethings(cls, num1: int, num2: int) -> int:
        return num1 + num2

    @staticmethod
    def add_somethings2(num1: int, num2: int) -> int:
        return num1 + num2

player1 = Player("Baba", 19)
player2 = Player("Smit", 19)
player3 = Player("Yash", 20)

player3.player_details()

print(f"{Player.add_somethings(1, 2)}")
print(f"{Player.add_somethings2(1, 2)}")
"""
we dont have access to the class in @staticmethod
and we do have access to the class in @classmethod
"""