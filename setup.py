import cx_Freeze

import os
os.environ['TCL_LIBRARY'] = r'C:\Users\Meet\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Meet\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

executables = [
        #                   name of your game script
        cx_Freeze.Executable("pyGameTutorial.py") 
] 
cx_Freeze.setup( 
        name = "Slither", 
        options = {"build_exe": {"packages":["pygame"],"include_files":["apple.png","snakehead.png"]}},
        description = "Slither game tutorial", 
        executables = executables)
