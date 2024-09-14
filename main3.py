import datetime
import webbrowser
import sys
import pyperclip
import json

time = datetime.datetime.now()
hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
day = time.strftime("%A")
if minute < 10:
    minute = str(minute)
    minute = "0"+minute

currenttime = int(str(hour)+str(minute))
currentday = 0

if day == "Monday":
    currentday = 1
elif day == "Tuesday":
    currentday = 2
elif day == "Wednesday":
    currentday = 3
elif day == "Thursday":
    currentday = 4
elif day == "Friday":
    currentday = 5
elif day == 'Saturday':
    currentday = 6
elif day == 'Sunday':
    currentday = 7

with open('./timetable.json') as d:
  data = json.load(d)

n_of_periods = len(data['timedivisions'])

timedivisions = data['timedivisions']

period_timings = []

for time in timedivisions:
    period_timings.append(timedivisions[time])

def find_period(period_timings, current_time):
    x = 0
    for time_ in period_timings:
        if current_time >= time_[0] and current_time < time_[1]:
            return x
        x += 1
current_period_number = find_period(period_timings, currenttime)
period_schedule = data['meetingids']
req_part = period_schedule[str(currentday)]
current_period_number = find_period(period_timings, currenttime)
current_period = req_part[current_period_number]
meeting_id = current_period[1]
password = current_period[2]
url = "https://zoom.us/j/"+meeting_id
webbrowser.open(url, new=0, autoraise=True)
pyperclip.copy(password)
import time
import string
import ctypes.wintypes

# part one: clipboard text retrieval
CF_UNICODETEXT = 13  # unicode text format; terminates with a linefeed

OpenClipboard = ctypes.windll.user32.OpenClipboard
OpenClipboard.argtypes = ctypes.wintypes.HWND,
OpenClipboard.restype = ctypes.wintypes.BOOL

GetClipboardData = ctypes.windll.user32.GetClipboardData
GetClipboardData.argtypes = ctypes.wintypes.UINT,
GetClipboardData.restype = ctypes.wintypes.HANDLE

GlobalLock = ctypes.windll.kernel32.GlobalLock
GlobalLock.argtypes = ctypes.wintypes.HGLOBAL,
GlobalLock.restype = ctypes.wintypes.LPVOID

GlobalUnlock = ctypes.windll.kernel32.GlobalUnlock
GlobalUnlock.argtypes = ctypes.wintypes.HGLOBAL,
GlobalUnlock.restype = ctypes.wintypes.BOOL

CloseClipboard = ctypes.windll.user32.CloseClipboard
CloseClipboard.argtypes = None
CloseClipboard.restype = ctypes.wintypes.BOOL


def get_clipboard_text():
    text = ""
    if OpenClipboard(None):
        h_clip_mem = GetClipboardData(CF_UNICODETEXT)
        text = ctypes.wstring_at(GlobalLock(h_clip_mem))
        GlobalUnlock(h_clip_mem)
        CloseClipboard()
    return text


CB_TEXT = get_clipboard_text()

# part two: typing it into the focused element of a window

LONG = ctypes.c_long
DWORD = ctypes.c_ulong
ULONG_PTR = ctypes.POINTER(DWORD)
WORD = ctypes.c_ushort

VK_SHIFT = 0x10  # Shift key
# special keys
VK_OEM_1 = 0xBA
VK_OEM_PLUS = 0xBB
VK_OEM_COMMA = 0xBC
VK_OEM_MINUS = 0xBD
VK_OEM_PERIOD = 0xBE
VK_OEM_2 = 0xBF
VK_OEM_3 = 0xC0
VK_OEM_4 = 0xDB
VK_OEM_5 = 0xDC
VK_OEM_6 = 0xDD
VK_OEM_7 = 0xDE
KEYEVENTF_KEYUP = 0x0002  # Releases the key
INPUT_KEYBOARD = 1


UPPER = frozenset('~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?')
LOWER = frozenset("`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./")
ORDER = string.ascii_letters + string.digits + ' \b\r\t'
ALTER = dict(zip('!@#$%^&*()', '1234567890'))
OTHER = {
    '`': VK_OEM_3, '~': VK_OEM_3, '-': VK_OEM_MINUS, '_': VK_OEM_MINUS,
    '=': VK_OEM_PLUS, '+': VK_OEM_PLUS, '[': VK_OEM_4, '{': VK_OEM_4,
    ']': VK_OEM_6, '}': VK_OEM_6, '\\': VK_OEM_5, '|': VK_OEM_5,
    ';': VK_OEM_1, ':': VK_OEM_1, "'": VK_OEM_7, '"': VK_OEM_7,
    ',': VK_OEM_COMMA, '<': VK_OEM_COMMA, '.': VK_OEM_PERIOD,
    '>': VK_OEM_PERIOD, '/': VK_OEM_2, '?': VK_OEM_2
}


class KEYBDINPUT(ctypes.Structure):
    _fields_ = (
        ('wVk', WORD),
        ('wScan', WORD),
        ('dwFlags', DWORD),
        ('time', DWORD),
        ('dwExtraInfo', ULONG_PTR)
    )


class INPUT(ctypes.Structure):
    _fields_ = ('type', DWORD), ('ki', KEYBDINPUT), ('pad', ctypes.c_ubyte * 8)


def Input(structure):
    return INPUT(INPUT_KEYBOARD, structure)


def KeyboardInput(code, flags):
    return KEYBDINPUT(code, code, flags, 0, None)


def Keyboard(code, flags=0):
    return Input(KeyboardInput(code, flags))


def SendInput(*inputs):
    nInputs = len(inputs)
    LPINPUT = INPUT * nInputs
    pInputs = LPINPUT(*inputs)
    cbSize = ctypes.c_int(ctypes.sizeof(INPUT))
    return ctypes.windll.user32.SendInput(nInputs, pInputs, cbSize)


def stream(string):
    mode = False
    for character in string.replace('\r\n', '\r').replace('\n', '\r'):
        if mode and character in LOWER or not mode and character in UPPER:
            yield Keyboard(VK_SHIFT, mode and KEYEVENTF_KEYUP)
            mode = not mode
        character = ALTER.get(character, character)
        if character in ORDER:
            code = ord(character.upper())
        elif character in OTHER:
            code = OTHER[character]
        else:
            continue
            raise ValueError('Undecoded')
        yield Keyboard(code)
        yield Keyboard(code, KEYEVENTF_KEYUP)
    if mode:
        yield Keyboard(VK_SHIFT, KEYEVENTF_KEYUP)


def send_clipboard():
    for k in stream(CB_TEXT + '\r'):
        SendInput(k)


def demo(wait=3):
    time.sleep(wait)
    send_clipboard()

import pygetwindow as gw
isThere = False
done = False
while not done:
    try:
        gw.getWindowsWithTitle('Zoom')[1]
        isThere = True
    except Exception:
        pass

    if isThere:
        demo()
        break