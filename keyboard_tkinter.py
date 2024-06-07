import tkinter
a = tkinter.Tk()
a.iconbitmap("myicon.ico")

a.title("SIKANDRA'S KEYBOARD")

def Button_click(alfabet):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, tkinter.END)
    e.insert(0, str(current) + str(alfabet))


def spacee(spaceee):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, tkinter.END)
    e.insert(0, str(current) + str(spaceee))



def backspacee():
     current = e.get()
     e.delete(0, tkinter.END)
     e.insert(0, current[:len(current)-1])


def caps():
    current=e.get()
    e.delete(0,tkinter.END)
    e.insert(0,str(current).lower)

    
    
         
    
    






current_bg=a.cget("bg")
new_bg="white" if current_bg =="black" else "black" 
a.configure(bg=new_bg)
    

# NUM
upper = tkinter.Button(text="~", background="black",foreground="white",font=("courier"), width=3,command=lambda:Button_click("~"))
num1 = tkinter.Button(text="1",  width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("1"))
num2 = tkinter.Button(text="2",  width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("2"))
num3 = tkinter.Button(text="3", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("3"))
num4 = tkinter.Button(text="4", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("4"))
num5 = tkinter.Button(text="5", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("5"))
num6 = tkinter.Button(text="6", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("6"))
num7 = tkinter.Button(text="7", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("7"))
num8 = tkinter.Button(text="8", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("8"))
num9 = tkinter.Button(text="9", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("9"))
num0 = tkinter.Button(text="0", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("0"))
minus= tkinter.Button(text="-", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("-"))
equal = tkinter.Button(text="=", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("="))
backspace=tkinter.Button(text="backspace", background="black",foreground="white",font=("courier"),width=10 ,command=lambda:backspacee())

# 1
tab = tkinter.Button(text="tab", width=3, background="black",foreground="white",font=("courier"))
Q = tkinter.Button(text="Q", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("Q"))
W = tkinter.Button(text="W", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("W"))
E = tkinter.Button(text="E", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("E"))
R = tkinter.Button(text="R", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("R"))
T = tkinter.Button(text="T", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("T"))
Y = tkinter.Button(text="Y", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("Y"))
U = tkinter.Button(text="U", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("U"))
I = tkinter.Button(text="I", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("I"))
O = tkinter.Button(text="O", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("O"))
P = tkinter.Button(text="P", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("P"))
openbracket=tkinter.Button(text="[",width=3 ,background="black",foreground="white",font=("courier"))
closebracket=tkinter.Button(text="]",width=3 ,background="black",foreground="white",font=("courier"))
slace=tkinter.Button(text="\ ",width=3 ,background="black",foreground="white",font=("courier"))

# 2
capslock = tkinter.Button(text="capslock", width=8, background="black",foreground="white",font=("courier") ,command=lambda:caps())
A = tkinter.Button(text="A", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("A"))
S = tkinter.Button(text="S", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("S"))
D = tkinter.Button(text="D", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("D"))
F = tkinter.Button(text="F", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("F"))
G = tkinter.Button(text="G", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("G"))
H = tkinter.Button(text="H", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("H"))
J = tkinter.Button(text="J", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("j"))
K = tkinter.Button(text="K", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("K"))
L = tkinter.Button(text="L", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("L"))
comaa= tkinter.Button(text=";", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click(";"))
comma= tkinter.Button(text="'", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("'"))
enter= tkinter.Button(text="enter", width=5, background="black",foreground="white",font=("courier") )

# 3
shift = tkinter.Button(text="shift", width=5, background="black",foreground="white",font=("courier"))
z = tkinter.Button(text="z", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("Z"))
X = tkinter.Button(text="X", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("X"))
C = tkinter.Button(text="C", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("C"))
V = tkinter.Button(text="V", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("V"))
B = tkinter.Button(text="B", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("B"))
N = tkinter.Button(text="N", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("N"))
M= tkinter.Button(text="M", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("M"))
comaaa= tkinter.Button(text=",", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click(","))
dot= tkinter.Button(text=".", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("."))
slace2= tkinter.Button(text="/", width=3, background="black",foreground="white",font=("courier"),command=lambda:Button_click("/"))
shift2= tkinter.Button(text="shift", width=5, background="black",foreground="white",font=("courier"))

# 4
ctrl = tkinter.Button(text="ctrl", width=3, background="black",foreground="white",font=("courier"))
fn = tkinter.Button(text="fn", width=2, background="black",foreground="white",font=("courier"))
window=tkinter.Button(text="win",width=3, background="black",foreground="white",font=("courier"))
alt = tkinter.Button(text="alt", width=3, background="black",foreground="white",font=("courier"))
space = tkinter.Button(text="space", width=19, background="black",foreground="white",font=("courier")  ,command=lambda:spacee(" "))  
alt2=tkinter.Button(text="alt",width=3, background="black",foreground="white",font=("courier"))
ctrl2=tkinter.Button(text="ctrl",width=3, background="black",foreground="white",font=("courier"))
sidearrow=tkinter.Button(text="<",width=3, background="black",foreground="white",font=("courier"))
uperarrow=tkinter.Button(text="Λ",width=3, background="black",foreground="white",font=("courier"))
sidearrow2=tkinter.Button(text=">",width=3, background="black",foreground="white",font=("courier"))


lowarrow=tkinter.Button(text="V",width=3, background="black",foreground="white",font=("courier"))






# Grid layout
upper.grid(row=0, column=0, padx=5, pady=2)
num1.grid(row=0, column=1, padx=10, pady=2)
num2.grid(row=0, column=2, padx=10, pady=2)
num3.grid(row=0, column=3, padx=10, pady=2)
num4.grid(row=0, column=4, padx=10, pady=2)
num5.grid(row=0, column=5, padx=10, pady=2)
num6.grid(row=0, column=6, padx=10, pady=2)
num7.grid(row=0, column=7, padx=10, pady=2)
num8.grid(row=0, column=8, padx=10, pady=2)
num9.grid(row=0, column=9, padx=10, pady=2)
num0.grid(row=0, column=10, padx=10, pady=2)
minus.grid(row=0, column=11, padx=10, pady=2)
equal.grid(row=0, column=12, padx=10, pady=2)
backspace.grid(row=0,column=13,padx=10,pady=2,columnspan=2)


tab.grid(row=1, column=0, padx=5, pady=2)
Q.grid(row=1, column=1, padx=10, pady=2)
W.grid(row=1, column=2, padx=10, pady=2)
E.grid(row=1, column=3, padx=10, pady=2)
R.grid(row=1, column=4, padx=10, pady=2)
T.grid(row=1, column=5, padx=10, pady=2)
Y.grid(row=1, column=6, padx=10, pady=2)
U.grid(row=1, column=7, padx=10, pady=2)
I.grid(row=1, column=8, padx=10, pady=2)
O.grid(row=1, column=9, padx=10, pady=2)
P.grid(row=1, column=10, padx=10, pady=2)
openbracket.grid(row=1, column=11, padx=10, pady=2)
closebracket.grid(row=1, column=12, padx=10, pady=2)
slace.grid(row=1, column=13, padx=10, pady=2)

capslock.grid(row=2, column=0, padx=5, pady=2)
A.grid(row=2, column=1, padx=10, pady=1)
S.grid(row=2, column=2, padx=10, pady=1)
D.grid(row=2, column=3, padx=10, pady=1)
F.grid(row=2, column=4, padx=10, pady=1)
G.grid(row=2, column=5, padx=10, pady=1)
H.grid(row=2, column=6, padx=10, pady=1)
J.grid(row=2, column=7, padx=10, pady=1)
K.grid(row=2, column=8, padx=10, pady=1)
L.grid(row=2, column=9, padx=10, pady=1)
comaa.grid(row=2, column=10, padx=10, pady=1)
comma.grid(row=2, column=11, padx=10, pady=1)
enter.grid(row=2, column=12, padx=10, pady=1)

shift.grid(row=3, column=0, padx=10, pady=1)
z.grid(row=3, column=1, padx=10, pady=1)
X.grid(row=3, column=2, padx=10, pady=1)
C.grid(row=3, column=3, padx=10, pady=1)
V.grid(row=3, column=4, padx=10, pady=1)
B.grid(row=3, column=5, padx=10, pady=1)
N.grid(row=3, column=6, padx=10, pady=1)
M.grid(row=3, column=7, padx=10, pady=1)
comaaa.grid(row=3, column=8, padx=10, pady=1)
dot.grid(row=3, column=9, padx=10, pady=1)
slace2.grid(row=3, column=10, padx=10, pady=1)
shift2.grid(row=3, column=11, padx=10, pady=1)


ctrl.grid(row=5, column=0, padx=10, pady=1)
fn.grid(row=5, column=1, padx=10, pady=1)
window.grid(row=5,column=2,padx=10,pady=1)
alt.grid(row=5, column=3, padx=10, pady=1)
space.grid(row=5, column=4, columnspan=3, padx=10, pady=1)
alt2.grid(row=5, column=7, padx=10, pady=1)
ctrl2.grid(row=5, column=8,  padx=10, pady=1)
sidearrow.grid(row=5, column=9,  padx=10, pady=1)
uperarrow.grid(row=5, column=10,  padx=10, pady=1)
sidearrow2.grid(row=5, column=11,  padx=10, pady=1)
lowarrow.grid(row=6, column=10,  padx=10, pady=1)




e = tkinter.Entry( width=70, border=7,background="black",foreground="white",font=("courier"))
e.grid(row=9, column=1,rowspan=10, columnspan=10,padx=20,pady=1,ipady=30)
a.mainloop()