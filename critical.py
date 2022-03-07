import json
import random


class Critical:
    """Provides handlers for critical (hit or fumble) descriptions

    It contains the name and effect of the critical effect.
    """

    def __init__(self, name: str = "", effect: str = "", **kwargs):
        """Constructor"""
        self.__name = name
        self.__effect = effect

        # I need to check whether this will be necessary in the future
        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

        return

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect):
        self.__effect = effect

    # Operator needed for sorting
    def __lt__(self, other) -> bool:
        return self.__name < other.name

    def __repr__(self) -> str:
        return f"{self.__name}"

    def __str__(self) -> str:
        return f"{self.__name}\n{self.__effect}"


class CriticalLoader:
    """Loader for JSON files with information for critical roles"""

    def __init__(self, filename):
        # Loads the required file
        with open(filename) as f:
            critical_dict = json.load(f)

        # Dictionary for critical lists
        # Each key should be a critical type, which are strings
        self.__critical_dict = {}
        for key in critical_dict:
            self.__critical_dict[key] = [Critical(**d) for d in critical_dict[key]]

    def random_select(self, crit_type: str) -> Critical:
        """Returns a randomly selected critical according to the type"""
        return random.choice(self[crit_type])

    def __getitem__(self, item):
        """Parser to the internal dictionary"""
        return self.__critical_dict[item]


# CONSTANTS
HITS = CriticalLoader("hits.json")
FUMBLE = CriticalLoader("fumble.json")
