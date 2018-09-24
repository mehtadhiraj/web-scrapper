'''import pyautogui as pg
from pywinauto.application import Application as Ap
from time import sleep
import os
 
if os.path.isfile("C:/Users/ithod/Documents/hello.txt"):
    os.remove("C:/Users/ithod/Documents/hello.txt")
     
app =  Ap().start("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe --force-renderer-accessibility --start-maximized https://www.bigbasket.com/pd/10000170/fresho-cabbage-red-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop")
sleep(4)
pg.hotkey('ctrl', 'a')
pg.hotkey('ctrl', 'c')
sleep(3)
app1 = Ap().start('notepad.exe')
sleep(3)
pg.hotkey('ctrl','v')
win = app1.UntitledNotepad
sleep(2)
win.menu_select("File->Save")
pg.typewrite("hello")
pg.press('enter')
sleep(2)
win = app1.helloNotepad
win.menu_select("File->Exit")
pg.hotkey('alt','tab')
f = open("C:/Users/ithod/Documents/hello.txt",'r')
a = f.readlines()
for i in range(len(a)):
    if 'Inclusive of all taxes' in a[i]:
        k=i
        break
for j in range(k-8,k+2):
    print(a[j])
        
     '''
class Analyser():
    def __init__(self):
        self.a  = ' hello'
        #self.tyru()
    def pqr(self,i):
        self.a = 'google.com/' + str(i)
        print(self.a)
        #self.tyru()
    def tyru(self):
        self.a += 'por'
        print(self.a)
if __name__ == '__main__':

    for i in range (5):
        Analyser().pqr(i)
    