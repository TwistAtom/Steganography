#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.filedialog as dlg
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from PIL import Image,ImageTk
import LibImg as fct



fenetre = tk.Tk ()
fenetre.title ("Steganographe")
#fenetre.iconbitmap("Icone2.ico")

#***************************************** Positionnement de la fenêtre principale *********************************************


ws = fenetre.winfo_screenwidth()
hs = fenetre.winfo_screenheight()

print(ws,hs)
# Centrage de la fenêtre à l'écran
x = (ws/2) - (1200/2)
y = (hs/2) - (1024/2)
fenetre.geometry('+%d+%d' % (x, y))

# Blocage du dimensionnement de la fenêtre
#fenetre.resizable(width=False, height=False)
#fenetre.rowconfigure(0, weight=1)
#fenetre.columnconfigure(0, weight=1)


#**************************************** Variables globales de l'interface *******************************************************
couleur1 = "#595959"
couleurf = "#008fd5"
couleur2 = "red"

VarImSrc       = tk.StringVar()
VarImCach      = tk.StringVar()
VarImRev       = tk.StringVar()
VarImDestRev   = tk.StringVar()
VarImDestCach  = tk.StringVar()
VarCleCach    = tk.StringVar()
VarCleRev    =   tk.StringVar()
VarLsbLevel    = tk.IntVar()
VarChiffCacher = tk.StringVar()
VarChiffReveler = tk.StringVar()
VarChiffCacher.set('off')
VarChiffReveler.set('off')

#**************************************************  | DEFINITION DES FONCTIONS | *************************************************************

def update_frame_img_file(Img,size_l,size_h):
    
    im = fct.image_miniature(Img,size_l,size_h)
    ImgMiniSrc = ImageTk.PhotoImage(im)
    InfoImg = fct.infos_image (Img)
    return ImgMiniSrc , str(InfoImg[0]) + "x" + str(InfoImg[1]) + " px"

def select_file_img(Btn):

    ImgSelect = dlg.askopenfilename(title="Selection Image",filetypes=[('jpg files','.jpg'),('png files','.png'),('all files','.*')])
    #print(fct.CompteurProgess)
    if Btn == "BtnImSrc":
        VarImSrc.set(ImgSelect)
        ImgMini , f1_visu_taille['text'] = update_frame_img_file (ImgSelect,150,150)
        f1_visu_image['image'] = ImgMini
        f1_visu_image.image =  ImgMini
    elif Btn == "BtnImCach":
        VarImCach.set(ImgSelect)
        ImgMini , f2_visu_taille['text'] = update_frame_img_file (ImgSelect,150,150)
        f2_visu_image['image'] = ImgMini
        f2_visu_image.image =  ImgMini
    elif Btn == "BtnImRev":
        VarImRev.set(ImgSelect)
        ImgMini , f4_visu_taille['text'] = update_frame_img_file (ImgSelect,180,180)
        f4_visu_image['image'] = ImgMini
        f4_visu_image.image =  ImgMini

def chiffrement_choix(ChkBxName):
    
    if ChkBxName == "C_LibCheck":
        print(VarChiffCacher.get())
        if VarChiffCacher.get() == 'on' :
            f3_entree_chiffrement['state'] = "normal"
        else:
            f3_entree_chiffrement['state'] = "disabled"
    elif ChkBxName == "R_LibCheck":
        print(VarChiffReveler.get())
        if VarChiffReveler.get() == 'on' :
            f5_entree_chiffrement['state'] = "normal"
        else:
            f5_entree_chiffrement['state'] = "disabled"

def select_file_dest_cacher():
    DestFile = dlg.asksaveasfilename(title="Sauvegarde nouvelle Image",filetypes=[('png files','.png')],)
    VarImDestCach.set(DestFile)
    
def select_file_dest_reveler():
    DestFile = dlg.asksaveasfilename(title="Sauvegarde nouvelle Image",filetypes=[('png files','.png')])
    VarImDestRev.set(DestFile)


def affiche_image(Img, Operation):

    FenPopUp = tk.Toplevel(fenetre, bg=couleur1)
    FenPopUp.transient(fenetre)

    if Operation == "C":
        FenPopUp.title("Rendu Image Cachée")
    else:
        FenPopUp.title("Révélation Image Cachée")

    #Taille de l'image à charger et de la fenêtre
    InfosImg= fct.infos_image(Img)
    w=InfosImg[0]
    h=InfosImg[1]
    ws = fenetre.winfo_screenwidth()
    hs = fenetre.winfo_screenheight()

    # Centrage de la fenêtre à l'écran
    x = (ws/2) - (w/2) 
    y = (hs/2) - (h/2)
    FenPopUp.geometry('%dx%d+%d+%d' % (w, h, x, y))
 
    ImgAff = ImageTk.PhotoImage(file=Img)
    visu_image_FenPopUp = tk.Label(FenPopUp, bg = couleur1)
    visu_image_FenPopUp['image'] = ImgAff
    visu_image_FenPopUp.image =  ImgAff
    visu_image_FenPopUp.pack()

def start_cacher():
    fct.cacher(VarLsbLevel.get(), VarImSrc.get(), VarImCach.get(), VarImDestCach.get(),VarChiffCacher.get(),VarCleCach.get()) 
    pb_cacher.start()
    affiche_image(VarImDestCach.get(),"C")
    
def start_reveler():
    print("StartPopup")
    fct.reveler(VarImRev.get(), VarImDestRev.get(), VarChiffReveler.get(),VarCleRev.get()) 
    f7_pb.start()
    affiche_image(VarImDestRev.get(),"R")
  
def reset_cacher ():

    #reset des variables Windget
    VarImSrc.set('')
    VarImCach.set('')
    VarImDestCach.set('')
    VarLsbLevel.set(0)
    #Reset des Miniatures
    f1_visu_image.image =  ""
    f2_visu_image.image =  ""
    f1_visu_taille['text'] = ""
    f2_visu_taille['text'] = ""
    #Reset paramètres chiffrement
    VarChiffCacher.set('off')
    f3_entree_chiffrement['state'] = 'disabled'
    VarCleCach.set ("")

 
def reset_reveler ():

    VarImRev.set('')
    VarImDestRev.set('')
    f4_visu_image.image =  ""
    f4_visu_taille['text'] = ""
    VarChiffReveler.set('off')
    f5_entree_chiffrement['state'] = 'disabled'
    VarCleRev.set ("")
"""
def update_progress(delay=200):

    #global counter
    #widget.step(2)
    #counter += 2
    #if counter < 98:
    #    widget.after(delay, update)
    #update()
"""
# Initialisation des icones
DossierLire = ImageTk.PhotoImage(file="DossierLire.png")
DossierDest = ImageTk.PhotoImage(file="DossierDest.png")
extraire = ImageTk.PhotoImage(file="Extract.png")
Lock = ImageTk.PhotoImage(file="Lock.png")
Unlock = ImageTk.PhotoImage(file="UnLock.png")
Cacher = ImageTk.PhotoImage(file="Start_Cache.png")
Reset = ImageTk.PhotoImage(file="settings.png")
ImKey = ImageTk.PhotoImage(file="key2.png")

# Création des Onglets
nb = ttk.Notebook(fenetre)
nb.enable_traversal()
onglet_cacher = tk.Frame(bg=couleur1) 
#tk.Frame(width=400, height=200, bg=couleur1) 
onglet_reveler = tk.Frame(bg=couleur1)
#tk.Frame(width=650, height=400, bg=couleur1) 
nb.add(onglet_cacher,  text='CACHER', image = Lock, compound="right")
nb.add(onglet_reveler, text='REVELER', image = Unlock, compound="right")
nb.grid(row=0,column=0)

# Définition des Polices
font_S = "-size 8 -weight bold"
font_infos = "-size 8 -weight normal"

#********************************************* DECLARATION DES OBJETS TKINTER (Windget)  *******************************************

# Déclaration des Frames de l'onglet [CACHER]
 #,width = 650, height=125)
f1 = tk.LabelFrame (onglet_cacher, text = "Image source", bg = couleurf, fg = "white", relief = "groove", borderwidth = 5, pady=15)
f2 = tk.LabelFrame (onglet_cacher, text = "Image à cacher", bg = couleurf, fg = "white",relief = "groove", borderwidth = 5)
f3 = tk.LabelFrame (onglet_cacher, text = "Options", bg = couleurf, fg = "white",relief = "groove", borderwidth = 5)


# Déclaration des Frames de l'onglet [REVELER]
f4 = tk.LabelFrame (onglet_reveler, text = "Image", bg = couleurf, fg = "white", relief = "groove", borderwidth = 5)
f5 = tk.LabelFrame (onglet_reveler, text = "Dechiffrement", bg = couleurf,fg = "white", relief = "groove", borderwidth = 5)
f6 = tk.Frame (onglet_reveler,bg = couleur1)
f7 = tk.Frame (onglet_reveler,  bg = couleurf, relief = "groove",borderwidth = 2)

# Déclaration des windgets de l'onglet [CACHER]
pb_cacher = ttk.Progressbar(onglet_cacher, orient = "horizontal",  mode = "determinate")
f1_radio_text = tk.Radiobutton(onglet_cacher, text = "Text", value = 1, bg = couleur1,fg = "white", selectcolor=couleur1,borderwidth=2)
f1_radio_image = tk.Radiobutton(onglet_cacher, text = "Image", value = 2, bg = couleur1,fg = "white",selectcolor=couleur1,borderwidth=2)
bouton_cacher = tk.Button(onglet_cacher, text = "Cacher", command = start_cacher ,image=Cacher,borderwidth=3)
bouton_reset1 = tk.Button(onglet_cacher, text = "Reset", command = reset_cacher, highlightcolor = "red",image=Reset,borderwidth=4)
Signature = tk.Label (onglet_cacher, text = "© T² Industrie 2018 ", bg = couleur1, fg = "yellow", font = font_S)

# Déclaration des windgets de F1 <Selection image source>
f1_BtnSelImg = tk.Button(f1, text = "BtnImSrc", command = lambda: select_file_img(f1_BtnSelImg['text']), image = DossierLire,borderwidth=3)
f1_visu_chemin = tk.Entry (f1, textvariable = VarImSrc, width=40)
f1_visu_image = tk.Label (f1, bg = couleurf)
f1_col_vide = tk.Label (f1, width=30,bg = couleurf)
f1_label_taille = tk.Label (f1, text="Taille image : ", font = font_infos,bg = couleurf)
f1_visu_taille = tk.Label (f1, font = font_infos,bg = couleurf,fg="white")

# Déclaration des windgets de F2 <Selection Image Cache>
f2_BtnSelImg = tk.Button(f2, text = "BtnImCach", command = lambda: select_file_img(f2_BtnSelImg['text']), image = DossierLire, borderwidth=3)
f2_visu_chemin = tk.Entry (f2, textvariable = VarImCach, width=40)
f2_visu_image = tk.Label (f2,bg = couleurf)
f2_col_vide = tk.Label(f2, width=30,bg = couleurf)
f2_label_taille = tk.Label (f2, text="Taille image : ", font = font_infos,bg = couleurf)
f2_visu_taille = tk.Label (f2, font = font_infos,bg = couleurf,fg="white")
#f2_unite = tk.Label (f2, text="byte", font = font_infos, bg = couleurf)

# Déclaration des windgets de F3 <Options>
C_LibCheck = "  Saisie mot de passe / Clé pour chiffrement :"
f3_BtnSelDest = tk.Button(f3, text = " Emplacement : ", command = select_file_dest_cacher, image = DossierDest, compound="top",borderwidth=3)
f3_visu_chemin = tk.Entry (f3, textvariable = VarImDestCach, width=30)
f3_checkbutton_chiffrement = tk.Checkbutton(f3, text = C_LibCheck, variable = VarChiffCacher,offvalue ="off", onvalue='on', 
                                                command = lambda:chiffrement_choix("C_LibCheck"),image=ImKey, compound="left",bg = couleurf)
f3_entree_chiffrement = tk.Entry(f3, textvariable = VarCleCach, state="disabled",disabledbackground="#cfcfcf")
f3_echelle = tk.Scale(f3, orient = "horizontal", variable = VarLsbLevel, from_= 1, to = 8, resolution = 1, tickinterval = 2, length = 30, label = 'Qualité (Kb)', bg = couleurf)

# Déclaration des windgets de F4
f4_BtnSelImg = tk.Button(f4, text = "BtnImRev", command = lambda: select_file_img(f4_BtnSelImg['text']), image = DossierLire,borderwidth=3)
f4_visu_chemin = tk.Entry (f4, textvariable = VarImRev, width=40)
f4_visu_image = tk.Label (f4,bg = couleurf)
f4_col_vide = tk.Label (f4, width=30,bg = couleurf)
f4_label_taille = tk.Label (f4, text="Taille image : ", font = font_infos,bg = couleurf)
f4_visu_taille = tk.Label (f4, font = font_infos,bg = couleurf,fg="white")

# Déclaration des windgets de F5
R_LibCheck = "  Saisie mot de passe / Clé pour déchiffrement :"
f5_bouton_emplacement = tk.Button(f5, text = " Emplacement : ", command = select_file_dest_reveler, image = DossierDest, compound="top",borderwidth=3)
f5_visu_chemin = tk.Entry (f5, textvariable = VarImDestRev, width=30)
f5_checkbutton_chiffrement = tk.Checkbutton(f5, text = R_LibCheck, variable = VarChiffReveler,offvalue ="off", onvalue='on', 
                                                command = lambda: chiffrement_choix("R_LibCheck"),image=ImKey, compound="left",bg = couleurf)
f5_label_pass = tk.Label (f5, text="Password : ", bg = couleurf)
f5_entree_chiffrement = tk.Entry(f5, textvariable = VarCleRev, state="disabled",disabledbackground="#cfcfcf")

# Declaration des windgets de F6
f6_bouton_extraire = tk.Button(f6, text = "Extraire", command = start_reveler, highlightcolor = "red",image=extraire)
f6_bouton_reset = tk.Button(f6, text = "Reset", command = reset_reveler, highlightcolor = "red",image=Reset)

# Declaration des windgets de F7
f7_pb = ttk.Progressbar (onglet_reveler, orient = "horizontal", mode = "determinate")
f7_Signature = tk.Label (onglet_reveler, text = "© T² Industrie 2018 ", bg = couleur1, fg = "yellow" , font = font_S)


#********************************************* PLACEMENT DES OBJETS TKINTER (Windget) *******************************************


# Placement des widgets de Onglet [Cacher]
f1_radio_image.grid (row = 0, column = 0, columnspan = 3, sticky='ne', padx = 300)
f1_radio_text.grid (row = 0, column = 0, columnspan = 3, sticky='nw', padx = 300) 


#f1.rowconfigure(0, weight=1)
#f1.columnconfigure(0, weight=1)
f1.grid(row = 1, column = 0, columnspan = 3, sticky='nesw', padx = 20,pady=5)
f2.grid(row = 2, column = 0, columnspan = 3, sticky='nesw', padx = 20, pady = 5, ipady=3)
f3.grid(row = 3, column = 0, sticky='wns', padx = 20, pady = 3,ipadx=10)
bouton_cacher.grid(row = 3, column = 1, padx = 0)
bouton_reset1.grid(row = 3, column = 2, padx = 5)
pb_cacher.grid (row = 4, column = 0, columnspan = 3, sticky='nesw', padx = 20, pady = 5)
Signature.grid(row = 5, column = 2, sticky='se', padx = 10)

# Placement des windgets de F1
f1_BtnSelImg.grid (row = 0, column = 0, padx = 15, pady = 10)
f1_visu_chemin.grid (row = 0, column = 1)
f1_col_vide.grid (row = 0, column = 2, sticky='ns',padx = 15)
f1_visu_image.grid (row = 0, column = 3,rowspan=2,padx = 15,sticky='nse')
f1_label_taille.grid (row = 1, column = 0,columnspan = 2, sticky='nsw', padx = 15)
f1_visu_taille.grid (row = 1, column = 1,sticky='nsw')

# Placement des windgets de F2
f2_BtnSelImg.grid (row = 0, column = 0, padx = 15, pady = 10)
f2_visu_chemin.grid (row = 0, column = 1)
f2_col_vide.grid (row = 0, column = 2, sticky='ns',padx = 15)
f2_visu_image.grid (row = 0, column = 3,rowspan=2,padx = 15,sticky='nse')
f2_label_taille.grid (row = 1, column = 0,columnspan = 2, sticky='nsw', padx = 15)
f2_visu_taille.grid (row = 1, column = 1,sticky='nsw')

# Placement des widgets de F3 <Options>
f3_BtnSelDest.grid (row = 0, column = 0, sticky='nsw', padx = 15, pady = 5)
f3_checkbutton_chiffrement.grid (row = 0, column = 1,sticky='w')
f3_visu_chemin.grid (row = 1, column = 0, padx = 15, pady = 10)
f3_entree_chiffrement.grid (row = 1, column = 1 ,columnspan = 2, padx = 5, sticky='w')
f3_echelle.grid (row = 2, column = 0, columnspan = 2, sticky='nesw', padx = 5, pady=5)

# Placement des Frames de l'onglet [REVELER]
f4.pack(fill=tk.BOTH,padx=20,pady = 10)
f5.pack(fill=tk.BOTH,padx=20,pady = 10)
f6.pack(fill=tk.BOTH,padx=20,pady = 10)
#f7.pack(fill=tk.BOTH,padx=20,pady = 20)

# Placement des windgets de F4
f4_BtnSelImg.grid (row = 0, column = 0, sticky='w', padx = 15, pady = 20)
f4_visu_chemin.grid (row = 0, column = 1)
f4_col_vide.grid (row = 0, column = 2, sticky='ns',padx = 15)
f4_visu_image.grid (row = 0, column = 3,rowspan=2,padx = 15,pady = 20,sticky='nse')
f4_label_taille.grid (row = 1, column = 0,columnspan = 2, sticky='nsw', padx = 15)
f4_visu_taille.grid (row = 1, column = 1,sticky='nsw')

# Placement des windgets de F5
f5_bouton_emplacement.grid (row = 0, column = 0, sticky='w', padx = 15, pady = 5)
f5_visu_chemin.grid (row = 1, column = 0,padx = 15, pady = 5)
f5_checkbutton_chiffrement.grid(row = 0, column = 1, columnspan = 3, sticky='we', padx = 15, pady = 10)
#f5_label_pass.grid(row = 1, column = 2,pady = 10)
f5_entree_chiffrement.grid(row = 1, column = 1, pady = 10)

# Placement des windgets de F6
f6_bouton_extraire.grid(row = 0, column = 0, padx = 20, pady = 20)
f6_bouton_reset.grid(row = 0, column = 1, sticky='we',padx = 50,pady = 20)

# Placement des windgets de F7
f7_pb.pack(fill="both",padx = 15, pady = 50)
#grid(row = 0, column = 0, padx = 15, pady = 20,sticky='nswe')
f7_Signature.pack(side="bottom",padx = 10,anchor = 'se')
#grid(row = 1, column = 0, sticky='e')

    
f7_pb.start()


#hid.cacher(3,"metagabbro.jpg", "dragibus.jpg", "titi.png") 

fenetre.mainloop()
#fenetre.destroy