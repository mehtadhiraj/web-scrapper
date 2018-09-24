import pyautogui as pg
from pywinauto.application import Application as Ap
from time import sleep
import os

if os.path.isfile("C:/Users/ithod/Documents/hello.txt"):
    os.remove("C:/Users/ithod/Documents/hello.txt")
    
app =  Ap().start("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe --force-renderer-accessibility --start-maximized https://terragalleria.com/")
sleep(20)
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