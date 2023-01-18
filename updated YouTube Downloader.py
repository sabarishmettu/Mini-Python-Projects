from tkinter import *
from pytube import YouTube
from tkinter import messagebox,filedialog

def download_video():
    url = url_entry.get()
    folder_path = folder_path_label['text']
    video_quality = quality_var.get()
    if url:
        try:
            yt = YouTube(url)
            if video_quality == '360p':
                video = yt.streams.filter(res='360p').first()
            elif video_quality == '480p':
                video = yt.streams.filter(res='480p').first()
            elif video_quality == '720p':
                video = yt.streams.filter(res='720p').first()
            elif video_quality == '1080p':
                video = yt.streams.filter(res='1080p').first()
            else:
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

# Create a label for the video quality
quality_label = Label(root, text="Select Video Quality")
quality_label.pack()

# Create a variable to store the selected video quality
quality_var = StringVar(value='360p')

# Create radio buttons for video quality
quality_360p = Radiobutton(root, text='360p', variable=quality_var, value='360p')
quality_360p.pack()
quality_480p = Radiobutton(root, text='480p', variable=quality_var, value='480p')
quality_480p.pack()
quality_720p = Radiobutton(root, text='720p', variable=quality_var, value='720p')
quality_720p.pack()
quality_1080p = Radiobutton(root, text='1080p', variable=quality_var, value='1080p')
quality_1080p.pack()

# Create a download button
download_button = Button(root, text="Download", command=download_video)
download_button.pack()

root.mainloop()
