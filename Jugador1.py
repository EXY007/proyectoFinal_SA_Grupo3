
import socket
import threading
import tablero as gb

from tkinter import *
from tkinter import messagebox

serverAddress = socket.gethostname()
#serverAddress = '127.0.0.1'
port = 4444


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverAddress,port))
serverSocket.listen(1)


clientSocket,clientAddress = None,None

start = False
user = False
player2 = ""
board = None
pos = 0
finish = False


def createThread(con):
    thread = threading.Thread(target=con)
    thread.daemon = True
    thread.start()

def receive():
    global start,user,player2,board
    while True:     
        if start and not user:
            try:
                data,addr = clientSocket.recvfrom(1024)
                name = data.decode()
                print(data)
                board = gb.Board(name)
                player2 = name
                sendData = '{}'.format("player1").encode()
                clientSocket.send(sendData)
                user = True
            except:
                pass
            

def receiveMove():
    global pos,start
    while True:
        if start and user:
            try:
                data,addr = clientSocket.recvfrom(1024)
                data = data.decode()
                print(data)
                if data == "Play Again":
                    reset()
                elif data == "Fun Times":
                    gameOver()
                else:
                    pos,board.lastMove = data.split("-")
                    board.playMoveOnBoard(int(pos),board.lastMove)
                    updateBoard()
                    lblTurn["text"] = "Tu turno"
                    play()
            except:
                pass



def acceptConnection():
    print("Servidor iniciado")
    global clientSocket,clientAddress,start
    clientSocket,clientAddress = serverSocket.accept()
    message = str(clientAddress)+" quiere jugar con tigo"
    answer = messagebox.askyesno("Question",message)
    if answer:
        sendData = '{}'.format("accepted").encode()
        clientSocket.send(sendData)
        start = True
        reset()
        resetStat()
        print(sendData)
        print("Ip del jugador 2: ",clientAddress)
        receive()
    else:
        sendData = '{}'.format("Not accepted").encode()
        clientSocket.send(sendData)
        clientSocket.close()
        print("se cerro el socket")
    
def clickQuit():
    if start or user:
        serverSocket.close()
    window.destroy()

createThread(acceptConnection)
createThread(receiveMove)

window=Tk()
window.title("Jugador 1")
window.geometry("920x700+0+0")
window.configure(background = 'Black')



tops = Frame(window, bg ='Green', pady =2, width = 1350, height=150, relief = RIDGE)
tops.grid(row=0, column =0)

lblTitle = Label(tops, font=('times',50,'bold'),text="Jugador O", bd=21,fg='Black',justify = CENTER)
lblTitle.grid(row=0,column = 0)

mainFrame = Frame (window, bg = 'bisque', bd=10,width = 1350, height=600, relief=RIDGE)
mainFrame.grid(row=1,column=0)

leftFrame = Frame (mainFrame ,bd=10, width =750, height=500, pady=2, padx=10, bg="old lace", relief=RIDGE)
leftFrame.pack(side=LEFT)

messagebox.showinfo("Info", "Esperando solicitud de un oponente")



def clicked1():
    global finish,board
    if start and user and btn1["text"]==" ":
        if board.lastMove == player2:
            btn1["text"]="O"
            board.lastMove = "player1"
            sendData = '{}-{}'.format("0",board.lastMove).encode()
            clientSocket.send(sendData)
            board.playMoveOnBoard(0,board.lastMove)
            lblTurn["text"] = "Oponente"
            print(sendData)
            play()

def clicked2():
    global finish,board
    if start and user and btn2["text"]==" ":
        if board.lastMove == player2:
            btn2["text"]="O"
            board.lastMove = "player1"
            sendData = '{}-{}'.format("1",board.lastMove).encode()
            clientSocket.send(sendData)
            board.playMoveOnBoard(1,board.lastMove)
            lblTurn["text"] = "Oponente"
            print(sendData)
            play()

def clicked3():
    global finish,board
    if start and user and btn3["text"]==" ":
        if board.lastMove == player2:
            btn3["text"]="O"
            board.lastMove = "player1"
            sendData = '{}-{}'.format("2",board.lastMove).encode()
            clientSocket.send(sendData)
            board.playMoveOnBoard(2,board.lastMove)
            lblTurn["text"] = "Oponente"
            print(sendData)
            play()

def clicked4():
    global finish,board
    if start and user and btn4["text"]==" ":
        if board.lastMove == player2:
            btn4["text"]="O"
            board.lastMove = "player1"
            sendData = '{}-{}'.format("3",board.lastMove).encode()
            clientSocket.send(sendData)
            board.playMoveOnBoard(3,board.lastMove)
            lblTurn["text"] = "Oponente"
            print(sendData)
            play()

def clicked5():
    global finish,board
    if start and user and btn5["text"]==" ":
        if board.lastMove == player2:
            btn5["text"]="O"
            board.lastMove = "player1"
            sendData = '{}-{}'.format("4",board.lastMove).encode()
            clientSocket.send(sendData)
            board.playMoveOnBoard(4,board.lastMove)
            lblTurn["text"] = "Oponente"
            print(sendData)
            play()

def clicked6():
    global finish,board
    if start and user and btn6["text"]==" ":
        if board.lastMove == player2:
            btn6["text"]="O"
            board.lastMove = "player1"
            sendData = '{}-{}'.format("5",board.lastMove).encode()
            clientSocket.send(sendData)
            board.playMoveOnBoard(5,board.lastMove)
            lblTurn["text"] = "Oponente"
            print(sendData)
            play()

def clicked7():
    global finish,board
    if start and user and btn7["text"]==" ":
        if board.lastMove == player2:
            btn7["text"]="O"
            board.lastMove = "player1"
            sendData = '{}-{}'.format("6",board.lastMove).encode()
            clientSocket.send(sendData)
            board.playMoveOnBoard(6,board.lastMove)
            lblTurn["text"] = "Oponente"
            print(sendData)
            play()

def clicked8():
    global finish,board
    if start and user and btn8["text"]==" ":
        if board.lastMove == player2:
            btn8["text"]="O"
            board.lastMove = "player1"
            sendData = '{}-{}'.format("7",board.lastMove).encode()
            clientSocket.send(sendData)
            board.playMoveOnBoard(7,board.lastMove)
            lblTurn["text"] = "Oponente"
            print(sendData)
            play()

def clicked9():
    global finish,board
    if start and user and btn9["text"]==" ":
        if board.lastMove == player2:
            btn9["text"]="O"
            board.lastMove = "player1"
            sendData = '{}-{}'.format("8",board.lastMove).encode()
            clientSocket.send(sendData)
            board.playMoveOnBoard(8,board.lastMove)
            lblTurn["text"] = "Oponente"
            print(sendData)
            play()


def play():
    finish,won = board.isGameFinished()
    if finish:
        reset()
        board.recordGamePlayed()
        board.resetGameBoard()
        board.lastMove = "player1"

def reset():
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "


def resetStat():
    lblTurn["text"] = "Oponente"


def updateBoard():
    if int(pos) == 0:
        btn1["text"]="X"
    elif int(pos) == 1:
        btn2["text"]="X"
    elif int(pos) == 2:
        btn3["text"]="X"
    elif int(pos) == 3:
        btn4["text"]="X"
    elif int(pos) == 4:
        btn5["text"]="X"
    elif int(pos) == 5:
        btn6["text"]="X"
    elif int(pos) == 6:
        btn7["text"]="X"
    elif int(pos) == 7:
        btn8["text"]="X"
    elif int(pos) == 8:
        btn9["text"]="X"


def gameOver():
    isCon = False
    start = False
    user = False
    close = True
    clientSocket.close()
    board.numGames = board.numGames - 1
    comData = board.computeStats()

    # Crear el mensaje de estadísticas
    message = f"Partidas jugadas: {comData['numGames']}\n"
    message += f"Partidas ganadas como 'O': {comData['wins']['O']}\n"
    message += f"Partidas perdidas como 'O': {comData['loss']['O']}\n"
    message += f"Partidas empatadas: {comData['ties']}"

    # Mostrar el mensaje en un cuadro de diálogo
    messagebox.showinfo("Estadísticas jugador 1", message)

    lblTurn["text"] = "opponent"
    reset()

btn1 = Button(leftFrame, text=" ",bg="White", fg="Black",width=8,height=3,font=('Times', 26),command=clicked1)
btn1.grid(column=1, row=1, sticky = S+N+E+W)
btn2 = Button(leftFrame, text=" ",bg="White", fg="Black",width=8,height=3,font=('Times', 26), command=clicked2)
btn2.grid(column=2, row=1, sticky = S+N+E+W)
btn3 = Button(leftFrame, text=" ",bg="White", fg="Black",width=8,height=3,font=('Times', 26),command=clicked3)
btn3.grid(column=3, row=1, sticky = S+N+E+W)
btn4 = Button(leftFrame, text=" ",bg="White", fg="Black",width=8,height=3,font=('Times', 26),command=clicked4)
btn4.grid(column=1, row=2, sticky = S+N+E+W)
btn5 = Button(leftFrame, text=" ",bg="White", fg="Black",width=8,height=3,font=('Times', 26),command=clicked5)
btn5.grid(column=2, row=2, sticky = S+N+E+W)
btn6 = Button(leftFrame, text=" ",bg="White", fg="Black",width=8,height=3,font=('Times', 26),command=clicked6)
btn6.grid(column=3, row=2, sticky = S+N+E+W)
btn7 = Button(leftFrame, text=" ",bg="White", fg="Black",width=8,height=3,font=('Times', 26),command=clicked7)
btn7.grid(column=1, row=3, sticky = S+N+E+W)
btn8 = Button(leftFrame, text=" ",bg="White", fg="Black",width=8,height=3,font=('Times', 26),command=clicked8)
btn8.grid(column=2, row=3, sticky = S+N+E+W)
btn9 = Button(leftFrame, text=" ",bg="White", fg="Black",width=8,height=3,font=('Times', 26),command=clicked9)
btn9.grid(column=3, row=3, sticky = S+N+E+W)

btnQuit=Button (leftFrame, text="Salir", font=('arial', 20, 'bold'),bg="Black", fg="White" ,height = 1, width =15,command = clickQuit)
btnQuit.grid(row=4, column=2 ,padx=6, pady=10)


lbl=Label(leftFrame, font=('arial', 20, 'bold'), text="Turno: ",padx=2, pady=2)
lbl.grid (row=0, column=0, sticky=W)
lblTurn=Label(leftFrame, font=('arial', 20, 'bold'), text="Jugador X",padx=2, pady=2,width=10)
lblTurn.grid (row=0, column=1, sticky=W)

window.mainloop()
