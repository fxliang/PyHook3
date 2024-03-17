import pythoncom
import PyHook3 as pyhook

def on_kb_event(event):
    down =  [ 'key down' , 'key up  '][ event.MessageName == 'key up' ]
    print(f"{down} -> key: {event.Key}, ascii: {chr(event.Ascii)}, key.flags: {event.Mod}")
    return True

hm = pyhook.HookManager()
hm.KeyDown = on_kb_event
hm.KeyUp = on_kb_event

hm.HookKeyboard()
pythoncom.PumpMessages()
