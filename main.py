# TODO: document
# TODO: make a history of criticals
# TODO: refine interface
# TODO: clean the code
import json
import random
import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from main_ui import UiMainWindow


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
            criticals = json.load(f)

        # Dictionary for critical lists
        # Each key should be a critical type, which are strings
        self.__critical_dict = {}
        for key in criticals:
            self.__critical_dict[key] = [Critical(**d) for d in criticals[key]]

    def random_select(self, crit_type: str) -> Critical:
        """Returns a randomly selected critical according to the type"""
        return random.choice(self[crit_type])

    def __getitem__(self, item):
        """Parser to the internal dictionary"""
        return self.__critical_dict[item]


# Ordenar esta mierda
HITS = CriticalLoader("hits.json")
FUMBLE = CriticalLoader("fumble.json")


class ButtonSelector:
    def __init__(self, ui):
        self.__ui = ui

    def add_critical_effect(self, effect: Critical):
        self.__ui.results_box.setHtml(f'<p style="color: blue"><strong>{effect.name}</strong></p>'
                                      f'<p>{effect.effect}</p>')

    def add_fumble_effect(self, effect: Critical):
        self.__ui.results_box.setHtml(f'<p style="color: red"><strong>{effect.name}</strong></p>'
                                      f'<p>{effect.effect}</p>')

    def get_bludgeoning_crit(self):
        self.add_critical_effect(HITS.random_select("bludgeoning"))

    def get_piercing_crit(self):
        self.add_critical_effect(HITS.random_select("piercing"))

    def get_slashing_crit(self):
        self.add_critical_effect(HITS.random_select("slashing"))

    def get_magic_crit(self):
        self.add_critical_effect(HITS.random_select("magic"))

    def get_melee_fumble(self):
        self.add_fumble_effect(FUMBLE.random_select("melee"))

    def get_ranged_fumble(self):
        self.add_fumble_effect(FUMBLE.random_select("melee"))

    def get_natural_fumble(self):
        self.add_fumble_effect(FUMBLE.random_select("natural"))

    def get_magic_fumble(self):
        self.add_fumble_effect(FUMBLE.random_select("magic"))


if __name__ == '__main__':
    app = QApplication([])

    # Interface
    ui_setter = UiMainWindow()

    # Main window
    mw = QMainWindow()

    # Setup UI
    ui_setter.setup_ui(mw)

    selector = ButtonSelector(ui_setter)

    # Signals
    ui_setter.bludgeoning_btn.clicked.connect(selector.get_bludgeoning_crit)
    ui_setter.slashing_btn.clicked.connect(selector.get_slashing_crit)
    ui_setter.piercing_btn.clicked.connect(selector.get_piercing_crit)
    ui_setter.magic_hit_btn.clicked.connect(selector.get_magic_crit)

    ui_setter.melee_btn.clicked.connect(selector.get_melee_fumble)
    ui_setter.ranged_btn.clicked.connect(selector.get_ranged_fumble)
    ui_setter.natural_btn.clicked.connect(selector.get_natural_fumble)
    ui_setter.magic_fumble_btn.clicked.connect(selector.get_magic_fumble)

    mw.show()

    sys.exit(app.exec_())
