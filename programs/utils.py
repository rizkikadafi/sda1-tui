from textual.app import ComposeResult
from textual.widgets import Label, Static

class HeaderProgram(Static):
    DEFAULT_CSS = """
    HeaderProgram {
        dock: top;
        width: 100%;
        background: $foreground 5%;
        color: $text;
        height: 3;
    }
    
    HeaderProgram Label {
        width: 100%;
        height: 100%;
        content-align: center middle;
    }
    """
    def __init__(self, title: str):
        super().__init__()
        self.title = title

    def compose(self) -> ComposeResult:
        yield Label(self.title)
