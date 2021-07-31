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
    """Parser for the buttons.

    Each method sets the text box in the interface with the right format for the required
    effect, be it a critical hit or a fumble.
    """

    def __init__(self, ui):
        # Just sets the interface to update with the effects
        self.__ui = ui

    def get_multiplier(self):
        if self.__ui.crit_mult_x2.isChecked():
            return 1
        elif self.__ui.crit_mult_x3.isChecked():
            return 2
        elif self.__ui.crit_mult_x4.isChecked():
            return 3
        return -1

    def add_critical_effect(self, effects: list[Critical]):
        """Sets text for critical hit"""
        previous_text = self.__ui.results_box.toHtml()
        text = ''
        for effect in effects:
            text += f'<p style="color: blue"><strong>{effect.name}</strong></p>' \
                    f'<p>{effect.effect}</p><hr>'

        self.__ui.results_box.setHtml(text + previous_text)

    def add_fumble_effect(self, effect: Critical):
        """Sets text for critical fumble"""
        previous_text = self.__ui.results_box.toHtml()
        text = f'<p style="color: red"><strong>{effect.name}</strong></p>' \
               f'<p>{effect.effect}</p><hr>'
        self.__ui.results_box.setHtml(text + previous_text)

    def get_critical(self, crit_type: str):
        effects = [HITS.random_select(crit_type) for _ in range(self.get_multiplier())]
        self.add_critical_effect(effects)

    def get_fumble(self, fumble_type: str):
        self.add_fumble_effect(FUMBLE.random_select(fumble_type))


if __name__ == '__main__':
    # Main application
    app = QApplication([])

    # Interface
    ui_setter = UiMainWindow()

    # Main window
    mw = QMainWindow()

    # Setup UI
    ui_setter.setup_ui(mw)

    selector = ButtonSelector(ui_setter)

    # Set signals and targets
    ui_setter.bludgeoning_btn.clicked.connect(lambda: selector.get_critical("bludgeoning"))
    ui_setter.slashing_btn.clicked.connect(lambda: selector.get_critical("slashing"))
    ui_setter.piercing_btn.clicked.connect(lambda: selector.get_critical("piercing"))
    ui_setter.magic_hit_btn.clicked.connect(lambda: selector.get_critical("magic"))

    ui_setter.melee_btn.clicked.connect(lambda: selector.get_fumble("melee"))
    ui_setter.ranged_btn.clicked.connect(lambda: selector.get_fumble("ranged"))
    ui_setter.natural_btn.clicked.connect(lambda: selector.get_fumble("natural"))
    ui_setter.magic_fumble_btn.clicked.connect(lambda: selector.get_fumble("magic"))

    # Show main window
    mw.show()

    # Main loop
    sys.exit(app.exec_())
