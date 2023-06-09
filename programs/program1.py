from textual.screen import Screen
from textual.binding import Binding
from textual.app import ComposeResult
from textual.widgets import Footer, Button, Static, OptionList

from .utils import HeaderProgram

class Screen1(Screen):
    BINDINGS = [
        Binding(key="b", action="back", description="Kembali"),
        Binding(key="q", action="quit", description="Keluar Program"),
    ]
    def compose(self) -> ComposeResult:
        yield HeaderProgram("Program 1")
        yield OptionList(
            "Biner", 
            "Oktal",
            "Desimal",
            "Hexadesimal"
        )
        yield Footer()
