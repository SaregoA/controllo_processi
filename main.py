from guizero import App,Box,Text,TextBox,PushButton
import subprocess
import psutil
import telegram_send
import pyautogui


def nomeprocesso():
    return input_box.value

def nomepid():
    return input_box2.value

def secondi():
    return input_box3.value

def controllo():
    seconds = int(secondi())
    sec = seconds * 1000
    button.repeat(sec,controllo2)

def controllo2():
    nomeproc = nomeprocesso()
    numpid = int(nomepid())
    a = 0
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info['name'] == nomeproc:
            if proc.info['pid'] == numpid:
                a = 1
                pass
    if a == 0:
        print('il programma si e  chiuso')
        telegram_send.send(messages=['il programma si e chiuso'])
        im = pyautogui.screenshot('py.png')
        subprocess.run(["telegram-send", "--image", "py.png","--caption", "ScreenShot"])
        button.cancel(controllo2)

def ferma():
    button.cancel(controllo2)
    print('fermato')


def main():
    global button
    global input_box,input_box2,input_box3
    app = App(layout='grid',title="Controllo Processi",width=380, height=160)
    box = Box(app, border=True,grid=[0,0])
    box2 = Box(app, border=True, grid=[0, 1])
    box3 = Box(app, border=True, grid=[0, 2])
    testo1 = Text(box, text="Nome Processo", size=14, font="Arial")
    testo2 = Text(box2, text="Pid Processo", size=14, font="Arial")
    testo3 = Text(box3, text="Ogni quanti secondi", size=14, font="Arial")
    input_box = TextBox(app,grid=[1,0],width=20)
    input_box2 = TextBox(app,grid=[1,1],width=20)
    input_box3 = TextBox(app,grid=[1,2])
    button = PushButton(app, text='Avvia',command=controllo,grid=[0,3])
    button2 = PushButton(app,command=ferma,text='Ferma',grid=[3,3])
    app.display()


if __name__ == "__main__":
    main()

