import urllib.request
import requests
import time

currentVersion = "1.0.0"
URL = urllib.request.urlopen('https://github.com/arkantuka/Thesis-Project/tree/main/datasets/data')

data = URL.read()
if (data == currentVersion):
    print("App is up to date!")
else:
    print("App is not up to date! App is on version " + currentVersion + " but could be on version " + data + "!")
    print("Downloading new version now!")
    newVersion = requests.get("https://github.com/yourapp/app-"+data+".exe")
    open("app.exe", "wb").write(newVersion.content)
    print("New version downloaded, restarting in 5 seconds!")
    time.sleep(5)
    quit()