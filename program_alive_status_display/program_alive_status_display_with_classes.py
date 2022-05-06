#!/usr/bin/python

import threading
import time


class ProgramAliveStatusDisplay(threading.Thread):
    """
    This class provides a small progress indicator showing the user an initial
    message an printing a "." every second thereafter to show that the program
    is currently performing a calculation.
    
    Usage:
    <Initialize other Thread(s)>
    program_alive_status_display = ProgramAliveStatusDisplay()
    program_alive_status_display.setDaemon(True)
    <start other Thread(s)>
    program_alive_status_display.start()
    """

    def __init__(self, some_string, time_interval=1):
        """
        Constructor.
        
        :some_string:   A string to show in the initial message.
        :time_interval: optional; default value `1`; must be of type `int.` 
                        Determines how often a "." should be printed, in seconds.
        """
        self.some_string = some_string
        self.time_interval = time_interval
        threading.Thread.__init__(self)
        
    def run(self):
        self.progress_indicator()
    
    def progress_indicator(self):
        print(f"The calculation of {self.some_string} is in progress, please wait..", end="", flush=True)
        while(True):
            print(".", end="", flush=True)
            time.sleep(self.time_interval)


class SomethingElse(threading.Thread):
    
    def __init__(self, some_string=""):
        threading.Thread.__init__(self)
    
    def run(self):
        self.do_something()
            
    def do_something(self):
        # Add some useful code here
        time.sleep(10)
        print("\nCalculation finished!")


if __name__ == "__main__":
    something_else = SomethingElse()
    program_alive_status_display = ProgramAliveStatusDisplay("something")
    # Automatically terminate `program_alive_status_display` if the other
    # thread(s) are terminated:
    program_alive_status_display.setDaemon(True)
    something_else.start()
    program_alive_status_display.start()
