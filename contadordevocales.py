from tkinter import *

ventana = Tk()
ventana.title("Contador de Vocales")
ventana.geometry("450x100")
ventana.resizable(1,1)
ventana.configure(bg="#FFF2CC")


#Función
def calcular_todos(*args):
    vowels = 'aeiou'
    ip_str = str(texEntry.get())
    ip_str = ip_str.casefold()
    count = {}.fromkeys(vowels, 0)

    for i in ip_str:
        if i in count:
            count[i] += 1

    [a_count, e_count, i_count, o_count, u_count] = count.values()

    a_label_rta.config(text=a_count)
    e_label_rta.config(text=e_count)
    i_label_rta.config(text=i_count)
    o_label_rta.config(text=o_count)
    u_label_rta.config(text=u_count)

#A
a_label = Label(ventana,
                text="A =",
                font=("Algerian 14 bold"),
                bg="#FFF2CC").grid(row=0, column=0)
a_label_rta = Label(ventana,
                    text=" ",
                    font=("Algerian 14 bold"),
                    bg="#FFE5CC",
                    fg="#FF6565")
a_label_rta.grid(row=0, column=1)

#E
e_label = Label(ventana,
                text="E =",
                font=("Algerian", 14, "bold"),
                bg="#FFF2CC").grid(row=0, column=2)
e_label_rta = Label(ventana,
                    text=" ",
                    font=("Algerian 14 bold"),
                    bg="#FFE5CC",
                    fg="#FF6565")
e_label_rta.grid(row=0, column=3)

#I
i_label = Label(ventana,
                text="I =",
                font=("Algerian 14 bold"),
                bg="#FFF2CC").grid(row=0, column=4)
i_label_rta = Label(ventana,
                    text=" ",
                    font=("Algerian 14 bold"),
                    bg="#FFE5CC",
                    fg="#FF6565")
i_label_rta.grid(row=0, column=5)

#O
o_label = Label(ventana,
                text="O =",
                font=("Algerian 14 bold"),
                bg="#FFF2CC").grid(row=0, column=6)
o_label_rta = Label(ventana,
                    text=" ",
                    font=("Algerian 14 bold"),
                    bg="#FFE5CC",
                    fg="#FF6565")
o_label_rta.grid(row=0, column=7)

#U
u_label = Label(ventana,
                text="U =",
                font=("Algerian 14 bold"),
                bg="#FFF2CC").grid(row=0, column=8)
u_label_rta = Label(ventana,
                    text=" ",
                    font=("Algerian 14 bold"),
                    bg="#FFE5CC",
                    fg="#FF6565")
u_label_rta.grid(row=0, column=9)

texEntry = Entry(ventana,
                 bg="#fbc599",
                 fg="#9b726f",
                 font=("Algerian 12 bold"),
                 width=35)
texEntry.bind("<Key>", calcular_todos)
texEntry.grid(row=2, column=1, columnspan=8)

ventana.mainloop()
