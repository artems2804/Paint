from tkinter import *
from tkinter import ttk
from PIL import ImageGrab
root = Tk()
root.title("Paint")
root.geometry("800x800")
root.resizable(False, False)
root.option_add("*tearOff", FALSE)
menu = Menu()
file_Menu = Menu()
settings_Menu = Menu()
canvas = Canvas(root, width=800, height=600,bg='white')
canvas.pack()
color = ["красный", "синий", "зелёный", "жёлтый", "чёрный","ластик"]
size = [10, 20, 30, 40]
choice_draw = ["пиксели","круги"]
# логика
def paint(event):
    selected_color = combobox.get()
    selected_size = combobox2.get()
    selected_choice_draw = combobox3.get()
    if selected_choice_draw == "круги":
        if selected_color == "красный":
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="red",outline="red")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="red",outline="red")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="red",outline="red")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="red",outline="red")
        elif selected_color == "синий":
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="blue",outline="blue")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="blue",outline="blue")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="blue",outline="blue")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="blue",outline="blue")
        elif selected_color == "зелёный":
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="green",outline="green")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="green",outline="green")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="green",outline="green")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="green",outline="green")
        elif selected_color == "жёлтый":
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="yellow",outline="yellow")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="yellow",outline="yellow")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="yellow",outline="yellow")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="yellow",outline="yellow")
        elif selected_color == "ластик":
            canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="white",outline="white")
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="white",outline="white")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="white",outline="white")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="white",outline="white")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="white",outline="white")
        else:
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="black",outline="black")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="black",outline="black")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="black",outline="black")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="black",outline="black")
    elif selected_choice_draw == "пиксели":
        if selected_color == "красный":
            if selected_size == "20":
                canvas.create_rectangle(event.x, event.y, event.x + 20, event.y + 20, fill="red",outline="red")
            elif selected_size == "30":
                canvas.create_rectangle(event.x, event.y, event.x + 30, event.y + 30, fill="red",outline="red")
            elif selected_size == "40":
                canvas.create_rectangle(event.x, event.y, event.x + 40, event.y + 40, fill="red",outline="red")
            else:
                canvas.create_rectangle(event.x, event.y, event.x + 10, event.y + 10, fill="red",outline="red")
        elif selected_color == "синий":
            if selected_size == "20":
                canvas.create_rectangle(event.x, event.y, event.x + 20, event.y + 20, fill="blue",outline="blue")
            elif selected_size == "30":
                canvas.create_rectangle(event.x, event.y, event.x + 30, event.y + 30, fill="blue",outline="blue")
            elif selected_size == "40":
                canvas.create_rectangle(event.x, event.y, event.x + 40, event.y + 40, fill="blue",outline="blue")
            else:
                canvas.create_rectangle(event.x, event.y, event.x + 10, event.y + 10, fill="blue",outline="blue")
        elif selected_color == "зелёный":
            if selected_size == "20":
                canvas.create_rectangle(event.x, event.y, event.x + 20, event.y + 20, fill="green",outline="green")
            elif selected_size == "30":
                canvas.create_rectangle(event.x, event.y, event.x + 30, event.y + 30, fill="green",outline="green")
            elif selected_size == "40":
                canvas.create_rectangle(event.x, event.y, event.x + 40, event.y + 40, fill="green",outline="green")
            else:
                canvas.create_rectangle(event.x, event.y, event.x + 10, event.y + 10, fill="green",outline="green")
        elif selected_color == "жёлтый":
            if selected_size == "20":
                canvas.create_rectangle(event.x, event.y, event.x + 20, event.y + 20, fill="yellow",outline="yellow")
            elif selected_size == "30":
                canvas.create_rectangle(event.x, event.y, event.x + 30, event.y + 30, fill="yellow",outline="yellow")
            elif selected_size == "40":
                canvas.create_rectangle(event.x, event.y, event.x + 40, event.y + 40, fill="yellow",outline="yellow")
            else:
                canvas.create_rectangle(event.x, event.y, event.x + 10, event.y + 10, fill="yellow",outline="yellow")
        elif selected_color == "ластик":
            canvas.create_rectangle(event.x, event.y, event.x + 10, event.y + 10, fill="white",outline="white")
            if selected_size == "20":
                canvas.create_rectangle(event.x, event.y, event.x + 20, event.y + 20, fill="white",outline="white")
            elif selected_size == "30":
                canvas.create_rectangle(event.x, event.y, event.x + 30, event.y + 30, fill="white",outline="white")
            elif selected_size == "40":
                canvas.create_rectangle(event.x, event.y, event.x + 40, event.y + 40, fill="white",outline="white")
            else:
                canvas.create_rectangle(event.x, event.y, event.x + 10, event.y + 10, fill="white",outline="white")
        else:
            if selected_size == "20":
                canvas.create_rectangle(event.x, event.y, event.x + 20, event.y + 20, fill="black",outline="black")
            elif selected_size == "30":
                canvas.create_rectangle(event.x, event.y, event.x + 30, event.y + 30, fill="black",outline="black")
            elif selected_size == "40":
                canvas.create_rectangle(event.x, event.y, event.x + 40, event.y + 40, fill="black",outline="black")
            else:
                canvas.create_rectangle(event.x, event.y, event.x + 10, event.y + 10, fill="black",outline="black")
    else:
        if selected_color == "красный":
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="red",outline="red")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="red",outline="red")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="red",outline="red")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="red",outline="red")
        elif selected_color == "синий":
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="blue",outline="blue")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="blue",outline="blue")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="blue",outline="blue")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="blue",outline="blue")
        elif selected_color == "зелёный":
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="green",outline="green")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="green",outline="green")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="green",outline="green")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="green",outline="green")
        elif selected_color == "жёлтый":
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="yellow",outline="yellow")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="yellow",outline="yellow")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="yellow",outline="yellow")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="yellow",outline="yellow")
        elif selected_color == "ластик":
            canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="white",outline="white")
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="white",outline="white")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="white",outline="white")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="white",outline="white")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="white",outline="white")
        else:
            if selected_size == "20":
                canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="black",outline="black")
            elif selected_size == "30":
                canvas.create_oval(event.x, event.y, event.x + 30, event.y + 30, fill="black",outline="black")
            elif selected_size == "40":
                canvas.create_oval(event.x, event.y, event.x + 40, event.y + 40, fill="black",outline="black")
            else:
                canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="black",outline="black")
def save():
    x1 = canvas.winfo_rootx()
    y1 = canvas.winfo_rooty()
    x2 = x1 + canvas.winfo_width()
    y2 = y1 + canvas.winfo_height()
    
    # Захватываем изображение холста
    img = ImageGrab.grab((x1, y1, x2, y2))
    
    # Сохраняем изображение в файл
    img.save("my_canvas_image.png")
def clear_window():
    canvas.delete('all')
# Используем событие "<B1-Motion>" — движение мыши с нажатой левой кнопкой
root.bind("<B1-Motion>", paint)
Label(root,text="цвет:",font="Arial 14").place(x=0,y=610)
Label(root,text="размер:",font="Arial 14").place(x=0,y=650)
Label(root,text="Выбор рисовки:",font="Arial 14").place(x=0,y=700)
Button(root,text="Очистить!",command=clear_window).place(x=0,y=774)

#цвет
combobox = ttk.Combobox(values=color, state="readonly")
combobox.place(x=50,y=618)
#размер пера
combobox2 = ttk.Combobox(values=size, state="readonly")
combobox2.place(x=80,y=655)
# выбор рисовки
combobox3 = ttk.Combobox(values=choice_draw, state="readonly")
combobox3.place(x=150,y=705)
# сохранить
Button(root,text="Сохранить",command=save).place(x=100,y=774)
menu.add_cascade(label="File",menu=file_Menu)
file_Menu.add_cascade(label="Settings",menu=settings_Menu)
settings_Menu.add_command(label="Save",command=save)
root.config(menu=menu)
root.mainloop()
