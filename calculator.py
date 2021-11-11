# Créé par Romathom, le 11/11/2021 en Python 3.7
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

#Lancement de l'application
root = tk.Tk()
root.title(" Image Ratio Calculator ") #titre de l'application
root.geometry('500x300+50+10') #taille de la fenetre

#Ouvrir une image
def OpenImg():
    root.filename = filedialog.askopenfilename(title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("gif files", "*.gif*"), ("png files", "*.png"))) #extension supporter
    image_label = Label(root, text=root.filename)


    im= ImageTk.PhotoImage(Image.open(root.filename))
    OpenImg.h = im.height()
    OpenImg.w = im.width()
    H=OpenImg.h
    W=OpenImg.w
    T = tk.Text(root, height=2, width=50)
    T.pack()
    T.insert(tk.END, "la hauteur de l'image est de "+str(H)+" pixels\net sa largeur est de "+str(W)+" pixels")
    image_label.pack()
    T.config(font="calibri, 22")

    info_haut = 0
    info_larg = 0
    info_larg=Entry(root,width= 20,fg="grey")
    info_larg.insert(0,"la largeur voulue", )
    info_larg.config(font="calibri, 20")
    info_larg.pack()
    OU = tk.Label(root, text="OU",fg="red")
    OU.config(font=("calibri", 20))
    OU.pack()
    info_haut=Entry(root,width= 20,fg="grey")
    info_haut.insert(0,"la hauteur voulue")
    info_haut.config(font="calibri, 20")
    info_haut.pack()



    def test():
        HAUT=info_haut.get()
        LARG=info_larg.get()
        if(LARG == 0 or LARG == "la largeur voulue" or LARG=="" and str(H)>str(W)):
            S=H/W
            HAUT2=int(HAUT)
            result=HAUT2/S
            T.delete('1.0', END)
            T.insert(tk.END, "la largeur de votre rendu est de "+str(result)+" centimètres")
        elif(LARG == 0 or LARG == "la largeur voulue" or LARG=="" and str(W)>str(H)):
            S=W/H
            HAUT2=int(HAUT)
            result=S*HAUT2
            T.delete('1.0', END)
            T.insert(tk.END, "la largeur de votre rendu est de "+str(result)+" centimètres")
        elif(HAUT == 0 or HAUT == "la hauteur voulue" or HAUT=="" and str(H)>str(W)):
            S=H/W
            LARG2=int(LARG)
            result=S*LARG2
            T.delete('1.0', END)
            T.insert(tk.END, "la hauteur de votre rendu est de "+str(result)+" centimètres")
        elif(HAUT == 0 or HAUT == "la hauteur voulue" or HAUT=="" and str(W)>str(H)):
            S=W/H
            LARG2=int(LARG)
            result=LARG2/S
            T.delete('1.0', END)
            T.insert(tk.END, "la hauteur de votre rendu est de "+str(result)+" centimètres")
        else:
            T.delete('1.0', END)
            T.insert(tk.END, "Une erreur s'est produite veuillez redémarrer l'application")

    bouton=Button(root, text="Calculer la dimension manquante", command=test)
    bouton.pack()


button =Button(root, text='Ouvrir une image', command=OpenImg)
button.pack()

root.mainloop()