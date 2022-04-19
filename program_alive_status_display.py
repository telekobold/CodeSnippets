#!/usr/bin/python

"""
Sometimes, calculations take a few seconds or even minutes. This script shows 
how a simple "I'm still alive" indicator can be implemented in a separate thread 
printing some output to the console so that users don't type nervously on the 
console thinking the program has crashed.

"THE BEER-WARE LICENSE" (Revision 42):
Michael Merz <mail@telekobold.de> wrote this file. As long as you 
retain this notice you can do whatever you want with this stuff. If we meet 
some day, and you think this stuff is worth it, you can buy me a beer in 
return. telekobold.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
"""

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
        self.progrees_indicator()
    
    def progrees_indicator(self):
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
