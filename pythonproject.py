# final code 
# smile man
import time
start_time=time.time()
from tkinter import HIDDEN, NORMAL, Tk, Canvas
def smile_man() :
    
    def toggle_eyes():
        current_color = c.itemcget(eye_left, 'fill')
        new_color = c.body_color if current_color == 'white' else 'white'
        current_state = c.itemcget(pupil_left, 'state')
        new_state = NORMAL if current_state == HIDDEN else HIDDEN
        c.itemconfigure(pupil_left, state=new_state)
        c.itemconfigure(pupil_right, state=new_state)
        c.itemconfigure(eye_left, fill=new_color)
        c.itemconfigure(eye_right, fill=new_color)

    def blink():
        toggle_eyes()
        root.after(250, toggle_eyes)
        root.after(3000, blink)

    def toggle_pupils():
        if not c.eyes_crossed:
            c.move(pupil_left, 10, -5)
            c.move(pupil_right, -10, -5)
            c.eyes_crossed = True
        else:
            c.move(pupil_left, -10, 5)
            c.move(pupil_right, 10, 5)
            c.eyes_crossed = False

    def toggle_tongue():
        if not c.tongue_out:
            c.itemconfigure(tongue_tip, state=NORMAL)
            c.itemconfigure(tongue_main, state=NORMAL)
            c.tongue_out = True
        else:
            c.itemconfigure(tongue_tip, state=HIDDEN)
            c.itemconfigure(tongue_main, state=HIDDEN)
            c.tongue_out = False
    def cheeky(event):
        toggle_tongue()
        toggle_pupils()
        hide_happy(event)
        root.after(1000, toggle_tongue)
        root.after(1000, toggle_pupils)
        return

    def show_happy(event):
        if (20 <= event.x and event.x <= 350) and (20 <= event.y and event.y <= 350):
            c.itemconfigure(cheek_left, state=NORMAL)
            c.itemconfigure(cheek_right, state=NORMAL)
            c.itemconfigure(mouth_happy, state=NORMAL)
            c.itemconfigure(mouth_normal, state=HIDDEN)
            c.itemconfigure(mouth_sad, state=HIDDEN)
            c.happy_level = 10
        return

    def hide_happy(event):
        c.itemconfigure(cheek_left, state=HIDDEN)
        c.itemconfigure(cheek_right, state=HIDDEN)
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=NORMAL)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        return

    def sad():
        if c.happy_level == 0:
            c.itemconfigure(mouth_happy, state=HIDDEN)
            c.itemconfigure(mouth_normal, state=HIDDEN)
            c.itemconfigure(mouth_sad, state=NORMAL)
        else:
            c.happy_level -= 1
        root.after(5000, sad)

    root = Tk()
    root.title("Screen pet")
    c = Canvas(root, width=400, height=400)
    c.configure(bg='dark blue', highlightthickness=0)
    c.body_color = 'SkyBlue1'

    body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
    ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
    ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)
    foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
    foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

    eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
    pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
    eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
    pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')


    mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
    mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
    mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
    tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
    tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

    cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
    cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

    c.pack()
    c.bind('<Motion>', show_happy)
    c.bind('<Leave>', hide_happy)
    c.bind('<Double-1>', cheeky)

    c.happy_level = 10
    c.eyes_crossed = False
    c.tongue_out = False

    root.after(1000, blink)
    root.after(5000, sad)
    root.mainloop()

from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font
# rock paper scissor 
def rock_paper_scissor():
    import random
    user_win=0
    computer_win=0
    game_tied=0
    options=["stone","paper","scissor","test"]
    options[0]
    while True:
        user_input=input("Type stone/paper/scissor or q to quit: ").lower()
        if user_input=="q":
            break
    
        if user_input not in  options:
            continue
        random_number=random.randint(0,2)
        #rock:0,paper:1,scissors:2
        computer_pick=options[random_number]
        print("computer picked",computer_pick+".")
        if user_input == "stone" and computer_pick=="scissor":
            print("You Won!")
            user_win+=1
        elif user_input=="scissor" and computer_pick=="paper":
            print("You Won!")
            user_win+=1
        elif user_input=="paper" and computer_pick=="stone":
            print("You Won!")
            user_win+=1
        elif user_input==computer_pick:
            print("Game Tied!")
            game_tied+=1
        else:
            print("You Lost!")
            computer_win+=1
    print("You Won",user_win,"times.")
    print("The computer won",computer_win,"times.")
    print(game_tied,"Game Tied.")
    print("Goodbye!")
# tic tac toe
def tic_tac_toe():
    import time
    start=time.time()
    def sum(a, b, c ):
        return a + b + c

    def printBoard(xState, zState):
        zero = 'X' if xState[0] else ('O' if zState[0] else 0)
        one = 'X' if xState[1] else ('O' if zState[1] else 1)
        two = 'X' if xState[2] else ('O' if zState[2] else 2)
        three = 'X' if xState[3] else ('O' if zState[3] else 3)
        four = 'X' if xState[4] else ('O'  if zState[4] else 4)
        five = 'X' if xState[5] else ('O' if zState[5] else 5)
        six = 'X' if xState[6] else ('O' if zState[6] else 6)
        seven = 'X' if xState[7] else ('O' if zState[7] else 7)
        eight = 'X' if xState[8] else ('O' if zState[8] else 8)
        print(f"{zero} | {one} | {two} ")
        print(f"--|---|---")
        print(f"{three} | {four} | {five} ")
        print(f"--|---|---")
        print(f"{six} | {seven} | {eight} ") 

    def checkWin(xState, zState):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in wins:
            if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
                print("X Won the match")
                return 1
            if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
                print("O Won the match")
                return 0
        return -1
    
    if __name__ == "__main__":
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1 # 1 for X and 0 for O
        print("Welcome to Tic Tac Toe")
        while(True):
            printBoard(xState, zState)
            if(turn == 1):
                print("X's Chance")
                value = int(input("Please enter a value: "))
                xState[value] = 1
            else:
                print("O's Chance")
                value = int(input("Please enter a value: "))
                zState[value] = 1
            cwin = checkWin(xState, zState)
            if(cwin != -1):
                print("Match over")
                break
        
            turn = 1 - turn
    end=time.time()
    print("Time played:",int(end-start),"Seconds")
#fruit basket 
lives_remaining=3
def fruit_basket():

    canvas_width = 800
    canvas_height = 400

    root = Tk()
    root.title("fruit basket")
    c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue")
    c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0)
    c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
    c.pack()

    color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])
    egg_width = 45
    egg_height = 55
    egg_score = 10
    egg_speed = 500
    egg_interval = 4000
    difficulty = 0.95
    catcher_color = "blue"
    catcher_width = 100
    catcher_height = 100
    catcher_startx = canvas_width / 2 - catcher_width / 2
    catcher_starty = canvas_height - catcher_height - 20
    catcher_startx2 = catcher_startx + catcher_width
    catcher_starty2 = catcher_starty + catcher_height

    catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3)
    game_font = font.nametofont("TkFixedFont")
    game_font.config(size=18)


    score = 0
    score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score))

    lives_remaining = 3
    lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining))

    eggs = []

    def create_egg():
        x = randrange(10, 740)
        y = 40
        new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
        eggs.append(new_egg)
        root.after(egg_interval, create_egg)

    def move_eggs():
        for egg in eggs:
            (eggx, eggy, eggx2, eggy2) = c.coords(egg)
            c.move(egg, 0, 10)
            if eggy2 > canvas_height:
                egg_dropped(egg)
        root.after(egg_speed, move_eggs)

    def egg_dropped(egg):
        eggs.remove(egg)
        c.delete(egg)
        lose_a_life()
        if lives_remaining == 0:
            messagebox.showinfo("Game Over!", "Final Score: "+ str(score))
            root.destroy()

    def lose_a_life():
        global lives_remaining
        lives_remaining -= 1
        c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

    def check_catch():
        (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
        for egg in eggs:
            (eggx, eggy, eggx2, eggy2) = c.coords(egg)
            if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
                eggs.remove(egg)
                c.delete(egg)
                increase_score(egg_score)
        root.after(100, check_catch)

    def increase_score(points):
        global score, egg_speed, egg_interval
        score += points
        egg_speed = int(egg_speed * difficulty)
        egg_interval = int(egg_interval * difficulty)
        c.itemconfigure(score_text, text="Score: "+ str(score))

    def move_left(event):
        (x1, y1, x2, y2) = c.coords(catcher)
        if x1 > 0:
            c.move(catcher, -20, 0)

    def move_right(event):
        (x1, y1, x2, y2) = c.coords(catcher)
        if x2 < canvas_width:
            c.move(catcher, 20, 0)

    c.bind("<Left>", move_left)
    c.bind("<Right>", move_right)
    c.focus_set()
    root.after(1000, create_egg)
    root.after(1000, move_eggs)
    root.after(1000, check_catch)
    root.mainloop()


print("Hello, welcome to classic games ")
print("kindly type the index of the game you want to play ")
print("index table:")
print("1=smile man")
print("2=fruit basket")
print("3=rock paper scissor")
print("4=tic tac toe")
print("type the index")
print("or,type 5 to quit")
def myfunction():
    n=int(input())
    t=1
    while t==1:
        if n==1:
            smile_man()
            myfunction()
            t=t+1
        elif n==2:
            fruit_basket()
            myfunction()
            t=t+1
        elif n==3:
            rock_paper_scissor()
            myfunction()
            t=t+1
        elif n==4 :
            tic_tac_toe()
            myfunction()
            t=t+1

        else:
            print("thank you for playing")
            break
        
myfunction()
end_time =time.time()
print("you played",(end_time-start_time)//60 ,'minutes' , 'or,more exactly(',end_time-start_time,')seconds')
print('cost= ',(end_time-start_time)//60,'rupees')