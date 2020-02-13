from tkinter import *
from tkinter import ttk

class Interface:



    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.state("zoomed")
        self.fenetre.title("Simulation Réseau LTE")
        data_frame = LabelFrame(self.fenetre, bg="blue")
        data_frame.pack(fill=BOTH, expand=True)
        self.nb = ttk.Notebook(data_frame)
        self.nb.pack(fill='both', expand='yes')

        self.f1 = Canvas(data_frame, bg="white")


        self.f1.bind("<B1-Motion>", self.callback)
        self.f2 = Text(data_frame)

        self.nb.add(self.f1, text='Simulation')
        self.nb.add(self.f2, text='Output')


        controle_frame = LabelFrame(self.fenetre, text="Controle")
        controle_frame.pack(side=BOTTOM)
        bouton_start = Button(controle_frame, text="start")
        bouton_start.pack(side=LEFT)
        bouton_pause = Button(controle_frame, text="pause")
        bouton_pause.pack(side=LEFT)
        bouton_stop = Button(controle_frame, text="arrêt", command=self.creation_polygones)
        bouton_stop.pack(side=LEFT)

        self.fenetre.mainloop()

    def salut(self):
        print("Hello Jean Claude")

    def creation_polygones(self):
        w,h = self.f1.winfo_width(), self.f1.winfo_height()
        h = h - 10
        w = w - 10
        center_x = int(w/2)
        center_y = int(h/2)
        quart_y = int(h/4)
        liste_points1 = [center_x-2.5*quart_y,center_y,
                         center_x-2*quart_y,quart_y,
                         center_x-quart_y,quart_y,
                         center_x-0.5*quart_y,center_y,
                         center_x-quart_y,3*quart_y,
                         center_x-2*quart_y,3*quart_y]
        liste_points2 = [center_x-quart_y,quart_y,
                         center_x-0.5*quart_y,10,
                         center_x+0.5*quart_y,10,
                         center_x+quart_y,quart_y,
                         center_x+0.5*quart_y,center_y,
                         center_x-0.5*quart_y,center_y]
        liste_points3 = [center_x+0.5*quart_y,center_y,
                         center_x+quart_y,quart_y,
                         center_x+2*quart_y, quart_y,
                         center_x+2.5*quart_y, center_y,
                         center_x+2*quart_y, 3*quart_y,
                         center_x+quart_y,3*quart_y]
        liste_points4 = [center_x-quart_y,quart_y + center_y,
                         center_x-0.5*quart_y,center_y,
                         center_x+0.5*quart_y,center_y,
                         center_x+quart_y,quart_y+center_y,
                         center_x+0.5*quart_y,center_y+center_y,
                         center_x-0.5*quart_y,center_y+center_y]
        self.f1.create_polygon(liste_points1, outline='#fb0', width=2, fill='#ffe499')
        self.f1.create_polygon(liste_points2, outline='#1f1', width=2, fill='#99ff99')
        self.f1.create_polygon(liste_points3, outline='#05f', width=2, fill='#99bbff')
        self.f1.create_polygon(liste_points4, outline='#f50', width=2, fill='#ffbb99')
        self.f1.pack()
        self.nb.add(self.f1, text='Simulation')
        self.nb.add(self.f2, text='Output')

        print(w)
        print(h)

    def callback(self, event):
        self.fenetre.focus_set()
        print("clicked at", event.x, event.y)
