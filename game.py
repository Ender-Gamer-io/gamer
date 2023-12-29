import time
import keyboard
import tkinter
from tkinter import messagebox as mb
# Before using, customize the geometry for yourself. To avoid bugs, launch in a standard Python console (not IDE)
geometry = 210,50
root = tkinter.Tk()
root.withdraw()
keyboard.wait('esc')
tick = 0
player_animation = {'r':['3t%▲ ▲', '2t%(○-○)', '0t%\(___)', '1t%╘╘ ╘╘'], 'l':['1t%▲ ▲', '0t%(○-○)', '1t%(___)/', '1t%╛╛ ╛╛'],
                    'sl':['1t%▲ ▲', '0t%(---)', '1t%(___)/', '1t%╛╛ ╛╛'], 'sr':['3t%▲ ▲', '2t%(---)', '0t%\(___)', '1t%╘╘ ╘╘']}
texture ={'player': [['1t%▲ ▲', '0t%(○-○)', '1t%(___)/', '1t% ╘╘  ╘╘']], 'wall': '*', 'b': ' ', 'wall1': '|'}
enitys = {'player':[3, 25, 7, 4, 'en', 0], 'wall': [20, 20, 50, 25, 'w', 1], 'wall1': [100, 0, 5, 40, 'w', 1]}
play = True
ls = 'r'

def update(texture, enitys, ls, player_animation):
    global tick, geomety
    xg, yg = geometry
    if tick > 100:
        tick = 1
    else:
        tick += 1
    
    if 1 < tick < 5:
        texture['player'] = player_animation['s' + ls]
    else:
        texture['player'] = player_animation[ls]

    
    
    field = {}
    for enity in enitys.keys():
        x1, y1, w, h, textur, typ = enitys[enity]
        x1 = int(x1 // 1)
        y1 = int(y1 // 1)
        x2, y2 = x1 + w, y1 + h
        for y in range(y1, y2):
            field[y] = field.get(y, list())
            if textur == 'en':
                
                x, s = texture[enity][y - y1].split('t%')
                field[y].append([x1 + int(x), s])
            elif textur == 'w':
                field[y].append([x1, texture[enity] * (x2 - x1)])
    out = []
    for row in range(yg):
        if row in field.keys():
            o = texture['b'] * xg

            for i in field[row]:
                #print(i)
                x, l = i
                o = o[:x] + l + o[x + len(l):]
            out.append(o)
        else:
            out.append(texture['b'] * xg)
    print('\n' + '\n'.join(out), end="")

def walls_check(x, y, size, enitys):
    w, h = size
    x = int(x // 1)
    y = int(y // 1)
    f = 1
    for i in enitys.values():
        if i[-1] == 1:
            x1, y1, x2, y2 = (i[0],i[1],i[0] + i[2], i[1] + i[3])
            if (x1 < x < x2 and y1 < y < y2) or (x1 < x + w < x2 and y1 < y + h < y2) or (x1 < x + w < x2 and y1 < y < y2) or (x1 < x < x2 and y1 < y + h < y2)\
               or (x < x1 < x + w and y < y1 < y + h) or (x < x2 < x + w and y < y1 < y + h) or (x < x1 < x + w and y < y2 < y + h) or\
               (x < x2 < x + w and y < y2 < y + h):
                return False
    return True

while play:
    x, y = geometry
    sprint = 0

    if enitys.get('player') != None:
        if  keyboard.is_pressed('tab'):
            sprint = 1
        if keyboard.is_pressed('o'):
            del enitys['player']
            mb.showerror("Ошибка",
                     '''      ▲ ▲
    (○-○)
\(_____)
   [[    [[''')
        if keyboard.is_pressed('down'):
            if enitys['player'][1] < y - enitys['player'][3] and walls_check(enitys['player'][0], enitys['player'][1] + 1, enitys['player'][2:4], enitys):
                enitys['player'][1] += 0.5
        if keyboard.is_pressed('up'):
            if enitys['player'][1] > 0 and walls_check(enitys['player'][0], enitys['player'][1] - 1, enitys['player'][2:4], enitys):enitys['player'][1] -= 0.5

        if keyboard.is_pressed('right'):
            if enitys['player'][0] < x - enitys['player'][2] - 1 and walls_check(enitys['player'][0] + 1, enitys['player'][1], enitys['player'][2:4], enitys):
                if  sprint:
                    enitys['player'][0] += 1.5
                else:
                    enitys['player'][0] += 0.5
                ls = 'r'
        if keyboard.is_pressed('left'):
            if enitys['player'][0] > 0 and walls_check(enitys['player'][0] - 1, enitys['player'][1], enitys['player'][2:4], enitys):
                if  sprint:
                    enitys['player'][0] -= 1.5
                else:
                    enitys['player'][0] -= 0.5
                ls = 'l'
    time.sleep(0.02)
    update(texture, enitys, ls, player_animation)
