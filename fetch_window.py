import win32gui,win32con
from PIL import ImageGrab
def get_window_pos(name):
    name = name
    handle = win32gui.FindWindow(0, name)
    if handle == 0:
        return None
    else:
        return win32gui.GetWindowRect(handle), handle


def fetch_image():
    (x1, y1, x2, y2), handle = get_window_pos('video_cap')
    win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND,
                         win32con.SC_RESTORE, 0)
    win32gui.SetForegroundWindow(handle)
    grab_image = ImageGrab.grab((x1, y1, x2, y2))

    return grab_image
