class MobileGame:
    # Constructor to initialize the game
    def __init__(self, name, genre, platform):
        self.name = name
        self.genre = genre
        self.platform = platform

    # Method to display game details
    def get_details(self):
        return f"{self.name} is a {self.genre} game available on {self.platform}."

    # Method to play the game
    def play(self):
        return f"Starting the game {self.name}. Have fun playing!"

# Inheriting from MobileGame


class MultiplayerGame(MobileGame):
    def __init__(self, name, genre, platform, player_count):
        super().__init__(name, genre, platform)
        self.player_count = player_count

    # Overriding the method
    def play(self):
        return f"Starting the multiplayer game {self.name} with {self.player_count} players. Enjoy!"


# Creating instances
game1 = MobileGame("Candy Crusader", "Puzzle", "iOS and Android")
game2 = MultiplayerGame("Battle Royale Pro", "Action", "Android", 100)

print(game1.get_details())
print(game1.play())
print(game2.get_details())
print(game2.play())


#polymorphism challenge 

# Parent class
class Mover:
    def move(self):
        return "I'm moving in a generic way!"

# Animal classes inheriting from Mover


class Dog(Mover):
    def move(self):
        return "I run on all fours! 🐕"


class Bird(Mover):
    def move(self):
        return "I soar through the skies! 🐦"


class Fish(Mover):
    def move(self):
        return "I glide through the water! 🐟"

# Vehicle classes inheriting from Mover


class Car(Mover):
    def move(self):
        return "I drive on the road! 🚗"


class Plane(Mover):
    def move(self):
        return "I fly high in the sky! ✈️"


class Boat(Mover):
    def move(self):
        return "I sail across the sea! 🛥️"


# Using polymorphism to demonstrate the unique behavior of each class
movers = [Dog(), Bird(), Fish(), Car(), Plane(), Boat()]
for mover in movers:
    print(mover.move())
