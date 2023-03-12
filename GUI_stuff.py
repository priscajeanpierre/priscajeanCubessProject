import tkinter as tk
import sqlite3


def load_database():
    # Connect to database
    conn = sqlite3.connect("cubesProject.sqlite")
    cursor = conn.cursor()

    # Query database for entries
    cursor.execute("SELECT entryid, first_name , last_name,email, website, phone_number, guest_speaker, "
                   "site_visit, networking_event, project_topic, summer_23, fall_23, spring_23, subject_area,"
                   " funding, created_date,created_by FROM WufooData")
    WufooData = cursor.fetchall()

    # Close database connection
    conn.close()

    # Update listbox with entries
    for entry in WufooData:
        listbox.insert(tk.END, f"{entry[0]} - {entry[1]}")


def display_entries():
    # Get selected item from listbox
    index = listbox.curselection()[0]
    selected_item = listbox.get(index)

    # Get entry data from database
    conn = sqlite3.connect("cubesProject.sqlite")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM WufooData WHERE entryid={selected_item.split()[0]}")
    entry = cursor.fetchone()
    conn.close()

    # Display entry data in label widgets
    first_name_label.config(bg='hot pink', text=f"First Name: {entry[1]}")
    last_name_label.config(bg='hot pink', text=f"Last Name: {entry[2]}")
    email_label.config(bg='hot pink', text=f"Email: {entry[3]}")
    website_label.config(bg='hot pink', text=f"Website: {entry[4]}")
    phone_number_label.config(bg='hot pink', text=f"Phone Number: {entry[5]}")
    guest_speaker_label.config(bg='hot pink', text=f"Guest Speaker: {entry[6]}")
    site_visit_label.config(bg='hot pink', text=f"Site Visit: {entry[7]}")
    networking_event_label.config(bg='hot pink', text=f"Networking Event: {entry[8]}")
    project_topic_label.config(bg='hot pink', text=f"Project Topic: {entry[9]}")
    summer23_label.config(bg='hot pink', text=f"Summer 2023: {entry[10]}")
    fall23_label.config(bg='hot pink', text=f"Fall 2023: {entry[11]}")
    spring23_label.config(bg='hot pink', text=f"Spring 2023: {entry[12]}")
    created_date_label.config(bg='hot pink', text=f"Created Date: {entry[15]}")
    created_by_label.config(bg='hot pink', text=f"Created By: {entry[16]}")


# Create Tkinter window and widgets
root = tk.Tk()
root.configure(bg='pink')
root.title("Wufoo Database Entries")

listbox = tk.Listbox(root, width=50)
listbox.grid(row=0, column=0, rowspan=3)

load_button = tk.Button(root, text="Form Entries", command=load_database)
load_button.grid(row=0, column=1)

view_button = tk.Button(root, text="View Entry", command=display_entries)
view_button.grid(row=1, column=1)

first_name_label = tk.Label(root, text="First Name:")
first_name_label.grid(row=0, column=2)

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.grid(row=1, column=2)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=2)

website_label = tk.Label(root, text="Website:")
website_label.grid(row=3, column=2)

phone_number_label = tk.Label(root, text="Phone Number:")
phone_number_label.grid(row=4, column=2)

guest_speaker_label = tk.Label(root, text="Guest Speaker")
guest_speaker_label.grid(row=5, column=2)

site_visit_label = tk.Label(root, text="Site Visit")
site_visit_label.grid(row=6, column=2)

networking_event_label = tk.Label(root, text="Networking Event")
networking_event_label.grid(row=7, column=2)

project_topic_label = tk.Label(root, text="Project Topic:")
project_topic_label.grid(row=8, column=2)

summer23_label = tk.Label(root, text="Summer 2023")
summer23_label.grid(row=9, column=2)

fall23_label = tk.Label(root, text="Fall 2023")
fall23_label.grid(row=10, column=2)

spring23_label = tk.Label(root, text="Spring 2023")
spring23_label.grid(row=11, column=2)

created_date_label = tk.Label(root, text="Created Date:")
created_date_label.grid(row=14, column=2)

created_by_label = tk.Label(root, text="Created By:")
created_by_label.grid(row=15, column=2)

def update_data():
    conn = sqlite3.connect("cubesProject.sqlite")
    cursor = conn.cursor()
    select_entry = input("Enter entry ID number:")
    original_entries = input("Choose entry to update: ")
    updated_entries = input("Enter new data: ")

    try:
        cursor.execute(f'UPDATE WufooData set {original_entries} = "{updated_entries}" WHERE entryID = {select_entry}')
        print("*** Update Successful ***")
        data = cursor.execute(f'select * from WufooData WHERE entryID = {select_entry}')
        for entries in data:
            print(entries)
        conn.commit()
    except sqlite3.Error as error:
        print(f'Update Failed: {error}')


root.mainloop()


