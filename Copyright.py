from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image, ExifTags

import os

def copyright_apply(input_image_path,text):
    copyright_text = " © " + text + "   "
    for i in input_image_path:
        print(i)
        photo = Image.open(i)
        
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation]=='Orientation':
                    break

            exif=dict(photo._getexif().items())

            if exif[orientation] == 3:
                photo=photo.rotate(180, expand=True)
            elif exif[orientation] == 6:
                photo=photo.rotate(270, expand=True)
            elif exif[orientation] == 8:
                photo=photo.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
            pass

        #Store image width and height
        w, h = photo.size

        # make the image editable
        drawing = ImageDraw.Draw(photo)
        font = ImageFont.truetype("Helvetica.ttf", 68)

        #get text width and height
        text = copyright_text
        text_w, text_h = drawing.textsize(text, font)

        pos = w - text_w, (h - text_h) - 50

        c_text = Image.new('RGB', ((text_w),(text_h)+5) , color = '#000000')
        drawing = ImageDraw.Draw(c_text)

        drawing.text((0,0), text, fill="#ffffff", font=font)
        c_text.putalpha(100)

        photo.paste(c_text, pos, c_text)
        photo.save(str(i)+"copy.jpeg")
        
    mylabel = tk.Label(root, text="Done - Please close the window").pack()


    
import tkinter as tk
from tkinter import filedialog, Label, TOP

root = tk.Tk()
# add general settings
root.title('Copyright Automator - 2020')
root.minsize(700,200)

# add title
Label(root, text = 'Copyright Automator',  
      font =('Verdana', 15)).pack(side = TOP, pady = 10) 
# add instructions
Label(root, text = '1. Select your files \n 2. Script will add the copyright logo \n 3. Saved all under your Download folder \n\n',  
      font =('Verdana', 10)).pack() 

def runscript(file_list):
    print(text_entered.get())
    for i in file_list :
        print(i)
    copyright_text = text_entered.get()
    return copyright_text

def getfiles():
    file_path = filedialog.askopenfilenames(
        initialdir=os.path.join( "C:", "Download" ),
        title='Choose a file - You can also select multiple files')

    #save all into a list
    file_list=[]
    for file in root.tk.splitlist(file_path):
        file_list.append(file)
        #mylable = tk.Label(root, text=file_path).pack()
    mylable = tk.Label(root, text="Number of file to modify -> "+str(len(file_path))).pack()
    show = tk.Button(frame, text='Please Confirm', command=(lambda: copyright_apply(file_list,text_entered.get())))
    show.pack()
    
master = tk.Frame(root)
master.pack()

text_title =  Label(master, text="Copyright Text:",font =('Verdana', 10))
text_title.pack()

text_entered = tk.Entry(master)
text_entered.insert(10, "insieme Valais")
text_entered.pack()

frame = tk.Frame(root)
frame.pack()



slogan = tk.Button(frame,text="Run the Script Copyright",command=(lambda: getfiles()))
slogan.pack()

button = tk.Button(frame, text="Exit", fg="red",command=quit)
button.pack()

root.mainloop()