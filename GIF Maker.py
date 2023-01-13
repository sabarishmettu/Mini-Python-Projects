import tkinter as tk
from tkinter import filedialog
import imageio

def video_to_gif():
    video_path = filedialog.askopenfilename(title = "Select video file")
    gif_path = filedialog.asksaveasfilename(title = "Save GIF as", defaultextension=".gif")
    reader = imageio.get_reader(video_path)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(gif_path, fps=fps)
    for frames in reader:
        writer.append_data(frames)
    writer.close()
    print("GIF saved successfully!")

root = tk.Tk()
root.title("Video to GIF converter")

select_video_button = tk.Button(text="Select video", command=video_to_gif)
select_video_button.pack()

root.mainloop()
