python -m pip install subprocess
python -m pip install requests
python -m pip install os
python -m pip install shutil
python -m pip install rich
python -m pip install json
python -m pip install pyautogui
python -m pip install time
python -m pip install datetime
python -m pip install platform

cls
echo python omega.py >> start.bat
start start.bat
start /b "" cmd /c del "%~f0"&exit /b
