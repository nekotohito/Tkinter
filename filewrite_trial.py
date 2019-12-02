import tkinter as tk
# import tkinter.messagebox as tmb

root = tk.Tk()
root.geometry('300x300')

def neko_button():
    txt_entry.insert(tk.END, 'にゃー(´･ω･｀)')
# txtファイルを直接みると、ちゃんと表示されている。
# VScodeでみると文字化けしてる。なんで？

def add_button():
    add_msg = txt_entry.get()
    test_text.insert(tk.END, add_msg)

# ファイルに書き込むための関数。
def file_write():
    file_msg = test_text.get('1.0', tk.END)
    filename = 'neko.txt'
    with open(filename, 'a') as file_object:
        file_object.write(file_msg)

test_label = tk.Label(root, text="test画面", bg='LightskyBlue', width=10)
test_label.grid(row=0, column=0)
test_text = tk.Text(root, width=20, height=6)
test_text.grid(row=0, column=1)

tk.Label(root, text='entry').grid(row=1, column=0)
txt_entry =tk.Entry(width=20)
txt_entry.grid(row=1, column=1)

# sample_label = tk.Label(root, text='sample',width=10)
# sample_label.grid(row=3, column=0)

# test_button = tk.Button(root, text='OK', command=lambda:print('OK'))
test_button = tk.Button(root, text='ねこをよぶ', command=neko_button)
test_button.grid(row=4, column=0)

add_button = tk.Button(root, text='add', command=add_button)
add_button.grid(row=5, column=0)

file_button = tk.Button(root, text='fileに保存', command=file_write)
file_button.grid(row=6, column=0)

root.title("入力画面をつくるよ")
root.mainloop()

