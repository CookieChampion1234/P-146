from tkinter import*

root = Tk()

root.title("Fibonacci Sequence")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci Series")
label_flower = Label(root)
label_spiral = Label(root)

number = Entry(root)
number.place(relx=0.5, rely=0.4, anchor=CENTER)

def Fibonacci():
    num = int(number.get())
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while(counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
    label_flower['text'] = "Flower is fully bloomed"
    label_spiral['text'] = " Spirals in the right direction are " + \
        str(first_no) + " and spirals in the left direction are " + \
        str(second_no) + "\n. Total spiral are " + str(sum)

btn = Button(root, text="Show Fibonacci sequence", command=Fibonacci)

btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop()