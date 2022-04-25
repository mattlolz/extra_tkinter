import random
from tkinter import *
window = Tk()
window.title("Idea generator")
window.configure(bg='#2aa5e8')
window.geometry("800x600")

none = ''

first = ['trustworthy', 'emotional', 'angry', 'sad', 'happy', 'intense', 'fearful']
second = ['pencil', 'apple', 'computer', 'movie', 'human', 'milk', 'orange juice', 'apple juice', 'pen']

def get_random():
    first_choice = random.choice(first)
    second_choice = random.choice(second)

    lab.configure(text=f'{first_choice} {second_choice}')
    lab.place(x=312.5, y=250, width=175)


lab = Label(window, text='Press generate to generate', font=('arial', 15))
lab.place(x=300, y=250, width=200, height=40)

b1 = Button(window, text='Generate', command=lambda: get_random(), font=('arial', 20))
b1.place(x=325, y=350, width=150, height=30)


window.mainloop()
