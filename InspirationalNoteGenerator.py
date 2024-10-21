import tkinter as tk
import random

#Main window:
root = tk.Tk()
root.title("Inspirational Note Generator")
root.geometry("400x300")
root.config(bg="#7E9680")

#Add label to display love notes:
inspiration_note_label = tk.Label(root, text="Click the button to get inspiration", font=("Helvetica",14), wraplength=300, justify="center")
inspiration_note_label.pack(pady = 50)

#def function to update current label
def generate_inspiration_note():
    love_notes = [
        "'Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.' \n — Albert Schweitzer ",
        "'It always seems impossible until it's done.'\n — Nelson Mandela",
        "'If you can dream it, you can do it.' \n — Walt Disney",
        "'Hardships often prepare ordinary people for an extraordinary destiny.' \n — C.S. Lewis",
        "'Success is not how high you have climbed, but how you make a positive difference to the world.' \n — Roy T. Bennett",
        "'Do not go where the path may lead, go instead where there is no path and leave a trail.' \n — Ralph Waldo Emerson",
        "'The journey of a thousand miles begins with one step.' \n — Lao Tzu",
        "'The greatest glory in living lies not in never falling, but in rising every time we fall.' \n — Nelson Mandela",
        "'You must be the change you wish to see in the world.' \n — Mahatma Gandhi",
        "'Failure will never overtake me if my determination to succeed is strong enough.' \n  — Og Mandino",
        "'Life isn’t about finding yourself. Life is about creating yourself.' \n  — George Bernard Shaw",
        "'In the end, we only regret the chances we didn’t take.' \n — Lewis Carroll",
        "'Difficulties in life are intended to make us better, not bitter.' \n — Dan Reeves" 
    ]
    #Choose random note
    love_note = random.choice(love_notes)
    inspiration_note_label.config(text=love_note)

generate_button = tk.Button(root, text="Get an Inspirational Note", command=generate_inspiration_note, font=("Helvetica",12))
generate_button.pack(pady=20)

root.mainloop()