#!/usr/bin/python3

from random import randint

km_voyage = 300 # Distance à parcourir pour gagner .
km_norm_min = 10 # Distance min. à la vitesse normale .
km_norm_max = 15 # Distance max. à la vitesse normale.
km_rap_min = 20 # Distance min. à toute vitesse.
km_rap_max = 25 # Distance max. à toute vitesse.
avantage_voyageur = 20 # L'avantage initial du voyageur.
gourde_pleine = 12 # Le nombre de gorgées de la gourde.
mort_soif = 4 # Nombre de tours pour mourir de soif.
mort_fatigue = 4 # Nombre de tours pour mourir de fatigue.
dif_aide = 3 # Difficulté pour trouver de l'aide.
avance_natifs = 4 # Vitesse des natifs.
special = 7 # Chance d'avoir un événement (oasis, tempête de sable)

def affiche_debut() -> None :
    print('LE JEU DU CHAMEAU !')
    print()
    print('Vous avez volé un chameau pour traverser le grand désert.')
    print('Les natifs veulent le récupérer.')
    print('Votre objectif est de survivre à la traversée de 300 km sans être attrapé(e).')

def choix_option() :
    print('O P T I O N S :')
    print('1. Boire')
    print('2. Avancer normalement')
    print('3. Avancer à toute vitesse')
    print('4. Repos')
    print("5. Espérer de l'aide")
    print('T . Terminer la partie')
    print()
    option = input("Qu'allez-vous faire ? ")
    condition_fausse = option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != 'T'
    while condition_fausse :
        print('Option invalide !')
        option = input("Qu'allez-vous faire ? ")
        condition_fausse = option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != 'T'
    return option

def boire(nb_gorgees : int, soif : int) :
    if nb_gorgees == 0 :
        print('La gourde est vide.')
        liste = [0,soif]
    else :
        print("Vous avez bu une gorgée.")
        liste = [nb_gorgees-1,0]
    return liste

def avance(vitesse) :
    if vitesse == 'normal' :
        km_parcourus = randint(km_norm_min,km_norm_max)
    else :
        km_parcourus = randint(km_rap_min,km_rap_max)
    return km_parcourus

def avance_norm_voy() :
    km_parcourus = avance('normal')
    print('Vous avez avancé de',km_parcourus,'km.')
    return km_parcourus

def avance_rap_voy() :
    km_parcourus = avance('rapide')
    print('Vous avez avancé de',km_parcourus,'km.')
    return km_parcourus

def repos() :
    print("Votre chameau s’est bien reposé.")
    return 0

def aide(gourde : int, gourde_pleine : int) :
    chance = randint(0,dif_aide)
    gorgees = gourde
    if chance == 0 :
        print("Vous avez trouvé de l'aide.")
        if gourde == gourde_pleine :
            print('La gourde est déjà pleine.')
            gorgees = gourde_pleine
        elif gourde + 3 >= gourde_pleine :
            print("Quelques gorgées ont été ajoutées à votre gourde.")
            gorgees = gourde_pleine
        else :
            print("Quelques gorgées ont été ajoutées à votre gourde.")
            gorgees = gourde + 3 
    else :
        print("Vous n'avez trouvé aucune aide.")
    return gorgees

def avance_des_natifs():
    chance = randint(0,avance_natifs)
    if chance == 0 :
        km = avance('rapide')
    elif chance == 1 :
        km = avance('normal')
    else :
        km = 0
    return km

def niveau_de_soif (soif,gourde) :
    liste_soif = ["Vous n’avez pas soif.",'Vous avez un peu soif.','Vous avez beaucoup soif !','Vous allez mourir de soif ! !']
    print(liste_soif[soif])
    print("Votre gourde contient",gourde,end=" ")
    if gourde > 1 :
        print('gorgée',end=' ')
    else :
        print('gorgées',end=' ')
    print("d'eau.")

def niveau_de_fatigue (fatigue) :
    liste_fatigue = ["Le chameau est en bonne forme.","Le chameau est un peu fatigué.","Le chameau est très fatigué !","Le chameau va mourir de fatigue ! !"]
    print(liste_fatigue[fatigue])

def fin_du_tour (avance_voy,avance_nat,fatigue,soif,gourde):
    print()
    print("Vous avez parcouru un total de",avance_voy,"km jusqu'ici.")
    if avance_voy >= km_voyage :
        print('Bravo !')
        print('Vous avez réussi à survivre et à échaper aux natifs !')
        fin = False    
    elif avance_nat >= avance_voy :
        print('Perdu !')
        print('Les natifs vous ont attrapé !')
        fin = False
    elif soif >= mort_soif :
        print('Les natifs sont à',avance_voy-avance_nat,'km derriére vous')
        print('Perdu !')
        print('Vous êtes mort de soif !')
        fin = False
    elif fatigue >= mort_fatigue :
        print('Les natifs sont à',avance_voy-avance_nat,'km derriére vous')
        niveau_de_soif(soif,gourde)
        print('Perdu !')
        print('Votre chameau est mort de fatigue !')
        print('Les natifs vous ont attrapé !')
        fin = False
    else :
        print('Les natifs sont à',avance_voy-avance_nat,'km derriére vous')
        niveau_de_soif(soif,gourde)
        niveau_de_fatigue(fatigue)
        fin = True
    return fin

def evenement(num,gourde,gourde_pleine,km_natifs) :
    if num == 0 :
        print('Vous êtes chanceux !','Vous avez trouvé un oasis !','Vous remplissez complétement votre gourde et ne perdez pas plus de temps !',sep='\n')
        liste_event = [gourde_pleine,km_natifs]
    else :
        km = km_natifs + avance('normal')
        print('Vous êtes malchanceux !',"Une tempête de sable s'abat sur vous !",'Votre chameau est incontrôlable !',"Vous ne pouvez ni boire, ni espérer de l'aide, ni même vous reposer !","Les natifs eux y sont habitués et continuent d'avancer à vitesse normale !",sep="\n")
        liste_event = [gourde,km]
    return liste_event

def jeu_du_chameaux() :
    continuer = True
    while continuer :
        continuer = False
        affiche_debut()
        km_voyageur = 0 # Distance totale parcourue.
        km_natifs = km_voyageur - avantage_voyageur # Distance parcourue par les natifs.
        gourde = gourde_pleine // 2 # Nombre de gorgés dans l a gourde.
        soif = 0 # Niveau de soif du voyageur.
        fatigue = 0 # Niveau de fatigue du chameau.
        partie_non_fini = True
        while partie_non_fini :
            print()
            chance = randint(0,special)
            if chance <= 1 :
                soif = soif + chance
                liste_event = evenement(chance,gourde,gourde_pleine,km_natifs)
                gourde = liste_event[0]
                km_natifs = liste_event[1]
                partie_non_fini = fin_du_tour(km_voyageur,km_natifs,fatigue,soif,gourde)
            else :
                soif = soif + 1
                option = choix_option()
                # BOIRE
                if option == '1' :
                    liste_boire = boire(gourde,soif)
                    gourde = liste_boire[0]
                    soif = liste_boire[1]
                # AVANCE NORM
                elif option == '2' :
                    km_voyageur = km_voyageur + avance_norm_voy()
                    fatigue = fatigue + 1
                # AVANCE RAP
                elif option == '3' :
                    km_voyageur = km_voyageur + avance_rap_voy()
                    fatigue = fatigue + 2
                # REPOS
                elif option == '4' :
                    fatigue = repos()
                # ESPERER AIDE
                elif option == '5' :
                    gourde = aide(gourde,gourde_pleine)
                else :
                    partie_non_fini = False
                if partie_non_fini :
                    km_natifs = km_natifs + avance_des_natifs()
                    partie_non_fini = fin_du_tour(km_voyageur,km_natifs,fatigue,soif,gourde)
        print()
        nouvelle_partie = input('Voulez-vous jouer une nouvelle partie ? ')
        if nouvelle_partie == 'oui' or nouvelle_partie == 'Oui' :
            continuer = True
        
jeu_du_chameaux()
