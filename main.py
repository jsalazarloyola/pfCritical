# TODO: document
# TODO: refine interface
# TODO: clean the code
import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from main_ui import UiMainWindow
from critical import Critical, HITS, FUMBLE


class ButtonSelector:
    """Parser for the buttons.

    Each method sets the text box in the interface with the right format for the required
    effect, be it a critical hit or a fumble.
    """

    def __init__(self, ui):
        # Just sets the interface to update with the effects
        self.__ui = ui

    def get_multiplier(self):
        # Gets how many effects should be selected
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
        """Gets the critical hit effect and puts it in the text box"""
        effects = [HITS.random_select(crit_type) for _ in range(self.get_multiplier())]
        self.add_critical_effect(effects)

    def get_fumble(self, fumble_type: str):
        """Gets the fumble effect and puts it in the text box"""
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
