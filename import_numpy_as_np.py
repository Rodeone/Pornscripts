import numpy as np
import random as ran
import matplotlib.pyplot as plt

Limit = 1000
b = np.zeros(15)
mother_base = 150
Increment = 50
Base = mother_base 

def Random_ink(a):
    F = ran.uniform(-0.15,0.15)
    Z = a * (F + 1) 
    return Z

def Prediction_Line(Data,a,i):
    Line = np.zeros(15)
    for j in range(i):
        Line[j] = Data[j]
    while i <= 14:
        Line[i] = Line[i-1] + a 
        i = i+1
    return Line
Incb = Increment
Lines = []
for tik in range(15):
    Increment = Random_ink(Increment)
    b[tik] = Base + Increment
    if Increment > 1.2*Incb:
        Incb = Increment
    Lines.append(Prediction_Line(b,Incb,tik))
    Base = b[tik]


plt.plot(b,marker = 'x')
for i in range(len(Lines)):
    if np.max(Lines[i]) > Limit:
        print('Будь потише братишка')
    plt.plot(Lines[i],marker='p')
plt.show() 

