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

    image_label.pack()
    im= ImageTk.PhotoImage(Image.open(root.filename))
    OpenImg.h = im.height()
    OpenImg.w = im.width()
    H=OpenImg.h
    W=OpenImg.w
    T = tk.Text(root, height=2, width=50)
    T.pack()
    T.insert(tk.END, "Hauteur : "+str(H)+" pixels\nLargeur : "+str(W)+" pixels")

    T.config(font="calibri, 14")
    info_haut = 0
    info_larg = 0
    info_larg=Entry(root,width= 20,fg="grey")
    label_largeur= Label(text="La largeur souhaitée")
    label_largeur.pack()
    info_larg.insert(0,"", )
    info_larg.config(font="calibri, 16")
    info_larg.pack()
    OU = tk.Label(root, text="OU",fg="red")
    OU.config(font=("calibri", 20))
    OU.pack()
    info_haut=Entry(root,width= 20,fg="grey")
    label_hauteur= Label(text="La hauteur souhaitée")
    label_hauteur.pack()
    info_larg.insert(0,"", )
    info_haut.config(font="calibri, 16")
    info_haut.pack()
    label_largeur.config(font="calibri, 18")
    label_hauteur.config(font="calibri, 18")



    def test():
        HAUT=info_haut.get()
        LARG=info_larg.get()
        if(LARG=="" and str(H)>str(W)):
            S=H/W
            HAUT2=int(HAUT)
            result=round(HAUT2/S,1)
            T.delete('1.0', END)
            T.insert(tk.END, "la largeur de votre rendu est de : "+str(result)+" cm")
        elif(LARG=="" and str(W)>str(H)):
            S=W/H
            HAUT2=int(HAUT)
            result=round(S*HAUT2,1)
            T.delete('1.0', END)
            T.insert(tk.END, "La largeur de votre rendu est de : "+str(result)+" cm")
        elif(HAUT=="" and str(H)>str(W)):
            S=H/W
            LARG2=int(LARG)
            result=round(S*LARG2,1)
            T.delete('1.0', END)
            T.insert(tk.END, "La hauteur de votre rendu est de : "+str(result)+" cm")
        elif(HAUT=="" and str(W)>str(H)):
            S=W/H
            LARG2=int(LARG)
            result=round(LARG2/S,1)
            T.delete('1.0', END)
            T.insert(tk.END, "La hauteur de votre rendu est de : "+str(result)+" cm")
        else:
            T.delete('1.0', END)
            T.insert(tk.END, "Une erreur s'est produite \nVeuillez ne remplir qu'un seul champ et laisser l'autre vide")

    bouton=Button(root, text="Calculer la dimension manquante", command=test)
    bouton.config(font="calibri, 10", background="yellow")
    bouton.pack()


button =Button(root, text='Ouvrir une image', command=OpenImg)
button.pack()

root.mainloop()