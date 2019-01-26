# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 10:56:34 2018

@author: tanin
"""

def melange_max(lst):
    """
    melange_max : Liste -> Integer
    melange_max(lst) retourne la plus haut exposant 
    de 4 qui correspond au plus près de la longueur de la liste sans la depasser. 
    """
    n = 1
    
    while 4**n <= len(lst):   
        n += 1                #On utilise ce resultat pour faire le maximum de melange lors du cryptage
        
    if n-1 >= 6:              #Si elle est trop grande cela entraine un temps de traitement trop long pour la suite du programme
        n = 6                 #Donc nous la limiton afin que le programme traite des plus petit bout meme si il doit le faire plus de fois
        return n              #Cela permet de gagner un temps considerable
    else:
        return n-1



def clee(mode, n_lst, cle):
    """
    clee : String * Integer  -> Tuple
    clee(mode, n_lst, cle) retourne un tuple de 4 entiers differents entre 0 et 3,
    dont l'odre est generé à partir d'une chaine de caractere.
    """
    
    int_clee = 1
    
    for n in range(len(cle)):
        
        int_clee *= ord(cle[n]) + ord(cle[n])**3
        
    str_cle = str(int_clee) + "2031" 
    ab = [] # mettre cle
    
    for k in range(len(str_cle)):
        
        ab.append(int(str_cle[k]))
           
  
    #1ere
        
    if 0 < ab[8 + n_lst] < 4:
        a1 = ab[8 + n_lst]
    else:
        i = 0
        while ab[i] > 3 or ab[i] == 0:
            i += 1
        a1 = ab[i]
    
    #2eme
    
    if 0 <= ab[5 + n_lst] - ab[9 + n_lst] < 4 and ab[5 + n_lst] - ab[9 + n_lst] != a1 and ab[5 + n_lst] - ab[9 + n_lst] != 1:
                        
        a2 = ab[5 + n_lst] - ab[9 + n_lst]
        
    elif (ab[10 + n_lst] * ab[2 + n_lst]) % (ab[0] + n_lst) < 4 and (ab[10 + n_lst] * ab[2 + n_lst]) % (ab[0] + n_lst) != 1 and (ab[10 + n_lst] * ab[2 + n_lst]) % (ab[0] + n_lst) != a1:
        
        a2 = (ab[10 + n_lst] * ab[2 + n_lst]) % (ab[0] + n_lst)
        
    elif ab[0 + n_lst] % 4 + ab[0 + n_lst] // 4 != 1 and ab[0 + n_lst] % 4 + ab[0 + n_lst] // 4 != a1 and ab[0 + n_lst] % 4 + ab[0 + n_lst] // 4 != 4:
        
        a2 = ab[0 + n_lst] % 4 + ab[0 + n_lst] // 4
               
    else:    
        i = 0
        
        while ab[i] > 3 or ab[i] == 1 or ab[i] == a1:
            i += 1
            
        a2 = ab[i]
        
    #3eme
        
    if 0 <= ab[7 + n_lst] - ab[2 + n_lst] < 4 and ab[7 + n_lst] - ab[2 + n_lst] != a1 and ab[7 + n_lst] - ab[2 + n_lst] != a2 and ab[7 + n_lst] - ab[2 + n_lst] != 2:
        
        a3 = ab[7 + n_lst] - ab[2 + n_lst]
        
    elif (ab[6 + n_lst] * ab[1 + n_lst]) % (ab[0] + n_lst) < 4 and (ab[6 + n_lst] * ab[1 + n_lst]) % (ab[0] + n_lst) != 2 and (ab[6 + n_lst] * ab[1 + n_lst]) % (ab[0] + n_lst) != a1 and (ab[6 + n_lst] * ab[1 + n_lst]) % (ab[0] + n_lst) != a2:
        
        a3 = (ab[6 + n_lst] * ab[1 + n_lst]) % (ab[0]+n_lst)
        
    elif ab[4 + n_lst] % 4 + ab[4 + n_lst] // 4 != 2 and ab[4 + n_lst] % 4 + ab[4 + n_lst] // 4 != 4 and ab[4 + n_lst] % 4 + ab[4 + n_lst] // 4 != a1 and ab[4 + n_lst] % 4 + ab[4 + n_lst] // 4 != a2:
        
        a3 = ab[4 + n_lst] % 4 + ab[4 + n_lst] // 4
               
    else:     
        i = 0
        
        while ab[i] > 3 or ab[i] == 2 or ab[i] == a1 or ab[i] == a2:
            i += 1
            
        a3 = ab[i]
                     
    #4eme
        
    j = 0
    
    while j == a1 or j == a2 or j == a3:
        j += 1
        
    a4 = j
    
        
    if mode == 0:
    
        return (a1, a2, a3, a4)

    else:
        
        if a2 == 0:
            b1 = 1
        elif a3 == 0:
            b1 = 2
        elif a4 == 0:
            b1 = 3
        
        if a1 == 1:
            b2 = 0
        elif a3 == 1:
            b2 = 2
        elif a4 == 1:
            b2 = 3
            
        if a1 == 2:
            b3 = 0
        elif a2 == 2:
            b3 = 1
        elif a4 == 2:
            b3 = 3
        
        if a1 == 3:
            b4 = 0
        elif a2 == 3:
            b4 = 1
        elif a3 == 3:
            b4 = 2
        elif a4 == 3:
            b4 = 3

        return (b1, b2, b3, b4)

def Cryptage(lst, n_lst, cle):
    """
    Cryptage : Liste * Integer * String  -> Liste
    Cryptage(lst, n_lst, cle) retourne une liste de valeur melangé selon la clée.
    """
    
    nbr_melange = melange_max(lst)
    
    a1, a2, a3, a4 = clee(0, n_lst, cle)
    
    lst_fin = lst

    for i in range(nbr_melange):                        #boucle permetant de faire le nombre maximum de melange
               
        lst0 = []
                
        for j in range (0, 4**(nbr_melange), 4**(i+1)):
            lst_temp2 = lst_fin[j:j+4**(i+1)]
                        
            lst0 += lst_temp2[a1*(4**i):(a1+1)*(4**i)]      #Dans cette boucle on execute un melange d'un certain nombre de valeur decouper en blocs
            lst0 += lst_temp2[a2*(4**i):(a2+1)*(4**i)]      #A chaque tour de boucle i un nouveau melange s'effectue, le nombre de valeur contenu dans chaque bloc augmente passe a la puissance superieur de 4.
            lst0 += lst_temp2[a3*(4**i):(a3+1)*(4**i)]      #Donc 4**i est egale à un quart du nombre de valeur contenu dans la liste temporaire lst_temp, autrement dis cela correspond au nombre de valeur dans un bloc etant donné que la liste va etre divisé en quatre bloc.
            lst0 += lst_temp2[a4*(4**i):(a4+1)*(4**i)]      #On veut donc recuperer 4**i, en imaginant que l'on veut le 3 eme quart des valeurs totales, on va prendre les valeurs de 2*4**i à 3*4**i, on aura donc un bloc de 4**i valeurs. Si a1 est egal a 2, le premier bloc de la liste melangé sera le 3 eme bloc allant de l'indice 2*4**i de lst_temp à l'indice 3*4**i de lst_temp soit de a1+1*4**i
                                                                        #En imaginant que a2 = 3, on pourrait se dire qu'il faudrai ecrire a1*4**i et a2*4**i sauf que a1 et a2 sont des variables donc dans un autre cas si a1 = 1 et a2 = 3 alors on aurait un bloc de 2*4**i. 
        lst_fin = lst0
        
    return lst_fin
        

def Decryptage(lst, n_lst, cle):
    """
    Decryptage : Liste * Integer * String  -> Liste
    Decryptage(lst, n_lst, cle) retourne une liste de valeur melangé selon la clée.
    (Si la clée entrer est bonne la liste retourné est dans l'odre initial d'avant le cryptage)
    """
    
    nbr_melange = melange_max(lst)
    
    b1, b2, b3, b4 = clee(1, n_lst, cle)
    
    i = nbr_melange
    
    lst_fin = lst
    
    for x in range(nbr_melange):
        
        i = i - 1
        
        lst0 = []
                
        for j in range (0, 4**(nbr_melange), 4**(i+1)):
            lst_temp2 = lst_fin[j:j+4**(i+1)]
            
            lst0 += lst_temp2[b1*(4**i):(b1+1)*(4**i)]
            lst0 += lst_temp2[b2*(4**i):(b2+1)*(4**i)]
            lst0 += lst_temp2[b3*(4**i):(b3+1)*(4**i)]
            lst0 += lst_temp2[b4*(4**i):(b4+1)*(4**i)]
        
    return lst_fin


def algo_boucle(Lst, mode, n_lst, cle):
    """
    algo_boucle : Liste * String * Integer -> Liste
    algo_boucle(Lst, mode, n_lst, cle) retourne une liste melangé des valeurs 
    de la liste rentrée. 
    """    
    
    nv_data = []
    
    if mode == "c":
        
        while len(Lst) - len(nv_data) >= 4:                 #Boucle permetant de realiser le chiffrement jusqu'à la derniere valeur de la liste.
            lst_temp = Lst[len(nv_data):]                   #création d'une liste temporaire lst_temp qui contient les valeurs restante à cryptées.
            nv_data += Cryptage(lst_temp, n_lst, cle)       #Ajout a la liste nv_data de toute les valeurs crypté par la fonction cryptage qui à crypté lst_temp.
            
        nv_data += Lst[len(nv_data):]                       #Si il reste moins de quatre valeurs elles ne pouront etre crypté,
                                                            # donc ajout des valeurs à nv_data pour qu'elle soit de la meme taille que la liste à crypter.                          
        return nv_data
    
    else:
        
        while len(Lst) - len(nv_data) >= 4:                 #Meme principe que pour le mode cacher "c" mais avec la fonction decryptage.
            lst_temp = Lst[len(nv_data):]
            nv_data += Decryptage(lst_temp, n_lst, cle)
            
        nv_data += Lst[len(nv_data):]
        
        return nv_data
