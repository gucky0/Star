# from io 
# from win32com.client import Dispatch

# import os, winshell
# desktop = winshell.desktop()
# path = os.path.join(desktop, "myNeatWebsite.url")
# target = "http://www.google.com/"
# shortcut = io.file(path, 'w')
# shortcut.write('[InternetShortcut]\n')
# shortcut.write('URL=%s' % target)
# shortcut.close()

# def createShortcut(path, target='', wDir='', icon=''):    
#     ext = path[-3:]
#     if ext == 'url':
#         shortcut = file(path, 'w')
#         shortcut.write('[InternetShortcut]\n')
#         shortcut.write('URL=%s' % target)
#         shortcut.close()
#     else:
#         shell = Dispatch('WScript.Shell')
#         shortcut = shell.CreateShortCut(path)
#         shortcut.Targetpath = target
#         shortcut.WorkingDirectory = wDir
#         if icon == '':
#             pass
#         else:
#             shortcut.IconLocation = icon
#         shortcut.save()
from pathlib import Path
import win32com.client, os, getpass

target = str(Path("C:\\Users\hariiz\AppData\Local\Programs\Python\Python39\Scripts\MyPython\dist\hello.exe"))
dest = str(Path("C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"))
username = str(getpass.getuser())
# pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.

path = os.path.join(dest, '\\NameOfShortcut.lnk')
# target = r'C:\path\to\target\file.exe'
# icon = r'C:\path\to\icon\resource.ico' # not needed, but nice

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
# shortcut.IconLocation = icon
shortcut.WindowStyle = 7 # 7 - Minimized, 3 - Maximized, 1 - Normal
# shortcut.save()
