# TODO: document
# TODO: make a history of criticals
# TODO: refine interface
# TODO: clean the code
import json
import random
import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from main_ui import Ui_MainWindow


class Critical:
    def __init__(self, name="", effect="", **kwargs):
        self.__name = name
        self.__effect = effect

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

    def __lt__(self, other) -> bool:
        return self.__name < other.name

    def __repr__(self) -> str:
        return f"{self.__name}"

    def __str__(self) -> str:
        return f"{self.__name}\n{self.__effect}"


class CriticalLoader:
    def __init__(self, filename):
        with open(filename) as f:
            criticals = json.load(f)

        self.critical_dict = {}
        for key in criticals:
            self.critical_dict[key] = [Critical(**d) for d in criticals[key]]

    def random_select(self, crit_type) -> Critical:
        return random.choice(self[crit_type])

    def __getitem__(self, item):
        return self.critical_dict[item]


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
    ui = Ui_MainWindow()

    # Main window
    mw = QMainWindow()

    # Setup UI
    ui.setupUi(mw)

    selector = ButtonSelector(ui)

    # Signals
    ui.bludgeoning_btn.clicked.connect(selector.get_bludgeoning_crit)
    ui.slashing_btn.clicked.connect(selector.get_slashing_crit)
    ui.piercing_btn.clicked.connect(selector.get_piercing_crit)
    ui.magic_hit_btn.clicked.connect(selector.get_magic_crit)

    ui.melee_btn.clicked.connect(selector.get_melee_fumble)
    ui.ranged_btn.clicked.connect(selector.get_ranged_fumble)
    ui.natural_btn.clicked.connect(selector.get_natural_fumble)
    ui.magic_fumble_btn.clicked.connect(selector.get_magic_fumble)

    mw.show()

    sys.exit(app.exec_())
