import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import functionals

class App(tk.Tk, functionals.Functional_conf):
    def __init__(self):
        tk.Tk.__init__(self)
        self.resizable(False, False)
        self.geometry('300x300')
        self.overrideredirect(True)
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.background = 'black'
        self.colour = '#414A4C'
        self.fcolour = 'white'
        self.introduced = False
        self.start_ui()

    def start_ui(self):
        self.make_bg()
        self.set_ui_starting()

    def make_bg(self):
        self.back_bg = tk.Label(self, bg= self.colour, width=400, height=400)
        self.back_bg.pack(fill=tk.BOTH)
        self.game_intro_lbl = tk.Label(self, text='GUESSING GAME', font='Times 20', fg=self.fcolour, bg=self.colour)
        self.game_intro_lbl.place(relx=0.15, rely=0.1)
        self.tony_lbl = tk.Label(self, text = 'Made by Tony Kuzmenko', fg = self.fcolour, bg = self.colour)
        self.tony_lbl.place(relx = 0.32, rely = 0.9)

    def set_ui_starting(self):
        self.nick_lbl = tk.Label(self, text = 'NICKNAME:', width = 15, fg = self.fcolour, bg = self.colour)
        self.nick_lbl.place(relx = 0.35, rely = 0.28)
        self.save_children()
        self.nick_ent = tk.Entry(self, width = 15)
        self.nick_ent.place(relx = 0.37, rely = 0.35)
        self.nick_ent.focus()
        start_btt = tk.Button(self, text = 'START', width = 15, command = self.enter_game_btt)
        start_btt.place(relx = 0.35 , rely = 0.5)
        self.change_theme_btt = tk.Button(self, text = 'LIGHT THEME', width = 15, command = self.set_light_bg)
        self.change_theme_btt.place(relx = 0.35, rely = 0.6)
        options_btt = tk.Button(self, text = 'OPTIONS', width = 15, command = self.set_options_menu)
        options_btt.place(relx = 0.35, rely = 0.7)
        exit_btt = tk.Button(self, text = 'EXIT', width = 15, command = self.ask_quit)
        exit_btt.place(relx = 0.35, rely = 0.8)

        self.bind('<Return>', self.enter_game)

    def set_options_menu(self):
        self.clear_win()
        self.make_bg()
        self.save_children()
        self.move_btt = tk.Button(self, text = 'MOVE WINDOW', width = 15, command = self.movement_win)
        self.move_btt.place(relx = 0.35, rely = 0.5)
        self.back_btt = tk.Button(self, text = 'BACK', width = 10, command = self.back_to_menu)
        self.back_btt.place(relx = 0.01, rely = 0.92)

    def set_game_ui(self):
        self.clear_win()
        self.make_bg()
        self.help_btt = tk.Button(text = 'HELP TABLE', width = 10, command = self.help_table_ui)
        self.help_btt.place(relx = 0.72, rely = 0.01)
        self.back_btt = tk.Button(self, text = 'BACK', width = 10, command = self.back_to_menu)
        self.back_btt.place(relx = 0.01, rely = 0.01)
        if not self.introduced:
            self.starting_dialogue_ui()

    def starting_dialogue_ui(self):
        self.dialogue_fr = ttk.LabelFrame(self, text = 'GUESS')
        self.dialogue_fr.place(relx = 0.02, rely = 0.25)
        self.dialogue_lbl = tk.Label(self.dialogue_fr, text = '', width = 40, height = 8)
        self.dialogue_lbl.pack(fill = tk.BOTH)
        self.update()

    def activate_game_btt_ui(self):
        self.go_btt = tk.Button(self.dialogue_fr, text = 'ПОЕХАЛИ!', width = 15, command = self.activate_game)
        self.go_btt.pack()
        self.update()

    def help_table_ui(self):
        self.clear_win()
        self.make_bg()
        self.help_lbl = tk.Label(self, text = 'Ваша задача - угадать число, используя цветовые\nподсказки.\n'
                                'Если подсказка появилась справа, значит Ваше число\nменьше загаданного.\n'
                                'Если подсказка появилась слева, значит Ваше число\nбольше загаданного.\n'
                                'В игре присутствует 3 типа цветовых подсказок\nв зависимости от цвета:\n'
                                'Синяя - разница между вашим числом и загаданным\nбольше 20.\n'
                                'Жёлтая - разница между вашим числом и загаданным\nбольше 10 и меньше 20\n'
                                'Красная - разница между вашим числом и загаданным\n меньше 10.\n'
                                'УДАЧИ!',bg = self.colour, fg = self.fcolour, font = 'Times 9', justify = 'left')
        self.help_lbl.place(relx = 0, rely = 0.2)
        self.back_to_game_btt = tk.Button(self, text = 'BACK', width = 10, command = self.activate_game)
        self.back_to_game_btt.place(relx = 0.01, rely = 0.01)
        self.update()

    def start_timer(self):
        self.start_guess_btt.destroy()
        self.timer_cnt_lbl = tk.Label(self, font = 'Times 25', fg = self.fcolour, bg = self.colour)
        self.timer_cnt_lbl.place(relx = 0.5, rely = 0.4)
        self.guess_ent = tk.Entry(self, width=15)
        self.guess_ent.place(relx=0.35, rely=0.6)
        self.guess_ent.focus()
        self.update()
        self.timer_count()
        self.random_val()
        self.guess_btt = tk.Button(text = 'УГАДАТЬ', width = 15, command = self.check_guess)
        self.guess_btt.place(relx = 0.3, rely = 0.7)
        self.update()

    def activate_game(self):
        self.clear_win()
        self.make_bg()
        self.set_game_ui()
        self.start_guess_btt = tk.Button(self, text = 'START GUESS', width = 15, command = self.start_timer)
        self.start_guess_btt.place(relx = 0.35, rely = 0.45)
        self.left_lbl = tk.Label(self, width = 3, height = 10, bg = self.colour)
        self.left_lbl.place(relx = 0.01, rely = 0.5)
        self.right_lbl = tk.Label(self, width = 5, height = 10, bg = self.colour)
        self.right_lbl.place(relx = 0.9 , rely = 0.5)
        self.update()


    def set_winner_ui(self):
        self.clear_win()
        self.make_bg()
        self.info_lbl = tk.Label(self, text = 'WINNER!', bg = self.colour, fg = self.fcolour, font = 'Times 20')
        self.info_lbl.place(relx = 0.3, rely = 0.3)
        self.start_game_btt = tk.Button(self, text = 'RESTART', width = 15, command = self.activate_game)
        self.start_game_btt.place(relx = 0.3, rely = 0.5)
        self.exit_btt = tk.Button(self, text = 'EXIT', width = 15, command = self.ask_quit)
        self.exit_btt.place(relx = 0.3, rely = 0.6)
        self.update()

    def clear_entry_guess(self):
        self.guess_ent.delete(0, tk.END)
        self.update()

    def send_warning_nick(self):
        self.nick_warn = messagebox.showwarning('WARNING', 'Длина ника должна быть меньше 12 символов!')

    def ask_quit(self):
        quit_ask = messagebox.askyesno('QUIT', 'Вы точно хотите выйти?')
        if quit_ask == True:
            self.exit_app()

    def send_warning_numb(self):
        self.numb_warn = messagebox.showwarning('WARNING', 'Вы должны ввести число')

    def disable_btt_guess(self):
        self.guess_btt['state'] = tk.DISABLED

    def enable_btt_guess(self):
        self.guess_btt['state'] = tk.NORMAL

if __name__ == '__main__':
    root = App()
    root.mainloop()