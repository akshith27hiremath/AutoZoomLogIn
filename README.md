# AUTO ZOOM LOGIN


# If cloning for testing purposes, clone the repository and skip to step 9 (very important one step process).

### Description 
I developed this script at the start of online classes because I found manually searching up the Meeting ID number and password in the timetable pdf, then copying both into zoom, to be time consuming. This script requires some initial setup, but then shortens the login process from the 30+ seconds hassle of finding the ID/pwd and multiple uneccessary keystrokes to an instantaneous process from there on out.

#### A sample timetable.json file has been included in the repository for ease of testing, the html file generates a new timetable.json file for the user's timetable which can replace the current timetable.json file

<br>

### Features
<br><b>Converts</b> your timetable into a JSON file using JavaScript<br><b>Reads</b> current system time and day using datetime library,<br><b>retrieves</b> the correct Meeting ID and password using the json library, <br><b>opens</b> Zoom in a browser which triggers it to be opened in the system using webbrowser library, <br><b>Brings</b> the zoom window to the front using pygetwindow, <br><b>pastes</b> the correct password into the dialog box using pyperclip and pygetwindow, logging you into your meeting without you having to lift a finger.

<br>

### Tools used
HTML/Semantic UI, JavaScript, Python

### BONUS: 
A side benefit of using an .exe file instead of a .py file is you can assign it to a keyboard shortcut in windows (I used alt+shift+z) to shorten the entire instaneneous process from clicking a file to a single keystroke.

# SETUP

### 1. Clone the repository

`git clone https://github.com/akshith27hiremath/AutoZoomLogIn.git` <br>

### 2. Install Zoom, and keep Zoom minimized in your app drawer

### 3. Open createtimetable.html

Open file explorer and click on the html file (it should open in your browser) <br>

### 4. Upload timetable

Follow the alerts instructions to create a dynamic and personalized timetable upload table. <br>
For example, for a BITS timetable you would type 9, 5, Monday/Tuesday/Wednesday/Thursday/Friday<br>

### 5. Enter time slots

In the upper white table, enter the time slots. (eg. Period 1 would be 8:00 - 9:00, Period 2 would be 9:00 - 10:00 etc.) <br>

### 6. Enter respective Meeting IDs and passwords

### 7. CLICK Submit Timetable (pressing enter will not trigger the JS function)

### 8. Copy the timetable.json file that just downloaded from your DOWNLOADS folder to the directory of the app.exe file.

### 9. <B> IMPORTANT </B> SINGLE ONBOARDING STEP

Click app.exe when you have a meeting, and upon the browser trigger alert "automatically open links from zoom", CHECK the box. this will automate the entire process from front to back for every time in the future <br>

### 10. You're done! click app.exe whenever you're 10 minutes within a time slot or inside the time slot and you'll automatically enter your meeting!