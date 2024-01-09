AUTHOR: KALYAN PATEL
INITIAL PROJECT INSPIRATION: https://github.com/mukundmadhav/declutter-downloads-folder-script/tree/main


_automatic-downloads-sorter.py_ continuously checks the downloads folder for new files/folders, then sorts them based on extension (e.g. .pdf, .jpeg, .zip).

- The script makes use of the "os" library to navigate directories, and the "shutil" library to move files around.
- run_sorter() contains the main logic, reading each file's extensions and moving them into the appropriate folder based on the filetype_map.
- A while loop runs indefinitely and checks the number of contents in the downloads folder every 20 seconds. When new files are added, run_sorter() is called.



**CONFIGURING THE PROGRAM TO RUN AUTOMATICALLY IN WINDOWS**
The Windows task scheduler can be used to start the program upon login so that the entire process is automated.

First create a task and give it a name.
Under the "Triggers" tab, set the program to run "At log on"
Under the "Actions" tab, configure the following
- Program/Script:   [PATH TO YOUR PYTHON.EXE]     -->    (This path can be found by typing "where python" into your Windows command prompt)
- Add arguments:    _automatic-downloads-sorter.py_
- Start in:         [PATH TO automatic-downloads-sorter.py]

