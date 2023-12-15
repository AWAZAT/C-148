from tkinter import *
import random

root=Tk()

root.title("Kiddzanina gift donation")
root.geometry("500x500")

list1 = ["Bottle", "Chocolates", "Chips", "Gift Card", "Toy"]
print(list1)

def random_number():
    random_no = random.randint(0, 4)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("You got: " + random_lucky_friend)
    
btn1 = Button(root)
btn1 = Button(root, text="What Will This Kid Get? ", command = random_number)
btn1.place(relx= 0.5, rely = 0.5, anchor = CENTER )


root.mainloop()