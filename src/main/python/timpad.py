import dbops
import bcrypt
import tkinter as tk
from datetime import datetime
note_id_list = []
selected = 0
bit1 = 0
bit2 = 0
auth = ""
# ======= FUNCTIONS ========
# list box stuff
def onselect(evt):
    w = evt.widget
    try:
        index = int(w.curselection()[0])
    except IndexError:
        return
    delete_text()
    global selected
    selected = note_id_list[index]
    add_text(note_id_list[index])

def sort_list(tup, pos, way):
    list = len(tup)
    for i in range(0, list):
        for j in range(0, list - i - 1):
            if way:
                if (tup[j][pos] < tup[j + 1][pos]):
                    temp = tup[j]
                    tup[j] = tup[j + 1]
                    tup[j + 1] = temp
            else:
                if (tup[j][pos] > tup[j + 1][pos]):
                    temp = tup[j]
                    tup[j] = tup[j + 1]
                    tup[j + 1] = temp
    return tup
def update_list(notelist):
    list_box.delete(0, tk.END)
    for idx, note in enumerate(notelist):
        if dbops.get_user_type(dbops.conn, auth)[0] == note[1]:
            list_box.insert(idx, str(note[4]) + " " + note[2])
            if len(note_id_list) > idx:
                note_id_list[idx] = note[0]
            else:
                note_id_list.append(note[0])
def sort_name():
    notelist = dbops.select_all_notes(dbops.conn)
    global bit1
    if bit1:
        update_list(sort_list(notelist, 2, 0))
        status.config(text="Sorted A-Z")
        bit1 = 0
    else:
        update_list(sort_list(notelist, 2, 1))
        status.config(text="Sorted Z-A")
        bit1 = 1
def sort_date():
    notelist = dbops.select_all_notes(dbops.conn)
    global bit2
    if bit2:
        update_list(sort_list(notelist, 4, 0))
        status.config(text="Sorted first to last")
        bit2 = 0
    else:
        update_list(sort_list(notelist, 4, 1))
        status.config(text="Sorted last to first")
        bit2 = 1

# text box stuff (contents)
def add_text(idx):
    note = dbops.select_specific_note(dbops.conn, idx)
    title_box.insert(0, note[0])
    text_box.insert('1.0', note[1])
def delete_text():
    title_box.delete(0, tk.END)
    text_box.delete('1.0', tk.END)
def add_note():
    title = title_box.get()
    contents = text_box.get("1.0", tk.END)
    if title != "":
        dbops.insert_note(dbops.conn, title, contents)
        update_list(dbops.select_all_notes(dbops.conn))
        status.config(text="Note added!")
    else:
        status.config(text="Note doesn't have a title")
def save_note():
    if selected:
        title = title_box.get()
        contents = text_box.get("1.0", tk.END)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dbops.update_note(dbops.conn, title, contents, selected, now)
        status.config(text="Note saved!")
    else:
        status.config(text="Note was not selected!")
def delete_note():
    global selected
    if selected:
        delete_text()
        dbops.delete_note(dbops.conn, selected)
        update_list(dbops.select_all_notes(dbops.conn))
        status.config(text="Note deleted!")
    else:
        status.config(text="Note was not selected!")
def check_user():
    user = login_user_box.get()
    pw = login_pw_box.get()
    global auth
    output = dbops.find_user(dbops.conn, user, pw)
    if output != "NULL":
        login_window.destroy()
        auth = user
    else:
        login_msg.config(text="Incorrect credentials!")

login_window = tk.Tk()
user_frame = tk.Frame().pack(side=tk.TOP)
pw_frame = tk.Frame().pack(side=tk.BOTTOM)
login_msg = tk.Label(master=user_frame, text="Please login")
login_msg.pack()
login_user_label = tk.Label(master=user_frame, text="Username:")
login_user_label.pack(side=tk.LEFT)
login_user_box = tk.Entry(master=user_frame, width=20)
login_user_box.pack(side=tk.LEFT)
login_pw_label = tk.Label(master=pw_frame, text="Password:")
login_pw_label.pack(side=tk.LEFT)
login_pw_box = tk.Entry(master=pw_frame, width=20)
login_pw_box.pack(side=tk.LEFT)
submit = tk.Button(login_window, text="Login", command=check_user)
submit.pack()
out = tk.Button(login_window, text="Quit", command=login_window.destroy)
out.pack(side=tk.BOTTOM)
login_window.mainloop()
# ======= USER INTERFACE ========
if auth != "":
    window = tk.Tk()
    list_frame = tk.Frame()
    list_frame.pack(side=tk.LEFT)
    content_frame = tk.Frame()
    content_frame.pack(side=tk.RIGHT)
    greeting = tk.Label(master=list_frame, text="Hello, " + auth)
    greeting.pack()
    title_box = tk.Entry(master=content_frame, width=100)
    title_box.pack()
    text_box = tk.Text(master=content_frame, width=75)
    text_box.pack()
    status = tk.Label(master=list_frame, text="")
    status.pack()
    list_box = tk.Listbox(master=list_frame, width=70, height=20)
    list_box.pack()
    list_box.bind('<<ListboxSelect>>', onselect)
    update_list(dbops.select_all_notes(dbops.conn))
    # buttons
    name_btn = tk.Button(master=list_frame, text="Sort name", width=8, command=sort_name)
    name_btn.pack(side=tk.LEFT)
    date_btn = tk.Button(master=list_frame, text="Sort date", width=8, command=sort_date)
    date_btn.pack(side=tk.LEFT)
    add = tk.Button(master=list_frame, text="Add", width=8, command=add_note)
    add.pack(side=tk.LEFT)
    edit = tk.Button(master=list_frame, text="Save", width=8, command=save_note)
    edit.pack(side=tk.LEFT)
    delete = tk.Button(master=list_frame, text="Delete", width=8, command=delete_note)
    delete.pack(side=tk.LEFT)
    print(dbops.get_user_type(dbops.conn, auth))
    if dbops.get_user_type(dbops.conn, auth)[1]:
        admin = tk.Button(master=list_frame, text="Admin", width=8, command=delete_note)
        admin.pack(side=tk.LEFT)
    window.mainloop()
def helloworld(out):
    out.write("Hello world of Python\n")


