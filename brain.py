import tkinter as tk

def main(self,tk):
    global intt, text
    """Configuracion De La Aplicación"""
    self.title("Conversor")
    self.geometry("250x120")
    self.resizable(False,False)
    """
    Elementos De La Aplicacion
    """
    tk.Label(self,text="Ingresa La Temperatura").pack()
    intt = tk.Text(self,width=10,height=1)
    intt.pack()
    text = tk.Label(self)
    text.place(x=0, y=90)
    tk.Button(self,text="Celsius A Fahrenheit",command=celsius_fahrenheit).place(x=5, y=50)
    tk.Button(self,text="Fahrenheit A Celsius",command=fahrenheit_celsius).place(x=127, y=50)
    tk.Button(self,text="Salir",command=self.destroy).place(x=215,y=90)
    self.mainloop()

def celsius_fahrenheit():
    """
    obtiene el valor del elemento intt 
    """
    temp = intt.get(1.0, "end-1c")
 
    return text.configure(text=f"{(int(temp)*9/5+32)} Grados Fahrenheit")

def fahrenheit_celsius():
    temp = intt.get(1.0, "end-1c")
    return text.configure(text=f"{round((int(temp)-32)*5/9)} Grados Celsius")

if __name__ == "__main__":
    main(tk.Tk(),tk)
