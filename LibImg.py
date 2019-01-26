#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:34:16 2018

@author: Zibau
"""
import tkinter as tk
import tkinter.ttk as ttk
import tkinter as tk
import PIL.Image as pi
import LibCrypto as isn


global CompteurProgess

#ttk.Progressbar(onglet_cacher, orient = "horizontal",  mode = "determinate")


def infos_image(nom_image):
    
    """
    infos_image : String -> Tuple
    infos_image(nom_image) retourne les informations d'une image donnée 
    sous forme de Tuple contenant la largeur, la hauteur et les listes 
    des valeurs des canaux RGB. 
    """ 
    
    image = pi.open(nom_image)
    largeur, hauteur = image.size
    
    r, v, b = image.split()
    
    rouge =  list(r.getdata())
    vert =  list(v.getdata())
    bleu =  list(b.getdata())
    return (largeur, hauteur, rouge, vert, bleu)

def image_miniature(nom_image,size_l,size_h):
    """
    image_miniature : String * Integer -> Image
    image_miniature(nom_image,size_l,size_h) retourne une Image selon le nom,
    la largeur et la hauteur rentrée. 
    """ 
    im = pi.open(nom_image)
    im.thumbnail((size_l,size_h))
    im.save("MiniSrc.png")
    #print(im.mode)
    return im
 
def cacher(Q1, Nom_Image_qui_Cache, Nom_Image_a_Cache, nom_image, cryptage,cle):
    """
    cacher : Integer * String -> Fonction
    cacher(Q1, Nom_Image_qui_Cache, Nom_Image_a_Cache, nom_image, cryptage,cle)
    execute une fonction (creation_image) selon les informations qu'il créé. 
    """ 
    largeur, hauteur, rouge, vert, bleu = infos_image(Nom_Image_qui_Cache)
    print ("ImASrc => ",largeur, hauteur, len(rouge), len(vert), len(bleu))

    bin_rouge = []
    bin_rouge2 = []
    bin_rouge_final = []
    entier_rouge_final = []

    bin_vert = []
    bin_vert2 = []
    bin_vert_final = []
    entier_vert_final = []


    bin_bleu = []
    bin_bleu2 = []
    bin_bleu_final = []
    entier_bleu_final = []

    Q2 = 8 - Q1
    CompteurProgess = 0


    largeur2, hauteur2, rouge2, vert2, bleu2 = infos_image(Nom_Image_a_Cache)

    print ("ImACacher => ",largeur2, hauteur2, len(rouge2), len(vert2), len(bleu2))
    CompteurProgess = len(rouge) + len(vert) + len(bleu) + len(rouge2) + len(vert2) + len(bleu2)
    print (CompteurProgess)

    bin_qualite1 = bin (Q1)[2:].rjust(5,"0") 

    bin_hauteur2 = bin(hauteur2)[2:].rjust(15,"0")
    bin_largeur2 = bin(largeur2)[2:].rjust(15,"0")

    for i in range(15):
        entier_rouge_final.append(2*int(rouge[i]//2)+int(bin_hauteur2[i]))

    for j in range(15):
        entier_rouge_final.append(2*int(rouge[j+15]//2)+int(bin_largeur2[j]))

    for h in range (5):
        entier_rouge_final.append(2*int(rouge[h+30]//2)+int(bin_qualite1[h]))


    for g in range(35, len(rouge)):
    
        bin_rouge.append(bin(int(rouge[g]))[2:].rjust(8, "0"))    

    for c in range(len(vert)):
    
        bin_vert.append(bin(int(vert[c]))[2:].rjust(8, "0"))
        bin_bleu.append(bin(int(bleu[c]))[2:].rjust(8, "0"))


    for l in range(len(rouge2)):
    
        bin_rouge2.append(bin(int(rouge2[l]))[2:].rjust(8, "0")) 
        bin_vert2.append(bin(int(vert2[l]))[2:].rjust(8, "0"))
        bin_bleu2.append(bin(int(bleu2[l]))[2:].rjust(8, "0"))
    
    if cryptage == "on":
        
        bin_rouge_crypt = isn.algo_boucle(bin_rouge2,'c',1,cle)
        bin_vert_crypt = isn.algo_boucle(bin_vert2,'c',2,cle)
        bin_bleu_crypt = isn.algo_boucle(bin_bleu2,'c',3,cle)
        
        for a in range(len(bin_rouge2)):
    
            bin_rouge_final.append(bin_rouge[a][0:Q1] + bin_rouge_crypt[a][0:Q2])
            bin_vert_final.append(bin_vert[a][0:Q1] + bin_vert_crypt[a][0:Q2])
            bin_bleu_final.append(bin_bleu[a][0:Q1] + bin_bleu_crypt[a][0:Q2]) 
            CompteurProgess -= 1      
    else: 
        for a in range(len(bin_rouge2)):

            bin_rouge_final.append(bin_rouge[a][0:Q1] + bin_rouge2[a][0:Q2])
            bin_vert_final.append(bin_vert[a][0:Q1] + bin_vert2[a][0:Q2])
            bin_bleu_final.append(bin_bleu[a][0:Q1] + bin_bleu2[a][0:Q2])
            CompteurProgess -= 1
    
    for p in range(len(bin_rouge_final)):

        entier_rouge_final.append(int(bin_rouge_final[p], 2))
        entier_vert_final.append(int(bin_vert_final[p], 2))
        entier_bleu_final.append(int(bin_bleu_final[p], 2))
        CompteurProgess -= 1
    
    for t in range(len(bin_rouge_final)+35, len(rouge)):
    
        entier_rouge_final.append(rouge[t])

    for f in range(len(bin_vert_final), len(vert)):
    
        entier_vert_final.append(vert[f])
        entier_bleu_final.append(bleu[f])
        CompteurProgess -= 1

    creation_image(largeur, hauteur, entier_rouge_final, entier_vert_final,
                   entier_bleu_final, nom_image)  
    
     
    
    
    
def creation_image(largeur, hauteur, data_rouge, data_vert, data_bleu, nom_image):
    """
    creation_image : Integer * Liste * String -> Image
    creation_image(largeur, hauteur, data_rouge, data_vert, data_bleu, nom_image)
    créé une image selon la largeur, la hauteur, les canaux RGB et le nom de l'image donnée.
    """ 
    nouveau_rouge = pi.new("L",(largeur,hauteur))    
    nouveau_vert = pi.new("L",(largeur,hauteur))  
    nouveau_bleu = pi.new("L",(largeur,hauteur))
    
    nouveau_rouge.putdata(data_rouge)
    nouveau_vert.putdata(data_vert)
    nouveau_bleu.putdata(data_bleu)
    
    nouvelle_image = pi.merge('RGB',(nouveau_rouge, nouveau_vert, nouveau_bleu)) 
    nouvelle_image.save(nom_image)



def reveler(Nom_Image_Cache, nom_image, cryptage, cle):
    """
    reveler : String -> Fonction
    reveler(Nom_Image_Cache, nom_image, cryptage, cle) execute une fonction (creation_image)
    selon les informations qu'il créé. 
    """
    largeur, hauteur, rouge, vert, bleu = infos_image(Nom_Image_Cache)
    
    
    bin_rouge = []
    bin_vert = []
    bin_bleu = []
    
    bin_rouge_final = []
    bin_vert_final = []
    bin_bleu_final = []
    
    entier_rouge_final = []
    entier_vert_final = []
    entier_bleu_final = []
    
    largeur_cache_bin = []
    hauteur_cache_bin = []
    
    qualite_cache_bin = []
    

    for n in range (15):
        
        hauteur_cache_bin.append(bin(rouge[n])[9:])
        
    for nn in range (15):
        largeur_cache_bin.append(bin(rouge[nn+15])[9:])
        
        
    hauteur_cache = (int("".join(hauteur_cache_bin), 2))
    largeur_cache = (int("".join(largeur_cache_bin), 2))
    
    definition = (largeur_cache * hauteur_cache)
    
    
    for ka in range (5):
        qualite_cache_bin.append(bin(rouge[ka+30])[9:])  
    
    qualite_cache = (int("".join(qualite_cache_bin), 2))
    
    
    for k in range(definition):
        
        bin_rouge.append(bin(int(rouge[k+35]))[2:].rjust(8, "0"))
        
        bin_vert.append(bin(int(vert[k]))[2:].rjust(8, "0"))
    
        bin_bleu.append(bin(int(bleu[k]))[2:].rjust(8, "0"))
    
        
    for pa in range(definition):
        
        bin_rouge_final.append(bin_rouge[pa][qualite_cache:].ljust(8, "0"))
    
        bin_vert_final.append(bin_vert[pa][qualite_cache:].ljust(8, "0"))
    
        bin_bleu_final.append(bin_bleu[pa][qualite_cache:].ljust(8, "0"))
     
    if cryptage == "on":
        
        bin_rouge_crypt2 = isn.algo_boucle(bin_rouge_final,'d',1,cle)
        bin_vert_crypt2 = isn.algo_boucle(bin_vert_final,'d',2,cle)
        bin_bleu_crypt2 = isn.algo_boucle(bin_bleu_final,'d',3,cle)
    
        for Ind in range(len(bin_rouge_final)):
    
            entier_rouge_final.append(int(bin_rouge_crypt2[Ind], 2))
            entier_vert_final.append(int(bin_vert_crypt2[Ind], 2))
            entier_bleu_final.append(int(bin_bleu_crypt2[Ind], 2))  
    else: 

        for Ind in range(len(bin_rouge_final)):

            entier_rouge_final.append(int(bin_rouge_final[Ind], 2))
            entier_vert_final.append(int(bin_vert_final[Ind], 2))
            entier_bleu_final.append(int(bin_bleu_final[Ind], 2)) 

    creation_image(largeur_cache, hauteur_cache, entier_rouge_final, 
                   entier_vert_final, entier_bleu_final, nom_image)
