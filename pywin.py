from selenium import webdriver
from pywinauto import application
import time
from pywinauto.controls.win32_controls import ButtonWrapper
#import pyautogui
app=application.Application()
url="https://www.amazon.in/Sunfeast-Dark-Fantasy-Choco-Fills/dp/B01CHUSZJ8/ref=sr_1_1?srs=9574332031&ie=UTF8&qid=1537696125&sr=1-1"
app.start(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe https://www.amazon.in/Sunfeast-Dark-Fantasy-Choco-Fills/dp/B01CHUSZJ8/ref=sr_1_1?srs=9574332031&ie=UTF8&qid=1537696125&sr=1-1')
time.sleep(6)
app.mouse.click(coords=(274, 84))
#vbapp = app.window(title_re="MainWindow")
#vbButton1 = ButtonWrapper(vbapp.Button.wrapperobject("sell")).Click




#pyautogui.FAILSAFE = True

#app = Application().Start(cmd_line=u'"C:\\VBPrograms\\SimpleWPFApp.exe"')
#app.MainWindow.Wait('ready')
#vbapp = app.window_(title_re="MainWindow")
#vbButton1 = ButtonWrapper(vbapp.Button.WrapperObject("Start")).Click