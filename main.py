import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox

import pytube.exceptions
from pytube import YouTube


# This function downloads the video with designated resolution
def download_video():
    url_address = entry_url_address.get()
    file_address = entry_file_address.get()
    resolution = option.get()
    yt = YouTube(url_address, on_progress_callback=PercentCalculator, on_complete_callback=download_complete)
    yt.streams.get_by_resolution(resolution=resolution).download(output_path=file_address)


# This function checks if the URL exists or not
def video_check():
    try:
        download_video()
    except pytube.exceptions.VideoUnavailable:
        tk.messagebox.showinfo('Video Not Available!', 'Video Not Available. Check the URL Path Again.')


def PercentCalculator(stream, chunk, remaining):
    file_size = stream.filesize
    percent = ((file_size - remaining) / file_size)*100
    progress_bar['value'] = percent
    label_percent.configure(text='{p}%'.format(p=round(percent,1)))
    label_percent.update()
    window.update_idletasks()
    # print("{p}% downloaded ".format(p=round(percent,1)))


def download_complete(stream, filepath):
    tk.messagebox.showinfo('Download Complete!','Download Successfully Completed!')

# Create the GUI
window = tk.Tk()
window.title('Sir Sina YouTube Downloader')
window.geometry("640x480")
pic = tk.PhotoImage(file="/Volumes/Personal/Python_Training/pythonProject/06_Youtube_Downloader/logo.gif")
logo = tk.Label(window, image = pic).place(x = 10, y = 10)
label_url_address = tk.Label(window, text = "Enter the YouTube URL:")

label_url_address.place(x = 10, y = 300)
entry_url_address = tk.Entry(window)
entry_url_address.place(x = 250, y = 300)
# entry_url_address.insert(0,'https://www.youtube.com/watch?v=CfWevlsPRMo')
label_file_address = tk.Label(window, text = "Enter the path to save the video:")
label_file_address.place(x = 10, y = 330)
entry_file_address = tk.Entry(window)
entry_file_address.place(x = 250, y = 330)
entry_file_address.insert(0, "/Users/sina/Downloads")

label_resolution = tk.Label(window, text = "Enter the video download resolution:")
label_resolution.place(x = 10, y = 360)
option = tk.StringVar(window)
option.set("360p")
options = ["360p", "720p"]
entry_resolution = tk.OptionMenu(window, option, *options).place(x = 250, y = 360)

download_cmd = tk.Button(text = 'Download!', height = 4, width = 10, fg = 'red', command = video_check)
download_cmd.place(x = 500, y = 320)

label_progress = tk.Label(window, text = 'Progress: ')
label_progress.place(x = 10, y = 400)
progress_bar = ttk.Progressbar(window, length = 100, mode = 'determinate')
progress_bar.place(x=250, y=400)
label_percent = tk.Label(window, text = '')
label_percent.place(x=370, y=400)
window.mainloop()

