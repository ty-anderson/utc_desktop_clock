import tkinter as tk
import datetime

root = tk.Tk()
root.title("UTC Clock")
root.overrideredirect(True)
root.attributes('-topmost', True)
root.configure(bg='black')
root.attributes('-transparentcolor', 'black')

time_label = tk.Label(root, font=('Helvetica', 20), fg='black')
time_label.pack(pady=20)


def update_time():
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    time_label.config(text=f'{current_time}UTC')
    root.after(1000, update_time)  # Schedule the update_time function to be called after 1000 ms (1 second)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 80
x = screen_width - window_width
y = 0

root.geometry(f'{window_width}x{window_height}+{x}+{y}')
update_time()
root.mainloop()
