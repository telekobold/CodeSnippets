#!/usr/bin/python

import threading
import time


def progress_indicator(some_string, time_interval):
    print(f"The calculation of {some_string} is in progress, please wait..", end="", flush=True)
    while(True):
        print(".", end="", flush=True)
        time.sleep(time_interval)

        
def something_else():
    # Add some useful code here
    time.sleep(10)
    print("\nCalculation finished!")

    
if __name__ == "__main__":
    thread_1 = threading.Thread(target = something_else)
    thread_2 = threading.Thread(target = progress_indicator, args=("something", 1))
    thread_2.setDaemon(True)
    thread_1.start()
    thread_2.start()
