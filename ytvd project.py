from tkinter import * # * means everything from tkinter
from pytube import YouTube  #means import youtube from pytube
window = Tk()  #for making window
window.geometry("700x400")   #window size
window.configure(bg="pink")   #window backgrounk colour
#button function
def download():
    link_fetch = YouTube(str(e.get()))
    video_download = link_fetch.streams.first()
    video_download.download("C://Users//sherafzal//Desktop")
    Label(window,text="Video Downloaded",font="impack 15 bold",bg="pink",fg="green").place(x=290,y=300)
#heading for window
Label(window,text="YouTube Video Downloader",font="chiller 35 bold",bg="black",fg="yellow").pack(fill="x")
Label(window,text="Paste Link Here :",font="impack 15 bold",bg="pink",fg="black").place(x=40,y=130)
#entry box
e=Entry(window,width=60,bd=7,font="impack 10 bold",justify="left")
e.place(x=220,y=130)
#button for download
Button(window,text="Download",font="impack 20 bold",bg="blue",fg="white",command=download).place(x=300,y=200)

mainloop()

