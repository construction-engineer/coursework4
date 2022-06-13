from dataclasses import dataclass
from typing import List
from random import uniform


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors: List[Armor]

    def get_weapon(self, weapon_name: str) -> Weapon:
        for weapon in self.weapons:
            if weapon.name == weapon_name:
                return weapon
        raise RuntimeError

    def get_armor(self, armor_name) -> Armor:
        for armor in self.armors:
            if armor.name == armor_name:
                return armor
        raise RuntimeError

    @property
    def weapons_names(self) -> List[str]:
        return [item.name for item in self.weapons]

    @property
    def armors_names(self) -> List[str]:
        return [item.name for item in self.armors]
