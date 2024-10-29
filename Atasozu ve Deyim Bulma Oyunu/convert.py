import os
from PyQt5 import uic

def convert_ui_to_py(directory):
    for filename in os.listdir(directory):  
        if filename.endswith(".ui"):
            ui_file = os.path.join(directory, filename)
            py_file = os.path.join(directory, f"{os.path.splitext(filename)[0]}UI.py")
            with open(py_file, "w", encoding="utf-8") as fout:
                uic.compileUi(ui_file, fout)
            print(f"Converted {ui_file} to {py_file}")

directory = "C:/Users/defne/OneDrive/Masaüstü/kelime_bulma"
convert_ui_to_py(directory)
