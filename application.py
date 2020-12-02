from tkinter import Tk,Canvas,Label,Entry,Toplevel,StringVar,Button
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import phishingDetection
from threading import Thread
from requests.exceptions import ConnectionError
import os
class SplashScreen: 
    """
    Here we are creating class for splash screen.
    """
    def __init__(self, parent):
        """
        Here we are defineing constructor for SplashScreen class.
        This function will get window in its parameter. and calling aturSplash function and aturWindow function
         """ 
        self.parent = parent 
        self.aturSplash() 
        self.aturWindow() 

    def aturSplash(self): 
        """This function will load our image for splash screen"""
        self.gambar = Image.open('./image/phishing-alert.png')
        self.imgSplash = ImageTk.PhotoImage(self.gambar)

    def aturWindow(self):
        """Here we create our splash screen"""
        lebar, tinggi = self.gambar.size 
        setengahLebar = (self.parent.winfo_screenwidth()-lebar)//2 
        setengahTinggi = (self.parent.winfo_screenheight()-tinggi)//2
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi, setengahLebar,setengahTinggi))
        Label(self.parent, image=self.imgSplash).pack()

class PhishingAlert(SplashScreen):
    """
    This is our main class that inherit all the functionallity of SplashScreen. 
    In this class we are write the code for create our frontend
    """
    def __init__(self, master=None):
        """
        Here we are define constructor for PhishingAlert class.
        It will take window as parameter.
        """
        # if user not did not pass any parameter to this class then we create our own windows
        if master:
            self.win = master
        else:
            self.win =Tk()
        # withdraw() function is use for hide windows
        self.win.withdraw()
        # Here we are creating windows for splash screen
        self.loadingscreen=Toplevel(self.win)
        # Here we write code to make window on top
        self.loadingscreen.attributes('-topmost', True)
        # overrideredirect() is use for remove title bar from windows.
        self.loadingscreen.overrideredirect(True) 
        # Here we are adding Progressbar in the bottom of windows
        self.progressbar = Progressbar(self.loadingscreen, orient='horizontal', length=10000, mode='determinate') 
        self.progressbar.pack(side="bottom")
        # Here we run the __init__() function (constructor) of inherited class
        super().__init__(self.loadingscreen)
        # Here we start our prograss bar with 25 speed
        self.progressbar.start(25)
        # Here we write the code for calling _on_ending_progressbar function afer 3 seconds
        self.win.after(3000, self._on_ending_progressbar) 
        # following code will execute in backgournd while running splash screen
        # calling load things function to load thing in background
        self.win.after(500, self.load_things) 

        if not master:
            # start our windoes mainloop
            self.win.mainloop()
# Country show ho
# Domain name
# Create date
# Expiry date
# Name server
# Page rank 
# Ip addres
# Url length
# SSLfinal_state
# Favicon
# Port 
# Http_token
# DNSrecord
    def load_things(self):
        """ Here we write the things that we want to execute in background while splash screen is running"""
        # load images
        back = Image.open('./image/image.png')
        self.bgimg = ImageTk.PhotoImage(back)
        back = Image.open('./image/success.png')
        self.successimg = ImageTk.PhotoImage(back)
        back = Image.open('./image/unsuccess.png')
        self.unsuccessimg = ImageTk.PhotoImage(back)
        self.urlvar =StringVar()
        self.precisionvar=StringVar()
        self.countryvar=StringVar()
        self.domainvar=StringVar()
        self.createdatevar=StringVar()
        self.expirydatevar=StringVar()
        self.servernamevar=StringVar()
        self.ipaddressvar=StringVar()
        self.urllenvar=StringVar()
        self.orgnamevar=StringVar()
        self.statevar=StringVar()
        # main windows setting 
        self.win.title("PhishAnt ")
        self.win.iconbitmap(r'./image/icon.ico')
        self.win.geometry("1220x600")
        self.win.resizable(height=False,width=False)
        # binding ctrl with open text files
        self.win.bind("<Control-p>",lambda e: os.startfile("phishing-sites.txt"))
        self.win.bind("<Control-P>",lambda e: os.startfile("phishing-sites.txt"))
        self.win.bind("<Control-l>",lambda e: os.startfile("legit-sites.txt"))
        self.win.bind("<Control-L>",lambda e: os.startfile("legit-sites.txt"))
        # calling mkframe function 
        self.mkframe()
        
    def _on_ending_progressbar(self):
        """Here we write the code for destroy our splash window and show our main window"""
        self.progressbar.stop()
        self.loadingscreen.destroy()
        # deiconify is use for again show window that we hide in very start
        self.win.deiconify()
        # center() function, we define it very bottom of code
        self.center(self.win)
        
    def mkframe(self):
        """Create frame for url input field and button"""
        # canvas is just like a frame. we are not use tk.Frame because we have to set our background
        self.f1 =Canvas(width = 720, height = 600)
        self.f1.pack(expand =True, fill='both')

        # seting background image
        self.f1.create_image(0, 0, image = self.bgimg, anchor ='nw')
        # seting Labels and titles
        self.f1.itemconfig(self.f1.create_text(30, 120, anchor = "nw"), text="Phish Ant", font=("Showcard Gothic", 72, "bold"), fill='white')
        self.f1.itemconfig(self.f1.create_text(30, 250, anchor = "nw"), text="Phishing Website Detection", font="Arial 17", fill='white')
        self.f1.itemconfig(self.f1.create_text(30, 365, anchor = "nw"), text="Enter URL : ", fill='white', font="Arial 20")
        # this is status lable that show our errors and other messages to user
        self.statuslabel = self.f1.create_text(300, 450, anchor = "nw")
        self.f1.itemconfig(self.statuslabel, text="Enter URL and click check button", fill='white', font="Arial 25")

        # Creating entry for URL
        ent=Entry(self.f1, textvariable=self.urlvar, borderwidth=15, width=50, font="Arial 20", bg="#9D4EEF",fg='white')
        ent.grid(column=2,row=2,padx=(200,0),pady=(350,0))
        ent.focus()
        # creating check button
        self.checkbtn=Button(self.f1, text="  Check  ", bg='#F13E7F',font =("Lucida Fax", 20, "bold"), fg='white', relief='flat', command=self.check, highlightthickness =5)
        self.checkbtn.grid(column=3,row=2, padx = 20,pady=(350,0))

    def show_message(self,msgtype,title,message):
        """This function will show our success and unsuccess message to user"""
        # all functionas that use in this function we was discussed at top
        msg =Toplevel(self.win,bg='#FFFFFF')
        msg.overrideredirect(True)
        msg.attributes('-topmost', True)
        # msg.geometry("512x308")
        msg.geometry("512x508")
        self.center(msg)
        f1 =Canvas(msg, width = 720, height = 600)
        f1.pack(expand =True, fill ='both')
        # show Precision
        self.f1.itemconfig(self.statuslabel, text=f"Precision: {self.precisionvar.get()}", fill='white', font="Arial 25")
        Button(f1, text="      OK      ", bg='#0d47a1',fg='white',font =("Arial", 15), command=msg.destroy).pack(padx=(0,0),pady=(450,0))
        
        f1.itemconfig(f1.create_text(40, 230, anchor = "nw"), text=f"Country : {self.countryvar.get()}", font="Arial 15", fill='black')
        f1.itemconfig(f1.create_text(40, 255, anchor = "nw"), text=f"Organization : {self.orgnamevar.get()}", font="Arial 15", fill='black')
        f1.itemconfig(f1.create_text(40, 280, anchor = "nw"), text=f"Domain : {self.domainvar.get()}", font="Arial 15", fill='black')
        f1.itemconfig(f1.create_text(40, 305, anchor = "nw"), text=f"State Name : {self.statevar.get()}", font="Arial 15", fill='black')
        f1.itemconfig(f1.create_text(40, 330, anchor = "nw"), text=f"Server name : {self.servernamevar.get()}", font="Arial 15", fill='black')
        f1.itemconfig(f1.create_text(40, 355, anchor = "nw"), text=f"Creation date : {self.createdatevar.get()}", font="Arial 15", fill='black')
        f1.itemconfig(f1.create_text(40, 380, anchor = "nw"), text=f"Expiration date : {self.expirydatevar.get()}", font="Arial 15", fill='black')
        f1.itemconfig(f1.create_text(40, 405, anchor = "nw"), text=f"IP Address : {self.ipaddressvar.get()}", font="Arial 15", fill='black')
        f1.itemconfig(f1.create_text(40, 430, anchor = "nw"), text=f"URL Length : {self.urllenvar.get()}", font="Arial 15", fill='black')
        
        if msgtype=="success":
            f1.create_image(210, 10, image = self.successimg, anchor ='nw')
            f1.itemconfig(f1.create_text(170, 140, anchor = "nw"), text=title, font="Arial 30 bold", fill='#5cb85c')
            f1.itemconfig(f1.create_text(180-len(message), 210, anchor = "nw"), text=message, font="Arial 15", fill='black')
        else:
            f1.create_image(210, 10, image = self.unsuccessimg, anchor ='nw')
            f1.itemconfig(f1.create_text(170, 140, anchor = "nw"), text=title, font="Arial 30 bold", fill='#d9534f')
            f1.itemconfig(f1.create_text(180-len(message), 210, anchor = "nw"), text=message, font="Arial 15", fill='black')
        
        

    def _check(self):
        """This will run in threading on check button click"""
        # getting url from urlvar variable that we define in top
        url = self.urlvar.get()
        # if user type url in entry box
        if url:
            try:
                # getting result 
                result = phishingDetection.CheckUrl(url,setPrecisionTo=self.precisionvar,country=self.countryvar,setdomain=self.domainvar,createdate=self.createdatevar,expirydate=self.expirydatevar,servername=self.servernamevar,setipaddress=self.ipaddressvar,urllen=self.urllenvar,orgname=self.orgnamevar,statename=self.statevar)
            except ConnectionError :
                # If internet connection not found
                self.f1.itemconfig(self.statuslabel, text="Internet connection not found.", fill='red', font="Arial 25")
                # cnange button state back to normal
                self.checkbtn['state']='normal'
                return
            except ValueError as e:
                # if user type invalid url or phishing url
                result = False
            except Exception as e:
                # If any exception occurred following code will show it in sataus label
                self.f1.itemconfig(self.statuslabel, text=e, fill='red', font="Arial 25")
                self.checkbtn['state']='normal'
                return
            # change button state back to normal
            self.checkbtn['state']='normal'
            if result:
                self.show_message("success","Legitimate","This site is Legitimate")
            else:
                self.show_message("unsuccess","Phishing","This site is Phishing site")

        else:
            self.f1.itemconfig(self.statuslabel, text="Please enter url first", fill='#CC0000', font="Arial 25")
            self.checkbtn['state']='normal'
            return

    def check(self):
        """This function will call on check button click"""
        # disable check button
        self.checkbtn['state']='disabled'
        # Here we are create a thread for check function
        # with the help of thread a specific part of program will run in background and our main program will not hangout 
        t = Thread(target=self._check)
        t.daemon = True
        t.start()
        self.f1.itemconfig(self.statuslabel, text="Checking....Please wait", fill='white', font="Arial 25")

    
    def center(self, win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

if __name__ == "__main__":
    PhishingAlert()




        
        
