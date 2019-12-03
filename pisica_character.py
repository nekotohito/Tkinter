import tkinter as tk
import tkinter.messagebox as tmb
# https://qiita.com/takanorimutoh/items/bd8c2cf27a2c5bb14bc0
# simpledialogについては謎。
# ウィジェットはここからまねた。
# https://www.nakamuri.info/mw/index.php/%E3%81%84%E3%82%8D%E3%81%84%E3%82%8D%E3%81%AA%E3%82%A6%E3%82%A3%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88

# 課題1：packとgridをうまく組み合わせて配置・デザインしたい。
# ベストは何？

root = tk.Tk()
root.title('キャラクター設定')
root.geometry("600x600")

main_frame = tk.Frame(root)
main_frame.pack()

### メニューバー
def hello_menu():
    tmb.showinfo('message', '(/・ω・)/ 「はろー」')
    
men =tk.Menu(root)
root.config(menu=men)
menu_file = tk.Menu(root)
men.add_cascade(label='メニュー', menu=menu_file)
menu_file.add_command(label='(/・ω・)/', command=hello_menu)
menu_file.add_separator()
menu_file.add_command(label='閉じる', command=quit)

### 名前
def name_command():
    myname = name_entry.get()
    name_ok["text"] = myname

name_label = tk.Label(main_frame, text='名前', bg='LightSkyBlue',width=10)
name_label.grid(row=0, column=0)
name_button = tk.Button(main_frame, text='入力', command=name_command)
name_button.grid(row=0, column=2, columnspan=2)
name_ok = tk.Label(main_frame, text='決定名をここに出したい', bg="white", width=20)
name_ok.grid(row=0, column=4)
# とりあえずentryでやっておく。
name_entry = tk.Entry(main_frame, width=20)
name_entry.grid(row=0, column=1)

### 動物
# ラジオボタンの情報を取得するクリックイベント
# 見本　https://pg-chain.com/python-radiobutton-event
def tribe_click():
    tribe_kind = iv1.get()
    res = tmb.askokcancel('メッセージ', rdo_txt[tribe_kind] + 'で良いですか？')
    if res == True:
        mytribe = rdo_txt[tribe_kind]
        tribe_ok["text"] = mytribe
    elif res == False:
        pass

tribe_label =tk.Label(main_frame, text='動物', bg='LightskyBlue', width=10)
tribe_label.grid(row=1, column=0, sticky="e")
frame_for_tribe = tk.Frame(main_frame)
# root > main_frame >frame_for_tribeの構成。
# ラジオボタンをpackで縦並びにつくるため。
frame_for_tribe.grid(row=1, column=1, padx=5, pady=5)
tribe_ok = tk.Label(main_frame, text='決定名をここに出したい', bg="white", width=20)
tribe_ok.grid(row=1, column=4)

rdo_txt = ['ねこ', 'いぬ', 'うさぎ', 'あざらし', 'サンタ']
iv1 = tk.IntVar()
# iv1.set(1)
# tk.Radiobutton(frame_for_tribe, text="ねこ", value=1, variable=iv1).pack()
# tk.Radiobutton(frame_for_tribe, text="いぬ", value=2, variable=iv1).pack()
# tk.Radiobutton(frame_for_tribe, text="うさぎ", value=3, variable=iv1).pack()
for i in range (len(rdo_txt)):
    tk.Radiobutton(frame_for_tribe, value=i, variable=iv1, text=rdo_txt[i]).pack()

tribe_button = tk.Button(main_frame, text='これにする',
                        # command=lambda:print('ok'))   これはできた
                        # command=tribe_click())        これやると、command関係なく、とりあえずtribe_clickが実行される！
                        command=tribe_click)
tribe_button.grid(row=1, column=2, columnspan=2)

### 性格
def character_click():
    character_kind = character_listbox.curselection()[0]
# curselection = 選択された行のインデックスをタプルで返す。
# タプルの要素を使うためにさらにインデックスを指定。
# やり方が回りくどい？もっと良い方法がある気がする。

    mycharacter = characteristics[character_kind]
    character_ok["text"] = mycharacter
# 何も選択せずに「これにする」ボタンを押すとerrorおきる。
# 「選択されていません」messageをだす必要がある。

character_label = tk.Label(main_frame, text="性格", bg='LightskyBlue', width=10)
character_label.grid(row=2, column=0, sticky="e")
frame_for_character = tk.Frame(main_frame)
frame_for_character.grid(row=2, column=1)
# root > main_frame >frame_for_characterの構成。
# リストボックスと縦並びにれるため。
character_listbox = tk.Listbox(frame_for_character, height=5)
characteristics = ['ポジティブ', '真面目', 'おしゃべり','ねぼすけ','人見知り', 'アグレッシブ',
                   'わがまま', '', '', '', '', '', 'end']
for line in characteristics:
    character_listbox.insert(tk.END, line)
# character_listbox.select_set(1)
# これは選択したもの取るときに、もう1回やるやつ？
character_listbox.pack(side=tk.LEFT)
# character_listbox.grid(row=0, column=0, padx=10, pady=10)
scroll_bar = tk.Scrollbar(frame_for_character, command=character_listbox.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
character_listbox.config(yscrollcommand=scroll_bar.set)

character_button = tk.Button(main_frame, text="これにする", command=character_click)
character_button.grid(row=2, column=2, columnspan=2)
character_ok = tk.Label(main_frame, text='決定名をここに出したい', bg="white", width=20)
character_ok.grid(row=2, column=4)

### その他
etcetera_label = tk.Label(main_frame, text="その他", bg='LightskyBlue', width=10)
etcetera_label.grid(row=3, column=0, sticky="e")
etcetera_text = tk.Text(main_frame, width=20, height=6)
etcetera_text.insert(tk.END, "入力してね")
etcetera_text.grid(row=3, column=1, padx=10, pady=10)

### 決定ボタン
ok_button = tk.Button(main_frame, text='決定',
                      command=lambda:tmb.askokcancel('メッセージ','これで良いですか？'),
                      width=20)
ok_button.grid(row=5, column=0, columnspan=2)


root.mainloop()
