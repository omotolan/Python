class Player:
    def __init__(self, nameless: str, age: int) -> None:
        self.name = nameless
        self.age = age


player1 = Player("messi", 45)
print(player1.name)
