# Web-Monitor
Turkish Gymnastics Federation course announcements tracking application

A simple website monitoring script. If the followed course comes to the list, 
a message is sent automatically with the registration link to the previously created telegram group.

## How to run monitoring app?

* First of all, download the repo and extract it to a location you want. For mac users open new terminal and for the windows users open new Command Prompt. Then open directory of the downloaded folder. Example:  

```bash
cd /Users/user/Desktop/Web-Monitor
```
* Next, run the web_monitor.py  
```bash
python web_monitor.py
```
Then app will start automatically and will check the course page in every 2 minutes. If desired course exist within the page, an automatic message will be sent to the telegram group.

## How to export monitoring app as .exe for windows?
If you are using windows instead of using the command line you may want to convert the application into .exe format and start using it with an only a double click. Again download the repo and extract it to a location you want and open directory folder with "cd /Users/user/Desktop/Web-Monitor" like in the previous example. As a next step just run the following command:

```bash
pyinstaller --onefile -w "web_monitor.py"
```
After that, a new file will be created under the name "dist" in the same file. In it you can find a ready-to-run program called web_monitor.exe. Just double click to run the application.

## How to setup telegram bot and the group for automated messages?

* first go the the telegram app and search for "@botfather":
<!-- ![botfather](./assets/botfather.png){ width=50% } -->

<p align="center">
<img src="./assets/botfather.png" width="350">
</p>

* Write "/newbot" to create new bot and choose a new name and also an user name for the new bot.


<p align="center">
<img src="./assets/newbot.png">
</p>


* After that store access token for the bot to able to send automated messages.

<p align="center">
<img src="./assets/token.png">
</p>

* Also invite the bot to the desired telegram group.