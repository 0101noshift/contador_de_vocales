from tkinter import *

ventana = Tk()
ventana.title("Contador de Vocales")
ventana.geometry("530x140")
ventana.configure(bg="#FFF2CC")


def calcular_todos():
    global a_label_rta
    global e_label_rta
    global i_label_rta
    global o_label_rta
    global u_label_rta

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


a_label = Label(ventana, text="A =", font=(
    "Courier", 14, "bold"), bg="#FFF2CC").grid(row=0, column=0)
e_label = Label(ventana, text="E =", font=(
    "Courier", 14, "bold"), bg="#FFF2CC").grid(row=0, column=2)
i_label = Label(ventana, text="I =", font=(
    "Courier", 14, "bold"), bg="#FFF2CC").grid(row=0, column=4)
o_label = Label(ventana, text="O =", font=(
    "Courier", 14, "bold"), bg="#FFF2CC").grid(row=0, column=6)
u_label = Label(ventana, text="U =", font=(
    "Courier", 14, "bold"), bg="#FFF2CC").grid(row=0, column=8)

a_label_rta = Label(ventana, text=" ", font=(
    "Courier", 14, "bold"), bg="#FFE5CC", fg="#FF6565")
e_label_rta = Label(ventana, text=" ", font=(
    "Courier", 14, "bold"), bg="#FFE5CC", fg="#FF6565")
i_label_rta = Label(ventana, text=" ", font=(
    "Courier", 14, "bold"), bg="#FFE5CC", fg="#FF6565")
o_label_rta = Label(ventana, text=" ", font=(
    "Courier", 14, "bold"), bg="#FFE5CC", fg="#FF6565")
u_label_rta = Label(ventana, text=" ", font=(
    "Courier", 14, "bold"), bg="#FFE5CC", fg="#FF6565")

a_label_rta.grid(row=0, column=1)
e_label_rta.grid(row=0, column=3)
i_label_rta.grid(row=0, column=5)
o_label_rta.grid(row=0, column=7)
u_label_rta.grid(row=0, column=9)

btn1 = Button(ventana, text="CONTAR", command=calcular_todos,
              width=11, height=1, bg="yellow", font=("Courier", 12, "bold"))
btn1.grid(row=1, column=3, columnspan=3, sticky=S+E)

texEntry = Entry(ventana, bg="#fbc599", fg="#9b726f",
                 font=("Courier", 12, "bold"), width=50)
texEntry.focus()
texEntry.grid(row=2, column=0, columnspan=10)

ventana.mainloop()
