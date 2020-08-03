from PIL import Image
import tkinter

def get_img_data():
    return {
        "normal": Image.open("assets/normal.png"),
        "moderado": Image.open("assets/moderado.png"),
        "dificil": Image.open("assets/dificil.png"),
        "bloqueado": Image.open("assets/bloqueado.png")
    }