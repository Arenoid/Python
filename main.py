import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def createQR():
    data = text_entry.get()
    if data:
        
        image = qrcode.make(data)
        image = image.resize((200, 200))
        tk_image = ImageTk.PhotoImage(image)
        
        qr_label.config(image=tk_image)
        qr_label.image = tk_image
        
        messagebox.showinfo("Success", "QR Code generated successfully!")
    else:
        messagebox.showwarning("Input Required", "Please enter some text to generate a QR code.")

def saveQR():
    if qr_label.image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            qr_label.image._PhotoImage__photo.write(file_path)
            messagebox.showinfo("Success", f"QR Code saved at {file_path}")
    else:
        messagebox.showwarning("No QR Code", "Please create a QR code before saving.")

def exitQR():
    root.quit()


root = tk.Tk()
root.title("QR Code Generator")
window_width, window_height = 300, 380
root.geometry(f"{window_width}x{window_height}")
root.config(bg="white")
root.resizable(False, False)


frame1_width, frame1_height = 280, 250
frame2_width, frame2_height = 280, 100

frame1_x = (window_width - frame1_width) // 2
frame1_y = (window_height - frame1_height - frame2_height) // 3
frame2_x = (window_width - frame2_width) // 2
frame2_y = frame1_y + frame1_height + 10

frame1 = tk.Frame(root, bd=2, relief=tk.SUNKEN, bg="white")
frame1.place(x=frame1_x, y=frame1_y, width=frame1_width, height=frame1_height)

qr_label = tk.Label(frame1, text="Your QR Code will appear here", bg="white", fg="gray", font=("Sans", 12))
qr_label.place(relx=0.5, rely=0.5, anchor="center")

frame2 = tk.Frame(root, bd=2, relief=tk.RAISED, bg="lightgray")
frame2.place(x=frame2_x, y=frame2_y, width=frame2_width, height=frame2_height)

text_entry = tk.Entry(frame2, width=26, font=("Sans", 10), justify=tk.CENTER)
text_entry.place(relx=0.5, y=10, anchor="n")

style = ttk.Style()
style.configure("TButton", font=("Sans", 9), padding=5)

btn_create = ttk.Button(frame2, text="Create", style="TButton", command=createQR)
btn_create.place(relx=0.2, rely=0.7, anchor="center")

btn_save = ttk.Button(frame2, text="Save", style="TButton", command=saveQR)
btn_save.place(relx=0.5, rely=0.7, anchor="center")

btn_exit = ttk.Button(frame2, text="Exit", style="TButton", command=exitQR)
btn_exit.place(relx=0.8, rely=0.7, anchor="center")

root.mainloop()
