#Packages include tkinter for GUI, ctypes for system resolution, and PIL for image manipulation
import tkinter as tk
import tkinter.messagebox as tkm
import ctypes
import os, subprocess, threading

#Runs the server
server = threading.Thread(target=subprocess.call,args=['python recieve_sms.py'])
server.start()

#Gets the window resolution and assigns it to width and height
user32 = ctypes.windll.user32
w, h = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

#Make the window and declare entry string variables
win = tk.Tk()
win.configure(bg = "gold")
v = tk.StringVar()
i = tk.StringVar()
y = tk.StringVar()

#Definitions
#The entries function counts the number of entries
def entries(key, value):
    d = {}
    d[key] = value
    return d
#The handle_request function makes StringVar variables and returns new variables
def handle_request():
    name = ''
    number = ''
    #If all strings are unempty, continue and go on with texting and adding a contact
    if v != '' and i != '' and y != '':
        name = v.get()
        number = i.get()
        message = y.get()
        print(name, number, message)
        #entries(name,number)
        # entry_field1.delete(0, tk.END)
        # entry_field2.delete(0, tk.END)
        v.set("")
        i.set("")
        y.set("")
        label_field = tk.Label(master = win, text = name + ',' + number, width = 30, justify = 'left')
        label_field.pack(side = 'top')
        sendText(number,message)
        return(name, number)

        # #Create a simple alert box to choose between keeping contacts
        # response = tkm.askquestion("Confirmation", "Do you want to send this message?")

        # # If user clicks 'Yes' then it returns 1 else it returns 0
        # if response == 1:
        #     #Makes a text field to hold contacts
        #     
        #     tkm.showinfo("Confirmation", "Message was sent.")
        # else:
        #     pass
    else:
        #Show a warning anc clear out all strings
        tkm.showinfo("Warning", "One or both of the text fields do not have anything inside. Please try again.")        
        v.set("")
        i.set("")
        y.set("")

def sendText(toNum,text):
    from twilio.rest import Client

    # Your Account SID from twilio.com/console
    account_sid = "AC4c4e1052c676a72b5b92c7b8e7d5dd0b"
    # Your Auth Token from twilio.com/console
    auth_token  = "417430b4e40ba1a62c32d837315d0c63"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+"+str(toNum), 
        from_="+12563673601",
        body=text)

    #print(message.sid)
    print("Sent")

#Actual Interface

#Useful alert stuff
tkm.showinfo("Alert!", "Adjusting your pizza screen to " + str(w) +' and ' + str(h))

win.title("Text Messager")

#Window size in pixels
win.geometry(str(w)+'x'+str(h))
# win.geometry("400x400")
# w, h = 400,400

#Label Title
title = tk.Label(win, text = "Welcome to the Text Messenger!", font = ("Times New Roman",20), bg = "gold")
title.pack()

#Label Desc
label1 = tk.Label(win, bg = 'gold', wraplength = 500, font = ("Times New Roman",10), text = "This will send a message to a client and keep their contact on a cloud").pack()

#Label Name
label2 = tk.Label(win, bg = 'gold', wraplength = 500, font = ("Times New Roman",11), text = "Name: ").pack()

#Entry field Name
entry_field1 = tk.Entry(win, textvariable = v).pack()

#Label Number
label3 = tk.Label(win, bg = 'gold', wraplength = 500, font = ("Times New Roman",10), text = "Number: ").pack()

#Entry field Number
entry_field2 = tk.Entry(win, textvariable = i).pack()

#Label Message
label4 = tk.Label(win, bg = 'gold', wraplength = 500, font = ("Times New Roman",10), text = "Message: ").pack()

#Entry field Message
entry_field3 = tk.Entry(win, textvariable = y).pack()

#Makes a button
button1 = tk.Button(win, text = "SEND", cursor = 'heart', command = handle_request)
button1.pack()

#label4 = tk.Label(win, bg = 'gold', wraplength = 500, font = ("Times New Roman",10), text = "Response: ").pack()
##texti = tk.Text(win,width=30,height=30,justify='left').pack()

#Picture
img = tk.PhotoImage(file = ("C:/Users/Major League Hacking/Documents/Pizza Test2/pizza.gif"))
img = img.zoom(25) #with 250, I ended up running out of memory
img = img.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
label = tk.Label(win, image = img).pack(side = "right")

#Picture2
img2 = tk.PhotoImage(file = ("C:/Users/Major League Hacking/Documents/Pizza Test2/pizza.gif"))
img2 = img2.zoom(25) #with 250, I ended up running out of memory
img2 = img2.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
label = tk.Label(win, image = img2).pack(side = "left")

#Runs all the code above
win.mainloop()

#We need a title, a label, a entry field to enter contact information separated by a comma
#We need a button to contact them, we need an entry field that can load contacts
#Have 2 plus buttons
#1 Button for new contact that deals with 2 textboxes that
#Section
#Two text boxes
#Name
#Number
#Are you sure you want to add this?
