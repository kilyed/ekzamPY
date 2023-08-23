from tkinter import *
from  random import choice
import time

frm = []; btn = []                              # Списки с фреймами и кнопками
xBtn = 16; yBtn = 16                            # Размеры поля (количество кнопок)
playTime = 0                                    # Время игры
mines = xBtn * yBtn * 10 // 64                  # Количество мин
imgMark = '\u2661'; imgMine = '\u2665'          # Символ маркера и мины
playArea = []; nMoves = 0; mrk=0                # Игровое поле, счётчик ходов и маркеров
tk = Tk()
tk.title('Achtung, Minen!')
tk.geometry(str(44*xBtn)+'x'+str(44*yBtn+10))

def play(n):                                    # n - номер нажатой кнопки
    global xBtn, yBtn, mines, nMoves, mrk, playTime
    if len(playArea) < xBtn*yBtn:               # Если поле ещё не создано
        return()
    nMoves += 1
    if nMoves == 1:                             # Если это первый ход игрока,
        playTime = time.time()
        i = 0
        while i<mines:                          # поставим мины,
            j = choice(range(0, xBtn*yBtn))
            if j != n and playArea[j] != -1:
                playArea[j] = -1
                i += 1
        for i in range(0, xBtn*yBtn):           # подсчитаем количесво мин вокруг каждой клетки
            if playArea[i] != -1:
                k = 0
                if i not in range(0, xBtn*yBtn, xBtn):
                    if playArea[i-1] == -1: k += 1              # слева
                    if i > xBtn-1:
                        if playArea[i-xBtn-1] == -1: k += 1     # слева сверху
                    if i < xBtn*yBtn-xBtn:
                        if playArea[i+xBtn-1] == -1: k += 1     # слева снизу
                if i not in range(-1, xBtn*yBtn, xBtn):
                    if playArea[i+1] == -1: k += 1              # справа
                    if i > xBtn-1:
                        if playArea[i-xBtn+1] == -1: k += 1     # справа сверху
                    if i < xBtn*yBtn-xBtn:
                        if playArea[i+xBtn+1] == -1: k += 1     # справа снизу
                if i > xBtn-1:
                    if playArea[i-xBtn] == -1: k += 1           # сверху
                if i < xBtn*yBtn-xBtn:
                    if playArea[i+xBtn] == -1: k += 1           # снизу
                playArea[i] = k
    if btn[n].cget('text') == imgMark:                          # Если поле было промаркировано
        mrk -= 1
        tk.title('Achtung, '+str(mines-mrk)+' Minen!')
    btn[n].config(text=playArea[n], state=DISABLED, bg='white') # Отображаем игровую ситуацию
    if playArea[n] == 0:                                        # Пустое поле без соседей
        btn[n].config(text=' ', bg='#ccb')
    elif playArea[n] == -1:                                     # Ой мина!
        btn[n].config(text=imgMine)
        if nMoves <= (xBtn*yBtn - mines) or mines >= mrk:       # Если игрок ещё не выиграл, то проиграл
            nMoves = 32000                                      # Если проиграл, то уже не выиграет
            chainReaction(0)                                    # Цепная реакция
            tk.title('Your game is over.')
    if nMoves == (xBtn*yBtn - mines) and mines == mrk:          # Если все клетки открыты и мины помечены
        tk.title('You win! '+str(int(time.time() - playTime))+' сек')
        winner(0)

def chainReaction(j):                               # Цепная реакция
    if j <= len(playArea):                          # Если не запустили новую игру
        for i in range(j, xBtn*yBtn):
            if playArea[i] == -1 and btn[i].cget('text') == ' ':
                btn[i].config(text=imgMine)
                btn[i].flash()
                tk.bell()
                tk.after(50, chainReaction, i + 1)
                break

def winner(j):                                      # Победа
    if j <= len(playArea):                          # Если не запустили новую игру
        for i in range(j, xBtn*yBtn):
            if playArea[i] == 0:
                btn[i].config(state=NORMAL, text='☺')
                btn[i].flash()
                tk.bell()
                btn[i].config(text=' ', state=DISABLED)
                tk.after(50, winner, i + 1)
                break

def marker(n):                                      # помечаем то, где возможно скрывается мина.
    global mrk, mines, playTime
    if (btn[n].cget('state')) != 'disabled':
        if btn[n].cget('text') == imgMark:
            btn[n].config(text=' ')
            mrk -= 1
        else:
            btn[n].config(text=imgMark, fg='blue')
            mrk += 1
        tk.title('Achtung, '+str(mines-mrk)+' Minen!')
    if nMoves == (xBtn*yBtn - mines) and mines == mrk:          # Если все клетки открыты и мины помечены
        tk.title('You win! '+str(int(time.time() - playTime))+' сек')
        winner(0)


