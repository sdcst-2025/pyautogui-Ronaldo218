#!working with time

import random
import keybord




import time

"""
Task 1
Basic Assignment:
Create a program to display 10 characters on screen, one at a time,
to the user.  They have to press that key to advance to the next character.
Tell the user how long it took them to press all 10 characters.

Alternately, you can select a random word from a list of words that you provide.
Have the user type in the word before the next word is selected.  This version
is easier because you can use the existing input() command that you are more
familiar with.

Your assignment should make appropriate use of functions to break the
code up into more manageable sections.  

Your assignment will be graded on the following criteria:

functionality (does it work the way it is intended)
modularity (is it broken up into functions to make your main block momre readable)
appropriate use of return values and input parameters

"""

# The code shown below is one way to read a single 
# keystroke from the keyboard and store it into 
# a variable. We will use it as the basis for this 
# assignment.

while True:
    y = keyboard.read_key()
    print(y)
    print(time.now())
    t = time.localtime()
    print(t)
    print(time.strftime("%H",t))

    break

hellow  = input("type your name: ")
print( world) - #izehpyinstaller
# Example: Using PyInstaller to Create an Executable

# Step 1: Install PyInstaller
# Open your terminal or command prompt and run:
# pip install pyinstaller

# Step 2: Create a simple Python script (example_script.py)
print("Hello, World!")
input("Press Enter to exit!")

# Step 3: Use PyInstaller to create an executable
# In your terminal or command prompt, navigate to the directory containing example_script.py and run:
# pyinstaller --onefile --windowed --icon=path/to/icon.ico example_script.py
""" pyinstaller --onefile example_script.py """

# This will generate a 'dist' folder containing the executable file.

# Step 4: Running the Executable
# Navigate to the 'dist' folder and run the executable file:
# On Windows:
# dist\example_script.exe
# On macOS/Linux:
# ./dist/example_script

# Step 5: Customizing the Executable
# You can customize the executable by adding more options to the PyInstaller command.
# For more options and customization, refer to the PyInstaller documentation:
# https://pyinstaller.readthedocs.io/en/stable/usage.html
# Step 6: Debugging and Troubleshooting
# If you encounter any issues, refer to the PyInstaller documentation or seek help from the community forums.
# https://github.com/pyinstaller/pyinstaller/issues
