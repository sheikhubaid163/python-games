import tkinter as tk
from tkinter import messagebox


# Function to show event details
def show_event():
    event_details = (
        "🔹 **Military Coup in Pakistan** (12 October 1999)\n\n"
        "📌 **Leader**: General Pervez Musharraf\n"
        "📌 **Target**: Prime Minister Nawaz Sharif\n"
        "📌 **Cause**: Nawaz Sharif attempted to dismiss Musharraf as Army Chief.\n"
        "📌 **Result**: Military takeover, Musharraf became Pakistan's de facto ruler.\n\n"
        "➡ The military arrested Nawaz Sharif and took control of the country.\n"
        "➡ A state of emergency was declared, and Musharraf later became the President.\n"
    )

    messagebox.showinfo("Historical Event - 12 Oct 1999", event_details)


# Create main GUI window
root = tk.Tk()
root.title("Pakistan Historical Events")
root.geometry("400x300")
root.resizable(False, False)

# Create UI components
label = tk.Label(root, text="📜 Click the button to view historical events of 12 October 1999:", wraplength=380,
                 justify="center", font=("Arial", 12))
label.pack(pady=20)

event_button = tk.Button(root, text="Show Event Details", command=show_event, bg="blue", fg="white",
                         font=("Arial", 12, "bold"))
event_button.pack(pady=10)

# Run GUI application
root.mainloop()
