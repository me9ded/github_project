from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def motdepasse (ch):
    mdp=""
    ch=ch+" "
    while ch!="":
        p=ch.find(" ")
        if ch[:p].isdecimal():
            mdp=mdp+ch[:p]
        else:
            mdp=mdp+ch[:p][0]
        ch=ch[p+1:]
    return mdp
def generer (ch):
    if ch.find(" ") ==-1:
        msg="verifier votre message"
    else:
        msg=motdepasse (ch)
    return msg
def traiter ():
    ph=fen.phrase.text()
    ch=generer(ph)
    fen.mes.setText(ch)
app=QApplication([])
fen=loadUi("projet9.ui")
fen.show()
fen.generer.clicked.connect(traiter)
app.exec()


        
    
        