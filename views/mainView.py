from tkinter import *
from PIL import ImageTk, Image

class MainView:

    def __init__(self, root_window, terreno):
        self.main_container = Frame(root_window)
        self.main_container.grid(row=0, column=0)
        self.btn_container = Frame(root_window)
        self.btn_container.grid(row=0, column=1)
        self.change_btn = Button(self.btn_container, text="presioname")
        self.change_btn.grid(row=0, column=0)
        # Cargar imagenes
        self.terreno_normal = ImageTk.PhotoImage(Image.open("assets/normal.png"))
        self.terreno_moderado = ImageTk.PhotoImage(Image.open("assets/moderado.png"))
        self.terreno_dificil = ImageTk.PhotoImage(Image.open("assets/dificil.png"))
        self.terreno_bloqueado = ImageTk.PhotoImage(Image.open("assets/bloqueado.png"))
        # Display del terreno
        self.terrain_grid = [[0 for j in range(20)] for i in range(20)]
        self.terrain_img_grid = [[0 for j in range(20)] for i in range(20)]
        for fila_terreno in range(20):
            for bloque in range(20):
                if terreno[fila_terreno][bloque] == 1:
                    bloque_canvas = Canvas(self.main_container, width=20, height=20, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_normal, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas
                elif terreno[fila_terreno][bloque] == 2:
                    bloque_canvas = Canvas(self.main_container, width=20, height=20, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_moderado, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas
                elif terreno[fila_terreno][bloque] == 3:
                    bloque_canvas = Canvas(self.main_container, width=20, height=20, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_dificil, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas
                else:
                    bloque_canvas = Canvas(self.main_container, width=20, height=20, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_bloqueado, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas

