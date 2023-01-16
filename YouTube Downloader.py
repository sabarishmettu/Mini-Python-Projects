from tkinter import *
from pytube import YouTube
from tkinter import messagebox,filedialog

def download_video():
    url = url_entry.get()
    folder_path = folder_path_label['text']
    if url:
        try:
            yt = YouTube(url)
            video = yt.streams.first()
            if folder_path:
                video.download(output_path=folder_path)
            else:
                video.download()
            messagebox.showinfo("Download Complete", "The video has been downloaded!")
        except Exception as e:
            messagebox.showerror("Error", "An error occurred while downloading the video: "+str(e))
    else:
        messagebox.showerror("Error", "Please enter a valid URL.")

def select_folder():
    folder_path = filedialog.askdirectory()
    folder_path_label.config(text = folder_path)

# Create the main window
root = Tk()
root.title("YouTube Downloader")

# Create a label for the URL entry field
url_label = Label(root, text="Enter the YouTube video URL:")
url_label.pack()

# Create the URL entry field
url_entry = Entry(root)
url_entry.pack()

# Create a button to select the folder
folder_select_button = Button(root, text="Select Folder", command=select_folder)
folder_select_button.pack()

# Create label to show the selected folder path
folder_path_label = Label(root, text="")
folder_path_label.pack()

# Create a download button
download_button = Button(root, text="Download", command=download_video)
download_button.pack()

root.mainloop()
