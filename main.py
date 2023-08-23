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

