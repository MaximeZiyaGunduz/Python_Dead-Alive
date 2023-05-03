import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame

time_left = 120

# Une variable globale pour indiquer si le jeu a commencé ou non
game_started = False
point = 0

def run_game():
    global message_label, score_label, time_left, life_button, death_button
    window = tk.Tk()
    window.title("Dead or Alive")


    # Loading images
    life_image = Image.open("life.png")
    death_image = Image.open("death.png")

    # Resizing images to have the same dimensions
    width = 250
    height = 400
    life_image = life_image.resize((width, height))
    death_image = death_image.resize((width, height))

    # Converting images to PhotoImage objects
    life_image = ImageTk.PhotoImage(life_image)
    death_image = ImageTk.PhotoImage(death_image)

    # Creating a canvas
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack()

    # Creating buttons for the doors
    life_button = tk.Button(window, image=life_image, borderwidth=0)
    death_button = tk.Button(window, image=death_image, borderwidth=0)

    # Calculating the coordinates of the buttons
    canvas_width = 800
    canvas_height = 600
    margin = 100  # The space between the buttons and the edges of the canvas
    x1 = margin  # The x coordinate of the life button
    y1 = (canvas_height - height) / 2  # The y coordinate of both buttons
    x2 = canvas_width - margin - width  # The x coordinate of the death button

    # Placing the buttons on the canvas
    life_button.place(x=x1, y=y1)
    death_button.place(x=x2, y=y1)

    # Creating a label for the score
    score_label = tk.Label(window, text="Score: 0", font=("Arial", 24), bg="white")
    score_label.place(x=50, y=50)

    # Creating a label for the messages
    message_label = tk.Label(window, text="", font=("Arial", 24), bg="white")
    message_label.place(x=200, y=500)

    time_label = tk.Label(window, text="Temps restant : " + str(time_left), font=("Arial", 24), bg="white")
    time_label.place(x=500, y=50)

    # Function to update the remaining time label
    def update_time():
        global time_left
        time_left -= 1
        time_label.config(text=f"Time: {time_left}")
        if time_left == 0:
            window.destroy()
        else:
            window.after(1000, update_time)

    # Initializing the score and the door values

    timer_running = True

    global life_value
    life_value = random.randint(0, 1)
    global death_value
    death_value = 1 - life_value

    # Defining a function to check the user's choice
    def check_choice(choice, life_button, death_button):
        global point, life_value, death_value

        # If the user chooses the life door
        if choice == "life":
            # If the life door has value 1
            if life_value == 1:
                # Increment the score by 1
                point += 1

                # Update the score label
                score_label.config(text=f"Score: {point}")
                # If the score is 4, the user wins
                if point == 4:
                    # Display a message to congratulate the user
                    message_label.config(text="Vous avez gagner ! Félicitation!")
                    # Disable the buttons
                    life_button.config(state=tk.DISABLED)
                    death_button.config(state=tk.DISABLED)
                    pygame.mixer.init()
                    pygame.mixer.music.load('GameWin.mp3')
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        pass
                    window.destroy()  # détruire la fenêtre Tkinter
                # Else, the game continues
                else:
                    # Display a message to encourage the user
                    message_label.config(text="Vous etes vivant ! Continue!")
                    # Randomize the door values again
                    life_value = random.randint(0, 1)
                    death_value = 1 - life_value
            # Else, if the life door has value 0
            else:
                # Display a message to inform the user
                message_label.config(text="Vous etes éliminer! Game over!")
                # Disable the buttons
                life_button.config(state=tk.DISABLED)
                death_button.config(state=tk.DISABLED)
                window.after(5000, window.destroy)

        # Else, if the user chooses the death door
        elif choice == "death":
            # If the life door has value 1
            if life_value == 1:
                # Increment the score by 1
                point += 1
                # Update the score label
                score_label.config(text=f"Score: {point}")
                # If the score is 4, the user wins
                if point == 4:
                    # Display a message to congratulate the user
                    message_label.config(text="Vous avez gagner ! Félicitation!")
                    # Disable the buttons
                    life_button.config(state=tk.DISABLED)
                    death_button.config(state=tk.DISABLED)
                    pygame.mixer.init()
                    pygame.mixer.music.load('GameWin.mp3')
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        pass
                    window.destroy()  # détruire la fenêtre Tkinter
                else:
                    # Display a message to encourage the user
                    message_label.config(text="Vous etes vivant ! Continue!")
                    # Randomize the door values again
                    life_value = random.randint(0, 1)
                    death_value = 1 - life_value
            # Else, if the life door has value 0
            else:
                # Display a message to inform the user
                message_label.config(text="Vous etes éliminé ! Game over!")
                # Disable the buttons
                life_button.config(state=tk.DISABLED)
                death_button.config(state=tk.DISABLED)
                window.after(5000, window.destroy)

    # Binding the buttons to call the check_choice function with different arguments
    life_button.config(command=lambda: check_choice("life", life_button, death_button))
    death_button.config(command=lambda: check_choice("death", life_button, death_button))

    # Defining a function to quit the game when pressing "q"
    def quit_game(event):
        window.destroy()

    if time_left == 120:
        pygame.mixer.init()
        pygame.mixer.music.load('Intro.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        update_time()
    else:
        update_time()
    # Making the window loop
    window.mainloop()

run_game()