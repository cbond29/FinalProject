#Importing tkinter module
from os import write
from tkinter import *
from tkinter.ttk import *

#Initializing window
master = Tk()

#Defines all windows main and selections
class Frames(object):
    #Defines soap window     
    def soapWindow():
        #Defines pop-up description text for rose
        def rLabel():
            i = Label(soapWindow, text="A floral scent, reminiscent of a walk through a garden")
            i.place(x=150, y=75)
        #Defines pop-up description text for linen
        def lLabel():
            i = Label(soapWindow, text="A fresh laundry scent, get lost in the wind")
            i.place(x=150, y=125)
        #Defines pop-up description text for Lavender
        def lvLabel():
            i = Label(soapWindow, text="A vibrant lavender scent, very soothing")
            i.place(x=150, y=175)
        soapWindow = Toplevel(master)
        soapWindow.title('Soap Suds - Soaps')
        soapWindow.geometry("500x300") 
        soapWindow.resizable(0, 0)
        #Displays window text
        sText = Label(soapWindow, text="Please select a Soap fragrance to learn more:")
        sText.place(x=130, y=0)
        #Creates clickable buttons to display scent information on click
        rose = Button(soapWindow,text='Rose', command=rLabel)
        linen = Button(soapWindow,text='Linen', command=lLabel)
        lavender = Button(soapWindow,text='Lavender', command=lvLabel)
        #Aligns buttons on page using coordinates
        rose.place(x=220,y=50)
        linen.place(x=220,y=100)
        lavender.place(x=220,y=150)
        #Creates button to close window and return to main selections
        Button(soapWindow, text="I'm done looking, take me back to main menu", command=soapWindow.destroy).place(x=130, y=200)
        
    #Defines candle order window   
    def candleWindow():
        #Defines pop-up description text for Storm
        def sLabel():
            i = Label(candleWindow, text="Smells like a stormy night, rain not included")
            i.place(x=150, y=75)
        #Defines pop-up description text for Sunrise
        def srLabel():
            i = Label(candleWindow, text="Smells like a new day, fresh and clean")
            i.place(x=150, y=125)
        #Defines pop-up description text for Breeze
        def bLabel():
            i = Label(candleWindow, text="Crisp and cold, very aromatic")
            i.place(x=150, y=175)
        candleWindow = Toplevel(master)
        candleWindow.title('Soap Suds - Candles')
        candleWindow.geometry("500x300") 
        candleWindow.resizable(0, 0)
        #Displays window text
        cText = Label(candleWindow, text="Please select a Candle fragrance to learn more:")
        cText.place(x=130, y=0)
        #Creates clickable buttons to display scent information on click
        storm = Button(candleWindow,text='Storm', command=sLabel)
        sunrise = Button(candleWindow,text='Sunrise', command=srLabel)
        breeze = Button(candleWindow,text='Breeze', command=bLabel)
        #Aligns buttons on page using coordinates
        storm.place(x=220,y=50)
        sunrise.place(x=220,y=100)
        breeze.place(x=220,y=150)
        #Creates button to close window and return to main selections
        Button(candleWindow, text="I'm done looking, take me back to main menu", command=candleWindow.destroy).place(x=130, y=200)
        
    #Defines Bath Bomb order window   
    def bathBombWindow():
        #Defines pop-up description text for Orange Citrus
        def oLabel():
            i = Label(bathBombWindow, text="Like a fresh squeezed orange juice for your nose")
            i.place(x=150, y=75)
        #Defines pop-up description text for Green Forest
        def gLabel():
            i = Label(bathBombWindow, text="Get lost in the forest, surreal mountain air")
            i.place(x=150, y=125)
        #Defines pop-up description text for Blue Ocean
        def bLabel():
            i = Label(bathBombWindow, text="Let the waves wash over you, truly a vibe")
            i.place(x=150, y=175) 
        bathBombWindow = Toplevel(master)
        bathBombWindow.title('Soap Suds - Bath Bombs')
        bathBombWindow.geometry("500x300") 
        bathBombWindow.resizable(0, 0)
        #Displays window text
        bText = Label(bathBombWindow, text="Please select a Bath Bomb color & fragrance to learn more:")
        bText.place(x=130, y=0)
        #Creates clickable buttons to display scent information on click
        orangeCitrus = Button(bathBombWindow,text='Orange Citrus', command=oLabel)
        greenForest = Button(bathBombWindow,text='Green Forest', command=gLabel)
        blueOcean = Button(bathBombWindow,text='Blue Ocean', command=bLabel)
        #Aligns buttons on page using coordinates
        orangeCitrus.place(x=220,y=50)
        greenForest.place(x=220,y=100)
        blueOcean.place(x=220,y=150)
        #Creates button to close window and return to main selections
        Button(bathBombWindow, text="I'm done looking, take me back to main menu", command=bathBombWindow.destroy).place(x=130, y=200)
        
    #Defines master frame
    def mainFrame(self,master):
        master.title('Soap Suds')
        master.geometry("500x300") 
        master.resizable(0, 0)
                
#Sets background image
img = PhotoImage(file="soapbg.png")
LabelOne = Label(master, image=img)
LabelOne.place(x=0, y=0)

#Places text to prompt selection in main window
firstText = Label(master, text="Hello, Welcome to the Soap Suds catalog! \nPlease select a product to view all fragrances:")
firstText.place(x=130,y=00)

#Creates buttons that link to new windows depending on selection
soap = Button(master,text='Soap', command=Frames.soapWindow)
candles = Button(master,text='Candles', command=Frames.candleWindow)
bathBombs = Button(master,text='Bath Bombs', command=Frames.bathBombWindow)

#Sets alignment and spacing on GUI for choices
soap.place(x=220,y=50)
candles.place(x=220,y=100)
bathBombs.place(x=220,y=150)
#Creates button to close master catalog window quitting application
Button(master, text="Quit this catalog", command=master.destroy).place(x=210, y=200)


app = Frames()
app.mainFrame(master)
master.mainloop()