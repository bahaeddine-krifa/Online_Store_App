from tkinter import *
from tkinter import filedialog,messagebox
import tkinter.messagebox as tkMessageBox
import random
import time

#Functions

def reset():
    textReceipt.delete(1.0,END)
    e_rice.set('0')
    e_meat.set('0')
    e_fish.set('0')
    e_chicken.set('0')
    e_egg.set('0')
    e_cheese.set('0')
    e_sugar.set('0')
    e_salt.set('0')
    e_tomato.set('0')

    e_cocacola.set('0')
    e_pepsi.set('0')
    e_colddrinks.set('0')
    e_coffee.set('0')
    e_water.set('0')
    e_milk.set('0')
    e_tea.set('0')
    e_lemonade.set('0')
    e_smoothie.set('0')

    e_oreo.set('0')
    e_apple.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')

    textrice.config(state=DISABLED)
    textmeat.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textegg.config(state=DISABLED)
    textcheese.config(state=DISABLED)
    textsugar.config(state=DISABLED)
    textsalt.config(state=DISABLED)
    texttomato.config(state=DISABLED)

    textcocacola.config(state=DISABLED)
    textpepsi.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textwater.config(state=DISABLED)
    textmilk.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textlemonade.config(state=DISABLED)
    textsmoothie.config(state=DISABLED)

    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicedeliveryvar.set('')
    totalcostvar.set('')

def send():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        def send_msg():
            varr1 = costoffoodvar.get()
            varr2 = costofdrinksvar.get()
            varr3 = costofcakesvar.get()
            varr4= subtotalvar.get()
            varr5=servicedeliveryvar.get()
            varr6=totalcostvar.get()
            result = tkMessageBox.askquestion("Submit","Are you sure to enter following details?\n" +"cost of food\t"+varr1 + "\n" +"cost of drinks\t"+varr2 + "\n" +"cost of cakes\t"+varr3+ "\n"+"sub total \t"+varr4+ "\n"+"service delivery\t"+varr5+ "\n"+"total cost\t"+varr6)
            if result== "yes" and accountfield.get()=='onlinestore@gmail.com':
                messagebox.showinfo('Information', 'Your Bill Is Successfully Sent')
            else:
                messagebox.showerror('error', 'Your Bill Is not Sent')


        root2 =Toplevel()
        root2.title("Send Bill")
        root2.config(bg='#3E32F8')
        root2.geometry('485x620+50+50')

        logoImage = PhotoImage(file='sender.png')
        label = Label(root2,image=logoImage,bg='#3E32F8')
        label.pack(pady=5)

        accountLabel = Label(root2, text='Google Account', font=('arial', 18, 'bold underline'), bg='#3E32F8', fg='white')
        accountLabel.pack(pady=5)
        accountfield = Entry(root2,font=('helvetica', 22, 'bold'), bd=3, width=24)
        accountfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='#3E32F8', fg='white')
        billLabel.pack(pady=5)
        textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
        textarea.pack(pady=5)
        textarea.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n\n')

        textarea.insert(END, '***************************************************************\n')

        if costoffoodvar.get() != '0 DT':
            textarea.insert(END, f'Cost Of Food\t\t\t{priceofFood}DT\n')
        if costofdrinksvar.get() != '0 DT':
            textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}DT\n')
        if costofcakesvar.get() != '0 DT':
            textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}DT\n')

        textarea.insert(END, '***************************************************************\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}DT\n')
        textarea.insert(END, f'Service Delivery\t\t\t{5000}DT\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems+5000}DT\n')

        sendButton = Button(root2, text='SEND', font=('arial', 19, 'bold'), bg='white', fg='#3E32F8', bd=7, relief=GROOVE
                            ,command=send_msg)
        sendButton.pack(pady=5)

        root2.mainloop()

def save():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None:
            pass
        else:

            bill_data = textReceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information', 'Your Bill Is Succesfully Saved')

def receipt():
    global billnumber,date
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0, END)
        x = random.randint(1000, 10000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')
        textReceipt.insert(END, billnumber + ' \t' +'    Welcome to our store !   ' +'   \t\t' + date + '\n')
        textReceipt.insert(END, '***************************************************************\n')
        textReceipt.insert(END, 'Items:\t\t Cost Of Items(DT)\n')
        textReceipt.insert(END, '***************************************************************\n')
        if e_rice.get() != '0':
            textReceipt.insert(END, f'Rice:\t\t\t{int(e_rice.get()) * 5000}\n\n')

        if e_meat.get() != '0':
            textReceipt.insert(END, f'Meat:\t\t\t{int(e_meat.get()) * 20000}\n\n')

        if e_fish.get() != '0':
            textReceipt.insert(END, f'Fish:\t\t\t{int(e_fish.get()) * 18000}\n\n')

        if e_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 11500}\n\n')

        if e_egg.get() != '0':
            textReceipt.insert(END, f'Egg:\t\t\t{int(e_egg.get()) * 9000}\n\n')

        if e_cheese.get() != '0':
            textReceipt.insert(END, f'Cheese:\t\t\t{int(e_cheese.get()) * 7500}\n\n')

        if e_sugar.get() != '0':
            textReceipt.insert(END, f'Sugar:\t\t\t{int(e_sugar.get()) * 1400}\n\n')

        if e_salt.get() != '0':
            textReceipt.insert(END, f'Salt:\t\t\t{int(e_salt.get()) * 660}\n\n')

        if e_tomato.get() != '0':
            textReceipt.insert(END, f'Tomato:\t\t\t{int(e_tomato.get()) * 3750}\n\n')

        if e_cocacola.get() != '0':
            textReceipt.insert(END, f'Coca Cola:\t\t\t{int(e_cocacola.get()) * 1250}\n\n')

        if e_pepsi.get() != '0':
            textReceipt.insert(END, f'Pepsi:\t\t\t{int(e_pepsi.get()) * 1500}\n\n')

        if e_colddrinks.get() != '0':
            textReceipt.insert(END, f'Cold drinks:\t\t\t{int(e_colddrinks.get()) * 2100}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffee.get()) * 1400}\n\n')

        if e_water.get() != '0':
            textReceipt.insert(END, f'Water:\t\t\t{int(e_water.get()) * 550}\n\n')

        if e_milk.get() != '0':
            textReceipt.insert(END, f'Milk:\t\t\t{int(e_milk.get()) * 1350}\n\n')

        if e_tea.get() != '0':
            textReceipt.insert(END, f'Tea:\t\t\t{int(e_tea.get()) * 1750}\n\n')

        if e_lemonade.get() != '0':
            textReceipt.insert(END, f'Lemonade:\t\t\t{int(e_lemonade.get()) * 3500}\n\n')

        if e_smoothie.get() != '0':
            textReceipt.insert(END, f'Smoothie:\t\t\t{int(e_smoothie.get()) * 4500}\n\n')

        if e_oreo.get() != '0':
            textReceipt.insert(END, f'Oreo:\t\t\t{int(e_oreo.get()) * 4600}\n\n')

        if e_apple.get() != '0':
            textReceipt.insert(END, f'Apple:\t\t\t{int(e_apple.get()) * 3600}\n\n')

        if e_kitkat.get() != '0':
            textReceipt.insert(END, f'Kitkat:\t\t\t{int(e_kitkat.get()) * 2900}\n\n')

        if e_vanilla.get() != '0':
            textReceipt.insert(END, f'Vanilla:\t\t\t{int(e_vanilla.get()) * 3100}\n\n')

        if e_banana.get() != '0':
            textReceipt.insert(END, f'Banana:\t\t\t{int(e_banana.get()) * 3550}\n\n')

        if e_brownie.get() != '0':
            textReceipt.insert(END, f'Brownie:\t\t\t{int(e_brownie.get()) * 4100}\n\n')

        if e_pineapple.get() != '0':
            textReceipt.insert(END, f'Pine apple:\t\t\t{int(e_pineapple.get()) * 3750}\n\n')

        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate:\t\t\t{int(e_chocolate.get()) * 4850}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black forest:\t\t\t{int(e_blackforest.get()) * 5200}\n\n')

        textReceipt.insert(END, '***************************************************************\n')

        if costoffoodvar.get() != '0 DT':
            textReceipt.insert(END, f'Cost Of Food\t\t\t{priceofFood}DT\n\n')
        if costofdrinksvar.get() != '0 DT':
            textReceipt.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}DT\n\n')
        if costofcakesvar.get() != '0 DT':
            textReceipt.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}DT\n\n')

        textReceipt.insert(END, '***************************************************************\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}DT\n\n')
        textReceipt.insert(END, f'Service Delivery\t\t\t{5000}DT\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+5000}DT\n\n')
        textReceipt.insert(END,'***************************************************************\n')

        textReceipt.insert(END,'\t\tTHANK YOU\n')
        textReceipt.insert(END, '\t_           See You Next Time           _\n')
    else:
        messagebox.showerror('Error', 'No Item Is selected')

def totalcost():
    global priceofFood, priceofDrinks, priceofCakes, subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
       var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
       var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
       var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
       var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
       var26.get() != 0 or var27.get() != 0:
            item1 = int(e_rice.get())
            item2 = int(e_meat.get())
            item3 = int(e_fish.get())
            item4 = int(e_chicken.get())
            item5 = int(e_egg.get())
            item6 = int(e_cheese.get())
            item7 = int(e_sugar.get())
            item8 = int(e_salt.get())
            item9 = int(e_tomato.get())

            item10 = int(e_cocacola.get())
            item11 = int(e_pepsi.get())
            item12 = int(e_colddrinks.get())
            item13 = int(e_coffee.get())
            item14 = int(e_water.get())
            item15 = int(e_milk.get())
            item16 = int(e_tea.get())
            item17 = int(e_lemonade.get())
            item18 = int(e_smoothie.get())

            item19 = int(e_oreo.get())
            item20 = int(e_apple.get())
            item21 = int(e_kitkat.get())
            item22 = int(e_vanilla.get())
            item23 = int(e_banana.get())
            item24 = int(e_brownie.get())
            item25 = int(e_pineapple.get())
            item26 = int(e_chocolate.get())
            item27 = int(e_blackforest.get())

            priceofFood = (item1 * 5000) + (item2 * 20000) + (item3 * 18000) + (item4 * 11500) + (item5 * 9000) + (item6 * 7500) + (item7 * 1400) \
                          + (item8 * 660) + (item9 * 3750)

            priceofDrinks = (item10 * 1250) + (item11 * 1500) + (item12 * 2100) + (item13 * 1400) + (item14 * 550) + (item15 * 1350) \
                            + (item16 * 1750) + (item17 * 3500) + (item18 * 4500)

            priceofCakes = (item19 * 4600) + (item20 * 3600) + (item21 * 2900) + (item22 * 3100) + (item23 * 3550) + (item24 * 4100) \
                           + (item25 * 3750) + (item26 * 4850) + (item27 * 5200)

            costoffoodvar.set(str(priceofFood) + ' DT')
            costofdrinksvar.set(str(priceofDrinks) + ' DT')
            costofcakesvar.set(str(priceofCakes) + ' DT')

            subtotalofItems = priceofFood + priceofDrinks + priceofCakes
            subtotalvar.set(str(subtotalofItems) + ' DT')

            servicedeliveryvar.set('5000 DT')

            tottalcost = subtotalofItems + 5000
            totalcostvar.set(str(tottalcost) + ' DT')
    else:
        messagebox.showerror('Error', 'No Item Is selected')

def rice():
        if var1.get() == 1:
            textrice.config(state=NORMAL)
            textrice.delete(0, END)
            textrice.focus()
        else:
            textrice.config(state=DISABLED)
            e_rice.set('0')
def meat():
    if var2.get()==1:
        textmeat.config(state=NORMAL)
        textmeat.delete(0,END)
        textmeat.focus()
    else:
        textmeat.config(state=DISABLED)
        e_meat.set('0')
def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')
def chicken():
    if var4.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.focus()
        textchicken.delete(0, END)
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')
def egg():
    if var5.get() == 1:
        textegg.config(state=NORMAL)
        textegg.focus()
        textegg.delete(0, END)
    else:
        textegg.config(state=DISABLED)
        e_egg.set('0')
def cheese():
    if var6.get() == 1:
        textcheese.config(state=NORMAL)
        textcheese.focus()
        textcheese.delete(0, END)
    else:
        textcheese.config(state=DISABLED)
        e_cheese.set('0')
def sugar():
    if var7.get() == 1:
        textsugar.config(state=NORMAL)
        textsugar.focus()
        textsugar.delete(0, END)
    else:
        textsugar.config(state=DISABLED)
        e_sugar.set('0')
def salt():
    if var8.get() == 1:
        textsalt.config(state=NORMAL)
        textsalt.focus()
        textsalt.delete(0, END)
    else:
        textsalt.config(state=DISABLED)
        e_salt.set('0')
def tomato():
    if var9.get() == 1:
        texttomato.config(state=NORMAL)
        texttomato.focus()
        texttomato.delete(0, END)
    else:
        texttomato.config(state=DISABLED)
        e_tomato.set('0')
def cocacola():
    if var10.get() == 1:
        textcocacola.config(state=NORMAL)
        textcocacola.focus()
        textcocacola.delete(0, END)
    else:
        textcocacola.config(state=DISABLED)
        e_cocacola.set('0')
def pepsi():
    if var11.get() == 1:
        textpepsi.config(state=NORMAL)
        textpepsi.focus()
        textpepsi.delete(0, END)
    else:
        textpepsi.config(state=DISABLED)
        e_pepsi.set('0')
def colddrinks():
    if var12.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.focus()
        textcolddrinks.delete(0, END)
    else:
        textcolddrinks.config(state=DISABLED)
        e_colddrinks.set('0')
def coffee():
    if var13.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')
def water():
    if var14.get() == 1:
        textwater.config(state=NORMAL)
        textwater.focus()
        textwater.delete(0, END)
    else:
        textwater.config(state=DISABLED)
        e_water.set('0')
def milk():
    if var15.get() == 1:
        textmilk.config(state=NORMAL)
        textmilk.focus()
        textmilk.delete(0, END)
    else:
        textmilk.config(state=DISABLED)
        e_milk.set('0')
def tea():
    if var16.get() == 1:
        texttea.config(state=NORMAL)
        texttea.focus()
        texttea.delete(0, END)
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')
def lemonade():
    if var17.get() == 1:
        textlemonade.config(state=NORMAL)
        textlemonade.focus()
        textlemonade.delete(0, END)
    else:
        textlemonade.config(state=DISABLED)
        e_lemonade.set('0')
def smoothie():
    if var18.get() == 1:
        textsmoothie.config(state=NORMAL)
        textsmoothie.focus()
        textsmoothie.delete(0, END)
    else:
        textsmoothie.config(state=DISABLED)
        e_smoothie.set('0')
def oreo():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')
def apple():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
        textapple.delete(0, END)
    else:
        textapple.config(state=DISABLED)
        e_apple.set('0')
def kitkat():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
        textkitkat.delete(0, END)
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')
def vanilla():
    if var22.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.focus()
        textvanilla.delete(0, END)
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')
def banana():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.focus()
        textbanana.delete(0, END)
    else:
        textbanana.config(state=DISABLED)
        e_banana.set('0')
def brownie():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()
        textbrownie.delete(0, END)
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')
def pineapple():
    if var25.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.focus()
        textpineapple.delete(0, END)
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')
def chocolate():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')
def blackforest():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')
root=Tk()
root.geometry('1270x690+0+0')
root.resizable(0,0)
root.title(' Online store created by Bahaeddine krifa')
root.config(bg='#3E32F8')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='#2B4FD9')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='*******************************Online Store*******************************',font=('arial',30,'bold'),fg='#FF1817',bd=9,
                 bg='#3694FF',width=51)
labelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='#3694FF')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='#3694FF',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='#39B3DB',)
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='#39B3DB')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='#39B3DB')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='#3694FF')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='#3694FF')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='#3694FF')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='#3694FF')
buttonFrame.pack()

#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_rice=StringVar()
e_meat=StringVar()
e_fish = StringVar()
e_chicken = StringVar()
e_egg = StringVar()
e_cheese = StringVar()
e_sugar = StringVar()
e_salt = StringVar()
e_tomato = StringVar()

e_cocacola=StringVar()
e_pepsi = StringVar()
e_colddrinks = StringVar()
e_coffee = StringVar()
e_water = StringVar()
e_milk = StringVar()
e_tea = StringVar()
e_lemonade = StringVar()
e_smoothie = StringVar()

e_oreo=StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicedeliveryvar=StringVar()
totalcostvar=StringVar()

e_rice.set('0')
e_meat.set('0')
e_fish.set('0')
e_chicken.set('0')
e_egg.set('0')
e_cheese.set('0')
e_sugar.set('0')
e_salt.set('0')
e_tomato.set('0')

e_cocacola.set('0')
e_pepsi.set('0')
e_colddrinks.set('0')
e_coffee.set('0')
e_water.set('0')
e_milk.set('0')
e_tea.set('0')
e_lemonade.set('0')
e_smoothie.set('0')

e_kitkat.set('0')
e_banana.set('0')
e_pineapple.set('0')
e_apple.set('0')
e_chocolate.set('0')
e_oreo.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_vanilla.set('0')

##FOOD

rice=Checkbutton(foodFrame,text='Rice',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,
                 command=rice)
rice.grid(row=0,column=0,sticky=W)

meat=Checkbutton(foodFrame,text='Meat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,
                 command=meat)
meat.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='Fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,
                 command=fish)
fish.grid(row=2,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,
                 command=chicken)
chicken.grid(row=3,column=0,sticky=W)

egg=Checkbutton(foodFrame,text='Egg',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,
                 command=egg)
egg.grid(row=4,column=0,sticky=W)

cheese=Checkbutton(foodFrame,text='Cheese',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,
                 command=cheese)
cheese.grid(row=5,column=0,sticky=W)

sugar=Checkbutton(foodFrame,text='Sugar',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,
                 command=sugar)
sugar.grid(row=6,column=0,sticky=W)

salt=Checkbutton(foodFrame,text='salt',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,
                 command=salt)
salt.grid(row=7,column=0,sticky=W)

tomato=Checkbutton(foodFrame,text='Tomato',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,
                 command=tomato)
tomato.grid(row=8,column=0,sticky=W)

#Entry Fields for Food Items

textrice=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rice)
textrice.grid(row=0,column=1)

textmeat=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_meat)
textmeat.grid(row=1,column=1)

textfish=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textchicken = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=3, column=1)

textegg = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_egg)
textegg.grid(row=4, column=1)

textcheese = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cheese)
textcheese.grid(row=5, column=1)

textsugar = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sugar)
textsugar.grid(row=6, column=1)

textsalt = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_salt)
textsalt.grid(row=7, column=1)

texttomato = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tomato)
texttomato.grid(row=8, column=1)

#Drinks

cocacola=Checkbutton(drinksFrame,text='Coca Cola',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,
                 command=cocacola)
cocacola.grid(row=0,column=0,sticky=W)

pepsi=Checkbutton(drinksFrame,text='Pepsi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,
                 command=pepsi)
pepsi.grid(row=1,column=0,sticky=W)

colddrinks=Checkbutton(drinksFrame,text='Cold drinks',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,
                 command=colddrinks)
colddrinks.grid(row=2,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,
                 command=coffee)
coffee.grid(row=3,column=0,sticky=W)

water=Checkbutton(drinksFrame,text='Water',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,
                 command=water)
water.grid(row=4,column=0,sticky=W)

milk=Checkbutton(drinksFrame,text='Milk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,
                 command=milk)
milk.grid(row=5,column=0,sticky=W)

tea=Checkbutton(drinksFrame,text='Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,
                 command=tea)
tea.grid(row=6,column=0,sticky=W)

lemonade=Checkbutton(drinksFrame,text='Lemonade',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,
                 command=lemonade)
lemonade.grid(row=7,column=0,sticky=W)

smoothie=Checkbutton(drinksFrame,text='Smoothie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,
                 command=smoothie)
smoothie.grid(row=8,column=0,sticky=W)

#entry fields for drink items

textcocacola = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cocacola)
textcocacola.grid(row=0, column=1)

textpepsi= Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pepsi)
textpepsi.grid(row=1, column=1)

textcolddrinks = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_colddrinks)
textcolddrinks.grid(row=2, column=1)

textcoffee  = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee )
textcoffee .grid(row=3, column=1)

textwater = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_water)
textwater.grid(row=4, column=1)

textmilk = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_milk)
textmilk.grid(row=5, column=1)

texttea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_tea)
texttea.grid(row=6, column=1)

textlemonade = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_lemonade)
textlemonade.grid(row=7, column=1)

textsmoothie = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_smoothie)
textsmoothie.grid(row=8, column=1)

#Cakes

oreocake=Checkbutton(cakesFrame,text='Oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,
                 command=oreo)
oreocake.grid(row=0,column=0,sticky=W)

applecake=Checkbutton(cakesFrame,text='Apple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,
                 command=apple)
applecake.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(cakesFrame,text='Kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,
                 command=kitkat)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,
                 command=vanilla)
vanillacake.grid(row=3,column=0,sticky=W)

bananacake=Checkbutton(cakesFrame,text='Banana',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,
                 command=banana)
bananacake.grid(row=4,column=0,sticky=W)

browniecake=Checkbutton(cakesFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,
                 command=brownie)
browniecake.grid(row=5,column=0,sticky=W)

pineapplecake=Checkbutton(cakesFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,
                 command=pineapple)
pineapplecake.grid(row=6,column=0,sticky=W)

chocolatecake=Checkbutton(cakesFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,
                 command=chocolate)
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(cakesFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,
                 command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)

#entry fields for cakes

textoreo = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=1)

textapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_apple)
textapple.grid(row=1, column=1)

textkitkat = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=2, column=1)

textvanilla = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanilla)
textvanilla.grid(row=3, column=1)

textbanana = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_banana)
textbanana.grid(row=4, column=1)

textbrownie = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=5, column=1)

textpineapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pineapple)
textpineapple.grid(row=6, column=1)

textchocolate = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=7, column=1)

textblackforest = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)

#costlabels & entry fields

labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='#3694FF',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='#3694FF',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='#3694FF',fg='white')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='#3694FF',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServicedelivery=Label(costFrame,text='Ser Delivery',font=('arial',16,'bold'),bg='#3694FF',fg='white')
labelServicedelivery.grid(row=1,column=2)

textServicedelivery=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicedeliveryvar)
textServicedelivery.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='#3694FF',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='#171380',bd=3,padx=5,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='#171380',bd=3,padx=5,
                     command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='#171380',bd=3,padx=5,
                command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='#171380',bd=3,padx=5,
                  command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='#171380',bd=3,padx=5,
                   command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator

operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=lambda:buttonClick('7')
               )
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=lambda:buttonClick('8')
               )
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=lambda:buttonClick('9')
               )
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=lambda:buttonClick('+')
                  )
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=lambda:buttonClick('4')
              )
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='#361380',bg='#FF7C5C',bd=6,width=6,
               command=lambda:buttonClick('5')
               )
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='#361380',bg='#FF7C5C',bd=6,width=6,
               command=lambda:buttonClick('6')
              )
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=lambda:buttonClick('-')
                  )
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=lambda:buttonClick('1')
              )
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='#361380',bg='#FF7C5C',bd=6,width=6,
               command=lambda:buttonClick('2')
            )
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='#361380',bg='#FF7C5C',bd=6,width=6,
               command=lambda:buttonClick('3')
               )
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=lambda:buttonClick('*')
               )
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='=',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='C',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=lambda:buttonClick('0')
               )
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='#FF5C3D',bg='#361380',bd=6,width=6,
               command=lambda:buttonClick('/')
                 )
buttonDiv.grid(row=4,column=3)


root.mainloop()
