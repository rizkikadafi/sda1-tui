from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, Footer, Button, Static, Label
from textual.screen import Screen
from textual.containers import Container, Vertical, Horizontal

from programs.program1 import Screen1

#Description widgets
class Description(Static):
    DEFAULT_CSS = """
        #desc {
            margin: 1 0 0 0;
            color: #f8f8f2;
        }
    """

    def __init__(self, desccription: str, id: str):
        super().__init__()
        self.description = desccription
        self.id = id

    def compose(self) -> ComposeResult:
        yield Label("[bold underline]Deskripsi:[/]")
        yield Static(self.description, id="desc")

# Main Screen
class MainScreen(Screen):
    BINDINGS = [
        Binding(key="q", action="quit", description="Keluar Program"),
    ]

    DESCRIPTION = """Project Struktur Data dan Algoritma (SDA) 1 merupakan project yang berisi kumpulan program implementasi struktur data tumpukan (stack)"""

    def compose(self) -> ComposeResult:
        # header
        header = Header()
        header.tall = True
        yield header

        # Description
        yield Description(id="description", desccription=self.DESCRIPTION)

        # Menu
        yield Label("[bold underline]Menu Program", id="menu-title")
        with Container(id="menus"):
            yield Button("Program 1", classes="menu", variant="primary")
            yield Button("Program 2", classes="menu", variant="primary")
            yield Button("Program 3", classes="menu", variant="primary")
            yield Button("Program 4", classes="menu", variant="primary")

        # Footer
        yield Footer()

# Main App
class Main(App):
    CSS_PATH = "main.css"
    TITLE = "Project SDA 1"
    SUB_TITLE = "Implementasi Struktur Data Stack"

    def on_mount(self):
        self.install_screen(MainScreen(), "main_screen")
        self.push_screen("main_screen")

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "program1":
            self.install_screen(Screen1(), name="screen1")
            self.push_screen("screen1")

    def action_back(self) -> None:
        self.uninstall_screen(self.pop_screen())

if __name__ == "__main__":
    app = Main()
    app.run()
