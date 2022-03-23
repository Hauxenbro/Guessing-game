import random, time
class Game_interaction:
    def starting_dialogue(self):
        self.dialogue_lbl['text'] = f'\tПривет {self.nickname}!\nТвоя задача в этой игре - угадать число,\n' \
                                    f'используя подсказки, которые тебе даёт игра.\n Для более полной информации' \
                                    f' о подсказках\n используй кнопку " HELP TABLE "\n в верхнем правом углу окна.\n' \
                                    f'УДАЧИ!'
        self.update()
        self.introduced = True
        time.sleep(1)
        self.activate_game_btt_ui()