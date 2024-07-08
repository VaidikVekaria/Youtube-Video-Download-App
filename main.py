import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObj = YouTube(ytLink, on_progress_callback=on_progress)
        title.configure(text = ytObj.title, text_color = "white")
        video = ytObj.streams.get_highest_resolution()
        finishLabel.configure(text = "In Progress...", text_color = "lightgrey")
        try: 
            video.download()
            finishLabel.configure(text = "Downloaded!", text_color = "lightgreen")
        except Exception as error:
            finishLabel.configure(text = error)
        
    except Exception as error:
        
        finishLabel.configure(text = "Error: " + str(error), text_color = "red")
        
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    per_stat = bytes_downloaded / total_size * 100
    per = str(int(per_stat))
    stat.configure(text = per + "%")
    stat.update()

    # update progress_bar
    pStat = float(per)/100
    progress_bar.set(pStat)

# system Settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.title("Vaidik's YouTube Downloader")
app.geometry("960x540")  # width x height
app.resizable(False, False)  # prevent resizing

# adding UI
# Welcome message with larger fonts and styling
welcome = customtkinter.CTkLabel(app, text="Welcome to Vaidik's YouTube Downloader",
                                 font=("Roboto", 24, "bold") )
welcome.pack(pady=(70, 10))

# Title label with custom font size
title = customtkinter.CTkLabel(app, text="Insert a YouTube link",
                               font=("Lato", 16) )
title.pack(padx=10, pady=10)

# Link input with placeholder
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, placeholder_text="Paste your link here")
link.pack()

# Finished downloading label
finishLabel = customtkinter.CTkLabel(app, text="", font=("Open Sans", 12))
finishLabel.pack()

# Progress percentage label
stat = customtkinter.CTkLabel(app, text="0%", font=("Fira Sans", 12))
stat.pack()

# Progress bar
progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download button with cool design
download = customtkinter.CTkButton(app, text="Download", command=startDownload,
                                   fg_color=("white", "green"), hover_color="darkgreen",
                                   font=("Montserrat", 14, "bold"))
download.pack(padx=10, pady=20)

# Run app
app.mainloop()