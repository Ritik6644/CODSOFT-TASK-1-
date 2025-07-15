import tkinter as tk
import re

# Define the chatbot's response logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r'\b(name|who are you)\b', user_input):
        return "I'm ChatBot, your virtual assistant."
    elif re.search(r'\b(weather)\b', user_input):
        return "I can't check live weather, but I hope it's great!"
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return "Goodbye! Have a nice day."
    elif re.search(r'\b(thank you|thanks)\b', user_input):
        return "You're welcome!"
    else:
        return "I'm not sure how to respond to that."

# Function to send user input and display the chatbot response
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot_response(user_input)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    chat_log.see(tk.END)

# GUI setup
window = tk.Tk()
window.title("Simple ChatBot")
window.geometry("400x500")
window.resizable(False, False)

chat_log = tk.Text(window, bg="white", fg="black", wrap=tk.WORD, state=tk.DISABLED)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(padx=10, pady=5, fill=tk.X)
entry.focus()

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

window.mainloop()

