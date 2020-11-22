
from tkinter import *

# creer une premiere fenetre
window = Tk()

#personaliser la fenetre
window.title("The Mads-Op")
window.geometry("1080x720")
window.minsize(1080, 720)
window.maxsize(1080, 720)
window.iconbitmap("MadsOpLogo.ico")
window.config(background='#2cdf81')

#creer la frame
frame = Frame(window, bg='#2cdf81', bd=1)
frameChiffre = Frame(window, bg='#2cdf81', bd=1)
frameReponse = Frame(window, bg='#2cdf81', bd=1)
frameFinale = Frame(window, bg='#2cdf81', bd=1)

#ajouter un premier texte
label_title = Label(frame, text="The MADS Operation", font=("Courrier", 40,"bold"), bg='#2cdf81', fg='#0C1248')
label_title.grid(row=0, column=1, padx=50)

#ajout d'une image
image = PhotoImage(file="MadsOpLogo.png").zoom(3).subsample(8)
canva = Canvas(frame, width=200, height=200, bg='#2cdf81', bd= 0, highlightthickness=0)
canva.create_image(200/2, 200/2, image=image)
canva.grid(row=0, column=0, padx=10)

#ajouter
frame.pack(pady=30)

#ajouter d'un mini-titre
label_chiffre = Label(frameChiffre, text="Voici vos chiffres:", font=("Courrier", 15), bg='#2cdf81', fg='#0C1248')
label_chiffre.grid(row=1, column=0, padx=10)

#ajout des chiffres
imageChiffre1 = PhotoImage(file="Numéro/10.png").zoom(1).subsample(8)
canvaChiffre1 = Canvas(frameChiffre, width=200, height=200, bg='#2cdf81', bd= 0, highlightthickness=0)
canvaChiffre1.create_image(200/2, 200/2, image=imageChiffre1)
canvaChiffre1.grid(row=1, column=1, padx=10)

imageChiffre2 = PhotoImage(file="Numéro/8.png").zoom(1).subsample(8)
canvaChiffre2 = Canvas(frameChiffre, width=200, height=200, bg='#2cdf81', bd= 0, highlightthickness=0)
canvaChiffre2.create_image(200/2, 200/2, image=imageChiffre2)
canvaChiffre2.grid(row=1, column=2, padx=10)

imageChiffre3 = PhotoImage(file="Numéro/6.png").zoom(1).subsample(8)
canvaChiffre3 = Canvas(frameChiffre, width=200, height=200, bg='#2cdf81', bd= 0, highlightthickness=0)
canvaChiffre3.create_image(200/2, 200/2, image=imageChiffre3)
canvaChiffre3.grid(row=1, column=3, padx=10)

imageChiffre4 = PhotoImage(file="Numéro/3.png").zoom(1).subsample(8)
canvaChiffre4 = Canvas(frameChiffre, width=200, height=200, bg='#2cdf81', bd= 0, highlightthickness=0)
canvaChiffre4.create_image(200/2, 200/2, image=imageChiffre4)
canvaChiffre4.grid(row=1, column=4, padx=10)

#ajouter
frameChiffre.pack(pady=30)

#ajouter d'un mini-titre
label_reponse = Label(frameReponse, text="Vos réponses:", font=("Courrier", 15), bg='#2cdf81', fg='#0C1248')
label_reponse.grid(row=1, column=0, padx=10)

chiffre_text = StringVar()
operation_text = StringVar()


#ajout des champs pour réponse
chiffre1 = Entry(frameReponse, font=("Courrier", 10), bg='white', fg='#0C1248', width=10, justify='center', textvariable=chiffre_text)
chiffre1.grid(row=1, column=1, padx=10)
label_chiffre1 = Label(frameReponse, text="Chiffre 1", font=("Courrier", 10), bg='#2cdf81', fg='#0C1248')
label_chiffre1.grid(row=0, column=1, padx=10)

operation1 = Entry(frameReponse, font=("Courrier", 10), bg='white', fg='#0C1248', width=10, justify='center', textvariable=operation_text)
operation1.grid(row=1, column=2, padx=10)
label_operation1 = Label(frameReponse, text="Opération 1", font=("Courrier", 10), bg='#2cdf81', fg='#0C1248')
label_operation1.grid(row=0, column=2, padx=10)

chiffre2 = Entry(frameReponse, font=("Courrier", 10), bg='white', fg='#0C1248', width=10, justify='center', textvariable=chiffre_text)
chiffre2.grid(row=1, column=3, padx=10)
label_chiffre2 = Label(frameReponse, text="Chiffre 2", font=("Courrier", 10), bg='#2cdf81', fg='#0C1248')
label_chiffre2.grid(row=0, column=3, padx=10)

operation2 = Entry(frameReponse, font=("Courrier", 10), bg='white', fg='#0C1248', width=10, justify='center', textvariable=operation_text)
operation2.grid(row=1, column=4, padx=10)
label_operation2 = Label(frameReponse, text="Opération 2", font=("Courrier", 10), bg='#2cdf81', fg='#0C1248')
label_operation2.grid(row=0, column=4, padx=10)

chiffre3 = Entry(frameReponse, font=("Courrier", 10), bg='white', fg='#0C1248', width=10, justify='center', textvariable=chiffre_text)
chiffre3.grid(row=1, column=5, padx=10)
label_chiffre3 = Label(frameReponse, text="Chiffre 3", font=("Courrier", 10), bg='#2cdf81', fg='#0C1248')
label_chiffre3.grid(row=0, column=5, padx=10)

operation3 = Entry(frameReponse, font=("Courrier", 10), bg='white', fg='#0C1248', width=10, justify='center', textvariable=operation_text)
operation3.grid(row=1, column=6, padx=10)
label_operation3 = Label(frameReponse, text="Opération 3", font=("Courrier", 10), bg='#2cdf81', fg='#0C1248')
label_operation3.grid(row=0, column=6, padx=10)

chiffre4 = Entry(frameReponse, font=("Courrier", 10), bg='white', fg='#0C1248', width=10, justify='center', textvariable=chiffre_text)
chiffre4.grid(row=1, column=7, padx=10)
label_chiffre4 = Label(frameReponse, text="Chiffre 4", font=("Courrier", 10), bg='#2cdf81', fg='#0C1248')
label_chiffre4.grid(row=0, column=7, padx=10)

#creer un bouton
boutonValider =Button(frameReponse,text="Valider", font=("Courrier", 10), bg='#2cdf81', fg='#0C1248', width=15)
boutonValider.grid(row=1, column=8, padx=10)

frameReponse.pack(pady=30)

def chiffre_limit(chiffre_text):
    if len(chiffre_text.get()) > 0:
        chiffre_text.set(chiffre_text.get()[:2])

chiffre_text.trace("w", lambda *args: chiffre_limit(chiffre_text))

def character_limit(operation_text):
    if len(operation_text.get()) > 0:
        operation_text.set(operation_text.get()[-1])

operation_text.trace("w", lambda *args: character_limit(operation_text))

#ajouter des réponses
label_ReponseUtilisateur = Label(frameFinale, text="La réponse de votre calcul est", font=("Courrier", 25), bg='#2cdf81', fg='#0C1248')
label_ReponseUtilisateur.grid(row=0, column=0, padx=50)

label_ReponseVoulue = Label(frameFinale, text="et la réponse voulue était", font=("Courrier", 25), bg='#2cdf81', fg='#0C1248')
label_ReponseVoulue.grid(row=0, column=1, padx=50)

frameFinale.pack()


# afficher
window.mainloop()