from tkinter import* 
from PIL import ImageTk, Image 
import random
root=Tk()

root.title("pokemon")
root.geometry("600x400")

root.configure(background="yellow2")

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))


pokemon_list = [abra,bulbasour,charmender,pikachu,jigglypuff]
pokemon_power =[30,60,50,100,70]

player1=Label(root,text="Player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2=Label(root,text="Player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root,bg="royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root,bg="royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

 

pic = Label(root)
pic.place(relx=0.5, rely=0.5, anchor= CENTER)


player1_score = 0 
def player1():
    global player1_score
    random_no = random.randint(0,4)
    random_pokemon = pokemon_power[random_no]
    random_pic = pokemon_list[random_no]
    pic["image"] = random_pic
    player1_score = player1_score + random_pokemon
    player_1_score_label["text"]=str(player1_score)
    
player_1_btn = Button(root, image= button, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)

player2_score = 0 
def player2():
    global player2_score
    random_no2 = random.randint(0,4)
    random_pokemon2 = pokemon_power[random_no2]
    random_pic2 = pokemon_list[random_no2]
    pic["image"] = random_pic2
    player2_score = player2_score + random_pokemon2
    player_2_score_label["text"]=str(player2_score)
    
player_2_btn = Button(root, image= button, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6, anchor = CENTER)

    
root.mainloop()


