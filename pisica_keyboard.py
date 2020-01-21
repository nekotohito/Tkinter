import tkinter as tk
import tkinter.messagebox as tmb

  
class PisicaKeyboard(tk.Frame):
 
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry()
        self.master.title('キャラクター名')
        self.entry = tk.Entry(self.master, justify="left")
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)
        self.create_widgets()

    def input(self, action):
        self.entry.insert(tk.END, action)
    def clear_all(self):
        self.entry.delete(0, tk.END)
    def clear_one(self):
        txt = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, txt[:-1])

    def ok_click(self):
        res = tmb.askokcancel('メッセージ', 'これで良いですか？')
        if res == True:
            pass
        elif res == False:
            pass

    def create_widgets(self):
        file_menu = tk.Menu(self.menu_bar)
        file_menu.add_command(label='test' )
        file_menu.add_command(label='閉じる', command=self.master.quit)
        self.menu_bar.add_cascade(label='メニュー', menu=file_menu)
 
        self.entry.grid(row=0, column=0, columnspan=4, pady=3)
        self.entry.focus_set()


        # hiraganas = 'あいうえお'
        # numbers = [2,3,4,5,6]
        # buttons = []
        # for i in range(5):
        #     buttons.append(tk.Button(self.master, text=hiraganas[i], width=4, 
        #                    command=lambda hiragana=hiraganas[i]: self.input(hiragana)).grid(row=numbers[i], column=0))

        tk.Button(self.master, text='あ', width=4,
                  command=lambda: self.input('あ')).grid(row=2, column=0)
        tk.Button(self.master, text='い', width=4,
                  command=lambda: self.input('い')).grid(row=3, column=0)
        tk.Button(self.master, text='う', width=4,
                  command=lambda: self.input('う')).grid(row=4, column=0)
        tk.Button(self.master, text='え', width=4,
                  command=lambda: self.input('え')).grid(row=5, column=0)
        tk.Button(self.master, text='お', width=4,
                  command=lambda: self.input('お')).grid(row=6, column=0)

        tk.Button(self.master, text='か', width=4,
                  command=lambda: self.input('か')).grid(row=2, column=1)
        tk.Button(self.master, text='き', width=4,
                  command=lambda: self.input('き')).grid(row=3, column=1)
        tk.Button(self.master, text='く', width=4,
                  command=lambda: self.input('く')).grid(row=4, column=1)
        tk.Button(self.master, text='け', width=4,
                  command=lambda: self.input('け')).grid(row=5, column=1)
        tk.Button(self.master, text='こ', width=4,
                  command=lambda: self.input('こ')).grid(row=6, column=1)

        tk.Button(self.master, text='さ', width=4,
                  command=lambda: self.input('さ')).grid(row=2, column=2)
        tk.Button(self.master, text='し', width=4,
                  command=lambda: self.input('し')).grid(row=3, column=2)
        tk.Button(self.master, text='す', width=4,
                  command=lambda: self.input('す')).grid(row=4, column=2)
        tk.Button(self.master, text='せ', width=4,
                  command=lambda: self.input('せ')).grid(row=5, column=2)
        tk.Button(self.master, text='そ', width=4,
                  command=lambda: self.input('そ')).grid(row=6, column=2)

        tk.Button(self.master, text='た', width=4,
                  command=lambda: self.input('た')).grid(row=2, column=3)
        tk.Button(self.master, text='ち', width=4,
                  command=lambda: self.input('ち')).grid(row=3, column=3)
        tk.Button(self.master, text='つ', width=4,
                  command=lambda: self.input('つ')).grid(row=4, column=3)
        tk.Button(self.master, text='て', width=4,
                  command=lambda: self.input('て')).grid(row=5, column=3)
        tk.Button(self.master, text='と', width=4,
                  command=lambda: self.input('と')).grid(row=6, column=3)

        tk.Button(self.master, text='な', width=4,
                  command=lambda: self.input('な')).grid(row=2, column=4)
        tk.Button(self.master, text='に', width=4,
                  command=lambda: self.input('に')).grid(row=3, column=4)
        tk.Button(self.master, text='ぬ', width=4,
                  command=lambda: self.input('ぬ')).grid(row=4, column=4)
        tk.Button(self.master, text='ね', width=4,
                  command=lambda: self.input('ね')).grid(row=5, column=4)
        tk.Button(self.master, text='の', width=4,
                  command=lambda: self.input('の')).grid(row=6, column=4)

        tk.Button(self.master, text='は', width=4,
                  command=lambda: self.input('は')).grid(row=2, column=5)
        tk.Button(self.master, text='ひ', width=4,
                  command=lambda: self.input('ひ')).grid(row=3, column=5)
        tk.Button(self.master, text='ふ', width=4,
                  command=lambda: self.input('ふ')).grid(row=4, column=5)
        tk.Button(self.master, text='へ', width=4,
                  command=lambda: self.input('へ')).grid(row=5, column=5)
        tk.Button(self.master, text='ほ', width=4,
                  command=lambda: self.input('ほ')).grid(row=6, column=5)

        tk.Button(self.master, text='ま', width=4,
                  command=lambda: self.input('ま')).grid(row=2, column=6)
        tk.Button(self.master, text='み', width=4,
                  command=lambda: self.input('み')).grid(row=3, column=6)
        tk.Button(self.master, text='む', width=4,
                  command=lambda: self.input('む')).grid(row=4, column=6)
        tk.Button(self.master, text='め', width=4,
                  command=lambda: self.input('め')).grid(row=5, column=6)
        tk.Button(self.master, text='も', width=4,
                  command=lambda: self.input('も')).grid(row=6, column=6)

        tk.Button(self.master, text='や', width=4,
                  command=lambda: self.input('や')).grid(row=2, column=7)
        tk.Button(self.master, text='ゆ', width=4,
                  command=lambda: self.input('ゆ')).grid(row=4, column=7)
        tk.Button(self.master, text='よ', width=4,
                  command=lambda: self.input('よ')).grid(row=6, column=7)

        tk.Button(self.master, text='ら', width=4,
                  command=lambda: self.input('ら')).grid(row=2, column=8)
        tk.Button(self.master, text='り', width=4,
                  command=lambda: self.input('り')).grid(row=3, column=8)
        tk.Button(self.master, text='る', width=4,
                  command=lambda: self.input('る')).grid(row=4, column=8)
        tk.Button(self.master, text='れ', width=4,
                  command=lambda: self.input('れ')).grid(row=5, column=8)
        tk.Button(self.master, text='ろ', width=4,
                  command=lambda: self.input('ろ')).grid(row=6, column=8)

        tk.Button(self.master, text='わ', width=4,
                  command=lambda: self.input('わ')).grid(row=2, column=9)
        tk.Button(self.master, text='を', width=4,
                  command=lambda: self.input('を')).grid(row=4, column=9)
        tk.Button(self.master, text='ん', width=4,
                  command=lambda: self.input('ん')).grid(row=6, column=9)

        tk.Button(self.master, text='決定', width=9,
                  command=lambda: self.ok_click()).grid(row=2, column=11, columnspan=2)
        # tk.Button(self.master, text='決定', width=9,
        #           command=lambda:tmb.showinfo('メッセージ',
        #           'これで良いですか？')).grid(row=2, column=11, columnspan=2)
        tk.Button(self.master, text='AC', width=4,
                  command=lambda: self.clear_all()).grid(row=4, column=11)
        tk.Button(self.master, text='C', width=4,
                  command=lambda: self.clear_one()).grid(row=5, column=11)

root = tk.Tk()
app = PisicaKeyboard(master=root)
app.mainloop()

