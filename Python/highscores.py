from tkinter import *
from tkinter import simpledialog

#pop up window for name
def get_me():
    s = simpledialog.askstring("input string", "Enter your name: ")
    print(s)

root = Tk()

button = Button(root, text="popup", command=get_me)
button.pack()
root.geometry("300x300")
root.mainloop()
#end pop up


name = input("Enter your name: ")
score = input("Enter your score: ")

f = open('test.txt', 'w')              # opens file to read contents
f.write(name+"       ")                          # writes username in file
f.write(score)                          # writes username in file


print("\nUsername | Score  | ")
with open('test.txt', 'r') as f:        # displays file contents
    f_contents = f.read()
    print(f_contents)
