#!/usr/bin/python
import schedule 
import time 

def job():
	print ("This is a test for every second")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)