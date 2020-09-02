from tkinter import *
from PIL import Image,ImageTk
def every_100(text):
    final_text=""
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="\n"
    return final_text








root=Tk()
root.title("Shivam News-India's most trusted channel")
root.geometry("1000x800")
texts=[]
photos=[]
for i in range(1):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(every_100(text))
    image=Image.open(f"shivam1.png")
    image=image.resize((250,200),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))
f0=Frame(root,width=800,height=70)
Label(f0,text="Shivam News",font="lucida 33 bold").pack()
Label(f0,text="Mar 22,2020",font="lucida 13 bold").pack()
f0.pack()
f1=Frame(root,width=900,height=200)
Label(f1,text=f"{texts[0]}",padx=22,pady=22).pack(side="left")
Label(f1,image=f"{photos[0]}",anchor="e").pack()
f1.pack(anchor="w")



root.mainloop()