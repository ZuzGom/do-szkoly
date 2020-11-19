from __future__ import unicode_literals
from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi, sqrt
from pathlib import Path


# kąt 67 linijka
# sinus 120 linijka

# numpy naprawić :c
# żeby czcz.get() zmienniał się podczas pracy animacji
# po co init

tlo = '#1C2429'  # taki ciemnoszaroniebieski

# definiowanie okna
okno = Tk()
okno.title('Układ Słoneczny')
okno['bg'] = tlo

ikona=Path('icona.ico')

if ikona.is_file():
    okno.iconbitmap('icona.ico')

# wykres

# fig to pole, a ax to konkretny wykres,
# w jednym polu może być kilka wykresów, w jedym wykresie wiele linii

fig, ax = plt.subplots(figsize=(7, 7))

plt.tight_layout()

fig.patch.set_facecolor('black')
ax.set_xlim(-10, 10)  # wielkość wykresu
ax.set_ylim(-10, 10)
ax.axis('off')


#próby (nieudane) usunięcia ramki

#fig.patch.set_visible(False)
#ax.patch.set_visible(False)
#fig = figure(frameon=False)
#for item in [fig, ax]:
#    item.patch.set_visible(False)
#ax.axis('off')
#ax.set_axis_off()

'''
axes[0,1].clear()
axes[1,0].axis("off")
axes[1,1].set_visible(False)
axes[0,2].remove()

'''

cosmic = FigureCanvasTkAgg(fig, master=okno)  # pole do osadzenia matplotlib w tkinter
cosmic.get_tk_widget().grid(row=2, column=2)


###### muszę poradzić sobię z deltą, żeby animacja kończyła się na 360 stopniach
d = np.linspace(0, 2*pi, 100)  # delta (chyba chodziło mi o alfę)  
# d = pd.Series(np.linspace(0, 2*pi, 100))


time_text = ax.text(0.02, 0.95, ' ', transform=ax.transAxes, color="white") # tekst który wyświetlał i dla każdej klatki, ale nic mi to nie mówiło


# def init():
#   time_text.set_text('')
#   line1.set_data([],[])
#   return line1, time_text

s = 4

slonce = plt.Circle((0, 0), s * 0.1, color='yellow')
ax.add_artist(slonce)

def run():

    def stop():
        if 'animacja' in locals():
            animacja.event_source.stop()
    stap = Button(planety, text="Stop", command=stop).grid(row=1, column=0)

    s = ss.get()  # skala
    cz = czcz.get() # upływ czasu
    slonce.set_radius(ss.get() * 0.1) 

    def animate(i):  # animacja wszystkich linii na raz

        line1, = ax.plot([], [])
        line2, = ax.plot([], [])
        line3, = ax.plot([], [])
        line4, = ax.plot([], [])
        line5, = ax.plot([], [])

        def orbita(e, a, T, g, col, i, line, ):  # po kolei: mimośród, mała półoś, duża, grubość linii, color, iterowana zmienna, linia
            b = sqrt(a ** 2 * (1 - e ** 2))  # mała półoś
            u = sqrt(a ** 2 - b ** 2)  # x przesunięty o ogniskową
            v = 0  # y
            plt.setp(line, animated=True, linestyle=':', linewidth=1.5 * g, color=col)
            t = (2 * pi) / T * d * i
            return a, b, u, v, t, T
        
        # definiuję dla każdej planety oddzielną linię

        if CheckMerk.get() == 1:
            a1, b1, u1, v1, t1, T1 = orbita(0.206, s * 0.388, s * 0.24, s * 0.2, 'rosybrown', i, line1)
            
            #### myślę, że należy zrobić to tutaj po sinusie, jednak nie mam pomysłu jak
            #### myślałam, żeby połączyć serie danych z pandas oraz array z numpy ale sama nie wiem
            
            line1.set_ydata(v1 + b1 * np.sin(d * cz * t1 / 50000))  # dlaczego tych linijek nie wstawiłam do funkcji orbita()?
            line1.set_xdata(u1 + a1 * np.cos(d * cz * t1 / 50000))  # nie wiem

        if CheckWenus.get() == 1:
            a2, b2, u2, v2, t2, T2 = orbita(0.0068, s * 0.723, s * 0.62, s * 0.4, 'mediumvioletred', i, line2)
            line2.set_ydata(v2 + b2 * np.sin(d * cz * t2 / 50000))
            line2.set_xdata(u2 + a2 * np.cos(d * cz * t2 / 50000))

        if CheckZiemia.get() == 1:
            a3, b3, u3, v3, t3, T3 = orbita(0.0147, s, s, s * 0.4, 'springgreen', i, line3)
            line3.set_ydata(v3 + b3 * np.sin(d * cz * t3 / 50000))
            line3.set_xdata(u3 + a3 * np.cos(d * cz * t3 / 50000))

        if CheckMars.get() == 1:
            a4, b4, u4, v4, t4, T4 = orbita(0.0934, s * 1.524, s * 1.88, s * 0.3, 'coral', i, line4)
            line4.set_ydata(v4 + b4 * np.sin(d * cz * t4 / 50000))
            line4.set_xdata(u4 + a4 * np.cos(d * cz * t4 / 50000))
            
        if CheckJow.get() == 1:			
            a5, b5, u5, v5, t5, T5 = orbita(0.0485, s * 5.203, s * 11.86, s, 'tan', i, line5)
            line5.set_ydata(v5 + b5 * np.sin(d * cz * t5 / 50000))
            line5.set_xdata(u5 + a5 * np.cos(d * cz * t5 / 50000))

        return line1, line2, line3, line4, line5,


    animacja = animation.FuncAnimation(fig, animate, frames=int(400 * s / cz), interval=20, blit=True)

    
    #poniższe funkcje są niepotrzebne, ponadto nie działają
    def star():
        if 'animacja' in locals():
            animacja.event_source.start()

    def clean():
        if 'animacja' in locals():
            animacja.frame_seq = animacja.new_frame_seq()

    def clean1():
        # os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        while True:  # Use True instead of 1
            run()
            if run() is None:  # The function call is equal to what it returned
                break
            else:
                continue
    #clean = Button(planety, text="Wyczyść", command=clean).grid(row=2, column=0)


# interfejs
tytul = Label(okno, text="\nSymulator ruchu planet w Układzie Słonecznym\n", bg=tlo, fg='white').grid(row=0, column=2)

# meni = Frame (okno, bg="black")
# meni.grid(row=0, column=0)

exit = Frame(okno)
exit.grid(row=3, column=3)
blackbutton = Button(exit, text="Wyjście", fg="black", bg="white", command=okno.quit).grid()

tcz = Label(okno, bg=tlo, fg='white', text="\n  upływ czasu  \n").grid(row=3, column=0)
czcz = IntVar()
sczas = Scale(okno, variable=czcz, bg=tlo, fg='gray',
              orient=HORIZONTAL, length=394, from_=1, to_=200).grid(row=3, column=2)
czcz.set(10)


sca = Frame (okno, bg=tlo)
sca.grid(row=2, column=3)
tss= Label(sca, bg =tlo, fg='white', text="       skala       \n").grid()
ss = IntVar()
sss= Scale(sca, variable=ss, bg=tlo, fg='gray',
           orient=VERTICAL, length= 394, from_=1, to_=5).grid()
ss.set(4)


planety = Frame(okno, bg=tlo)
planety.grid(row=2, column=0)


CheckMerk = IntVar()
CheckWenus = IntVar()
CheckZiemia = IntVar()
CheckMars = IntVar()
CheckJow = IntVar()
CheckSat = IntVar()

tlop =tlo
start = Button(planety, text="Start", command=run).grid(row=0, column=0)
stap = Button(planety, text="Stop").grid(row=1, column=0)
#clean = Button(planety, text="Wyczyść").grid(row=2, column=0)

blank = Label(planety,text="\n\n", bg=tlo).grid()

merkury = Checkbutton(planety, text="Merkury", fg="peru", bg=tlop,
                      variable=CheckMerk, onvalue=1, offvalue=0).grid(sticky=W)

wenus = Checkbutton(planety, text="Wenus", fg='mediumvioletred', bg=tlop,
                    variable=CheckWenus, onvalue=1, offvalue=0).grid(sticky=W)

ziemia = Checkbutton(planety, text="Ziemia", fg="springgreen", bg=tlop,
                     variable=CheckZiemia, onvalue=1, offvalue=0).grid(sticky=W)

mars = Checkbutton(planety, text=" Mars", fg="coral", bg=tlop,
                   variable=CheckMars).grid(sticky=W)

jowisz = Checkbutton(planety, text="Jowisz", fg="tan", bg=tlop,
                     variable=CheckJow, onvalue=1, offvalue=0).grid(sticky=W)

saturn = Checkbutton(planety, text="Saturn", fg="lightsteelblue", bg=tlop,
                     variable=CheckSat, onvalue=1, offvalue=0).grid(sticky=W)


# funkcja to zmieniania labeli to mylabel.configure

okno.mainloop()
