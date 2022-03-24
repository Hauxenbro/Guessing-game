import sys, game_conf
class Functional_conf(game_conf.Game_interaction):

    def save_children(self):
        self.__children_coloured = []
        for i in self.winfo_children():
            self.__children_coloured.append(i)

    def __change_colour(self):
        for i in self.__children_coloured:
            i['bg'], i['fg'] = self.colour, self.fcolour

    def set_dark_bg(self):
        self.background = 'black'
        self.colour = '#414A4C'
        self.fcolour = 'white'
        self.__change_colour()
        self.change_theme_btt['text'], self.change_theme_btt['command'] = 'LIGHT THEME', self.set_light_bg
        self.update()

    def set_light_bg(self):
        self.background = 'white'
        self.colour = '#FFFFF0'
        self.fcolour = 'black'
        self.__change_colour()
        self.change_theme_btt['text'], self.change_theme_btt['command'] = 'DARK THEME', self.set_dark_bg
        self.update()

    def clear_win(self):
        for i in self.winfo_children():
            i.destroy()
        self.update()

    def movement_win(self):
        if self.overrideredirect() == True:
            self.overrideredirect(False)
            self.move_btt['text'] = 'PIN'
        else:
            self.overrideredirect(True)
            self.move_btt['text'] = 'MOVE'


    def back_to_menu(self):
        self.clear_win()
        self.start_ui()
        self.update()

    def exit_app(self):
        self.destroy()
        sys.exit()

    def __save_nickname(self):
        if self.nick_ent.get() == '':
            self.nickname = 'UNKNOWN'
        else:
            if len(self.nick_ent.get()) <= 12:
                self.nickname = self.nick_ent.get()
            else:
                self.send_warning_nick()
                self.nickname = ''

    def enter_game_btt(self):
        self.enter_game('')

    def enter_game(self, event):
        self.unbind('<Return>')
        self.__save_nickname()
        if self.nickname != '':
            self.set_game_ui()
            if not self.introduced:
                self.starting_dialogue()
            else:
                self.activate_game()


