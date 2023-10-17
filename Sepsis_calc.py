
import math
import tkinter as tk
from tkinter import messagebox

def get_p(sad, satur, hr, sex, age, infect):
    x = -4.21691232+(-0.24223624*sad)+(-1.35440457*satur)+(0.26936224*hr) \
        +(-0.05847406*sex)+(0.61413925*age)+(4.6932873*infect)
    return 1/(1+math.exp(-x))
# _ _ _ _ _
def get_scale(sad, satur, hr, age):
    sad = (sad - 134.01169591) / 26.43855815
    satur = (satur - 93.63909774) / 5.23388566
    hr = (hr - 96.49373434) / 20.60884471
    age = (age - 68.93400167) / 18.6211804
    return sad, satur, hr, age

window = tk.Tk()
#
window.resizable(width=False, height=False)
window.title('Оценка вероятности сепсиса')
#
window.geometry('330x400')
#
window['bg'] = '#C1C1C1'
#
task_to_prog = tk.Label(window, text='СКРИНИНГ СЕПСИСА',
                        font=('Arial', 18), fg='#BDFCC9', bg='#8E8E8E')
task_to_prog.place(x=30, y=25)

# - - - - -
age_but = tk.Entry(window)
age_but.place(x=160, y=105)
tk.Label(window, text='Возраст (лет)', ).place(x=30, y=105)
# - - - - -
sex_but = tk.Entry(window)
sex_but.place(x=160, y=135)
tk.Label(window, text='Пол (м/ж)', ).place(x=30, y=135)
# - - - - -
sad_but = tk.Entry(window)
sad_but.place(x=160, y=165)
tk.Label(window, text='САД (мм. рт. ст.)', ).place(x=30, y=165)
# - - - - -
satur_but = tk.Entry(window)
satur_but.place(x=160, y=195)
tk.Label(window, text='Сатурация (%)', ).place(x=30, y=195)
# - - - - -
hr_but = tk.Entry(window)
hr_but.place(x=160, y=225)
tk.Label(window, text='ЧСС (уд/мин)', ).place(x=30, y=225)
# - - - - -
infect_but = tk.Entry(window)
infect_but.place(x=160, y=255)
tk.Label(window, text='Инфекция (да/нет)', ).place(x=30, y=255)

#- - - - - -
tk.Label(window,text='________',
         fg='white', bg='white',
         width=10, height=1).place(x=210, y=325)
# _ _ _ _ _ _

def get_entry():
    a = [age_but.get(), sex_but.get(), sad_but.get(),
         satur_but.get(), hr_but.get(), infect_but.get()]

    try:
        float(a[0])
        age = float(a[0])
    except:
        messagebox.showinfo('Report', 'Проверьте правильность введения показателя "Возраст"')
        return
    #
    if a[1].lower() == 'м':
        sex = 1
    elif a[1].lower() == 'ж':
        sex = 0
    else:
        messagebox.showinfo('Report', 'Проверьте правильность введения показателя "Пол"')
        return
    # _ _ _ _ _ _ _
    try:
        float(a[2])
        sad = float(a[2])
    except:
        messagebox.showinfo('Report', 'Проверьте правильность введения показателя "САД"')
        return
    # - - - - - - -
    try:
        float(a[3])
        satur = float(a[3])
    except:
        messagebox.showinfo('Report', 'Проверьте правильность введения показателя "Сатурация"')
        return
    # - - - - - - -
    try:
        float(a[4])
        hr = float(a[4])
    except:
        messagebox.showinfo('Report', 'Проверьте правильность введения показателя "ЧСС"')
        return
    # - - - - - - -
    if a[5].lower() == 'да':
        infect = 1
    elif a[5].lower() == 'нет':
        infect = 0
    else:
        messagebox.showinfo('Report', 'Проверьте правильность введения показателя "Инфекция"')
        return
    # _ _ _ _ _ _ _ _ _ _ _ _
    sad, satur, hr, age = get_scale(sad, satur, hr, age)
    #
    tk.Label(window, text=f'{round(get_p(sad, satur, hr, sex, age, infect),6)}',
             font=('Arial', 9), fg='black', bg='white',
         width=10, height=1).place(x=210, y=325)

check = tk.Button(window, text='ПОСЧИТАТЬ ВЕРОЯТНОСТЬ',
                  command=get_entry).place(x=30, y=323)

window.mainloop()
