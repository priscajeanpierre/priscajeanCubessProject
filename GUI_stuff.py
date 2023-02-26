import tkinter as tk
import sqlite3

import databaseStuff

# Create a new Tkinter window

window = tk.Tk()
    # Set the window title
window.title("Wufoo Data")

    # Set the window size
window.geometry("400x300")

listbox = tk.Listbox(window)
listbox.pack()

cursor = databaseStuff.connect_database()

cursor.execute("SELECT entry_id, first_name,last_name, email, website_link, phone_number"
                   "collab_opportunities, project_topic, collab_year FROM WufooData")
entries = cursor.fetchall()


for entry in entries:
    listbox.insert(tk.END, f"{entry[0]} - {entry[1]} ({entry[2]}  {entry[3]} {entry[4]} {entry[5]}"
                               f"{entry[6]} {entry[7]} {entry[8]} ) ")





def show_entry_data():
    # Get the selected entry ID from the listbox
    selection = listbox.curselection()
    if selection:
        entry_id = entries[selection[0]][0]
        # Retrieve the complete entry data from the database
        cursor.execute("SELECT * FROM WufooData WHERE id=?", (entry_id,))
        complete_entry = cursor().fetchone()
        # Create a new window to display the complete entry data
        entry_window = tk.Toplevel(window)
        entry_window.title("Entry Data")
        entry_window.geometry("400x300")
        # Add labels to display the complete entry data
        tk.Label(entry_window, text=f"ID: {complete_entry[0]}").pack()
        tk.Label(entry_window, text=f"First Name: {complete_entry[1]}").pack()
        tk.Label(entry_window, text=f"Last Name: {complete_entry[2]}").pack()
        tk.Label(entry_window, text=f"Email: {complete_entry[2]}").pack()
        tk.Label(entry_window, text=f"Website Link: {complete_entry[2]}").pack()
        tk.Label(entry_window, text=f"Phone Number: {complete_entry[2]}").pack()
        tk.Label(entry_window, text=f"Collab Opportunities: {complete_entry[2]}").pack()
        tk.Label(entry_window, text=f"Project Topic: {complete_entry[2]}").pack()
        tk.Label(entry_window, text=f"Collab Year: {complete_entry[2]}").pack()


# Create a button to show the complete entry data
button = tk.Button(window, text="Show Entry Data", command=show_entry_data)
button.pack()
window.mainloop()


