from tkinter import *
import random
import time
from PIL import ImageTk, Image



class View():

    def __init__(self):
        self.root = Tk()
        self.w = 1000
        self.h = 600
        self.canvas = Canvas(self.root, width=self.w, height=self.h, bg='#146372')
        self.canvas.pack()
        self.enter = self.resizeImage("assets/enter.png")
        self.cover = self.resizeImage2("assets/cover.png")
        self.level = 1

        self.ratio = 3**0.5

    def resizeImage(self, file_name):
        image = Image.open(file_name)
        resized_image = image.resize((50, 50), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def resizeImage2(self, file_name):
        image = Image.open(file_name)
        resized_image = image.resize((250, 250), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def drawStartScreen(self):
        self.canvas.create_text(500, 150, text="Once upon a time, there was a wonderful simple,\nbut tricky online game.It built up from tiny hexagons,\nwhich created a big hexagon, just like a beehive.\nThe aim was to fill the hive so, that all the hexagons have\nthe same colour. You can say the bees, which parts\nshould be coloured if you click any of the small hexagons.\nThe chosen hexagon and all its neighbours\nwill change their colours to the opposite.", anchor=NW, font=('Helvetica', 12), fill='white')
        self.canvas.create_text(200, 370, text="Do you wanna play?", font=('Helvetica', 18), anchor=NW, fill='white')
        self.canvas.create_text(200, 470, text="Push", font=('Helvetica', 20), anchor=NW, fill='white')
        self.canvas.create_image(200, 100, image=self.cover, anchor=NW)
        self.canvas.create_image(270, 455, image=self.enter, anchor=NW)
        self.canvas.create_text(330, 470, text="if you are ready", anchor=NW, font=('Helvetica', 20), fill='white')


    def creating_hexagon(self, x, y, a, j, i):
        position = [j, i]
        #color = ['white', 'yellow', 'white', 'yellow']
        filling = 'white'
        #time.sleep(0.1)
        hexa = self.canvas.create_polygon(x, y, x+a, y, x+a+(a/2), y+a*self.ratio/2, x+a, y+a*self.ratio, x, y+a*self.ratio, x-(a/2), y+a*self.ratio/2, outline='black', fill=filling, tags=[position, filling])
        self.canvas.create_text(600, 100, text="The HIVE", font=('Helvetica', 50), anchor=NW, fill='#eafbff')
        self.canvas.create_text(600, 200, text="Level "+str(self.level), font=('Helvetica', 30), anchor=NW, fill='red')
        self.canvas.create_text(600, 300, text="Choose one of the hexagons\nand click on it.\nThe tiny little bees will\nrebuild their hive for you", font=('Helvetica', 20), anchor=NW, fill='#eafffb')
        self.canvas.update()
        print(position)

    def generateBoard(self, n):
        for step in range(self.level+10):
            i = str(random.randint(0, n-1))
            j = str(random.randint(0, n-1))
            if self.canvas.find_withtag(j+" "+i):
                #print(self.canvas.gettags(CURRENT))
                pos = j+" "+i
                tags = self.canvas.gettags(pos)
                if 'yellow' in tags:
                    self.canvas.itemconfig(pos, fill='white')
                    self.canvas.dtag(pos, 'yellow') #deletes the yellow tag!!!
                    self.canvas.addtag_withtag('white', pos)
                    print(self.canvas.gettags(pos))
                elif 'white' in tags:
                    self.canvas.itemconfig(pos, fill='yellow')
                    self.canvas.dtag(pos, 'white')
                    self.canvas.addtag_withtag('yellow', pos)
                    print(self.canvas.gettags(pos))
            #neighbours:
                first = str(int(pos[0])-1)+" "+str(int(pos[2]))
                second = str(int(pos[0]))+" "+str(int(pos[2])-1)
                third = str(int(pos[0])-1)+" "+str(int(pos[2])-1)
                fourth = str(int(pos[0])+1)+" "+str(int(pos[2])+1)
                fifth = str(int(pos[0])+1)+" "+str(int(pos[2]))
                sixth = str(int(pos[0]))+" "+str(int(pos[2])+1)
                if 'white' in self.canvas.gettags(first):
                    self.canvas.itemconfig(self.canvas.find_withtag(first), fill="yellow")
                    self.canvas.dtag(self.canvas.find_withtag(first), 'white')
                    self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(first))
                else:
                    self.canvas.itemconfig(self.canvas.find_withtag(first), fill="white")
                    self.canvas.dtag(self.canvas.find_withtag(first), 'yellow')
                    self.canvas.addtag_withtag('white', self.canvas.find_withtag(first))
                if 'white' in self.canvas.gettags(second):
                    self.canvas.itemconfig(self.canvas.find_withtag(second), fill="yellow")
                    self.canvas.dtag(self.canvas.find_withtag(second), 'white')
                    self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(second))
                else:
                    self.canvas.itemconfig(self.canvas.find_withtag(second), fill="white")
                    self.canvas.dtag(self.canvas.find_withtag(second), 'yellow')
                    self.canvas.addtag_withtag('white', self.canvas.find_withtag(second))
                if 'white' in self.canvas.gettags(third):
                    self.canvas.itemconfig(self.canvas.find_withtag(third), fill="yellow")
                    self.canvas.dtag(self.canvas.find_withtag(third), 'white')
                    self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(third))
                else:
                    self.canvas.itemconfig(self.canvas.find_withtag(third), fill="white")
                    self.canvas.dtag(self.canvas.find_withtag(third), 'yellow')
                    self.canvas.addtag_withtag('white', self.canvas.find_withtag(third))
                if 'white' in self.canvas.gettags(fourth):
                    self.canvas.itemconfig(self.canvas.find_withtag(fourth), fill="yellow")
                    self.canvas.dtag(self.canvas.find_withtag(fourth), 'white')
                    self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(fourth))
                else:
                    self.canvas.itemconfig(self.canvas.find_withtag(fourth), fill="white")
                    self.canvas.dtag(self.canvas.find_withtag(fourth), 'yellow')
                    self.canvas.addtag_withtag('white', self.canvas.find_withtag(fourth))
                if 'white' in self.canvas.gettags(fifth):
                    self.canvas.itemconfig(self.canvas.find_withtag(fifth), fill="yellow")
                    self.canvas.dtag(self.canvas.find_withtag(fifth), 'white')
                    self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(fifth))
                else:
                    self.canvas.itemconfig(self.canvas.find_withtag(fifth), fill="white")
                    self.canvas.dtag(self.canvas.find_withtag(fifth), 'yellow')
                    self.canvas.addtag_withtag('white', self.canvas.find_withtag(fifth))
                if 'white' in self.canvas.gettags(sixth):
                    self.canvas.itemconfig(self.canvas.find_withtag(sixth), fill="yellow")
                    self.canvas.dtag(self.canvas.find_withtag(sixth), 'white')
                    self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(sixth))
                else:
                    self.canvas.itemconfig(self.canvas.find_withtag(sixth), fill="white")
                    self.canvas.dtag(self.canvas.find_withtag(sixth), 'yellow')
                    self.canvas.addtag_withtag('white', self.canvas.find_withtag(sixth))

                #self.canvas.itemconfig('<Button-1>', fill="blue")
                self.canvas.update_idletasks()
                #self.canvas.after(200)


    def click(self):
        if self.canvas.find_withtag(CURRENT):
            print(self.canvas.gettags(CURRENT))
            pos = self.canvas.gettags(CURRENT)[0]
            tags = self.canvas.gettags(CURRENT)
            if 'yellow' in tags:
                self.canvas.itemconfig(CURRENT, fill='white')
                self.canvas.dtag(CURRENT, 'yellow') #deletes the yellow tag!!!
                self.canvas.addtag_withtag('white', CURRENT)
                print(self.canvas.gettags(CURRENT))
            elif 'white' in tags:
                self.canvas.itemconfig(CURRENT, fill='yellow')
                self.canvas.dtag(CURRENT, 'white')
                self.canvas.addtag_withtag('yellow', CURRENT)
                print(self.canvas.gettags(CURRENT))
            #neighbours:
            first = str(int(pos[0])-1)+" "+str(int(pos[2]))
            second = str(int(pos[0]))+" "+str(int(pos[2])-1)
            third = str(int(pos[0])-1)+" "+str(int(pos[2])-1)
            fourth = str(int(pos[0])+1)+" "+str(int(pos[2])+1)
            fifth = str(int(pos[0])+1)+" "+str(int(pos[2]))
            sixth = str(int(pos[0]))+" "+str(int(pos[2])+1)
            if 'white' in self.canvas.gettags(first):
                self.canvas.itemconfig(self.canvas.find_withtag(first), fill="yellow")
                self.canvas.dtag(self.canvas.find_withtag(first), 'white')
                self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(first))
            else:
                self.canvas.itemconfig(self.canvas.find_withtag(first), fill="white")
                self.canvas.dtag(self.canvas.find_withtag(first), 'yellow')
                self.canvas.addtag_withtag('white', self.canvas.find_withtag(first))
            if 'white' in self.canvas.gettags(second):
                self.canvas.itemconfig(self.canvas.find_withtag(second), fill="yellow")
                self.canvas.dtag(self.canvas.find_withtag(second), 'white')
                self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(second))
            else:
                self.canvas.itemconfig(self.canvas.find_withtag(second), fill="white")
                self.canvas.dtag(self.canvas.find_withtag(second), 'yellow')
                self.canvas.addtag_withtag('white', self.canvas.find_withtag(second))
            if 'white' in self.canvas.gettags(third):
                self.canvas.itemconfig(self.canvas.find_withtag(third), fill="yellow")
                self.canvas.dtag(self.canvas.find_withtag(third), 'white')
                self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(third))
            else:
                self.canvas.itemconfig(self.canvas.find_withtag(third), fill="white")
                self.canvas.dtag(self.canvas.find_withtag(third), 'yellow')
                self.canvas.addtag_withtag('white', self.canvas.find_withtag(third))
            if 'white' in self.canvas.gettags(fourth):
                self.canvas.itemconfig(self.canvas.find_withtag(fourth), fill="yellow")
                self.canvas.dtag(self.canvas.find_withtag(fourth), 'white')
                self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(fourth))
            else:
                self.canvas.itemconfig(self.canvas.find_withtag(fourth), fill="white")
                self.canvas.dtag(self.canvas.find_withtag(fourth), 'yellow')
                self.canvas.addtag_withtag('white', self.canvas.find_withtag(fourth))
            if 'white' in self.canvas.gettags(fifth):
                self.canvas.itemconfig(self.canvas.find_withtag(fifth), fill="yellow")
                self.canvas.dtag(self.canvas.find_withtag(fifth), 'white')
                self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(fifth))
            else:
                self.canvas.itemconfig(self.canvas.find_withtag(fifth), fill="white")
                self.canvas.dtag(self.canvas.find_withtag(fifth), 'yellow')
                self.canvas.addtag_withtag('white', self.canvas.find_withtag(fifth))
            if 'white' in self.canvas.gettags(sixth):
                self.canvas.itemconfig(self.canvas.find_withtag(sixth), fill="yellow")
                self.canvas.dtag(self.canvas.find_withtag(sixth), 'white')
                self.canvas.addtag_withtag('yellow', self.canvas.find_withtag(sixth))
            else:
                self.canvas.itemconfig(self.canvas.find_withtag(sixth), fill="white")
                self.canvas.dtag(self.canvas.find_withtag(sixth), 'yellow')
                self.canvas.addtag_withtag('white', self.canvas.find_withtag(sixth))

            self.canvas.itemconfig('<Button-1>', fill="blue")
            self.canvas.update_idletasks()
            self.canvas.after(200)
            #canvas.itemconfig(CURRENT, fill="red")

    def checkColors(self):
        for row in range(self.level+4):
            for column in range(self.level+4):
                tags = self.canvas.gettags(str(row)+" "+str(column))
                if 'yellow' in tags:
                    return False
                elif row == self.level+3 and column == self.level+3 and 'yellow' not in tags:
                    self.level += 1
                    return True
