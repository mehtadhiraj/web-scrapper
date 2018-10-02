import time
import schedule
print('THE SCRAPING WILL START IN THE SCHEDULED TIME')
import os
def job():
    exec(compile(source=open('main_program.py').read(), filename='main_program.py', mode='exec'))

schedule.every().day.at("9:05").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)