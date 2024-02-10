import tkinter as tk
from tkinter import ttk
import sqlite3

def getBooks():
    finalTab = ttk.Frame(notebook)
    bookRecomendationText = ttk.Label(finalTab, text = 'Book Recomendations:', font=("Helvetica", 30), padding=20, foreground = '#00c7bd')
    bookRecomendationText.pack()
    notebook.add(finalTab, text = 'Book recomendation')
    connect = sqlite3.connect('books.db')
    command = connect.cursor()
    genre = selected_values["Question 1"].get()
    length = selected_values["Question 2"].get()
    age_group = selected_values["Question 3"].get()
    narrative_style = selected_values["Question 4"].get()
    reading_level = int(predictedReadingLevel.get())
    query = f"SELECT * FROM books WHERE genre = '{genre}' AND length = '{length}' AND age_group = '{age_group}' AND narrative_style = '{narrative_style}' AND reading_level = {reading_level} LIMIT 3;"
    command.execute(query)
    output = command.fetchall()
    for i, book in enumerate(output):
        book_label = tk.Label(finalTab, text=f"{i+1}. {book[1]} by {book[2]}", font = ("Helvetica", 20))
        book_label.pack()
    connect.close()

def predictReadingLevel(text):
    entered_text = text.get("1.0", tk.END)
    # Counting letters
    letters = sum(1 for char in entered_text if char.isalpha())
    # Counting words
    words = len(entered_text.split())
    # Counting sentences
    sentences = entered_text.count('.') + entered_text.count('?') + entered_text.count('!')
    # Coleman-Liau Index
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = (0.0588 * L) - (0.296 * S) - 15.8
    index = round(index)
    # Setting the predicted reading level
    if index < 1:
        predictedReadingLevel.set(0)  # Below Grade 1
    elif index > 8:
        predictedReadingLevel.set(9)  # Above Grade 8
    else:
        predictedReadingLevel.set(index)  # Grade

# Creating Main Window 
window = tk.Tk()
window.title('BookShelf')
window.geometry('800x550')

# Tabs
notebook = ttk.Notebook(window, width=800, height=550)

#Main font
font_style = ttk.Style()
font_style.configure("Custom.TRadiobutton", font=("Helvectica", 12))

# Storing User Input
selected_values = {
    "Question 1": tk.StringVar(),
    "Question 2": tk.StringVar(),
    "Question 3": tk.StringVar(),
    "Question 4": tk.StringVar()
}

# Question 1
question1 = ttk.Frame(notebook)
questionText = ttk.Label(question1, text = 'What genre would you like to read?', font=("Helvetica", 20), padding=20, foreground = '#00c7bd')
questionText.pack()
Oneoption1 = ttk.Radiobutton(question1, text = 'Fiction', value = 'Fiction', style="Custom.TRadiobutton", variable=selected_values["Question 1"], padding=20)
Oneoption1.pack(anchor="w")
Oneoption2= ttk.Radiobutton(question1, text = 'Mystery', value = 'Mystery', style="Custom.TRadiobutton", variable=selected_values["Question 1"], padding=20)
Oneoption2.pack(anchor="w")
Oneoption3 = ttk.Radiobutton(question1, text = 'Non-Fiction', value = 'Non-Fiction', style="Custom.TRadiobutton", variable=selected_values["Question 1"], padding=20)
Oneoption3.pack(anchor="w")
Oneoption4 = ttk.Radiobutton(question1, text = 'Realistic-Fiction', value = 'Realistic-Fiction', style="Custom.TRadiobutton", variable=selected_values["Question 1"], padding=20)
Oneoption4.pack(anchor="w")

# Question 2
question2 = ttk.Frame(notebook)
question2Text = ttk.Label(question2, text = 'How long do you want your story to be?', font=("Helvetica", 20), padding=20, foreground = '#34ED13')
question2Text.pack()
Twooption1 = ttk.Radiobutton(question2, text = 'Short', value = 'Short', style="Custom.TRadiobutton", variable=selected_values["Question 2"], padding=20)
Twooption1.pack(anchor="w")
Twooption2= ttk.Radiobutton(question2, text = 'Medium', value = 'Medium', style="Custom.TRadiobutton", variable=selected_values["Question 2"], padding=20)
Twooption2.pack(anchor="w")
Twooption3 = ttk.Radiobutton(question2, text = 'Long', value = 'Long', style="Custom.TRadiobutton", variable=selected_values["Question 2"], padding=20)
Twooption3.pack(anchor="w")

# Question 3
question3 = ttk.Frame(notebook)
question3Text = ttk.Label(question3, text = 'What is your age group', font=("Helvetica", 20), padding=20, foreground = '#F1A30A')
question3Text.pack()
Threeoption1 = ttk.Radiobutton(question3, text = 'Children', value = 'Children', style="Custom.TRadiobutton", variable=selected_values["Question 3"], padding=20)
Threeoption1.pack(anchor="w")
Threeoption2= ttk.Radiobutton(question3, text = 'Young Adult', value = 'Young Adult', style="Custom.TRadiobutton", variable=selected_values["Question 3"], padding=20)
Threeoption2.pack(anchor="w")
Threeoption3 = ttk.Radiobutton(question3, text = 'Adult', value = 'Adult', style="Custom.TRadiobutton", variable=selected_values["Question 3"], padding=20)
Threeoption3.pack(anchor="w")

# Question 4
question4 = ttk.Frame(notebook)
question4Text = ttk.Label(question4, text = 'What narrative style do you like?', font=("Helvetica", 20), padding=20, foreground = '#F10A70')
question4Text.pack()
Fouroption1 = ttk.Radiobutton(question4, text = 'First person', value = 'First person', style="Custom.TRadiobutton", variable=selected_values["Question 4"], padding=20)
Fouroption1.pack(anchor="w")
Fouroption2= ttk.Radiobutton(question4, text = 'Second person', value = 'Second person', style="Custom.TRadiobutton", variable=selected_values["Question 4"], padding=20)
Fouroption2.pack(anchor="w")
Fouroption3 = ttk.Radiobutton(question4, text = 'Third person', value = 'Third person', style="Custom.TRadiobutton", variable=selected_values["Question 4"], padding=20)
Fouroption3.pack(anchor="w")

# Question 5
question5 = ttk.Frame(notebook)
question5Text = ttk.Label(question5, text = 'Type some text from books that you read or your own writting:', font=("Helvetica", 20), padding=20, foreground = '#FD6BD0')
question5Text.pack()
text = tk.Text(question5, background = '#8AB2FF', pady = 10)
text.pack()
#Defining reading level
predictedReadingLevel = tk.StringVar()
#Submit button
submit_button = ttk.Button(question5, text="Submit", command=lambda: [predictReadingLevel(text), getBooks()])
submit_button.pack()

notebook.add(question1, text = 'Question 1')
notebook.add(question2, text = 'Question 2')
notebook.add(question3, text = 'Question 3')
notebook.add(question4, text = 'Question 4')
notebook.add(question5, text = 'Question 5')
notebook.pack()
# main loop
window.mainloop()