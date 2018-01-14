import speech_recognition as sr
import webbrowser as wb

#debser@author

def shutdown(self):
    import subprocess
    subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
def restart(self):
    import subprocess
    subprocess.call(["Restarting system", "-f", "-r", "-t", "60"])
def logout(self):
    import subprocess
    subprocess.call(["Logging Out User", "-f","-l","-t","60"])
def abort(self):
    import subprocess
    subprocess.call(["Aborting Shutdown", "-f","-a","-t","60"])
def player(self):
    import subprocess
    PLAYERPATH = "C:/Program Files (x86)/VideoLAN/VLC/vlc.exe"
    print("Player")
    FILEPATH = "C:\Program Files (x86)/forever.mp3"
    subprocess.call([PLAYERPATH, FILEPATH])
chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
r = sr.Recognizer()
with sr.Microphone() as source:


    audio = r.listen(source)
    user = r.recognize_google(audio)

if user=='shutdown':
    shutdown(1)
elif user=='restart':
     restart(1)
elif user=='log out':
    logout(1)
elif user=='abort':
    abort(1)
elif user=="player":
    player(1)
else:
    '''if(user[0:3]=="open"):
        user=user[3:]
    '''

    if(user[-4:0]!=".com"):
        user="www.google.co.in/search?q=" + user
    try:
        print("Command is " + user)
        wb.get(chrome_path).open(user)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
