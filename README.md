# Single_Cell_Sorter

create app using: 

``
 pyinstaller  --onefile --hidden-import='PIL._tkinter_finder' CellSorter.py
pyinstaller --onefile --hidden-import 'PIL._tkinter_finder' --hidden-import 'tkmacosx' CellSorter.py

``

