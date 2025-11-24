from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    hobbies: list
    is_alive: bool = True

    def __str__(self):
        return " ".join(self.name.split()).title()
    
    def play(self, index: int = 0):
        limit = len(self.hobbies) - 1

        if index > limit:
            return print("Index must be within 0 to ", limit)
        
        if index < 0:
            return print("Index must not be less than 0")

        return self.hobbies[index]

@dataclass
class Donsal(Person):
    profession: str
    eabab: list