# JS Recon
This is a tool to help infultrators with reconnaissance to web targets. Organize large sets of production code from a target by date & target.

Helpful Prod Recon features:
 - Helps you to discover files within other js files
 - Download production code
 - Organize JS files from by date & target
 - Lets you beautify target js files for easy reading.

It should soon allow you to compare older versions of the source code with newer ones to see changes that were pushed.

## Usage
 1. Create a new folder with the targets name in the "targets" folder.
 2. Download the JS file you want to scan and place it in the folder you just created.
 3. modify the TARGET variable in the "jsRecon.py" file to match the folder name of the target.
 4. run:
 ``` 
 python ./jsRecon.py
 ```