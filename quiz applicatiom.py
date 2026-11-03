from tkinter import *

root = Tk()
root.title("Quiz Application")
root.geometry("400x300")

Label(root, text="What is the capital of India?").pack()

answer = StringVar()

Radiobutton(root, text="Chennai", variable=answer, value="Chennai").pack()
Radiobutton(root, text="Mumbai", variable=answer, value="Mumbai").pack()
Radiobutton(root, text="Delhi", variable=answer, value="Delhi").pack()
Radiobutton(root, text="Kolkata", variable=answer, value="Kolkata").pack()

result = Label(root, text="")
result.pack()

def check():
    if answer.get() == "Delhi":
        result.config(text="Correct", fg="green")
    else:
        result.config(text="Wrong", fg="red")

Button(root, text="Submit", command=check).pack()

root.mainloop()