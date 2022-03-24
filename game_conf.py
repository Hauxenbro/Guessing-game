import random, time
class Game_interaction:

    def starting_dialogue(self):
        self.dialogue_lbl['text'] = f'\tПривет, {self.nickname}!\nТвоя задача в этой игре - угадать число 1-100,\n' \
                                    f'используя подсказки, которые тебе даёт игра.\n Для более полной информации' \
                                    f' о подсказках\n используй кнопку " HELP TABLE "\n в верхнем правом углу окна.\n' \
                                    f'УДАЧИ!'
        self.update()
        self.introduced = True
        time.sleep(1)
        self.activate_game_btt_ui()

    def timer_count(self):
        for i in range(5,0,-1):
            self.timer_cnt_lbl['text'] = i
            self.update()
            time.sleep(1)
            if i == 1:
                self.timer_cnt_lbl['text'] = 'Число?'
                self.timer_cnt_lbl.place(relx = 0.35, rely = 0.4)
                self.update()

    def random_val(self):
        self.random_value = random.randint(1,100)

    def win(self):
        for i in range(11):
            if i % 2 == 0:
                self.left_lbl['bg'] = 'green'
                self.right_lbl['bg'] = 'green'
                self.update()
            else:
                self.left_lbl['bg'] = 'white'
                self.right_lbl['bg'] = 'white'
                self.update()
            time.sleep(0.18)


    def get_guess_number(self):
        try:
            self.__guess_numb = int(self.guess_ent.get())
            return True
        except Exception:
            self.disable_btt_guess()
            self.send_warning_numb()
            time.sleep(0.8)
            self.enable_btt_guess()
            return False

    def signal_info(self):
        self.left_lbl['bg'] = self.colour
        self.right_lbl['bg'] = self.colour
        if self.__guess_numb > self.random_value:
            self.__bigger = True
        else:
            self.__bigger = False
        if self.__bigger:
            self.__diff = self.__guess_numb - self.random_value
            if self.__diff >= 20:
                self.left_lbl['bg'] = 'blue'
            elif self.__diff >= 10 and self.__diff < 20:
                self.left_lbl['bg'] = 'yellow'
            else:
                self.left_lbl['bg'] = 'red'
        else:
            self.__diff = self.random_value - self.__guess_numb
            if self.__diff >= 20:
                self.right_lbl['bg'] = 'blue'
            elif self.__diff >= 10 and self.__diff < 20:
                self.right_lbl['bg'] = 'yellow'
            else:
                self.right_lbl['bg'] = 'red'
        self.update()

    def check_guess(self):
        if self.get_guess_number():
            if self.__guess_numb == self.random_value:
                self.win()
                self.set_winner_ui()
            else:
                self.signal_info()
                self.clear_entry_guess()
                self.guess_ent.focus()