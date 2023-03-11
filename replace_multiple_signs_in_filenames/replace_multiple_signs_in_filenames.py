"""
I wanted to read some DMARC reports on a secure system, but unfortunately, the
.eml files exported by Thunderbird contain many special characters not
supported by the file system of the USB stick I wanted to export to. So I
wrote this small script which replaces each of those special characters in the
file names either by the empty character or by a special ASCII string.

I'm quite sure there is a beautiful, equivalent, one-line solution for this 
which uses list comprehensions.
"""

import os

path = os.getcwd()
filenames = os.listdir(path)
chars_replace_by_space =  ['{', '}', ':', '<', '>', '\"']
chars_with_replacement = {'@': "_at_"}
for filename in filenames:
    new_name = filename
    new_name_prev = filename
    for c in chars_replace_by_space:
        new_name_prev = new_name
        new_name = new_name.replace(c, "")
        os.rename(new_name_prev, new_name)
    for c in chars_with_replacement:
        new_name_prev = new_name
        new_name = new_name.replace(c, chars_with_replacement.get(c))
        os.rename(new_name_prev, new_name)

