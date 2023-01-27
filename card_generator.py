import random

# Generates Character cards

# Class to create the card objects
class Character_Card:
    def __init__(self, name, attack, defense, char_type):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.rating = self.attack + self.defense
        self.char_type = char_type

    def print_character(self):
        print(self.name)
        print("Attack:", self.attack, "Defense:", self.defense, "Rating:", self.rating)
        print("Type:", self.char_type)
        print("*")

# Class to create the eck objects
class Deck:
    def __init__(self):
        pass

    def set_random_deck(card_list):
        deck_limit = 20
        deck_list = []
        card_count = len(card_list)
        for card in range(deck_limit):
            index = random.randint(1, card_count)
            deck_list.append(card_list[index-1])
        return deck_list

# Starter card set

villager = Character_Card("Villager", 1, 1, "Human")
guard = Character_Card("Guard", 2, 2, "Human")
soldier = Character_Card("Soldier", 3, 2, "Human")
knight = Character_Card("Knight", 4, 4, "Human")
hunter = Character_Card("Hunter", 4, 3, "Human")
rogue = Character_Card("Rogue", 3, 2, "Human")
wizard = Character_Card("Wizard", 3, 1, "Human")
legend_knight = Character_Card("Legendary Knight", 6, 7, "Human")
rat = Character_Card("Rat", 1, 1, "Animal")
goblin = Character_Card("Goblin", 2, 1, "Monster")
slime = Character_Card("Slime", 1, 2, "Monster")
wolf = Character_Card("Wolf", 4, 2, "Animal")
zombie = Character_Card("Zombie", 3, 3, "Monster")
skeleton = Character_Card("Skeleton", 3, 4, "Monster")
dragon = Character_Card("Dragon", 6, 6, "Monster")

# Card set lists
0
starter_cards = (villager, guard, soldier, knight, hunter, rogue, wizard, legend_knight, rat, goblin, slime, wolf, zombie, skeleton, dragon)
starter_names = []
for card in starter_cards:
    starter_names.append(card.name)

# Decks
deck_one = Deck9
deck_two = Deck

def random_deck_gen(deck_one, deck_two):
    deck_one = deck_one.set_random_deck(starter_names)
    deck_two = deck_two.set_random_deck(starter_names)

random_deck_gen(deck_one, deck_two)
print(deck_one)/0