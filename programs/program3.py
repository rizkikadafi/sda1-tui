from textual.screen import Screen
from textual.binding import Binding
from textual.app import ComposeResult
from textual.widgets import Label, Header, Footer, Button, Static

from .utils import HeaderProgram

class Screen3(Screen):
    BINDINGS = [
        Binding(key="b", action="back", description="Kembali"),
        Binding(key="q", action="quit", description="Keluar Program"),
    ]
    def compose(self) -> ComposeResult:
        yield HeaderProgram("Program 3")
        yield Footer()
