import wikipedia as wiki
import os
import tkinter as tk
from tkinter import scrolledtext
import PyInstaller.__main__  # Import for .exe creation

print('Launching...')

print('Maximise(click square button at the top right of the window)')

def get_response(user_input, sentences):
    """Searches Wikipedia and returns a summary."""
    try:
        summary = wiki.summary(user_input, sentences=sentences)
        return summary

    except wiki.exceptions.PageError:
        return f"I couldn't find any information about '{user_input}' on Wikipedia."
    except wiki.exceptions.DisambiguationError as e:
        return f"Please be more specific. Wikipedia found multiple possible pages: {e.options[:10]}..."
    except Exception as e:
        return f"An error occurred, check your internet and python version. Error: {e}"

def search_wikipedia():
    user_input = input_entry.get()
    try:
        sentences = int(sentences_entry.get())
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid number of sentences. Using default (5).")
        sentences = 5

    response = get_response(user_input, sentences)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, response)

def clear_text():
    result_text.delete(1.0, tk.END)
    input_entry.delete(0, tk.END)

# GUI Setup
window = tk.Tk()
window.title("PyranAI")
window.geometry("1920x1080")
window.resizable(True,True)
try:
    window.iconphoto(True, tk.PhotoImage(file='C:/Users/Akhila Agencies/Desktop/PYRAN/Pyran.Main/icon-1.png'))
except:
    print("Icon file not found or invalid.")


input_label = tk.Label(window, text="Enter search term:")
input_label.pack()

input_entry = tk.Entry(window, width=50)
input_entry.pack()

sentences_label = tk.Label(window, text="Number of sentences:")
sentences_label.pack()

sentences_entry = tk.Entry(window, width=5)
sentences_entry.pack()
sentences_entry.insert(0, "5") #default value

search_button = tk.Button(window, text="Search", command=search_wikipedia)
search_button.pack()

clear_button = tk.Button(window, text="Clear", command=clear_text)
clear_button.pack()

result_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=15)
result_text.pack()

window.mainloop()
print('launched!')

# Create .exe (Run this from command line)
script_path = os.path.abspath(__file__)
PyInstaller.__main__.run([
    script_path,
    '--onefile',
    '--windowed',  # Prevents console window from appearing
    '--name=PyranAI'
])