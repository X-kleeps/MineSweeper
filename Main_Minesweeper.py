import tkinter as tk
from random import shuffle
from tkinter.messagebox import showinfo, showerror
import datetime

win = tk.Tk()

def dismiss(win1):
    win1.grab_release() 
    win1.destroy()
    win.deiconify()

def dismis1(roole):
    roole.grab_release() 
    roole.destroy()
    win.deiconify()

def dismis2(tabl_win):
    tabl_win.grab_release() 
    tabl_win.destroy()
    win1.deiconify()

def write_rezult():
    z = open('records.txt', 'a')

def tabl_rezult():
    global tabl_win
    win1.withdraw()
    tabl_win = tk.Toplevel()
    tabl_win.configure(bg='#04d438')
    tabl_win.protocol("WM_DELETE_WINDOW", lambda: dismis2(tabl_win))
    x = (tabl_win.winfo_screenwidth() - tabl_win.winfo_reqwidth()) / 2.8 #По середине экрана
    y = (tabl_win.winfo_screenheight() - tabl_win.winfo_reqheight()) / 5
    tabl_win.wm_geometry("+%d+%d" % (x, y))
    tabl_win.geometry('600x600')
    photo2 = tk.PhotoImage(file = 'D:\game\Mines.png')
    tabl_win.iconphoto(False, photo2)
    tabl_win.title('Таблица результатов')
    
    global z,zt,tx
    z = open('records.txt', 'r')
    tx=z.read()

    label_tabl = tk.Label(tabl_win, text= tx, font = ('Arial',20),bg='#04d438')
    label_tabl.place(x=60,y=200)
    z.close()

    label_rez = tk.Label(tabl_win, text='Таблица результатов',font = ('Arial',20),bg='#04d438')
    label_rez.place(x=160,y=100)

    def delite():
        z = open('records.txt', 'r+')
        z.truncate()
        z.close() 

    back3 = tk.Button(tabl_win, text = 'Удалить',font = ('Arial',20),command=delite)
    back3.place(x=160,y=500)

    back3 = tk.Button(tabl_win, text = 'Назад',font = ('Arial',20),command=lambda: dismis2(tabl_win),bg = 'red')
    back3.place(x=10,y=500)

def vibor():
    global win1
    win.withdraw()
    win1 = tk.Toplevel()
    win1.configure(bg='#04d438')
    win1.protocol("WM_DELETE_WINDOW", lambda: dismiss(win1))
    x = (win1.winfo_screenwidth() - win1.winfo_reqwidth()) / 2.8 #По середине экрана
    y = (win1.winfo_screenheight() - win1.winfo_reqheight()) / 5
    win1.wm_geometry("+%d+%d" % (x, y))
    win1.geometry('600x600')
    photo2 = tk.PhotoImage(file = 'D:\game\Mines.png')
    win1.iconphoto(False, photo2)
    win1.title('Выбор режима')
    back = tk.Button(win1, text = 'Назад',font = ('Arial',20),command=lambda: dismiss(win1),bg = 'red')
    back.place(x=10,y=500)

    label_vibor_mane = tk.Label(win1, text='Выбор режима',font = ('Arial',20),bg='#04d438')
    label_vibor_mane.place(x=210,y=100)

    MineSweeperclassic = tk.Button(win1, text = 'Классический сапер',font = ('Arial',20),bg = 'green',command=classic_Minesweeper)
    MineSweeperclassic.place(x=160,y=160)

    MineSweeper_with_3_live = tk.Button(win1, text = 'С тремя жизнями',font = ('Arial',20),bg = 'green', command=Minesweeper_with3)
    MineSweeper_with_3_live.place(x=180,y=220)

    MineSweeper_no_flags = tk.Button(win1, text = 'Без флажков',font = ('Arial',20),bg = 'green',command=no_flag)
    MineSweeper_no_flags.place(x=210,y=280)

    MineSweeper_tabl = tk.Button(win1, text = 'Таблица результатов',font = ('Arial',20),bg = 'green',command=tabl_rezult)
    MineSweeper_tabl.place(x=152,y=380)

    win1.resizable(0,0)

def game_exit():
    win.destroy()

def game_rules():
    win.withdraw()
    roole = tk.Toplevel()
    roole.configure(bg='#04d438')
    roole.protocol("WM_DELETE_WINDOW", lambda: dismis1(roole))
    x = (roole.winfo_screenwidth() - roole.winfo_reqwidth()) / 2.8 #По середине экрана
    y = (roole.winfo_screenheight() - roole.winfo_reqheight()) / 5
    roole.wm_geometry("+%d+%d" % (x, y))
    roole.geometry('600x600')
    photo2 = tk.PhotoImage(file = 'D:\game\Mines.png')
    roole.iconphoto(False, photo2)
    roole.title('Правила игры')
    back1 = tk.Button(roole, text = 'Назад',font = ('Arial',20),command=lambda: dismis1(roole),bg='red')
    back1.place(x=10,y=500)

    label_role_mane = tk.Label(roole, text='Правила игры',font = ('Arial',20),bg='#04d438')
    label_role_mane.place(x=210,y=60)

    label_role = tk.Label(roole, text = '''
    Игровое поле разделено на ячейки некоторые из которых
    «заминированы». Целью игры является открытие всех
    ячеек, не содержащих жизни. Игрок открывает ячейки (ЛКМ),
    стараясь не открыть ячейку с миной. Открыв ячейку с миной,
    он проигрывает. Потенциальную клетку с миной можно
    пометить флажком (ПКМ). Поле открытия клетки, если это
    не мина, появляется цифра, которая указывает количество
    мин в ее области (вокруг цифры на 1 клетку). 
    Открыв все «не заминированные» ячейки, игрок выигрывает.
    ''',font = ('Arial',15),justify=tk.LEFT,bg='#04d438')
    label_role.place(x=0,y=100)

    roole.resizable(0,0)


def main_menu():
    x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2.8 #По середине экрана
    y = (win.winfo_screenheight() - win.winfo_reqheight()) / 5
    win.wm_geometry("+%d+%d" % (x, y))
    win.geometry('600x600')
    win.configure(bg='#04d438')
    photo = tk.PhotoImage(file = 'D:\game\Mines.png')
    win.iconphoto(False, photo)
    win.title('Главное меню')
    win.protocol("WM_DELETE_WINDOW", lambda: win.destroy())

    label1 = tk.Label(win, text = 'Сапёр',font = ('Arial',20),bg='#04d438')
    label1.place(x=260,y=100)

    btn1 = tk.Button(win, text = 'Выбор режима',font = ('Arial',20),bg='green', command=vibor)
    btn1.place(x=200,y=150)


    btn2 = tk.Button(win, text = 'Правила игры',font = ('Arial',20),bg='green',command=game_rules)
    btn2.place(x=205,y=215)

    btn3 = tk.Button(win, text = 'Выход',font = ('Arial',20),bg='green', command = game_exit)
    btn3.place(x=250,y=280)
    
    win.protocol("WM_DELETE_WINDOW", game_exit)
    win.resizable(0,0)
    win.mainloop()

def classic_Minesweeper ():
    win1.withdraw()
    
    colors = {
        1: 'blue',
        2: 'lime',
        3: 'red',
        4: '#a134eb',
        5: '#ff00a2',
        6: '#ff9100',
        7: '#000dff',
        8: '#d869fa',
    }

    class MyButton (tk.Button):
        
        def __init__(self, master, x, y, number=0, *args, **kwargs):
                super(MyButton, self).__init__(master, width=3,font='Calibri 15 bold', background='green', *args, **kwargs)
                self.x=x
                self.y=y
                self.number=number
                self.is_mine=False
                self.count_bomb = 0
                self.is_open = False
        def __repr__(self):
            return f'MyButton {self.x} {self.y} {self.number} {self.is_mine}'


    class MineSweeper:
        window = tk.Toplevel()
        ROW=10      #Ряд
        COLUMS=10   #Колонка
        MINES=15    #Мина
        is_game_over = False
        is_win = False
        is_first_click = True
        number_move = 0
        flag = False
        
        def __init__(self):
            self.buttons = []
            for i in range(MineSweeper.ROW+2): #Создание кнопок
                temp = []
                for j in range(MineSweeper.COLUMS+2):
                    btn= MyButton(MineSweeper.window,x=i, y=j)
                    btn.config(command=lambda button=btn: self.click(button))
                    btn.bind("<Button-3>", self.right_click)
                    temp.append(btn)
                self.buttons.append(temp)

        def right_click(self, event):
            if MineSweeper.is_game_over:
                return

            current_btn = event.widget
            if current_btn['state'] == 'normal':
                current_btn['state'] = 'disable'
                current_btn['text'] = '🚩'
                current_btn['disabledforeground'] = 'red'
            elif current_btn['text'] == '🚩':
                current_btn['text'] = ''
                current_btn['state'] = 'normal'

        def click(self, cliked_button:MyButton):
            global overmenu,winmenu

            if MineSweeper.is_game_over:
                return

            if MineSweeper.is_win:
                return 

            if MineSweeper.is_first_click:
                self.insert_mines(cliked_button.number)
                self.count_mines_in_buttons()
                self.create_consol_button()
                MineSweeper.is_first_click = False

            if cliked_button.is_mine:
                cliked_button.config(text='💣', background='red',disabledforeground='black')
                cliked_button.is_open = True
                MineSweeper.is_game_over = True
                #------------------------------------------------------------------------------------------------------------------------#
                def over_exit():
                    over_menu.destroy()
                    print('Открыто клеток',MineSweeper.number_move)
                    for i in range(1,MineSweeper.ROW+1):
                        for j in range(1,MineSweeper.COLUMS+1):
                            btn=self.buttons[i][j]
                            if btn.is_mine:
                                btn['text'] = '💣'

                over_menu  = tk.Toplevel(self.window)
                over_menu.title('Проигрышь')
                over_menu.configure(bg='red')
                label11 = tk.Label(over_menu, text = 'Вы проиграли',font = ('Arial',20),bg='red')
                label11.pack()
                x = (over_menu.winfo_screenwidth() - over_menu.winfo_reqwidth()) / 1.9 #По середине экрана
                y = (over_menu.winfo_screenheight() - over_menu.winfo_reqheight()) / 2
                over_menu.resizable(0,0)
                over_menu.wm_geometry("+%d+%d" % (x, y))
                over_menu.geometry('200x100')
                over_menu.overrideredirect(True)
                over_menu.grab_set()
                btn_exit = tk.Button(over_menu, text = 'ОК',font = ('Arial',15,),bg='#A30008', command = over_exit)
                btn_exit.pack()

            else:
                MineSweeper.number_move+=1
                color = colors.get(cliked_button.count_bomb, 'black')
                if cliked_button.count_bomb:
                    cliked_button.config(text=cliked_button.count_bomb,disabledforeground=color,bg='yellow')
                    cliked_button.is_open = True
                else:
                    self.breadth_first_search(cliked_button)
            cliked_button.config(state='disable')
            cliked_button.config(relief=tk.SUNKEN)

            if MineSweeper.number_move == (MineSweeper.ROW*MineSweeper.COLUMS-MineSweeper.MINES):
                MineSweeper.is_win = True

                def win_exit():
                    winmenu.destroy()

                winmenu  = tk.Toplevel(self.window)
                global time_finish
                time_finish = datetime.datetime.today()
                print(time_finish)
                timer = time_finish - time_start
                time1 = str(timer)[:10]
                print(time1)
                z2 = sum(1 for line in open('records.txt', 'r'))
                if not (z2 == 5):
                    zz = open('records.txt', 'a')
                    zz.write(name1 + ' Классический ' + time1 + '\n')
                else:
                    zz = open('records.txt', 'w')
                    zz.write(name1 + ' Классический ' + time1 + '\n')

                winmenu.title('Победа')
                winmenu.configure(bg='lime')
                label_win = tk.Label(winmenu, text = 'Вы выиграли',font = ('Arial',20),bg='lime')
                label_win.pack()
                x = (label_win.winfo_screenwidth() - label_win.winfo_reqwidth()) / 2 #По середине экрана
                y = (label_win.winfo_screenheight() - label_win.winfo_reqheight()) / 2.2
                winmenu.resizable(0,0)
                winmenu.wm_geometry("+%d+%d" % (x, y))
                winmenu.geometry('200x100')
                winmenu.overrideredirect(True)
                winmenu.grab_set()
                btn_win = tk.Button(winmenu, text = 'ОК',font = ('Arial',15),bg='green', command = win_exit)
                btn_win.pack()
                
            

        def breadth_first_search (self, btn:MyButton): #Поиск в ширину
            queue = [btn]
            while queue:
                
                current_btn = queue.pop()
                color = colors.get(current_btn.count_bomb, 'black')
                if current_btn.count_bomb:
                    current_btn.config(text=current_btn.count_bomb, disabledforeground=color,bg='yellow')
                else:
                    current_btn.config(text='',disabledforeground=color, bg='yellow')
                current_btn.is_open = True
                current_btn.config(state='disable')
                current_btn.config(relief=tk.SUNKEN)

                if current_btn.count_bomb == 0:
                    x, y = current_btn.x, current_btn.y
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:

                            next_btn = self.buttons[x+dx][y+dy]
                            if  not next_btn.is_open and 1 <= next_btn.x <= MineSweeper.ROW and 1 <= next_btn.y <= MineSweeper.COLUMS and next_btn not in queue:
                                queue.append(next_btn)
                                MineSweeper.number_move+=1
                            

        def reload(self):
            [child.destroy() for child in self.window.winfo_children()]
            self.__init__()
            self.name_win()
            self.create_button()
            MineSweeper.is_first_click = True
            MineSweeper.is_game_over = False
            MineSweeper.is_win = False
            MineSweeper.number_move=0

        def creat_settings_win(self):
            global mines_entry, row_entry, column_entry
            win_settings = tk.Toplevel(self.window)
            win_settings.title('Настройки')
            tk.Label(win_settings, text = 'Количество рядов').grid(row = 0, column = 0)
            row_entry = tk.Entry(win_settings)
            row_entry.insert(0, MineSweeper.ROW)
            row_entry.grid(row = 0, column = 1,padx = 20, pady = 20)
            tk.Label(win_settings, text = 'Количество строк').grid(row = 1, column = 0)
            column_entry = tk.Entry(win_settings)
            column_entry.insert(0, MineSweeper.COLUMS)
            column_entry.grid(row = 1, column = 1,padx = 20, pady = 20)
            tk.Label(win_settings, text = 'Количество мин').grid(row = 2, column = 0)
            mines_entry = tk.Entry(win_settings)
            mines_entry.insert(0, MineSweeper.MINES)
            mines_entry.grid(row = 2, column = 1,padx = 20, pady = 20)
            save_btn = tk.Button(win_settings, text='Применить', command=lambda: self.change_settings(row_entry, column_entry, mines_entry))
            save_btn.grid(row = 3, column = 0, columnspan = 2, padx = 20, pady = 20)
            x = (win_settings.winfo_screenwidth() - win_settings.winfo_reqwidth()) / 2 #По середине экрана
            y = (win_settings.winfo_screenheight() - win_settings.winfo_reqheight()) / 2.2
            win_settings.resizable(0,0)
            win_settings.wm_geometry("+%d+%d" % (x, y))
            win_settings.grab_set()
            win_settings.focus_set()

        def change_settings(self, row: tk.Entry, column: tk.Entry, mines: tk.Entry):
            try:
                int(row.get()), int(column.get()), int(mines.get())
            except ValueError:
                showerror('Ошибка', 'Введено неправильное значение')
                return
            MineSweeper.ROW = int(row.get())
            MineSweeper.COLUMS = int(column.get())
            MineSweeper.MINES = int(mines.get())

            if MineSweeper.ROW < 10 or MineSweeper.ROW > 25:
                showerror('Ошибка', 'Строка не может быть меньше 10 или больше 25')
                MineSweeper.ROW = 10
                row_entry.delete("0","end")
                row_entry.insert(0, MineSweeper.ROW)
                return
            
            if MineSweeper.COLUMS < 10 or MineSweeper.COLUMS > 25:
                showerror('Ошибка', 'Ряд не может быть меньше 10 или больше 25')
                MineSweeper.COLUMS = 10
                column_entry.delete("0","end")
                column_entry.insert(0, MineSweeper.COLUMS)
                return
            
            if MineSweeper.ROW != MineSweeper.COLUMS:
                showerror('Ошибка', 'Строка должна быть равна ряду')
                MineSweeper.ROW = 10
                row_entry.delete("0","end")
                row_entry.insert(0, MineSweeper.ROW)
                MineSweeper.COLUMS = 10
                column_entry.delete("0","end")
                column_entry.insert(0, MineSweeper.ROW)
                return

            if (MineSweeper.MINES > (MineSweeper.ROW*MineSweeper.COLUMS-1)):
                showerror('Ошибка', 'Мин не может быть больше клеток')

                MineSweeper.MINES = 15
                mines_entry.delete("0","end")
                mines_entry.insert(0, MineSweeper.MINES)
                return
            else:
                self.reload()


        def rezinexit(self):
            self.window.destroy()
            win1.deiconify()

        def create_button(self):
            menubar = tk.Menu(self.window)
            self.window.config(menu=menubar)

            settings_menu = tk.Menu(menubar,tearoff = 0)
            menubar.add_command(label='Перезапустить', command=self.reload)
            menubar.add_command(label='Настройки', command= self.creat_settings_win)
            menubar.add_cascade(label='Выбор режима', command=self.rezinexit)
            MineSweeper.window.protocol("WM_DELETE_WINDOW", lambda: self.rezinexit())

            count = 1
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    btn.number = count
                    btn.grid (row=i, column=j,stick='NWES')
                    count += 1
            for i in range(1,MineSweeper.ROW+1):
                tk.Grid.rowconfigure(self.window, i, weight=1)
            for i in range(1,MineSweeper.COLUMS+1):
                tk.Grid.columnconfigure(self.window, i, weight=1)

        def open_all_butttons(self):
            for i in range(MineSweeper.ROW+2): #Присваивание кнопок к полю
                for j in range(MineSweeper.COLUMS+2):
                    btn=self.buttons[i][j]
                    if btn.is_mine:
                        btn.config(text="*", background='red',disabledforeground='black') 
                    elif btn.count_bomb in colors:
                        color = colors.get(btn.count_bomb, 'black')
                        btn.config(text=btn.count_bomb, fg=color)

        def name_win(self):
            global name,Nickmane

            def write_rezult():
                if len(Nickmane.get()) == 0 or Nickmane.get() == ' ':
                    showerror('Ошибка', 'Введено неправильное значение')
                    return                
                global time_start,name1
                name1 = Nickmane.get()
                name.destroy()
                time_start = datetime.datetime.today()
                print (time_start)
                
            name = tk.Toplevel(self.window)
            tk.Label(name, text = 'Введите имя').grid(row = 0, column = 0)
            Nickmane = tk.Entry(name)
            Nickmane.grid(row = 2, column = 0,padx = 20, pady = 5)
            Nickmane_ok= tk.Button(name, text='Применить',command=write_rezult)
            Nickmane_ok.grid(row = 3, column = 0, columnspan = 2, padx = 20, pady = 10)
            x = (name.winfo_screenwidth() - name.winfo_reqwidth()) / 2 #По середине экрана
            y = (name.winfo_screenheight() - name.winfo_reqheight()) / 2.2
            name.wm_geometry("+%d+%d" % (x, y))            
            name.resizable(0,0)
            name.grab_set()
            name.focus_set()
            name.overrideredirect(True)


        def start_classic_Minesweeper(self):
            self.name_win()
            self.create_button()
            MineSweeper.window.title('Сапер классический')
            x = (MineSweeper.window.winfo_screenwidth() - MineSweeper.window.winfo_reqwidth()) / 2.8 #По середине экрана
            y = (MineSweeper.window.winfo_screenheight() - MineSweeper.window.winfo_reqheight()) / 5
            MineSweeper.window.wm_geometry("+%d+%d" % (x, y))
            MineSweeper.window.geometry('600x600')
            photo = tk.PhotoImage(file = 'D:\game\Mines.png')
            MineSweeper.window.iconphoto(False, photo)
            MineSweeper.window.deiconify()
            MineSweeper.window.resizable(0,0) #Запрет Масштабирование 


        def create_consol_button(self):
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    if btn.is_mine:
                        print('*', end=' ')
                    else:
                        print(btn.count_bomb, end=' ')
                print()

        def insert_mines(self, number: int):
            index_mines = self.get_mines_places(number)
            print(index_mines)
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    if btn.number in index_mines:
                        btn.is_mine = True

        def count_mines_in_buttons(self):
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    count_bomb = 0
                    if not btn.is_mine:
                        for row_dx in [1, 0, -1]:
                            for col_dx in [1, 0, -1]:
                                neigbour = self.buttons[i+row_dx][j+col_dx]
                                if neigbour.is_mine:
                                    count_bomb +=1
                    btn.count_bomb = count_bomb

        @staticmethod
        def get_mines_places(exclude_number:int):
            indexes=list(range(1, MineSweeper.COLUMS * MineSweeper.ROW + 1))
            print(f'Исключить кнопку {exclude_number}')
            indexes.remove(exclude_number)
            shuffle(indexes)
            return indexes[:MineSweeper.MINES]
    
    game=MineSweeper()
    game.start_classic_Minesweeper()

def Minesweeper_with3 ():
    win1.withdraw()
    colors = {
        1: 'blue',
        2: 'lime',
        3: 'red',
        4: '#a134eb',
        5: '#ff00a2',
        6: '#ff9100',
        7: '#000dff',
        8: '#d869fa',
    }

    class MyButton (tk.Button):
        
        def __init__(self, master, x, y, number=0, *args, **kwargs):
                super(MyButton, self).__init__(master, width=3,font='Calibri 15 bold', background='green', *args, **kwargs)
                self.x=x
                self.y=y
                self.number=number
                self.is_mine=False
                self.count_bomb = 0
                self.is_open = False

        def __repr__(self):
            return f'MyButton {self.x} {self.y} {self.number} {self.is_mine}'


    class MineSweeper:
        window =tk.Toplevel()
        ROW=10      #Ряд
        COLUMS=10   #Колонка
        MINES=15    #Мина
        is_game_over = False
        is_win = False
        is_first_click = True
        number_move = 0
        live_point = 3

        def __init__(self):
            self.buttons = []
            for i in range(MineSweeper.ROW+2): #Создание кнопок
                temp = []
                for j in range(MineSweeper.COLUMS+2):
                    btn= MyButton(MineSweeper.window,x=i, y=j)
                    btn.config(command=lambda button=btn: self.click(button))
                    btn.bind("<Button-3>", self.right_click)
                    temp.append(btn)
                self.buttons.append(temp)

        def right_click(self, event):
            if MineSweeper.is_game_over:
                return

            current_btn = event.widget
            if current_btn['state'] == 'normal':
                current_btn['state'] = 'disable'
                current_btn['text'] = '🚩'
                current_btn['disabledforeground'] = 'red'
            elif current_btn['text'] == '🚩':
                current_btn['text'] = ''
                current_btn['state'] = 'normal'


        def click(self, cliked_button:MyButton):

            if MineSweeper.is_game_over:
                return

            if MineSweeper.is_win:
                return 

            if MineSweeper.is_first_click:
                self.insert_mines(cliked_button.number)
                self.count_mines_in_buttons()
                self.create_consol_button()
                MineSweeper.is_first_click = False

            if cliked_button.is_mine:
                cliked_button.config(text='💣', background='red',disabledforeground='black')
                cliked_button.is_open = True
                MineSweeper.live_point -=1
                print('сердечки',MineSweeper.live_point)   

                if MineSweeper.live_point == 0:
                    MineSweeper.is_game_over = True
                    def over_exit():
                        over_menu.destroy()
                        print('Открыто клеток',MineSweeper.number_move)
                        for i in range(1,MineSweeper.ROW+1):
                            for j in range(1,MineSweeper.COLUMS+1):
                                btn=self.buttons[i][j]
                                if btn.is_mine:
                                    btn['text'] = '💣'

                    over_menu  = tk.Toplevel(self.window)
                    over_menu.title('Проигрышь')
                    over_menu.configure(bg='red')
                    label11 = tk.Label(over_menu, text = 'Вы проиграли',font = ('Arial',20),bg='red')
                    label11.pack()
                    x = (over_menu.winfo_screenwidth() - over_menu.winfo_reqwidth()) / 2 #По середине экрана
                    y = (over_menu.winfo_screenheight() - over_menu.winfo_reqheight()) / 2
                    over_menu.resizable(0,0)
                    over_menu.wm_geometry("+%d+%d" % (x, y))
                    over_menu.geometry('200x100')
                    over_menu.overrideredirect(True)
                    over_menu.grab_set()
                    btn_exit = tk.Button(over_menu, text = 'ОК',font = ('Arial',15),bg='#A30008', command = over_exit)
                    btn_exit.pack()

            else:
                MineSweeper.number_move+=1
                color = colors.get(cliked_button.count_bomb, 'black')
                if cliked_button.count_bomb:
                    cliked_button.config(text=cliked_button.count_bomb,disabledforeground=color,bg='yellow')
                    cliked_button.is_open = True
                else:
                    self.breadth_first_search(cliked_button)
            cliked_button.config(state='disable')
            cliked_button.config(relief=tk.SUNKEN)

            if MineSweeper.number_move == (MineSweeper.ROW*MineSweeper.COLUMS-MineSweeper.MINES):
                MineSweeper.is_win = True
                def win_exit():
                    winmenu.destroy()

                winmenu  = tk.Toplevel(self.window)

                global time_finish
                time_finish = datetime.datetime.today()
                print(time_finish)
                timer = time_finish - time_start1
                time1 = str(timer)[:10]
                print(time1)
                z2 = sum(1 for line in open('records.txt', 'r'))
                if not (z2 == 5):
                    zz = open('records.txt', 'a')
                    zz.write(name1 + ' С тремя жизнями ' + time1 + '\n')
                else:
                    zz = open('records.txt', 'w')
                    zz.write(name1 + ' С тремя жизнями ' + time1 + '\n')

                winmenu.title('Победа')
                winmenu.configure(bg='lime')
                label_win = tk.Label(winmenu, text = 'Вы выиграли',font = ('Arial',20),bg='lime')
                label_win.pack()
                x = (label_win.winfo_screenwidth() - label_win.winfo_reqwidth()) / 2 #По середине экрана
                y = (label_win.winfo_screenheight() - label_win.winfo_reqheight()) / 2
                winmenu.resizable(0,0)
                winmenu.wm_geometry("+%d+%d" % (x, y))
                winmenu.geometry('200x100')
                winmenu.overrideredirect(True)
                winmenu.grab_set()
                btn_win = tk.Button(winmenu, text = 'ОК',font = ('Arial',15),bg='green', command = win_exit)
                btn_win.pack()
                
            

        def breadth_first_search (self, btn:MyButton):
            queue = [btn]
            while queue:
                
                current_btn = queue.pop()
                color = colors.get(current_btn.count_bomb, 'black')
                if current_btn.count_bomb:
                    current_btn.config(text=current_btn.count_bomb, disabledforeground=color,bg='yellow')
                else:
                    current_btn.config(text='',disabledforeground=color, bg='yellow')
                current_btn.is_open = True
                current_btn.config(state='disable')
                current_btn.config(relief=tk.SUNKEN)

                if current_btn.count_bomb == 0:
                    x, y = current_btn.x, current_btn.y
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:

                            next_btn = self.buttons[x+dx][y+dy]
                            if  not next_btn.is_open and 1 <= next_btn.x <= MineSweeper.ROW and 1 <= next_btn.y <= MineSweeper.COLUMS and next_btn not in queue:
                                queue.append(next_btn)
                                MineSweeper.number_move+=1
                            

        def reload(self):
            [child.destroy() for child in self.window.winfo_children()]
            self.__init__()
            self.name_win()
            self.create_button()
            MineSweeper.is_first_click = True
            MineSweeper.is_game_over = False
            MineSweeper.is_win = False
            MineSweeper.number_move=0
            MineSweeper.live_point = 3

        def creat_settings_win(self):
            global mines_entry, row_entry, column_entry
            win_settings = tk.Toplevel(self.window)
            win_settings.title('Настройки')
            tk.Label(win_settings, text = 'Количество рядов').grid(row = 0, column = 0)
            row_entry = tk.Entry(win_settings)
            row_entry.insert(0, MineSweeper.ROW)
            row_entry.grid(row = 0, column = 1,padx = 20, pady = 20)
            tk.Label(win_settings, text = 'Количество строк').grid(row = 1, column = 0)
            column_entry = tk.Entry(win_settings)
            column_entry.insert(0, MineSweeper.COLUMS)
            column_entry.grid(row = 1, column = 1,padx = 20, pady = 20)
            tk.Label(win_settings, text = 'Количество мин').grid(row = 2, column = 0)
            mines_entry = tk.Entry(win_settings)
            mines_entry.insert(0, MineSweeper.MINES)
            mines_entry.grid(row = 2, column = 1,padx = 20, pady = 20)
            save_btn = tk.Button(win_settings, text='Применить', command=lambda: self.change_settings(row_entry, column_entry, mines_entry))
            save_btn.grid(row = 3, column = 0, columnspan = 2, padx = 20, pady = 20)
            x = (win_settings.winfo_screenwidth() - win_settings.winfo_reqwidth()) / 2 #По середине экрана
            y = (win_settings.winfo_screenheight() - win_settings.winfo_reqheight()) / 2.2
            win_settings.resizable(0,0)
            win_settings.wm_geometry("+%d+%d" % (x, y))
            win_settings.grab_set()
            win_settings.focus_set()

        def change_settings(self, row: tk.Entry, column: tk.Entry, mines: tk.Entry):
            try:
                int(row.get()), int(column.get()), int(mines.get())
            except ValueError:
                showerror('Ошибка', 'Введено неправильное значение')
                return
            MineSweeper.ROW = int(row.get())
            MineSweeper.COLUMS = int(column.get())
            MineSweeper.MINES = int(mines.get())

            if MineSweeper.ROW < 10 or MineSweeper.ROW > 25:
                showerror('Ошибка', 'Ряд не может быть меньше 10 или больше 25')
                MineSweeper.ROW = 10
                row_entry.delete("0","end")
                row_entry.insert(0, MineSweeper.ROW)
                return
            
            if MineSweeper.COLUMS < 10 or MineSweeper.COLUMS > 25:
                showerror('Ошибка', 'Строк не может быть меньше 10 или больше 25')
                MineSweeper.COLUMS = 10
                column_entry.delete("0","end")
                column_entry.insert(0, MineSweeper.COLUMS)
                return

            if MineSweeper.ROW != MineSweeper.COLUMS:
                showerror('Ошибка', 'Строка должна быть равна ряду')
                MineSweeper.ROW = 10
                row_entry.delete("0","end")
                row_entry.insert(0, MineSweeper.ROW)
                MineSweeper.COLUMS = 10
                column_entry.delete("0","end")
                column_entry.insert(0, MineSweeper.ROW)
                return

            if (MineSweeper.MINES > (MineSweeper.ROW*MineSweeper.COLUMS-1)):
                showerror('Ошибка', 'Мин не может быть меньше 10')

                MineSweeper.MINES = 15
                mines_entry.delete("0","end")
                mines_entry.insert(0, MineSweeper.MINES)
                return
            else:
                self.reload()

        def rezinexit1(self):
            self.window.destroy()
            win1.deiconify()

        def create_button(self):
            menubar = tk.Menu(self.window)
            self.window.config(menu=menubar)

            settings_menu = tk.Menu(menubar,tearoff = 0)
            menubar.add_command(label='Перезапустить', command=self.reload)
            menubar.add_command(label='Настройки', command= self.creat_settings_win)
            menubar.add_cascade(label='Выбор режима', command=self.rezinexit1)
            MineSweeper.window.protocol("WM_DELETE_WINDOW", lambda: self.rezinexit1())
            
            if MineSweeper.live_point == 3:
                print('сердечки',MineSweeper.live_point)
            elif MineSweeper.live_point == 2:
                print('сердечки',MineSweeper.live_point)
            elif MineSweeper.live_point == 1:
                print('сердечки',MineSweeper.live_point)
            elif MineSweeper.live_point == 0:
                print('сердечки',MineSweeper.live_point)   


            count = 1
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    btn.number = count
                    btn.grid (row=i, column=j,stick='NWES')
                    count += 1
            for i in range(1,MineSweeper.ROW+1):
                tk.Grid.rowconfigure(self.window, i, weight=1)
            for i in range(1,MineSweeper.COLUMS+1):
                tk.Grid.columnconfigure(self.window, i, weight=1)

        def open_all_butttons(self):
            for i in range(MineSweeper.ROW+2): #Присваивание кнопок к полю
                for j in range(MineSweeper.COLUMS+2):
                    btn=self.buttons[i][j]
                    if btn.is_mine:
                        btn.config(text="*", background='red',disabledforeground='black') 
                    elif btn.count_bomb in colors:
                        color = colors.get(btn.count_bomb, 'black')
                        btn.config(text=btn.count_bomb, fg=color)

        def name_win(self):
            global name,Nickmane

            def write_rezult():
                if len(Nickmane.get()) == 0 or Nickmane.get() == ' ':
                    showerror('Ошибка', 'Введено неправильное значение')
                    return                
                global time_start1,name1
                name1 = Nickmane.get()
                name.destroy()
                time_start1 = datetime.datetime.today()
                print (time_start1)
                
            name = tk.Toplevel(self.window)
            tk.Label(name, text = 'Введите имя').grid(row = 0, column = 0)
            Nickmane = tk.Entry(name)
            Nickmane.grid(row = 2, column = 0,padx = 20, pady = 5)
            Nickmane_ok= tk.Button(name, text='Применить',command=write_rezult)
            Nickmane_ok.grid(row = 3, column = 0, columnspan = 2, padx = 20, pady = 10)
            x = (name.winfo_screenwidth() - name.winfo_reqwidth()) / 2 #По середине экрана
            y = (name.winfo_screenheight() - name.winfo_reqheight()) / 2.2
            name.wm_geometry("+%d+%d" % (x, y))            
            name.resizable(0,0)
            name.grab_set()
            name.focus_set()
            name.overrideredirect(True)

        def noflag_Minesweeper(self):
            self.name_win()
            self.create_button()
            MineSweeper.window.title('Сапер с тремя жизнями')
            x = (MineSweeper.window.winfo_screenwidth() - MineSweeper.window.winfo_reqwidth()) / 2.8 #По середине экрана
            y = (MineSweeper.window.winfo_screenheight() - MineSweeper.window.winfo_reqheight()) / 5
            MineSweeper.window.wm_geometry("+%d+%d" % (x, y))
            MineSweeper.window.geometry('600x600')           
            photo = tk.PhotoImage(file = 'D:\game\Mines.png')
            MineSweeper.window.iconphoto(False, photo)
            MineSweeper.window.deiconify()
            MineSweeper.window.resizable(0,0) #Запрет Масштабирование 

        def create_consol_button(self):
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    if btn.is_mine:
                        print('*', end=' ')
                    else:
                        print(btn.count_bomb, end=' ')
                print()

        def insert_mines(self, number: int):
            index_mines = self.get_mines_places(number)
            print(index_mines)
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    if btn.number in index_mines:
                        btn.is_mine = True

        def count_mines_in_buttons(self):
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    count_bomb = 0
                    if not btn.is_mine:
                        for row_dx in [1, 0, -1]:
                            for col_dx in [1, 0, -1]:
                                neigbour = self.buttons[i+row_dx][j+col_dx]
                                if neigbour.is_mine:
                                    count_bomb +=1
                    btn.count_bomb = count_bomb

        @staticmethod
        def get_mines_places(exclude_number:int):
            indexes=list(range(1, MineSweeper.COLUMS * MineSweeper.ROW + 1))
            print(f'Исключить кнопку {exclude_number}')
            indexes.remove(exclude_number)
            shuffle(indexes)
            return indexes[:MineSweeper.MINES]
    game=MineSweeper()
    game.noflag_Minesweeper() 

def no_flag ():
    win1.withdraw()
    colors = {
        1: 'blue',
        2: 'lime',
        3: 'red',
        4: '#a134eb',
        5: '#ff00a2',
        6: '#ff9100',
        7: '#000dff',
        8: '#d869fa',
    }

    class MyButton (tk.Button):
        
        def __init__(self, master, x, y, number=0, *args, **kwargs):
                super(MyButton, self).__init__(master, width=3,font='Calibri 15 bold', background='green', *args, **kwargs)
                self.x=x
                self.y=y
                self.number=number
                self.is_mine=False
                self.count_bomb = 0
                self.is_open = False
        def __repr__(self):
            return f'MyButton {self.x} {self.y} {self.number} {self.is_mine}'


    class MineSweeper:

        window = tk.Toplevel()
        ROW=10      #Ряд
        COLUMS=10   #Колонка
        MINES=15    #Мина
        is_game_over = False
        is_win = False
        is_first_click = True
        number_move = 0
        flag = False
        
        def __init__(self):
            self.buttons = []
            for i in range(MineSweeper.ROW+2): #Создание кнопок
                temp = []
                for j in range(MineSweeper.COLUMS+2):
                    btn= MyButton(MineSweeper.window,x=i, y=j)
                    btn.config(command=lambda button=btn: self.click(button))
                    btn.bind("<Button-3>", self.right_click)
                    temp.append(btn)
                self.buttons.append(temp)

        def right_click(self, event):
            if MineSweeper.is_game_over:
                return



        def click(self, cliked_button:MyButton):

            if MineSweeper.is_game_over:
                return

            if MineSweeper.is_win:
                return 

            if MineSweeper.is_first_click:
                self.insert_mines(cliked_button.number)
                self.count_mines_in_buttons()
                self.create_consol_button()
                MineSweeper.is_first_click = False

            if cliked_button.is_mine:
                cliked_button.config(text='💣', background='red',disabledforeground='black')
                cliked_button.is_open = True
                MineSweeper.is_game_over = True
                def over_exit():
                    over_menu.destroy()
                    print('Открыто клеток',MineSweeper.number_move)
                    for i in range(1,MineSweeper.ROW+1):
                        for j in range(1,MineSweeper.COLUMS+1):
                            btn=self.buttons[i][j]
                            if btn.is_mine:
                                btn['text'] = '💣'

                over_menu  = tk.Toplevel(self.window)
                over_menu.title('Проигрышь')
                over_menu.configure(bg='red')
                label11 = tk.Label(over_menu, text = 'Вы проиграли',font = ('Arial',20),bg='red')
                label11.pack()
                x = (over_menu.winfo_screenwidth() - over_menu.winfo_reqwidth()) / 2 #По середине экрана
                y = (over_menu.winfo_screenheight() - over_menu.winfo_reqheight()) / 2
                over_menu.resizable(0,0)
                over_menu.wm_geometry("+%d+%d" % (x, y))
                over_menu.geometry('200x100')
                over_menu.overrideredirect(True)
                over_menu.grab_set()
                btn_exit = tk.Button(over_menu, text = 'ОК',font = ('Arial',15),bg='#A30008', command = over_exit)
                btn_exit.pack()

            else:
                MineSweeper.number_move+=1
                color = colors.get(cliked_button.count_bomb, 'black')
                if cliked_button.count_bomb:
                    cliked_button.config(text=cliked_button.count_bomb,disabledforeground=color,bg='yellow')
                    cliked_button.is_open = True
                else:
                    self.breadth_first_search(cliked_button)
            cliked_button.config(state='disable')
            cliked_button.config(relief=tk.SUNKEN)

            if MineSweeper.number_move == (MineSweeper.ROW*MineSweeper.COLUMS-MineSweeper.MINES):
                MineSweeper.is_win = True
                
                def win_exit():
                    winmenu.destroy()

                winmenu  = tk.Toplevel(self.window)

                global time_finish
                time_finish = datetime.datetime.today()
                print(time_finish)
                timer = time_finish - time_start
                time1 = str(timer)[:10]
                print(time1)
                z2 = sum(1 for line in open('records.txt', 'r'))
                if not (z2 == 5):
                    zz = open('records.txt', 'a')
                    zz.write(name1 + ' Без флажков ' + time1 + '\n')
                else:
                    zz = open('records.txt', 'w')
                    zz.write(name1 + ' Без флажков ' + time1 + '\n')

                winmenu.title('Победа')
                winmenu.configure(bg='lime')
                label_win = tk.Label(winmenu, text = 'Вы выиграли',font = ('Arial',20),bg='lime')
                label_win.pack()
                x = (label_win.winfo_screenwidth() - label_win.winfo_reqwidth()) / 2 #По середине экрана
                y = (label_win.winfo_screenheight() - label_win.winfo_reqheight()) / 2
                winmenu.resizable(0,0)
                winmenu.wm_geometry("+%d+%d" % (x, y))
                winmenu.geometry('200x100')
                winmenu.overrideredirect(True)
                winmenu.grab_set()
                btn_win = tk.Button(winmenu, text = 'ОК',font = ('Arial',15),bg='green', command = win_exit)
                btn_win.pack()
                
            

        def breadth_first_search (self, btn:MyButton):
            queue = [btn]
            while queue:
                
                current_btn = queue.pop()
                color = colors.get(current_btn.count_bomb, 'black')
                if current_btn.count_bomb:
                    current_btn.config(text=current_btn.count_bomb, disabledforeground=color,bg='yellow')
                else:
                    current_btn.config(text='',disabledforeground=color, bg='yellow')
                current_btn.is_open = True
                current_btn.config(state='disable')
                current_btn.config(relief=tk.SUNKEN)

                if current_btn.count_bomb == 0:
                    x, y = current_btn.x, current_btn.y
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:

                            next_btn = self.buttons[x+dx][y+dy]
                            if  not next_btn.is_open and 1 <= next_btn.x <= MineSweeper.ROW and 1 <= next_btn.y <= MineSweeper.COLUMS and next_btn not in queue:
                                queue.append(next_btn)
                                MineSweeper.number_move+=1
                            

        def reload(self):
            [child.destroy() for child in self.window.winfo_children()]
            self.__init__()
            self.name_win()
            self.create_button()
            MineSweeper.is_first_click = True
            MineSweeper.is_game_over = False
            MineSweeper.is_win = False
            MineSweeper.number_move=0

        def creat_settings_win(self):
            global mines_entry, row_entry, column_entry
            win_settings = tk.Toplevel(self.window)
            win_settings.title('Настройки')
            tk.Label(win_settings, text = 'Количество строк').grid(row = 0, column = 0)
            row_entry = tk.Entry(win_settings)
            row_entry.insert(0, MineSweeper.ROW)
            row_entry.grid(row = 0, column = 1,padx = 20, pady = 20)
            tk.Label(win_settings, text = 'Количество колонок').grid(row = 1, column = 0)
            column_entry = tk.Entry(win_settings)
            column_entry.insert(0, MineSweeper.COLUMS)
            column_entry.grid(row = 1, column = 1,padx = 20, pady = 20)
            tk.Label(win_settings, text = 'Количество мин').grid(row = 2, column = 0)
            mines_entry = tk.Entry(win_settings)
            mines_entry.insert(0, MineSweeper.MINES)
            mines_entry.grid(row = 2, column = 1,padx = 20, pady = 20)
            save_btn = tk.Button(win_settings, text='Применить', command=lambda: self.change_settings(row_entry, column_entry, mines_entry))
            save_btn.grid(row = 3, column = 0, columnspan = 2, padx = 20, pady = 20)
            x = (win_settings.winfo_screenwidth() - win_settings.winfo_reqwidth()) / 2 #По середине экрана
            y = (win_settings.winfo_screenheight() - win_settings.winfo_reqheight()) / 2.2
            win_settings.resizable(0,0)
            win_settings.wm_geometry("+%d+%d" % (x, y))
            win_settings.grab_set()
            win_settings.focus_set()
            
        def change_settings(self, row: tk.Entry, column: tk.Entry, mines: tk.Entry):
            try:
                int(row.get()), int(column.get()), int(mines.get())
            except ValueError:
                showerror('Ошибка', 'Введено неправильное значение')
                return

            MineSweeper.ROW = int(row.get())
            MineSweeper.COLUMS = int(column.get())
            MineSweeper.MINES = int(mines.get())

            if MineSweeper.ROW < 10 or MineSweeper.ROW > 25:
                showerror('Ошибка', 'Строка не может быть меньше 10 или больше 25')
                MineSweeper.ROW = 10
                row_entry.delete("0","end")
                row_entry.insert(0, MineSweeper.ROW)
                return
            
            if MineSweeper.COLUMS < 10 or MineSweeper.COLUMS > 25:
                showerror('Ошибка', 'Ряд не может быть меньше 10 или больше 25')
                MineSweeper.COLUMS = 10
                column_entry.delete("0","end")
                column_entry.insert(0, MineSweeper.ROW)
                return
            
            if MineSweeper.ROW != MineSweeper.COLUMS:
                showerror('Ошибка', 'Строка должна быть равна ряду')
                MineSweeper.ROW = 10
                row_entry.delete("0","end")
                row_entry.insert(0, MineSweeper.ROW)
                MineSweeper.COLUMS = 10
                column_entry.delete("0","end")
                column_entry.insert(0, MineSweeper.ROW)
                return

            if (MineSweeper.MINES > (MineSweeper.ROW*MineSweeper.COLUMS-1)):
                showerror('Ошибка', 'Мин не может быть больше клеток')

                MineSweeper.MINES = 15
                mines_entry.delete("0","end")
                mines_entry.insert(0, MineSweeper.MINES)
                return
            else:
                self.reload()


        def rezinexit2(self):
            self.window.destroy()
            win1.deiconify()

        def create_button(self):
            menubar = tk.Menu(self.window)
            self.window.config(menu=menubar)

            settings_menu = tk.Menu(menubar,tearoff = 0)
            menubar.add_command(label='Перезапустить', command=self.reload)
            menubar.add_command(label='Настройки', command= self.creat_settings_win)
            menubar.add_cascade(label='Выбор режима', command=self.rezinexit2)
            MineSweeper.window.protocol("WM_DELETE_WINDOW", lambda: self.rezinexit2())

            count = 1
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    btn.number = count
                    btn.grid (row=i, column=j,stick='NWES')
                    count += 1
            for i in range(1,MineSweeper.ROW+1):
                tk.Grid.rowconfigure(self.window, i, weight=1)
            for i in range(1,MineSweeper.COLUMS+1):
                tk.Grid.columnconfigure(self.window, i, weight=1)

        def open_all_butttons(self):
            for i in range(MineSweeper.ROW+2): #Присваивание кнопок к полю
                for j in range(MineSweeper.COLUMS+2):
                    btn=self.buttons[i][j]
                    if btn.is_mine:
                        btn.config(text="*", background='red',disabledforeground='black') 
                    elif btn.count_bomb in colors:
                        color = colors.get(btn.count_bomb, 'black')
                        btn.config(text=btn.count_bomb, fg=color)


        def name_win(self):
            global name,Nickmane

            def write_rezult():
                if len(Nickmane.get()) == 0 or Nickmane.get() == ' ':
                    showerror('Ошибка', 'Введено неправильное значение')
                    return                
                global time_start,name1
                name1 = Nickmane.get()
                name.destroy()
                time_start = datetime.datetime.today()
                print (time_start)
                
            name = tk.Toplevel(self.window)
            tk.Label(name, text = 'Введите имя').grid(row = 0, column = 0)
            Nickmane = tk.Entry(name)
            Nickmane.grid(row = 2, column = 0,padx = 20, pady = 5)
            Nickmane_ok= tk.Button(name, text='Применить',command=write_rezult)
            Nickmane_ok.grid(row = 3, column = 0, columnspan = 2, padx = 20, pady = 10)
            x = (name.winfo_screenwidth() - name.winfo_reqwidth()) / 2 #По середине экрана
            y = (name.winfo_screenheight() - name.winfo_reqheight()) / 2.2
            name.wm_geometry("+%d+%d" % (x, y))            
            name.resizable(0,0)
            name.grab_set()
            name.focus_set()
            name.overrideredirect(True)

        def start_classic_Minesweeper(self):
            self.name_win()
            self.create_button()
            MineSweeper.window.title('Без флага')  
            x = (MineSweeper.window.winfo_screenwidth() - MineSweeper.window.winfo_reqwidth()) / 2.8 #По середине экрана
            y = (MineSweeper.window.winfo_screenheight() - MineSweeper.window.winfo_reqheight()) / 5
            MineSweeper.window.wm_geometry("+%d+%d" % (x, y))
            MineSweeper.window.geometry('600x600')
            MineSweeper.window.focus_set()  
            photo = tk.PhotoImage(file = 'D:\game\Mines.png')
            MineSweeper.window.iconphoto(False, photo)
            MineSweeper.window.deiconify()
            MineSweeper.window.resizable(0,0) #Запрет Масштабирование 

        def create_consol_button(self):
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    if btn.is_mine:
                        print('*', end=' ')
                    else:
                        print(btn.count_bomb, end=' ')
                print()

        def insert_mines(self, number: int):
            index_mines = self.get_mines_places(number)
            print(index_mines)
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    if btn.number in index_mines:
                        btn.is_mine = True

        def count_mines_in_buttons(self):
            for i in range(1,MineSweeper.ROW+1):
                for j in range(1,MineSweeper.COLUMS+1):
                    btn=self.buttons[i][j]
                    count_bomb = 0
                    if not btn.is_mine:
                        for row_dx in [1, 0, -1]:
                            for col_dx in [1, 0, -1]:
                                neigbour = self.buttons[i+row_dx][j+col_dx]
                                if neigbour.is_mine:
                                    count_bomb +=1
                    btn.count_bomb = count_bomb

        @staticmethod
        def get_mines_places(exclude_number:int):
            indexes=list(range(1, MineSweeper.COLUMS * MineSweeper.ROW + 1))
            print(f'Исключить кнопку {exclude_number}')
            indexes.remove(exclude_number)
            shuffle(indexes)
            return indexes[:MineSweeper.MINES]
    
    game=MineSweeper()
    game.start_classic_Minesweeper()

i=main_menu()