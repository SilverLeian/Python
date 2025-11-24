from dataclasses import dataclass
from enum import Enum

class AbilityType(Enum):
    DAMAGE = "Damage"
    HEAL = "Heal"
    DEBUff = "Debuff"
    SHIELD = "Shield"


@dataclass
class Ability:
    name: str
    type: AbilityType
    value: float

    def __str__(self):
        return self.name


@dataclass
class Pokemon:
    name: str
    level: int = 1
    xp: float = 0
    max_hp: int = 100
    current_hp: int = max_hp
    abilities: list

    def __str__(self):
        return self.name
    
    def useAbility(self, target: object, ability):
        return f"{self.name} used {ability} {target}"


# PICACHU SET
# Pica Abilities
thunder_bolt = Ability("Thunder Bolt", AbilityType.DAMAGE, 14.5)

picachu = Pokemon("Picachu", abilities=[thunder_bolt])



balbasaur = Pokemon("Balbasaur", xp=90)

print(picachu.useAbility(balbasaur))
# print(balbasaur)