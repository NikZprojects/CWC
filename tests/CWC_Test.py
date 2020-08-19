import os
import webbrowser
import subprocess
from threading import Thread

# Open CWC new incognito window (ensures fresh load)
def chrome():
    url = 'http://localhost:5000'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open(url)

# Open localhost server running CWC website
def localhost():
    python_venv = os.path.abspath('../venv/Scripts/python.exe')
    CWC_main = os.path.abspath('../main.py')
    subprocess.Popen([python_venv, CWC_main])

# Run both of these simultaneously:
if __name__ == '__main__':
    Thread(target=localhost).start()
    Thread(target=chrome).start()
