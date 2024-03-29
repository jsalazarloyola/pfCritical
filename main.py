# TODO: document
# TODO: refine interface
# TODO: clean the code
# TODO: should I get a unique function to update the text, with flags to select between fumble
# and hit?
# TODO: add selector for language of the interface
import sys

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QTranslator, QLocale

from main_ui import UiMainWindow
from critical import Critical, HITS, FUMBLE


class ButtonSelector:
    """Parser for the buttons.

    Each method sets the text box in the interface with the right format for the required
    effect, be it a critical hit or a fumble.
    """

    def __init__(self, ui):
        # The interface from whence the buttons will be retrieved and where the text will be
        # updated
        self.__ui = ui

        # The text to put in the (HTML) text box of the interface
        self.__text = ""
        # The style for the elements
        self.__stylesheet = "<style>" \
                            ".critical {color: dodgerblue; font-weight: bold;}" \
                            ".fumble {color: red; font-weight: bold;}" \
                            ".new {background-color: cornsilk; color: black;}" \
                            "</style>"

    def update_text(self, text):
        """Updates the text to show in the interface"""
        self.__text = self.__text.replace('class="new"', 'class="old"')
        self.__text = text + self.__text

    def update_box(self):
        """Updates the HTML in results' box in the interface"""
        self.__ui.results_box.setHtml(self.__stylesheet + self.__text)

    def get_multiplier(self):
        """Gets how many effects should be selected"""
        if self.__ui.crit_mult_x2.isChecked():
            return 1
        elif self.__ui.crit_mult_x3.isChecked():
            return 2
        elif self.__ui.crit_mult_x4.isChecked():
            return 3
        # Just in case
        return -1

    def add_critical_effect(self, effects: list[Critical]):
        """Sets text for critical hit"""
        text = ''
        for effect in effects:
            text += f'<div class="new">' \
                    f'<span class="critical">{effect.name}</span><br>' \
                    f'<span>{effect.effect}</span>' \
                    f'<hr></div>'

        self.update_text(text)
        self.update_box()

    def add_fumble_effect(self, effect: Critical):
        """Sets text for critical fumble"""
        text = f'<div class="new">' \
               f'<span class="fumble">{effect.name}</span><br>' \
               f'<span>{effect.effect}</span>' \
               f'</div><hr>'
        self.update_text(text)
        self.update_box()

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
    # Localización y weás :v
    translator = QTranslator()
    locale = QLocale("es")
    translator.load(locale, "mainWindow", prefix="_", directory='i18n')
    app.installTranslator(translator)

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
