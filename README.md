# AUTO ZOOM LOGIN

Description: I developed this script at the start of online classes because I found manually searching up the Meeting ID number and password in the timetable pdf, then copying both into zoom, to be time consuming. This script requires some initial setup and then shortens the login process from 30+ seconds and multiple keystrokes to an instantaneous process.

<br>

Features: <b>Reads</b> system time and compares it to a json timetable file, <b>retrieves</b> the correct Meeting ID and password, <b>opens</b> Zoom in a browser which triggers it to be opened in the system, <b>pastes</b> in the correct password automatically, lgoging you into your meeting without you having to lift a finger.

<br>

I converted the python file into an exe for portability onto other systems, but assigning a KEYBOARD SHORTCUT to a .bat file that opens 

# SETUP

1. Clone the repository

`git clone https://github.com/akshith27hiremath/AutoZoomLogIn.git` <br>

2. Install Zoom, and keep Zoom minimized in your app drawer

2. Open createtimetable.html

Open file explorer and click on the html file (it should open in your browser) <br>

3. Upload timetable

Follow the alerts instructions to create a dynamic and personalized timetable upload table. <br>
For example, for a BITS timetable you would type 9, 5, Monday/Tuesday/Wednesday/Thursday/Friday<br>

4. Enter time slots

In the upper white table, enter the time slots. (eg. Period 1 would be 8:00 - 9:00, Period 2 would be 9:00 - 10:00 etc.) <br>

5. Enter respective Meeting IDs and passwords

6. CLICK Submit Timetable (pressing enter will not trigger the JS function)

7. Copy the timetable.json file that just downloaded from your DOWNLOADS folder to the directory of the app.exe file.

8. <B> IMPORTANT </B> SINGLE ONBOARDING STEP

Click app.exe when you have a meeting, and upon the browser trigger alert "automatically open links from zoom", CHECK the box. this will automate the entire process from front to back for every time in the future <br>

9. You're done! click app.exe whenever you're 10 minutes within a time slot or inside the time slot and you'll automatically enter your meeting!