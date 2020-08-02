import tkinter
from views.mainView import MainView


class MainController:

    def __init__(self):
        self.root = tkinter.Tk()
        self.main_view = MainView(self.root)
        # Event listeners setup
        self.main_view.test_btn.bind("<Button-1>", self.test_btn_action)

    def run(self):
        self.root.title("Path finder robot")
        self.root.mainloop()

    def test_btn_action(self, event):
        print("Hello World")