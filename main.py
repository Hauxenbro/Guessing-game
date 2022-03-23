import tkinter as tk
from tkinter import ttk
import functionals

class App(tk.Tk, functionals.Functional_conf):
    def __init__(self):
        tk.Tk.__init__(self)
        self.resizable(False, False)
        self.geometry('300x300')
        self.overrideredirect(True)
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
        start_btt = tk.Button(self, text = 'START', width = 15, command = self.enter_game)
        start_btt.place(relx = 0.35 , rely = 0.5)
        self.change_theme_btt = tk.Button(self, text = 'LIGHT THEME', width = 15, command = self.set_light_bg)
        self.change_theme_btt.place(relx = 0.35, rely = 0.6)
        options_btt = tk.Button(self, text = 'OPTIONS', width = 15, command = self.set_options_menu)
        options_btt.place(relx = 0.35, rely = 0.7)
        exit_btt = tk.Button(self, text = 'EXIT', width = 15, command = self.exit_app)
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
        if not self.introduced:
            self.starting_dialogue_ui()

    def starting_dialogue_ui(self):
        self.dialogue_fr = ttk.LabelFrame(self, text = 'GUESS')
        self.dialogue_fr.place(relx = 0.02, rely = 0.25)
        self.dialogue_lbl = tk.Label(self.dialogue_fr, text = '', width = 40, height = 8)
        self.dialogue_lbl.pack(fill = tk.BOTH)
        self.update()

    def activate_game_btt_ui(self):
        self.go_btt = tk.Button(self.dialogue_fr, text = 'ПОЕХАЛИ!', width = 15)
        self.go_btt.pack()
        self.update()


if __name__ == '__main__':
    root = App()
    root.mainloop()