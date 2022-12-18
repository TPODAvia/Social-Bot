import subprocess, sys

def send_to_clipboard(path):
    #path = str("Facebook_API//Grass.mp4")
    path = str("Facebook_API//Screenshot.png")
    p = subprocess.Popen("powershell.exe -command \"Set-Clipboard -Path {0}\"".format(path), stdout=sys.stdout)
    p.communicate()