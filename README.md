# Single_Cell_Sorter

create app using:

``
 pyinstaller  --onefile --hidden-import='PIL._tkinter_finder' CellSorter.py
``

conda create --name env_sorter python=3.10
conda activate env_sorter
pip install -r requirements.txt
pip3 install pyinstaller

python example_data.py (kaggle)
<https://www.cancerimagingarchive.net/collection/bone-marrow-cytomorphology_mll_helmholtz_fraunhofer/>
cd /Users/lwenderoth/Documents/Single_Cell_Sorter/dist  
cd dist
./CellSorter

pyinstaller --onefile --hidden-import='PIL._tkinter_finder' --windowed --icon=icon.ico ClickCell.py
