from tkinter import *
from tkinter import ttk
from PIL import ImageGrab
root = Tk()
root.title("Paint")
root.geometry("800x800")
root.resizable(False, False)
canvas = Canvas(root, width=800, height=600,bg='white')
canvas.pack()
color = ["красный", "синий", "зелёный", "жёлтый", "чёрный"]
size = [10, 20, 30, 40]
def paint(event):
    selected_color = combobox.get()
    selected_size = combobox2.get()
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
def clear():
    canvas.delete('all')
# Используем событие "<B1-Motion>" — движение мыши с нажатой левой кнопкой
root.bind("<B1-Motion>", paint)
Label(root,text="цвет: ",font="Arial 14").place(x=0,y=610)
Label(root,text="размер: ",font="Arial 14").place(x=0,y=650)
Button(root,text="Очистить!",command=clear).place(x=0,y=700)
#цвет
combobox = ttk.Combobox(values=color, state="readonly")
combobox.place(x=50,y=618)
#размер пера
combobox2 = ttk.Combobox(values=size, state="readonly")
combobox2.place(x=80,y=655)
# сохранить
Button(root,text="Сохранить",command=save).place(x=100,y=700)
root.mainloop()
