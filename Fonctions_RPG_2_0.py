from os import stat, system 
from random import randint
import time
import keyboard
import os
import sys
import pickle

# Fonction qui permet de génerer un Pokémon en fonction de la zone 

def generation_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    if zone == 1:   # ville
        x = randint(0,12)
        if x == 0:
            ennemi_rattata(randint(3,5),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1 :
            ennemi_roucool(randint(3,5),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_roucoups(randint(4,8),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_rattatac(randint(4,8),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_piafabec(randint(3,5),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 5:
            ennemi_rapasdepic(randint(4,8),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 6:
            ennemi_abra(randint(3,5),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 7:
            ennemi_kadabra(randint(4,8),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 8:
            ennemi_soporifik(randint(3,5),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 9:
            ennemi_hypnomade(randint(4,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 10:
            ennemi_voltorbe(randint(3,5),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 11:
            ennemi_mr_mime(randint(3,5),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 12:
            ennemi_porygon(randint(3,5),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
    
    elif zone == 2:    # foret
        x = randint(0,9)
        if x == 0:
            ennemi_chenipan(randint(4,7),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1 :
            ennemi_chrysacier(randint(6,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_aspicot(randint(4,7),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_coconfort(randint(6,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_mystherbe(randint(6,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 5:
            ennemi_ortide(randint(4,7),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 6:
            ennemi_paras(randint(4,7),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 7:
            ennemi_parasect(randint(6,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 8:
            ennemi_builbizarre(randint(4,7),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 9:
            ennemi_herbizarre(randint(6,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
  
    
    elif zone == 3:   # campagne
        x = randint(0,13)
        if x == 0:
            ennemi_nidoran_m(randint(7,11),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1:
            ennemi_nidoran_f(randint(9,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_nidorino(randint(9,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_nidorina(randint(9,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_melofee(randint(7,11),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 5:
            ennemi_melodelfe(randint(9,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 6:
            ennemi_goupix(randint(7,11),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 7:
            ennemi_rondoudou(randint(7,11),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 8:
            ennemi_grodoudou(randint(9,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 9:
            ennemi_persian(randint(9,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 10:
            ennemi_ponyta(randint(7,11),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 11:
            ennemi_galopa(randint(9,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 12:
            ennemi_doduo(randint(7,11),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 13:
            ennemi_dodrio(randint(9,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

    elif zone == 4:   # plage
        x = randint(0,16)
        if x == 0:
            ennemi_carapuce(randint(10,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1:
            ennemi_carabaffe(randint(13,16),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_psykokwak(randint(10,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_akwakwak(randint(13,16),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_ptitard(randint(10,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 5:
            ennemi_tetarte(randint(13,16),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 6:
            ennemi_ramoloss(randint(10,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 7:
            ennemi_flagadoss(randint(13,16),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 8:
            ennemi_kokiyas(randint(10,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 9:
            ennemi_krabby(randint(10,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 10:
            ennemi_krabboss(randint(13,16),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 11:
            ennemi_noeunoeuf(randint(10,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 12:
            ennemi_noadkoko(randint(13,16),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 13:
            ennemi_stari(randint(10,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 14:
            ennemi_Staross(randint(13,16),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 15:
            ennemi_amonita(randint(10,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 16:
            ennemi_amonistar(randint(13,16),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        
        
    elif zone == 5:   # ocean
        x = randint(0,7)
        if x == 0:
            ennemi_tentacool(randint(4,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1:
            ennemi_otaria(randint(4,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_lamantine(randint(4,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_magicarpe(randint(4,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_poissirene(randint(4,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 5:
            ennemi_poissoroy(randint(4,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 6:
            ennemi_hypotrempe(randint(4,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 7:
            ennemi_lockhlass(randint(4,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        
    elif zone == 6:   # desert
        x = randint(0,9)
        if x == 0:
            ennemi_salameche(randint(20,23),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1:
            ennemi_reptincel(randint(23,26),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_ferosinge(randint(20,23),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_sabelette(randint(20,23),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_sablaireau(randint(23,26),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 5:
            ennemi_osselait(randint(20,23),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 6:
            ennemi_ossatueur(randint(23,26),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 7:
            ennemi_rhinocorne(randint(20,23),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 8:
            ennemi_tygnon(randint(23,26),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 9:
            ennemi_kicklee(randint(23,26),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
  
    elif zone == 7:   # grotte
        x = randint(0,14)
        if x == 0:
            ennemi_nosferapti(randint(25,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1:
            ennemi_nosferalto(randint(27,30),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_taupiqueur(randint(25,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
           ennemi_triopiqueur(randint(27,30),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_machoc(randint(25,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 5:
            ennemi_machopeur(randint(27,30),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 6:
            ennemi_racaillou(randint(25,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 7:
            ennemi_gravalanch(randint(27,30),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 8:
            ennemi_magneti(randint(25,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 9:
            ennemi_magneton(randint(27,30),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 10:
            ennemi_fantominus(randint(25,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 11:
            ennemi_Spectrum(randint(27,30),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 12:
            ennemi_onix(randint(27,30),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 13:
            ennemi_kabuto(randint(25,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 14:
            ennemi_kabutops(randint(27,30),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
    
    elif zone == 8:   # safari
        x = randint(0,10)
        if x == 0:
            ennemi_canarticho(25,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1:
            ennemi_excelangue(25,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_leveinard(40,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_kangourex(40,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_tauros(35,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 5:
            ennemi_evoli(15,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 6:
            ennemi_pyroli(35,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 7:
            ennemi_aquali(35,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 8:
            ennemi_pyroli(35,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 9:
            ennemi_ronflex(50,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 10:
            ennemi_raichu(40,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
  
    elif zone == 9:   # foret 2 
        x = randint(0,4)
        if x == 0:
            ennemi_mimitoss(randint(33,36),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1:
            ennemi_aeromite(randint(35,38),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_chetiflor(randint(33,36),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_boustiflor(randint(35,38),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_saquedeneu(randint(35,36),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
  
       
    elif zone == 10:  # montagne
        x = randint(0,6)
        if x == 0:
            ennemi_caninos(randint(40,44),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1:
            ennemi_lippoutou(randint(44,48),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_magmar(randint(40,48),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_elektek(randint(40,48),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_metamorph(randint(40,44),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 5:
            ennemi_minidraco(randint(40,44),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 6:
            ennemi_draco(randint(44,48),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
  
    elif zone == 11:  # egouts
        x = randint(0,4)
        if x == 0:
            ennemi_abo(randint(15,18),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1:
            ennemi_arbok(randint(17,19),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_tadmorv(randint(15,18),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_smogo(randint(15,18),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_smogogo(randint(17,19),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
    
    elif zone == 12:
        x = randint(0,6)
        if x == 0:
            ennemi_dracolosse(55,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 1:
            ennemi_mackogneur(55,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 2:
            ennemi_grolem(55,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 3:
            ennemi_ronflex(55,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 4:
            ennemi_Dracaufeu(55,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 5:
            ennemi_tortank(55,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        elif x == 6:
            ennemi_florizarre(55,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

    

# Fonction qui permet de choisir notre action lors d'un combat , le joueur joue toujours en 1er

def choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle):
    _ = system('cls')
    print(" ")
    print("",nom_ennemi," NIV ",niveau_ennemi,"(",stats_vie_ennemi," PV"" )")
    print(" ")
    print(" Il vous reste",stats_vie_joueur,"/",stats_vie_total_joueur,"PV"" ( NIV",niveau_joueur,")")
    print(" ")
    print(" 1 - Attaquer")
    print(" 2 - Inventaire")
    print(" 3 - Fuir")
    print(" ")
    choix = input(" Que voulez-vous faire ? ""\n")
    if choix == "1" :
        attaque_joueur(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
    elif choix == "2" :
        inventaire(1,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
    elif choix == "3" :
        fuite(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
    else:
        choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)    
    
# Fonction qui permet de choisir son attaque si on a choisi Attaquer

def attaque_joueur(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle):
    _ = system('cls')
    print(" ")
    print("",nom_ennemi," NIV ",niveau_ennemi,"(",stats_vie_ennemi," PV )""\n")
    print(" Il vous reste",stats_vie_joueur,"/",stats_vie_total_joueur,"PV"" ( NIV",niveau_joueur,")""\n")
    print(" 1 - Attaque 1 :",attaque1,)
    print(" 2 - Attaque 2 :",attaque2,)
    print(" 3 - Retour " "\n")
    choix = input(" Que voulez-vous faire ? ""\n")
    if choix == "1":
        if cooldown == 0: # si on choisis l'attaque 1, on commence par vérifier que le cooldown est = a 0 ou a 1 , si c'est 0 on ne peut pas refaire l'attaque , sinon on peut , le cooldown se réinitialise après chaque action en dehos de refaire l'attaque chargée 2 fois d'affilé
            print(" Vous ne pouvez pas refaire cette attaque 2 fois d'affilée .")
            time.sleep(3)
            choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
        elif cooldown == 1:
            cooldown = 0                                                                                                  # le cooldown passe donc à 0 après l'attaque chargé
            degat = effet1 - (effet1//100 * (stats_defense_ennemi//10))                                                   # on calcule les dégats de l'attaque , réduit par la défense ennemie
            critique = randint(0,9)                                                                                       # on fait un randint qui va déterminer si on fait une attaque critique, normale, ou ratée
            if critique == 0 or critique == 1 or critique == 2 or critique ==  3 or critique == 4 or critique == 5:
                degat = degat                                                                                             # 6 chances sur 10 de faire une attaque normale
            elif critique == 6 or critique == 7 or critique == 8:
                degat = degat + (degat//2)                                                                                # 3 chance sur 10 de faire une attaque critique
                print("\n"" COUP CRITIQUE !")
            else:                                                                                                         # 1 chance sur 10 de ratée l'attaque ( réinitlaise le cooldown quand même )
                degat = 0
                print(" Miaouss a raté son attaque .")
                print("")                                                                                                 # si on rate , on appel la fonction qui calcule les dégats de l'adversaire
                cooldown = 1
                calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
            stats_vie_ennemi -= degat  
            if stats_vie_ennemi > 0:                                                                                      # sinon , on regarde si l'attaque met ko , si oui on calcul l'xp gagné tout en remttant le cooldown a 1 pour le prochain combat, si non on appel la fonction qui calcule les dégats de l'adversaire
                print(" Miaouss utilise",attaque1,"et inflige",degat,"dégat(s) ! Le",nom_ennemi,"a maintenant",stats_vie_ennemi,"PV !""\n")
                calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
            else:
                cooldown = 1
                calcul_xp(1,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                

    elif choix == "2": # si on choisit l'attaque 2 , tout marche comme pour l'attaque 1 , à l'exception que quoiqu'il se passe , on remet le cooldown à 1
        degat = effet2 - (effet2//100 * (stats_defense_ennemi//10))
        critique = randint(0,9)
        cooldown = 1
        if critique == 0 or critique == 1 or critique == 2 or critique ==  3 or critique == 4 or critique == 5:
            degat = degat
        elif critique == 6 or critique == 7 or critique == 8:
            degat = degat + (degat//2)
            print(" COUP CRITIQUE !")
        else:
            degat = 0
            print(" Miaouss a raté son attaque .")
            print("")
            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

        stats_vie_ennemi -= degat
        if stats_vie_ennemi > 0:
            print(" Miaouss utilise",attaque2,"et inflige",degat,"dégat(s) ! Le",nom_ennemi,"a maintenant",stats_vie_ennemi,"PV !""\n")
            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
        else:
            cooldown = 1
            calcul_xp(2,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

    elif choix == "3":                          # si vous choisissez Retour , on appel la fonction choix_action
        _ = system('cls')
        print(" ")
        print(" ",nom_ennemi," NIV ",niveau_ennemi,"(",stats_vie_ennemi," PV"" )")
        choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
    else:                                       # si vous tappez autre chose que 1,2,3 , on relance la fonction attaque_joueur pour vous redemandez de choisir 
        print(" Erreur .Réessayez")
        attaque_joueur(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)



#-------------------------------------------------------------------------------------FONCTIONS INVENTAIRE---------------------------------------------------------------------------------------------------------------------



def inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle):
    
    # liste des Pokémons selon leur catégorie , allant des plus petits et faibles , aux plus gros et légendaires

    list_low_pkmn = ["Bulbizarre","Salamèche","Carapuce","Chenipan","Aspicot","Roucool","Rattata","Piafabec","Abo","Sabelette","Nidoran (F)","Nidoran (M)","Goupix","Rondoudou","Nosferapti","Mystherbe","Paras","Mimitoss","Taupiqueur","Psykokwak","Férosinge","Ptitard","Abra","Machoc","Chetiflor","Tentacool","Racaaillou","Ponyta","Ramoloss","Magnéti","Doduo","Otaria","Tadmorv","Kokiyas","Fantominus","Krabby","Voltorbe","Noeunoeuf","Osselait","Smogo","Saquedeneu","Hypotrempe","Poissirène","Stari","Magicarpe","Évoli","Amonita","Kabuto","Minidraco"]
    list_medium_pkmn = ["Herbizarre","Reptincel","Carabaffe","Chrysacier","Coconfort","Roucoups","Rattatac","Rapasdepic","Arbok","Sablaireau","Nidorina","Nidorino","Mélofée","Grodoudou","Nosferalto","Ortide","Parasect","Aéromite","Persian","Caninos","Têtarte","Kadabra","Machopeur","Boustiflor","Magnéton","Canarticho","Dodrio","Spectrum","Soporifik","Excelangue","Rhinocorne","Poissoroy","M.Mime","Scarabrute","Tauros","Métamorph","Porygon","Amonistar"]
    list_high_pkmn = ["Papilusion","Dardargnan","Roucarnage","Raichu","Mélodelfe","Feunard","Rafflesia","Triopiqueur","Akwakwak","Colossinge","Mackogneur","Empiflor","Tentacruel","Gravalanch","Galopa","Flagadoss","Lamantine","Grotadmorv","Crustabri","Ectoplasma","Onix","Hypnomade","Krabboss","Électrode","Noadkoko","Ossatueur","Kicklee","Tygnon","Smogogo","Rhinoféros","Leveinard","Kangourex","Hypocéan","Staross","Insécateur","Lippoutou","Élektek","Magmar","Aquali","Voltali","Pyroli","Kabutops","Ptéra","Draco"]
    list_premium_pkmn = ["Florizarre","Dracaufeu","Tortank","Nidoking","Nidoqueen","Arcanin","Tartard" ,"Alakazam","Grolem","Leviator","Lockhlass","Ronflex","Dracolosse"]
    list_legend_pkmn = ["Mew","Mewtwo,","Sulfura","Électhor","Artikodin"]
    

    Clear()
    if state_inventory == 0:                                                 # La variable state_inventory permet de savoir si on affiche l'invenataire pendant un combat ou non , car il n'affichera pas la même chose
        print(" 1 - Objets")
        print(" 2 - Pokémon")
        print(" 3 - Miaouss")
        print(" 4 - Retour""\n")
    elif state_inventory == 1:
        print(" 1 - Objets")
        print(" 2 - Miaouss")
        print(" 3 - Retour""\n")
    x = input()
    while x != "1" and x != "2" and x != "3" and x!= "4":                    # tant que la valeur entrée n'est pas bonne , on vous redemande une valeur
        print("Valeur Incorrecte.")
        time.sleep(2)
        x = input()
    if x == "1":                                                             # si 1 est choisi , on affiche nos objets
        i = 0
        count_net = 0
        count_potion = 0
        count_super_potion = 0
        count_hyper_potion = 0
        while i < len(list_item):                                            # ici on calcule le nombre d'objets possédés pour chaque type d'objets
            if list_item[i] == "Filet":
                count_net += 1
                i += 1
            elif list_item[i] == "Potion":
                count_potion += 1
                i += 1
            elif list_item[i] == "Super Potion":
                count_super_potion += 1
                i += 1
            elif list_item[i] == "Hyper Potion":
                count_hyper_potion += 1
                i += 1
        print(" 1 - Filet x",count_net)
        print(" 2 - Potion x",count_potion)
        print(" 3 - Super Potion x",count_super_potion)
        print(" 4 - Hyper Potion x",count_hyper_potion)
        print(" 5 - Retour""\n")
        y = input()
        
        while y != "5" and y != "1" and y != "2" and y != "3" and y != "4":             # si valeur incorrecte , on redemande
            print(" Valeur Incorrecte. ")
            time.sleep(2)
            y = input()
        
        if y == "5":        # si on choisis 5, on retourne au menu inventaire
         Clear()
         inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
        
        if y == "1" and state_inventory == 0:       # si on choisis 1 mais qu'on est pas en combat , le filet de capture n'est pas utilisable
            print(" Vous ne pouvez pas utiliser cet objet en dehors d'un combat .")
            time.sleep(3)
            inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
        
#-------------------------------------------------------------------------------------PARTIE CAPTURE DE L'INVENTAIRE---------------------------------------------------------------------------------------------------------------------
        
        if y == "1" and state_inventory == 1: 
            if count_net == 0:          # on regarde d'abord si on en possède
                print("Vous n'avez pas de Filet .")
                time.sleep(2)
                inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
            else:
                print(" Vous voulez utilisé un Filet sur le",nom_ennemi,"ennemi ?""\n")         # on demande vérification , pour être sur que l'on veut utiliser l'objet
                z = input(" Oui ou Non ? ")
                while z.lower() != "oui" and z.lower() != "non":                                # valeur incorrecte = redemande
                        print(" Valeur Incorrecte.")
                        time.sleep(2)
                        z = input()
                
                if z.lower() == "oui":    
                    degat = 0          # si on répond oui , on va calculer le taux de capture en fonction de sa catégorie et de son nombre de points de vie
                    
                    if stats_vie_ennemi == stats_vie_total_ennemi and nom_ennemi in list_low_pkmn:  
                        capture_rate = randint(0,4)
                        if capture_rate == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)         # si on le capture , on calcul l'xp gagné
                            degat = 0
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !") # si non , on réinitiliase le cooldown et on appel la fonction calcul_degat_ennemi
                            print()                                                  # dans tous las cas un filet est dépensée
                            cooldown = 1
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)*10 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*7 and nom_ennemi in list_low_pkmn: # exactement la même chose qu'au dessus et cela jusqu'à la fin de la partie capture , le seul changement étant le taux de capture
                        list_rate = [0,0,0,0,1,1,1,1,1,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            xp_joueur += xp_ennemi
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            print()
                            cooldown = 1
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 7 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*5 and nom_ennemi in list_low_pkmn:
                        list_rate = [0,0,0,0,0,0,1,1,1,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            xp_joueur += xp_ennemi
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" ...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            print()
                            cooldown = 1
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 5 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*2 and nom_ennemi in list_low_pkmn:
                        list_rate = [0,0,0,1]
                        capture_rate = randint(0,3)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            xp_joueur += xp_ennemi
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 2 and nom_ennemi in list_low_pkmn:
                        list_rate = [0,0,0,0,0,0,0,0,0,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            xp_joueur += xp_ennemi
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    








                    if stats_vie_ennemi == stats_vie_total_ennemi and nom_ennemi in list_medium_pkmn:
                        list_rate = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        capture_rate = randint(0,99)
                        if list_rate[capture_rate] == 1:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            xp_joueur += xp_ennemi
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)*10 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*7 and nom_ennemi in list_medium_pkmn:
                        list_rate = [0,0,0,1,1,1,1,1,1,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 7 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*5 and nom_ennemi in list_medium_pkmn:
                        list_rate = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        capture_rate = randint(0,99)
                        if list_rate[capture_rate] == 1:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 5 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*2 and nom_ennemi in list_medium_pkmn:
                        list_rate = [0,0,0,0,0,0,1,1,1,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 2 and nom_ennemi in list_medium_pkmn:
                        list_rate = [0,0,0,0,0,0,0,0,1,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)











                    if stats_vie_ennemi == stats_vie_total_ennemi and nom_ennemi in list_high_pkmn:
                        capture_rate = randint(0,9)
                        if capture_rate == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)*10 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*7 and nom_ennemi in list_high_pkmn:
                        list_rate = [0,0,1,1,1,1,1,1,1,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                            
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 7 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*5 and nom_ennemi in list_high_pkmn:
                        list_rate = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        capture_rate = randint(0,99)
                        if list_rate[capture_rate] == 1:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 5 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*2 and nom_ennemi in list_high_pkmn:
                        list_rate = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        capture_rate = randint(0,99)
                        if list_rate[capture_rate] == 1:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 2 and nom_ennemi in list_high_pkmn:
                        list_rate = [0,0,0,0,0,0,0,1,1,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)












                    if stats_vie_ennemi == stats_vie_total_ennemi and nom_ennemi in list_premium_pkmn:
                        capture_rate = randint(0,19)
                        if capture_rate == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)*10 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*7 and nom_ennemi in list_premium_pkmn:
                        list_rate = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        capture_rate = randint(0,99)
                        if list_rate[capture_rate] == 1:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 7 and stats_vie_ennemi > (stats_vie_total_ennemi//10)*5 and nom_ennemi in list_premium_pkmn:
                        capture_rate = randint(0,3)
                        if capture_rate == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 5 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*2 and nom_ennemi in list_premium_pkmn:
                        list_rate = [0,0,0,0,1,1,1,1,1,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 2 and nom_ennemi in list_premium_pkmn:
                        list_rate = [0,0,0,0,0,0,1,1,1,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)









                     
                    if stats_vie_ennemi == stats_vie_total_ennemi and nom_ennemi in list_legend_pkmn:
                        capture_rate = randint(0,99)
                        if capture_rate == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            print()
                            cooldown = 1
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)*10 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*7 and nom_ennemi in list_legend_pkmn:
                        capture_rate = randint(0,9)
                        if capture_rate == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            print()
                            cooldown = 1
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 7 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*5 and nom_ennemi in list_legend_pkmn:
                        list_rate = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        capture_rate = randint(0,99)
                        if list_rate[capture_rate] == 1:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 5 and stats_vie_ennemi >= (stats_vie_total_ennemi//10)*2 and nom_ennemi in list_legend_pkmn:
                        capture_rate = randint(0,3)
                        if capture_rate == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    
                    if stats_vie_ennemi < (stats_vie_total_ennemi//10)* 2 and nom_ennemi in list_legend_pkmn:
                        list_rate = [0,0,0,0,1,1,1,1,1,1]
                        capture_rate = randint(0,9)
                        if list_rate[capture_rate] == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

                    if nom_ennemi == "Pikachu":
                        capture_rate = randint(0,19)
                        if capture_rate == 0:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" 3...")
                            time.sleep(1)
                            print(" Vous avez capturé le",nom_ennemi,"adverse !")
                            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
                            if money_battle > 0:
                                print("Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                            time.sleep(2)
                            ListPokemonInBag.append(nom_ennemi)
                            calcul_xp(3,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                        else:
                            i = 0
                            while list_item[i] != "Filet":
                             i +=1
                            del list_item[i]
                            print(" 1...")
                            time.sleep(1)
                            print(" 2...")
                            time.sleep(1)
                            print(" Argh..le",nom_ennemi,"s'est échappé du Filet !")
                            cooldown = 1
                            print()
                            calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

                
                if z.lower() == "non": # on retourne au menu invenatire 
                        inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

                

        if y == "2" and state_inventory == 0: # on vérifie l'état de l'inventaire (combat ou non)
            if count_potion == 0:             # on calcule si on a des Potions
                print("Vous n'avez pas de Potion .")
                time.sleep(2)
                inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
            else:
                    if stats_vie_joueur == stats_vie_total_joueur:    # on vérifie si la barre de vie de Miaouss est déjà pleine
                     print(" Miaouss a déjà toute sa vie .")
                     time.sleep(3)
                     inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                    print(" Vous voulez utiliser une Potion sur Miaouss ?",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")        # si non on demande vérification
                    z = input(" Oui ou Non ? ")
                    while z.lower() != "oui" and z.lower() != "non": # si oui on retire 1 Potion de l'inventaire si non : retour au menu inventaire
                        print(" Valeur Incorrecte.")
                        time.sleep(2)
                        z = input()
                    if z.lower() == "oui":
                        i = 0
                        while list_item[i] != "Potion":
                            i +=1
                        del list_item[i]
                        stats_vie_joueur += 20
                        if stats_vie_joueur >= stats_vie_total_joueur:      # on calcule les PV rendu, si ils sont supérieusr ou égaux à ses PV max , alors sa vie = sa vie max 
                            stats_vie_joueur = stats_vie_total_joueur
                            print(" Miaouss a récupéré toute sa vie .")
                            time.sleep(2)
                            inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
                        else:                                               # sinon on affiche combien de PV la Potion lui a rendu et ses PV totaux
                            print(" Miaouss a regagné 20 PV . ",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                            time.sleep(3)
                            inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
                    if z.lower() == "non":
                        inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)


        if y == "2" and state_inventory == 1: # si on est en combat, la seule différence est qu'après utilisation , le Pokémon adverse nous attaque et notre cooldown se réinitialise (car compté comme une action)
            if count_potion == 0:             # et ça sera la même chose pour les autres objets qui ne sont que des Potions de plus en plus forte
                print("Vous n'avez pas de Potion .")
                time.sleep(2)
                inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
            else:   
                if stats_vie_joueur == stats_vie_total_joueur:
                 print(" Miaouss a déjà toute sa vie .")
                 time.sleep(3)
                 choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

                print(" Vous voulez utiliser une Potion sur Miaouss ?",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                z = input(" Oui ou Non ? ")
                while z.lower() != "oui" and z.lower() != "non":
                    print(" Valeur Incorrecte.")
                    time.sleep(2)
                    z = input()
                if z.lower() == "oui":
                    i = 0
                    while list_item[i] != "Potion":
                        i +=1
                    del list_item[i]
                    stats_vie_joueur += 20
                    if stats_vie_joueur >= stats_vie_total_joueur:
                        stats_vie_joueur = stats_vie_total_joueur
                        print(" Miaouss a récupéré toute sa vie .""\n")
                        time.sleep(2)
                        cooldown = 1
                        calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    else:
                        print(" Miaouss a regagné 20 PV . ",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                        time.sleep(3)
                        cooldown = 1
                        calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                if z.lower() == "non":
                    inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)      
        
        if y == "3" and state_inventory == 0:
            if count_super_potion == 0:
                print("Vous n'avez pas de Super Potion .")
                time.sleep(2)
                inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
            else:
                    if stats_vie_joueur == stats_vie_total_joueur:
                     print(" Miaouss a déjà toute sa vie .")
                     time.sleep(3)
                     inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)

                    print(" Vous voulez utiliser une Super Potion sur Miaouss ?",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                    z = input(" Oui ou Non ? ")
                    while z.lower() != "oui" and z.lower() != "non":
                        print(" Valeur Incorrecte.")
                        time.sleep(2)
                        z = input()
                    if z.lower() == "oui":
                        i = 0
                        while list_item[i] != "Super Potion":
                            i +=1
                        del list_item[i]
                        stats_vie_joueur += 50
                        if stats_vie_joueur >= stats_vie_total_joueur:
                            stats_vie_joueur = stats_vie_total_joueur
                            print(" Miaouss a récupéré toute sa vie .")
                            time.sleep(2)
                            inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
                        else:
                            print(" Miaouss a regagné 50 PV . ",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                            time.sleep(3)
                            inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
                    if z.lower() == "non":
                        inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)

        if y == "3" and state_inventory == 1:
            if count_super_potion == 0:
                print("Vous n'avez pas de Super Potion .")
                time.sleep(2)
                inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
            else:   
                if stats_vie_joueur == stats_vie_total_joueur:
                 print(" Miaouss a déjà toute sa vie .")
                 time.sleep(3)
                 choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

                print(" Vous voulez utiliser une Super Potion sur Miaouss ?",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                z = input(" Oui ou Non ? ")
                while z.lower() != "oui" and z.lower() != "non":
                    print(" Valeur Incorrecte.")
                    time.sleep(2)
                    z = input()
                if z.lower() == "oui":
                    i = 0
                    while list_item[i] != "Super Potion":
                        i +=1
                    del list_item[i]
                    stats_vie_joueur += 50
                    if stats_vie_joueur >= stats_vie_total_joueur:
                        stats_vie_joueur = stats_vie_total_joueur
                        print(" Miaouss a récupéré toute sa vie .""\n")
                        time.sleep(2)
                        cooldown = 1
                        calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    else:
                        print(" Miaouss a regagné 50 PV . ",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                        time.sleep(3)
                        cooldown = 1
                        calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                if z.lower() == "non":
                    inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)      
        
        if y == "4" and state_inventory == 0:
             if count_hyper_potion == 0:
                print("Vous n'avez pas d'Hyper Potion .")
                time.sleep(2)
                inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
             else:
                    if stats_vie_joueur == stats_vie_total_joueur:
                     print(" Miaouss a déjà toute sa vie .")
                     time.sleep(3)
                     inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)

                    print(" Vous voulez utiliser une Hyper Potion sur Miaouss ?",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                    z = input(" Oui ou Non ? ")
                    while z.lower() != "oui" and z.lower() != "non":
                        print(" Valeur Incorrecte.")
                        time.sleep(2)
                        z = input()
                    if z.lower() == "oui":
                        i = 0
                        while list_item[i] != "Hyper Potion":
                            i +=1
                        del list_item[i]
                        stats_vie_joueur += 200
                        if stats_vie_joueur >= stats_vie_total_joueur:
                            stats_vie_joueur = stats_vie_total_joueur
                            print(" Miaouss a récupéré toute sa vie .")
                            time.sleep(2)
                            inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
                        else:
                            print(" Miaouss a regagné 200 PV . ",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                            time.sleep(3)
                            inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
                    if z.lower() == "non":
                        inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
        if y == "4" and state_inventory == 1:
             if count_hyper_potion == 0:
                print("Vous n'avez pas d'Hyper Potion .")
                time.sleep(2)
                inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
             else:   
                if stats_vie_joueur == stats_vie_total_joueur:
                 print(" Miaouss a déjà toute sa vie .")
                 time.sleep(3)
                 choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

                print(" Vous voulez utiliser une Hyper Potion sur Miaouss ?",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                z = input(" Oui ou Non ? ")
                while z.lower() != "oui" and z.lower() != "non":
                    print(" Valeur Incorrecte.")
                    time.sleep(2)
                    z = input()
                if z.lower() == "oui":
                    i = 0
                    while list_item[i] != "Hyper Potion":
                        i +=1
                    del list_item[i]
                    stats_vie_joueur += 200
                    if stats_vie_joueur >= stats_vie_total_joueur:
                        stats_vie_joueur = stats_vie_total_joueur
                        print(" Miaouss a récupéré toute sa vie .""\n")
                        time.sleep(2)
                        cooldown = 1
                        calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                    else:
                        print(" Miaouss a regagné 200 PV . ",stats_vie_joueur,"/",stats_vie_total_joueur,"PV""\n")
                        time.sleep(3)
                        cooldown = 1
                        calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
               
                if z.lower() == "non":
                    inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)      


    elif x == "2" and state_inventory == 0: # si on choisit 2 en dehors des combats,on affiche la liste des Pokémon en notre possession
        print(" 0 - Retour")                # on choisit 0 pour retourner au menu inventaire
        j = 0
        while j < len(ListPokemonInBag):
         print("   -",''.join(ListPokemonInBag[j]))
         j += 1
        y = input()
        while y != "0":                     # valeur incorrecte = redemande
            print("\n"" Valeur Incorrecte.")
            time.sleep(2)
            y = input()
        Clear()
        inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
    
    elif x == "2" and state_inventory == 1:                                                             # si on choisit 2 en combat et 3 hors combat on affiche le menu Miaouss avec ses stats
        print("\n"" Miaouss NIV",niveau_joueur,"(",stats_vie_joueur,"/",stats_vie_total_joueur,"PV )")
        print(" Expérience :",xp_joueur,"/",xp_prochain_niveau)
        print(" Stat d'attaque :",stats_attaque_joueur)
        print(" Stat de défense :",stats_defense_joueur)
        print("\n"" < Appuyez sur Entrée pour Quitter >")
        z = input()
        inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

    
    
    elif x == "3" and state_inventory == 0:
        print("\n"" Miaouss NIV",niveau_joueur,"(",stats_vie_joueur,"/",stats_vie_total_joueur,"PV )")
        print(" Expérience :",xp_joueur,"/",xp_prochain_niveau)
        print(" Stat d'attaque :",stats_attaque_joueur)
        print(" Stat de défense :",stats_defense_joueur)
        print("\n"" < Appuyez sur Entrée pour Quitter >")
        z = input()
        inventaire(state_inventory,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)

    elif x == "4" and state_inventory == 0: # si on choisit 4 hors combat n fais retour et on affiche la map
        Clear()
        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
    elif x == "3" and state_inventory == 1:  # si on fais 3 en combat on retourne au menu choix_action
        Clear()
        choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)





# Fonction Fuite qui fais simplement quitter le combat et retour a la map

def fuite(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    print(" Vous fuyez le combat !")
    time.sleep(3)
    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)




# Fonction qui calcule les dégat de l'attaque adverse après notre tour
# Exactement le même fonctionnement que la fonction attaque_joueur

def calcul_degat_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle):
            if cooldown_ennemi == 0:
                            cooldown_ennemi = 1
                            degat = effet_attaque_ennemi2 - (effet_attaque_ennemi2//100 * (stats_defense_joueur//10))
                            critique = randint(0,9)
                            if critique == 0 or critique == 1 or critique == 2 or critique ==  3 or critique == 4 or critique == 5:
                                    degat = degat
                            elif critique == 6 or critique == 7 or critique == 8:
                                degat = degat + (degat//2)
                                print(" COUP CRITIQUE !")
                            else:
                                degat = 0
                                print(" Le",nom_ennemi,"a raté son attaque .")
                                cooldown_ennemi = 1
                                time.sleep(3)
                                choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                            if degat < stats_vie_joueur:
                                stats_vie_joueur -= degat
                                if degat <= 0:
                                    degat = 1
                                print("",nom_ennemi,"utilise",attaque_ennemi_2,"et vous inflige",degat,"dégat(s) ! Il vous reste",stats_vie_joueur,"PV !")
                                time.sleep(4)
                                choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                            elif degat >= stats_vie_joueur:
                                print(" Le",nom_ennemi,"utilise",attaque_ennemi_2,"et vous inflige",degat,"dégat(s) ! Vous êtes KO .")
                                time.sleep(3)
                                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
            elif cooldown_ennemi == 1:
                    attaque_ennemi = randint(1,2)
                    if attaque_ennemi == 1:
                            cooldown_ennemi = 0
                            degat = effet_attaque_ennemi1 - (effet_attaque_ennemi1//100 * (stats_defense_joueur//10))
                            critique = randint(0,9)
                            if critique == 0 or critique == 1 or critique == 2 or critique ==  3 or critique == 4 or critique == 5:
                                    degat = degat
                            elif critique == 6 or critique == 7 or critique == 8:
                                degat = degat + (degat//2)
                                print(" COUP CRITIQUE !")
                            else:
                                degat = 0
                                print(" Le",nom_ennemi,"a raté son attaque .")
                                cooldown_ennemi = 1
                                time.sleep(3)
                                choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                            if degat < stats_vie_joueur:
                                stats_vie_joueur -= degat
                                if degat <= 0:
                                    degat = 1
                                print("",nom_ennemi,"utilise",attaque_ennemi_2,"et vous inflige",degat,"dégat(s) ! Il vous reste",stats_vie_joueur,"PV !")
                                time.sleep(4)
                                choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                            elif degat >= stats_vie_joueur:
                                print(" Le",nom_ennemi,"utilise",attaque_ennemi_2,"et vous inflige",degat,"dégat(s)! Vous êtes KO .")
                                time.sleep(3)
                                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    elif attaque_ennemi == 2: 
                            cooldown_ennemi = 1
                            degat = effet_attaque_ennemi2 - (effet_attaque_ennemi2//100 * (stats_defense_joueur//10))
                            critique = randint(0,9)
                            if critique == 0 or critique == 1 or critique == 2 or critique ==  3 or critique == 4 or critique == 5:
                                    degat = degat
                            elif critique == 6 or critique == 7 or critique == 8:
                                degat = degat + (degat//2)
                                print(" COUP CRITIQUE !")
                            else:
                                degat = 0
                                print(" Le",nom_ennemi,"a raté son attaque .")
                                cooldown_ennemi = 1
                                time.sleep(3)
                                choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                            if degat < stats_vie_joueur:
                                stats_vie_joueur -= degat
                               
                                if degat <= 0:
                                    degat = 1
                                print("",nom_ennemi,"utilise",attaque_ennemi_2,"et vous inflige",degat,"dégat(s) ! Il vous reste",stats_vie_joueur,"PV !")
                                time.sleep(4)
                                choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
                            elif degat >= stats_vie_joueur:
                                print(" Le",nom_ennemi,"utilise",attaque_ennemi_2,"et vous inflige",degat,"dégat(s) ! Vous êtes KO .")
                                time.sleep(3)
                                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                               

# Fonction qui calcule l'xp gagné après un combat gagner ou une capture réussie


def calcul_xp(state_attack,degat,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle):
        
        if state_attack == 1:                                                                               # cette partie si on met KO avec l'attaque chargée
            print(" Miaouss utilise",attaque1,"et inflige",degat,"dégat(s) ! Le",nom_ennemi,"est KO .")
            xp_joueur += xp_ennemi                                                                          # on rajoute l'xp ennemi à la notre 
            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
            if xp_joueur >= xp_prochain_niveau:         # si l'xp gagné dépasse le necéssaire pour passer au prochain niveau, alors on calcule l'xp nécessaire pour celui d'après tout en gardant le surplus si il y en a eu
                niveau_joueur += 1                                                                          
                xp_joueur = xp_joueur - xp_prochain_niveau
                xp_prochain_niveau = xp_prochain_niveau + ((xp_prochain_niveau//10) * niveau_joueur)
                print(" Miaouss passe au niveau",niveau_joueur,"!")             # ici on calcule les nouvelles stats de Miaouss
                ancienne_stats_attaque = stats_attaque_joueur
                stats_attaque_joueur += (stats_attaque_joueur//10)
                
                ancienne_stats_defense = stats_defense_joueur
                stats_defense_joueur += (stats_defense_joueur//10)

                ancienne_stats_vie_total = stats_vie_total_joueur
                stats_vie_total_joueur += (stats_vie_total_joueur//10)
                stats_vie_joueur = stats_vie_total_joueur

                print(" Les stats de Miaouss augmentent :" )
                print("",ancienne_stats_attaque,"→",stats_attaque_joueur,"ATK""\n",ancienne_stats_defense,"→",stats_defense_joueur,"DEF""\n",ancienne_stats_vie_total,"→",stats_vie_total_joueur,"PV""\n")
                print(" Ses PV sont régénérés :",stats_vie_joueur,"/",stats_vie_total_joueur,"PV")
                if money_battle > 0:
                                print("\n"" Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                x = input()
                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
            
            else:                       # si pas de niveau passé , on retourne a la map
                if money_battle > 0:
                                print("\n"" Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                time.sleep(4)
                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
       
       
        elif state_attack == 2:                                                                             # exactement la meme chose mais avec l'attaque 2
            print(" Miaouss utilise",attaque2,"et inflige",degat,"dégat(s) ! Le",nom_ennemi,"est KO .")
            xp_joueur += xp_ennemi
            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
            if xp_joueur >= xp_prochain_niveau:
                niveau_joueur += 1
                xp_joueur = xp_joueur - xp_prochain_niveau
                xp_prochain_niveau = xp_prochain_niveau + ((xp_prochain_niveau//10) * niveau_joueur)
                print(" Miaouss passe au niveau",niveau_joueur,"!")
                ancienne_stats_attaque = stats_attaque_joueur
                stats_attaque_joueur += (stats_attaque_joueur//10)
                
                ancienne_stats_defense = stats_defense_joueur
                stats_defense_joueur += (stats_defense_joueur//10)

                ancienne_stats_vie_total = stats_vie_total_joueur
                stats_vie_total_joueur += (stats_vie_total_joueur//10)
                stats_vie_joueur = stats_vie_total_joueur

                print(" Les stats de Miaouss augmentent :" )
                print("",ancienne_stats_attaque,"→",stats_attaque_joueur,"ATK""\n",ancienne_stats_defense,"→",stats_defense_joueur,"DEF""\n",ancienne_stats_vie_total,"→",stats_vie_total_joueur,"PV""\n")
                print(" Ses PV sont régénérés :",stats_vie_joueur,"/",stats_vie_total_joueur,"PV")
                if money_battle > 0:
                                print("\n"" Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                x = input()
                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
            else:
                if money_battle > 0:
                                print("\n"" Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                time.sleep(4)
                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
       
        elif state_attack == 3:                                                                     # pareil mais après une capture réussis
            xp_joueur += xp_ennemi
            print(" Vous avez gagné ! +",xp_ennemi,"XP (",xp_joueur,"/",xp_prochain_niveau,")""\n")
            if xp_joueur >= xp_prochain_niveau:
                niveau_joueur += 1
                xp_joueur = xp_joueur - xp_prochain_niveau
                xp_prochain_niveau = xp_prochain_niveau + ((xp_prochain_niveau//10) * niveau_joueur)
                print(" Miaouss passe au niveau",niveau_joueur,"!")
                ancienne_stats_attaque = stats_attaque_joueur
                stats_attaque_joueur += (stats_attaque_joueur//10)
                
                ancienne_stats_defense = stats_defense_joueur
                stats_defense_joueur += (stats_defense_joueur//10)

                ancienne_stats_vie_total = stats_vie_total_joueur
                stats_vie_total_joueur += (stats_vie_total_joueur//10)
                stats_vie_joueur = stats_vie_total_joueur

                print(" Les stats de Miaouss augmentent :" )
                print("",ancienne_stats_attaque,"→",stats_attaque_joueur,"ATK""\n",ancienne_stats_defense,"→",stats_defense_joueur,"DEF""\n",ancienne_stats_vie_total,"→",stats_vie_total_joueur,"PV""\n")
                print(" Ses PV sont régénérés :",stats_vie_joueur,"/",stats_vie_total_joueur,"PV")
                if money_battle > 0:
                                print("\n"" Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                x = input()
                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
            else:
                if money_battle > 0:
                                print("\n"" Vous volez",money_battle,"₽ au Dresseur ! ")
                                bank_account += money_battle
                time.sleep(4)
                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)



# Fonction pas encore utilisé mais qui servira pour les Promotions de Miaouss


def niveau_superieur(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    if niveau_joueur == 10:
        print("Oh ? Miaouss évolue !")
        print("Il devient Racket Miaouss !")
        x = input
        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
    elif niveau_joueur == 20:
        print("Oh ? Miaouss évolue !")
        print("Il devient Miaouss Officier Racket !")
        x = input
        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
    elif niveau_joueur == 30:
        print("Oh ? Miaouss évolue !")
        print("Il devient Miaouss Giovanni !")
        x = input
        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
    else:
        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        
# Fonction dans le cas ou on perd

def game_over():
    print(" t'es nul")

# Fonction Clear

def Clear():
    os.system('cls')

#-------------------------------------------------------------------------------------FONCTIONS MAP/MOUVEMENT---------------------------------------------------------------------------------------------------------------------

# Fonction qui permet d'afficher les maps ligne par ligne

def LineByLine(map):
    i = 0
    while i < len(map):
        print(" ".join(map[i]))
        i += 1
    print("")


# Fonctions qui détecte les pressions sur les touches 

def Movement(MoveValue):

    if keyboard.is_pressed("up"):
        MoveValue[0] = 1 
        
    if keyboard.is_pressed("down"): 
        MoveValue[0] = 2
        
    if keyboard.is_pressed("left"): 
        MoveValue[0] = 3
        
    if keyboard.is_pressed("right"): 
        MoveValue[0] = 4

    if keyboard.is_pressed("i"):
        MoveValue[0] = 5
    
    if keyboard.is_pressed("l"):
        MoveValue[0] = 6

    if keyboard.read_key() == 'm':
        MoveValue[0] = 7

# les différentes maps

map_ville = [   ["■","■","■","■","■","■","■","F","F","■","■","■","■","■","■","■"], 
                ["■"," "," "," "," "," ","■"," "," "," "," ","■"," "," ","R","■"],
                ["■"," "," "," "," "," ","■"," "," ","■"," ","■"," ","■","■","■"], 
                ["■","■","■"," ","■","■","■"," "," ","■"," "," "," ","■","H","■"], 
                ["■","H","H"," ","H","H","H"," "," ","■","■","■","■","■","H","■"],
                ["■","H","H"," ","H","H","H"," "," ","H","H","H","H","D","H","■"],
                ["F"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","Z"],
                ["F"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","Z"],
                ["F"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","Z"],
                ["■","H","D","H","H","H"," "," "," ","H","H","H","H","H","H","■"],
                ["■","■","■","H","H","H"," "," "," ","H","H","H","H","H","H","■"],
                ["■"," ","■"," "," "," "," "," "," ","H","H","H","H","T","T","■"],
                ["■"," ","■"," "," "," "," "," "," ","H","■","■","■","■","■","■"],
                ["■","■","■","■","■"," ","H"," "," "," "," "," "," "," ","D","■"],
                ["■","E"," "," "," "," ","H"," "," ","H","■"," "," "," "," ","■"],
                ["■","■","■","■","■","■","■","P","P","■","■","■","■","■","■","■"]]

map_foret = [   ["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"],
                ["■","H","H","H","H","H","H","H","H","■","H","H","H","H","H","■"],
                ["■","H","H","H","H","H","H","H","H","■","H","H","H","H","H","■"],
                ["■","H","H","■","■","■","■","■","H","■","H","H","H","H","H","■"],
                ["■","H","H","■","L","L","L","■"," "," "," "," "," "," ","D","■"],
                ["■","H","H","■","L","L","L","■"," "," "," "," "," "," "," ","■"],
                ["■","H","H","■","■","L","■","■"," "," "," "," "," "," "," ","V"],
                ["■","H","H","H","■","L","■","■","■","■","■"," "," "," "," ","V"],
                ["■"," "," "," ","■","L","■"," "," "," ","■"," "," "," "," ","V"],
                ["■"," "," "," ","■","L","■","D"," ","■","■"," "," "," "," ","■"],
                ["■","D","■"," ","■","L","■"," "," ","■","■"," ","H","■","■","■"],
                ["■","■","■"," ","■","■","■"," "," "," "," "," ","H","H","H","■"],
                ["C"," "," "," ","H","H","■","H","■","H","H","H","H","H","H","■"],
                ["C"," "," "," ","■","H","■","H","■","H","H","H","H","H","H","■"],
                ["C"," "," "," ","■","H","H","H","■","H","H","H","H","H","H","■"],
                ["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"]]

map_plage = [   ["■","■","■","■","■","■","■","V","V","■","■","■","■","■","■","■"], 
                ["■"," "," "," "," "," "," "," "," "," "," "," ","H","H","H","■"],
                ["■"," "," ","D"," "," "," "," "," "," "," ","H","H","H","H","■"], 
                ["■"," "," "," "," "," "," ","H","H","H"," "," ","H","H","H","■"], 
                ["■","H","H"," "," "," ","H","H","H","H"," "," "," ","H"," ","■"],
                ["■","H","H"," "," "," ","H","H"," "," "," "," "," ","D"," ","■"],
                ["■","H","H","H"," "," "," "," "," "," ","H","H"," "," "," ","■"],
                ["■","H","H","H"," "," ","H","H","H"," ","H","H","H"," "," ","■"],
                ["■","H","H"," "," "," ","H","H","H"," ","H","H","H"," "," ","■"],
                ["■"," ","H"," "," ","H","H","H","H"," "," ","H","H","H"," ","■"],
                ["■"," "," "," "," ","H","H","H"," "," "," "," ","H","H"," ","■"],
                ["■"," ","D"," "," "," "," "," "," "," "," "," "," "," "," ","■"],
                ["■"," "," "," "," "," "," "," ","O","O"," "," "," "," "," ","■"], 
                ["■"," "," ","O","O"," ","O","O"," "," ","O"," ","O","O"," ","■"],
                ["■"," ","O"," "," ","O"," "," "," "," "," ","O"," "," ","O","■"],
                ["■","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","■"],]

map_ocean = [   ["■","P","P","P","P","P","P","P","P","P","P","P","P","P","P","■"], 
                ["■"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"],
                ["■","H","H"," "," "," "," "," "," "," "," "," "," "," "," ","■"], 
                ["■","H","H"," "," "," "," "," "," "," "," "," "," "," "," ","■"], 
                ["■","H","H","H"," "," ","D"," "," ","H","H"," "," ","D"," ","■"],
                ["■"," ","H","H"," "," "," "," ","H","H","H","H"," "," "," ","■"],
                ["■"," ","H","H"," "," "," "," "," ","H","H"," "," "," "," ","■"],
                ["■"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"],
                ["■"," "," ","D"," "," "," "," "," "," "," "," "," ","H"," ","■"],
                ["■","H"," "," "," "," "," ","H","H","H"," "," ","H","H","H","■"],
                ["■","H","H"," "," ","H","H","H","H","H","H"," ","H","H","H","■"],
                ["■","H","H"," "," ","H","H","H","H","H","H","H"," ","H"," ","■"],
                ["■","H","h","H"," "," ","H","H","H","H","H","H","H"," "," ","■"],
                ["■","H","H","H"," "," "," ","H","H","H","H","H"," "," "," ","■"],
                ["■"," ","H","H"," "," "," "," "," "," "," "," "," "," "," ","■"],
                ["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"],]


map_campagne = [["■","S","S","■","■","■","■","■","■","■","■","■","■","■","■","■"], 
                ["■"," "," ","■","H","H","H"," "," "," ","H","H","H","H","D","■"],
                ["■"," "," ","■","H","H","H"," "," "," ","H","H","H","■","■","■"], 
                ["■"," "," ","■","H","H","H"," "," ","■","H","H","H","■","M","■"], 
                ["■"," "," "," ","H","H","H"," "," ","■","H","H","H","■","■","■"],
                ["■"," "," "," ","H","H","H"," "," ","■","H","H","H","H","H","■"],
                ["■","■","■","■","■","■","■"," "," ","■","■","■","■","■","■","■"],
                ["■"," "," "," "," "," ","D"," "," "," "," "," "," ","H","H","■"],
                ["■"," "," "," "," "," "," "," "," "," "," "," "," ","H","H","■"],
                ["■"," "," "," ","H","H","H","H","H","■","■","■"," ","H","H","■"],
                ["■"," "," "," ","H","H","H","H","H","■","M","■"," ","H","H","■"],
                ["■","■","■"," ","■","■","■","■","■","■","■","■"," "," ","■","■"],
                ["■","H","H"," "," "," "," "," "," "," "," "," "," "," "," ","F"],
                ["■","H","H","H"," "," "," "," "," "," "," "," "," "," "," ","F"],
                ["■","H","H","H","H"," "," "," "," ","D"," "," "," "," "," ","F"],
                ["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"]]


map_safari = [  ["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"], 
                ["■","H"," ","H","■","H","H","H","H","H","H","H","H","H"," ","■"],
                ["■","H"," ","H","■","H"," ","H","H","H","H","H","H","H","H","■"],
                ["■","H"," ","H","■","H"," ","H","H","H","H","H","H","H","H","■"],
                ["■","H"," ","H","■","H"," "," "," "," "," "," "," ","H","H","■"],
                ["■","H"," ","H","■","H"," ","■","■","■","■"," "," ","H","H","■"],
                ["■","H"," ","H","H","H"," ","■","L","L","■"," "," ","H","H","■"],
                ["■","H"," "," "," "," "," ","■","■","■","■","■"," ","H","H","■"],
                ["■","H","H","H","H","H"," "," "," "," "," "," "," "," ","H","■"],
                ["■","■","■","■","■","■","H","H","H","H","H","H","H"," ","H","■"],
                ["■","H","H","H","H","■","■","■","H","H","H","H","H"," ","H","■"],
                ["■","H","H","H","H","■","H","H","H","H","H"," "," "," ","H","■"],
                ["■"," "," ","■","H","■","H","H","H","H","H"," ","H","H","H","■"],
                ["■"," "," ","■","H","H"," "," "," "," "," "," ","H","H","H","■"],
                ["■"," "," ","■","H","H"," "," ","H","H","H","H","H","H","H","■"],
                ["■","C","C","■","■","■","■","■","■","■","■","■","■","■","■","■"]]


map_desert =   [["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"], 
                ["■","H","H"," "," "," ","H","H","H","H","H"," "," "," ","D","■"],
                ["■","H","H"," "," "," ","H","H","H","H","H","■","■"," "," ","■"], 
                ["■","H","H"," "," "," "," "," "," "," "," ","■","■"," "," ","■"], 
                ["■","H","H","■","■","H","H"," "," "," "," "," "," ","H","H","■"],
                ["■","H","H","■","■","H","H"," ","H","H"," "," "," ","H","H","■"],
                ["V"," "," ","■","■","H","H"," ","H","H"," "," "," ","H","H","■"],
                ["V"," "," ","■","■","H","H"," ","H","H"," "," "," ","H","H","■"],
                ["V"," "," ","H","H","H","H"," "," "," ","■","■","■"," "," ","■"],
                ["■"," "," "," "," "," "," "," "," ","D","■","■","■"," "," ","■"],
                ["■"," "," "," "," "," "," "," "," "," ","■","■","■"," "," ","■"],
                ["■","H","H","H"," "," ","■","■"," "," "," "," "," ","■","■","■"],
                ["■","H","H","H"," "," ","■","■"," ","H","H","H","H","H","H","■"],
                ["■","H","H","■"," "," "," "," "," ","H","H","H","H","■"," ","■"],
                ["■","H","H","■","D"," "," "," "," ","H","H","H","H","■"," ","G"],
                ["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"]]


map_grotte =   [["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"], 
                ["■","H","D","■","■","H","H","H"," "," "," ","H","H","H","H","■"],
                ["■","H","H","■","H","H","H","H"," "," "," ","H","H","H","H","■"], 
                ["■","H","H","■","H","H","H","■","■","■","■","■","H","H","H","■"], 
                ["■","H","H","H","H","H","H","■","H","H","H","■","■","■","H","■"],
                ["■"," "," ","■"," "," "," ","■","H","H","H"," "," "," "," ","■"],
                ["■"," "," ","■"," "," "," ","■","H","H","H","■","■"," "," ","■"],
                ["■"," "," ","■","H","H","H","■","■"," "," ","■","■"," "," ","■"],
                ["■","H","H","■","■","H","H","H","■"," ","D","■","■","H","H","■"],
                ["■","H","H","H","■","H","H","H","■"," "," ","■","■","H","H","■"],
                ["■","H","H","H","H","H","H","H","■"," "," "," "," "," "," ","■"],
                ["■","H","■","■","■"," ","■","■","■","H","H","■","H","H","H","■"],
                ["■","H","■","H","H"," "," "," "," ","H","H","■","■","■","H","■"],
                ["■"," ","■","H","H"," "," "," "," "," ","H","H","H","■"," ","■"],
                ["D"," ","■","H","H"," "," "," "," "," ","H","H","H"," ","D","■"],
                ["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"]]


map_foret_2 =  [["■","■","■","■","■","■","■","M","M","■","■","■","■","■","■","■"], 
                ["■","H","D","H","H","■"," "," "," ","■","H","H","H"," ","D","■"],
                ["■","H","H","H","H","H"," "," "," ","H","H","H","H"," "," ","■"], 
                ["■","H","H","H","H","H"," "," "," ","■","■","■","■","■","■","■"], 
                ["■","H","H","H","H","H"," "," "," "," "," "," "," "," "," ","■"],
                ["■","H","H","H","H","■","■","■","■","■","■","■","■","H","H","■"],
                ["■","■","■","■","■","■","■","■","■","■","H","H","H","H","H","■"],
                ["■","D"," "," ","H","H","H","H","■","■","H","H","H","H","H","■"],
                ["■"," "," "," ","■","H","H","H","H","■","H","H","H","H","H","■"],
                ["■"," "," "," ","■","■","H","H","H","■","H","H","H","H","H","■"],
                ["■"," "," "," "," ","■","H","H","H"," "," "," "," "," "," ","■"],
                ["■","■","H","H","■","■","■","■","H"," "," "," "," "," "," ","■"],
                ["■","H","H","H","H","H","■","■","■","■","H","H","H","H","H","■"],
                ["■","H","H","H","H","H"," "," "," ","■","H","H","H","H","H","■"],
                ["■","H","H","H","H","H","■"," "," ","■","H","H","H","H","H","■"],
                ["■","■","■","■","■","■","■","V","V","■","■","■","■","■","■","■"]]


map_montagne = [["■","■","P","■","■","■","■","■","■","■","■","■","■","■","■","■"], 
                ["■"," "," "," ","■","■"," "," "," "," "," "," "," "," "," ","■"],
                ["■"," "," "," ","■","■"," "," "," ","■","■","■","■","H","H","■"], 
                ["■","H","H","H","■","■","D"," "," ","■","■","■","■","H","H","■"], 
                ["■","H","H","H","H","H"," "," "," ","H","H","■","■","H","H","■"],
                ["■","H","H","H","H","H"," "," "," ","H","H","■","■","H","H","■"],
                ["■","■","■","■","H","H"," "," "," ","H","H","■","■","H","D","■"],
                ["■","■","■","■"," "," ","■","■"," ","H","H","■","■","■","■","■"],
                ["■","■","■","■"," "," ","■","■"," ","H","H","■","■","■","■","■"],
                ["■","H","H","H"," ","D","■","■"," "," "," "," "," ","H","H","■"],
                ["■","H","H","H"," "," "," "," "," "," "," "," "," ","H","H","■"],
                ["■","■","■","H","■","■","■","■","■","■","■","■","■","H","■","■"],
                ["■","H","H","H","■","■"," "," "," "," ","■","■","■","H","H","■"],
                ["■","H","H","■","■"," "," "," "," "," "," ","H","H","H","H","■"],
                ["■","H","H","H","H"," "," "," "," "," "," ","■","■","H","H","■"],
                ["■","■","■","■","■","■","■","F","F","■","■","■","■","■","■","■"]] 



map_pic =      [["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"], 
                ["■","H","H","H","■"," "," ","■","■","■","■","A","■","■","■","■"],
                ["■","H","■"," ","■"," "," ","■","H","H","H"," ","■"," "," ","R"], 
                ["■","H","■","S","■"," ","H","H","H","■","■","■","■","H","■","■"], 
                ["■","H","■","■","■","■","H","H","H","■"," "," ","■","H","H","■"],
                ["■"," "," "," "," ","■","H","H","■","■"," "," ","■","■","H","■"],
                ["■"," "," "," "," ","■","H","H","H"," "," "," ","■","H","H","■"],
                ["■"," "," "," "," ","■","H","H","H"," "," "," ","■","H","■","■"],
                ["■","H","H","■","■","■","■","■","■"," "," "," ","■","H","H","■"],
                ["■","H","H","H","H","H"," ","E","■"," "," "," ","■","■","H","■"],
                ["■","H","H","H","H","■","■","■","■","H","H","H","■","H","H","■"],
                ["■","H","H","H","■","■"," "," "," ","H","H","H","■","H","■","■"],
                ["■"," "," "," ","H","H"," "," "," ","H","H","H","■","H","H","■"],
                ["■"," "," "," ","■","■","■"," "," "," "," "," ","■","■","H","■"],
                ["■"," "," "," ","■","■","■","■"," "," "," "," ","H","H","H","■"],
                ["■","■","M","■","■","■","■","■","■","■","■","■","■","■","■","■"]]


map_egout = [   ["■","■","■","■","■","■","■"], 
                ["■","D"," "," "," "," ","■"], 
                ["■"," "," ","■","H","H","■"], 
                ["■","■","■","■","H","H","■"], 
                ["■","H","H","H","H","H","■"],
                ["■","H","H","H","H","H","■"],
                ["■","H","H","■","■","■","■"],
                ["■","H","H","H"," "," ","■"],
                ["■"," "," ","■"," "," ","■"],
                ["■"," "," ","■"," ","V","■"],
                ["■","■","■","■","■","■","■"]]


map_red = [["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"],
           ["■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","R"," ","■"],
           ["P"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","E"," ","■"],
           ["■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","D"," ","■"],
           ["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"]]



qg_racket = [ ["■","■","■","■","■","■","■"], 
              ["■"," "," "," "," "," ","■"], 
              ["■"," "," "," "," "," ","■"], 
              ["■"," "," "," "," "," ","■"], 
              ["V"," "," "," "," ","M","■"],
              ["V"," "," "," "," "," ","■"],
              ["V"," "," "," "," ","E","■"],
              ["■"," "," "," "," "," ","■"],
              ["■"," "," "," "," "," ","■"],
              ["■"," "," ","L"," "," ","■"],
              ["■","■","■","■","■","■","■"],
    ]




X = 7
Y = 7


map = map_ville



# Fonction qui va définir tout ce qui est faisable sur la map actuelle


def map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    Clear()
    SpawnPlayer = map[X][Y] = "P"       # on fait apparaitre le joueur aux coordonnées X en tant que lettre P
    spawn = randint(0,7)                # on fait un randint qui va définir si un Pokémon va spawn si on se trouve dans un buisson 
    if state_spawn_pkmn == 1 and spawn == 0 and fight == 1: # on vérifie qu'on soit bien sur un buisson , que le Pokémon peut apparaitre et qu'a bien changer de case , si tout est bon alors un combat contre un Pokémon de la zone se lance
        fight = 0
        Clear()
        LineByLine(map)
        print(" Vous êtes attaqué ! ")
        time.sleep(2.5)
        generation_ennemi(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
    else:                                                       # sinon on se déplace juste en affichant la map et les infos nécessaire en dessous
        LineByLine(map)
        print(" Vous êtes dans la Zone",zone,".""\n")
        print(" Compte en banque :",bank_account,"₽""\n")
        print(" Appuyez sur < i > pour Ouvrir l'Inventaire")
        print(" Appuyez sur < m > pour Ouvrir le Menu")
        print(" Appuyez sur < l > pour Ouvrir la Légende")
        while True:
            MoveValue = [0]
            Movement(MoveValue)
        
            if MoveValue[0] == 1:                                              # on regarde quelle touche a été utilisé , si c'est un déplacement alors on regarde ce qu'il y a dans la direction du déplacement
                time.sleep(0.1)
                if map[X-1][Y] == "■":                                         # on vérifie si la prochaine case est un mur 
                    Clear()
                    LineByLine(map)
                    print(" Vous ne pouvez pas traverser le mur !""\n")
                    print(" Vous êtes dans la Zone",zone,".""\n") 
                    print(" Compte en banque :",bank_account,"₽""\n")
                    print(" Appuyez sur < i > pour Ouvrir l'Inventaire")
                    print(" Appuyez sur < m > pour Ouvrir le Menu")
                    print(" Appuyez sur < l > pour Ouvrir la Légende")
                
                elif map[X-1][Y] == "H":                                       # on vérifie si la prochaine case est un buisson
                 if state_spawn_pkmn == 0:                                     # si la case d'avant était vide alors on affiche du vide derrière nous
                    map[X][Y] = " "
                    X -= 1
                    map[X][Y] = "P"
                    state_spawn_pkmn = 1
                    fight = 1
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                 elif state_spawn_pkmn == 1:                                   # sinon on re-affiche une case buisson H ( pour herbe)
                    map[X][Y] = "H"
                    X -= 1
                    map[X][Y] = "P"
                    state_spawn_pkmn = 1
                    fight = 1
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    

                elif map[X-1][Y] == "P" and zone == 5:                                       # si la prochaine case est un P , alors cela veut dire que l'on passe dans la map Plage
                    map[X][Y] = " "
                    Clear()
                    map = map_plage
                    X = 11
                    zone = 4
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X-1][Y] == "S":                                       # si la prochaine case est un P , alors cela veut dire que l'on passe dans la map Plage
                    map[X][Y] = " "
                    Clear()
                    map = map_safari
                    X = 14
                    zone = 8
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                

                elif map[X-1][Y] == "F":                                       # si la prochaine case est un P , alors cela veut dire que l'on passe dans la map Plage
                    map[X][Y] = " "
                    Clear()
                    map = map_foret_2
                    X = 14
                    zone = 9
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X-1][Y] == "P" and zone == 10:                                       # si la prochaine case est un P , alors cela veut dire que l'on passe dans la map Plage
                    map[X][Y] = " "
                    Clear()
                    map = map_pic
                    X = 14
                    zone = 12
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                
                elif map[X-1][Y] == "V":                                       # si la prochaine case est un V , alors cela veut dire que l'on passe dans la map Ville
                    map[X][Y] = " "
                    Clear()
                    map = map_ville
                    X = 14
                    zone = 1
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X-1][Y] == "M":                                       # si la prochaine case est un V , alors cela veut dire que l'on passe dans la map Ville
                    map[X][Y] = " "
                    Clear()
                    map = map_montagne
                    X = 14
                    zone = 10
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X-1][Y] == "A":
                    map[X][Y] = " "
                    print("\n"" KROOOOOOOO !!!")
                    time.sleep(2)
                    ennemi_artikodin(60,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    

                elif map[X-1][Y] == "R":                                       # si la prochaine case est un R , alors cela veut dire que l'on passe dans la map Quartier Général Racket
                    map[X][Y] = " "
                    Clear()
                    map = qg_racket
                    X = 5
                    Y = 1
                    zone = 14
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X-1][Y] == "M" and zone == 14:                                       # si la prochaine case est un M , alors cela veut dire que l'on est dans le Marché Noir
                    map[X][Y] = " "
                    Clear()
                    print(" Vous voilà dans le Marché Noir. Vous y trouverez des objets très utiles et vous pouvez vendre vos Pokémons pour vous faire un max d'argent.""\n")
                    DarkMarket(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X-1][Y] == "D" and X-1 == 5 and Y == 13 and zone == 1 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_roucarnage(randint(11,12), zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 9 and Y == 2 and zone == 1 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_akwakwak(randint(12,13),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 13 and Y == 14 and zone == 1 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_elcetrode(randint(11,12),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                
                elif map[X-1][Y] == "D" and X-1 == 5 and Y == 14 and zone == 2 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_florizarre(randint(11,12),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 9 and Y == 7 and zone == 2 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_papilusion(randint(11,12),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 10 and Y == 1 and zone == 2 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_dardargan(randint(12,13),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)

                elif map[X-1][Y] == "D" and X-1 == 1 and Y == 14 and zone == 3 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_nidoking(randint(14,15),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 5 and Y == 1 and zone == 3 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_nidqueen(randint(14,15),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 14 and Y == 9 and zone == 3 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_feunard(randint(15,16),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)

                elif map[X-1][Y] == "D" and X-1 == 2 and Y == 3 and zone == 4 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_tortank(randint(16,17),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 11 and Y == 2 and zone == 4 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_tartard(randint(16,17),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 11 and Y == 11 and zone == 4 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_crustabri(randint(17,18),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                
                elif map[X-1][Y] == "D" and X-1 == 4 and Y == 6 and zone == 5 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_leviator(randint(24,25),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 4 and Y == 13 and zone == 5 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_tentacruel(randint(24,25),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 8 and Y == 3 and zone == 5 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_hypocean(randint(26,27),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                
                
                elif map[X-1][Y] == "D" and X-1 == 1 and Y == 14 and zone == 6 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_Dracaufeu(randint(27,28),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 9 and Y == 9 and zone == 6 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_colossinge(randint(27,28),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 14 and Y == 4 and zone == 6 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_rhinoferos(randint(28,29),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                
                elif map[X-1][Y] == "D" and X-1 == 1 and Y == 2 and zone == 7 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_mackogneur(randint(31,32),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 8 and Y == 10 and zone == 7 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_ectoplasma(randint(31,32),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 14 and Y == 14 and zone == 7 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_grolem(randint(32,33),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                
                elif map[X-1][Y] == "D" and X-1 == 1 and Y == 2 and zone == 9 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_empiflor(randint(39,40),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 1 and Y == 14 and zone == 9 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_insecateur(randint(39,40),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 7 and Y == 1 and zone == 9 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_scarabrute(randint(40,41),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                
                elif map[X-1][Y] == "D" and X-1 == 3 and Y == 6 and zone == 10 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_arcanin(randint(49,50),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 6 and Y == 14 and zone == 10 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_dracolosse(randint(49,50),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                elif map[X-1][Y] == "D" and X-1 == 9 and Y == 5 and zone == 10 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_ptera(randint(50,51),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                
                elif map[X-1][Y] == "D" and X-1 == 1 and Y == 1 and zone == 11 :
                    map[X][Y] = " "
                    print("Yo,Tu veux tater de mes Pokémons ? ")
                    time.sleep(2)
                    ennemi_grotadmorv(randint(15,21),zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, xp_joueur, xp_prochain_niveau, cooldown, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)

                else:                                       # si ce n'est rien de tout ça alors on remplace la case par une case vide 
                    if state_spawn_pkmn == 0:
                        map[X][Y] = " "
                        X -= 1
                        map[X][Y] = "P"
                        state_spawn_pkmn = 0
                        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    elif state_spawn_pkmn == 1:
                        map[X][Y] = "H"
                        X -= 1
                        map[X][Y] = "P"
                        state_spawn_pkmn = 0
                        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    
            if MoveValue[0] == 2:                                               # exactement la même chose qu'au dessus juste dans une autre direction, pareil pour en dessous pour les autres directions
                time.sleep(0.1)
                if map[X+1][Y] == "■":
                    Clear()
                    LineByLine(map)
                    print(" Vous ne pouvez pas traverser le mur !""\n")
                    print(" Vous êtes dans la Zone",zone,".""\n")
                    print(" Compte en banque :",bank_account,"₽""\n")
                    print(" Appuyez sur < i > pour Ouvrir l'Inventaire")
                    print(" Appuyez sur < m > pour Ouvrir le Menu")
                    print(" Appuyez sur < l > pour Ouvrir la Légende")
                
                elif map[X+1][Y] == "H":
                    if state_spawn_pkmn == 0:
                     map[X][Y] = " "
                     X += 1
                     map[X][Y] = "P"
                     state_spawn_pkmn = 1
                     fight = 1
                     map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
            
                    elif state_spawn_pkmn == 1:
                     map[X][Y] = "H"
                     X += 1
                     map[X][Y] = "P"
                     state_spawn_pkmn = 1
                     fight = 1
                     map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                     
                elif map[X+1][Y] == "F":
                    map[X][Y] = " "
                    Clear()
                    map = map_foret_2
                    X = 1
                    zone = 9
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "C":
                    map[X][Y] = " "
                    Clear()
                    map = map_campagne
                    X = 1
                    zone = 3
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "P":                                       # si la prochaine case est un P , alors cela veut dire que l'on passe dans la map Plage
                    map[X][Y] = " "
                    Clear()
                    map = map_plage
                    X = 1
                    Y = 7
                    zone = 4
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "O":   
                    map[X][Y] = " "                                    # si la prochaine case est un O , alors cela veut dire que l'on passe dans la map Océan
                    Clear()
                    map = map_ocean
                    X = 1
                    zone = 5
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "V" and zone == 9:
                    map[X][Y] = " "
                    Clear()
                    map = map_ville
                    X = 1
                    zone = 1
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "V" and zone == 11:
                    map[X][Y] = " "
                    Clear()
                    map = map_ville
                    X = 14
                    Y = 2
                    zone = 1
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "S":
                    map[X][Y] = " "
                    print("\n"" KRAAAAAAAAAA !!!")
                    time.sleep(2)
                    ennemi_sulfura(60,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X+1][Y] == "M" and zone == 12:
                    map[X][Y] = " "
                    Clear()
                    map = map_montagne
                    X = 1
                    zone = 10
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                

                elif map[X+1][Y] == "R":
                    map[X][Y] = " "
                    Clear()
                    map = qg_racket
                    X = 5
                    Y = 1
                    zone = 14
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "M" and zone == 14:
                    map[X][Y] = " "
                    Clear()
                    print(" Vous voilà dans le Marché Noir. Vous y trouverez des objets très utiles et vous pouvez vendre vos Pokémons pour vous faire un max d'argent.""\n")
                    DarkMarket(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "T" and niveau_joueur < 40:                                        
                    Clear()
                    LineByLine(map) 
                    print(" Vous êtes dans la Zone",zone,".""\n")
                    print(" Compte en banque :",bank_account,"₽""\n")
                    print(" Appuyez sur < i > pour Ouvrir l'Inventaire")
                    print(" Appuyez sur < m > pour Ouvrir le Menu")
                    print(" Appuyez sur < l > pour Ouvrir la Légende")
                    print("\n"" Un camion banal .")
                
                elif map[X+1][Y] == "T" and niveau_joueur >= 40:    
                    print("\n"" Quelque chose vous saute dessus !""\n")
                    time.sleep(3)                                      
                    Clear()
                    ennemi_mew(50,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "L" and niveau_joueur < 60:                                        
                    Clear()
                    LineByLine(map)
                    print(" Vous êtes dans la Zone",zone,".""\n")
                    print(" Compte en banque :",bank_account,"₽""\n")
                    print(" Appuyez sur < i > pour Ouvrir l'Inventaire")
                    print(" Appuyez sur < m > pour Ouvrir le Menu")
                    print(" Appuyez sur < l > pour Ouvrir la Légende")
                    print("\n"" Vous voyez une forme floue dans la capsule que vous n'arrivez pas à comprendre") 
                
                elif map[X+1][Y] == "L" and niveau_joueur >= 60:    
                    print("\n"" Quelque chose vous saute dessus !")
                    time.sleep(3)                                      
                    Clear()
                    ennemi_mewtwo(65,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X+1][Y] == "D" and X+1 == 5 and Y == 13 and zone == 1 : # 5, 13
                    map[X][Y] = " "
                    print("C'est l'heure dudududuel ! ")
                    time.sleep(2)
                    ennemi_roucarnage(randint(8,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 9 and Y == 2 and zone == 1 : # 9, 12
                    map[X][Y] = " "
                    print("Ptdrrr t ki ? ")
                    time.sleep(2)
                    ennemi_alakazam(randint(8,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 13 and Y == 14 and zone == 1 : # 13, 14
                    map[X][Y] = " "
                    print("Viens ici que je te tase ! ")
                    time.sleep(2)
                    ennemi_elcetrode(randint(10,11),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X+1][Y] == "D" and X+1 == 5 and Y == 14 and zone == 2 : # 5, 14
                    map[X][Y] = " "
                    print("T'aimes la salade ? Et bah, tu vas en manger ! ")
                    time.sleep(2)
                    ennemi_florizarre(randint(11,12),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 9 and Y == 7 and zone == 2 : # 9, 7
                    map[X][Y] = " "
                    print("Hey toi là ! Regarde-moi bien ! ")
                    time.sleep(2)
                    ennemi_papilusion(randint(11,12),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 10 and Y == 1 and zone == 2 : # 10, 1
                    map[X][Y] = " "
                    print("Tu veux voir le dard de mon pokemon ? ")
                    time.sleep(2)
                    ennemi_dardargan(randint(12,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X+1][Y] == "D" and X+1 == 1 and Y == 14 and zone == 3 : # 1, 14
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_nidoking(randint(14,15),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 5 and Y == 1 and zone == 3 : # 5, 1
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_nidqueen(randint(14,15),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 14 and Y == 9 and zone == 3 : # 14, 9
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_feunard(randint(16,17),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "D" and X+1 == 2 and Y == 3 and zone == 4 : # 2, 3
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_tortank(randint(16,17),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 11 and Y == 2 and zone == 4 : # 11, 2
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_tartard(randint(16,17),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 11 and Y == 11 and zone == 4 : # 11, 11
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_crustabri(randint(16,17),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "D" and X+1 == 4 and Y == 6 and zone == 5 : # 4, 6
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_leviator(randint(24,25),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 4 and Y == 13 and zone == 5 : # 4, 13
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_tentacruel(randint(24,25),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 8 and Y == 3 and zone == 5 : # 8, 3
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_hypocean(randint(24,25),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "D" and X+1 == 1 and Y == 14 and zone == 6 : # 1, 14
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_Dracaufeu(randint(27,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 9 and Y == 9 and zone == 6 : # 9, 9
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_colossinge(randint(27,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 14 and Y == 4 and zone == 6 : # 14, 4
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_rhinoferos(randint(29,30),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "D" and X+1 == 1 and Y == 2 and zone == 7 : # 1, 2
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_mackogneur(randint(31,32),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 8 and Y == 10 and zone == 7 : # 8, 10
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_ectoplasma(randint(31,32),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 14 and Y == 14 and zone == 7 : # 14, 14
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_grolem(randint(34,35),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X+1][Y] == "D" and X+1 == 1 and Y == 2 and zone == 9 : # 1, 2
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_empiflor(randint(39,40),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 1 and Y == 14 and zone == 9 : # 1, 14
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_insecateur(randint(39,40),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 7 and Y == 1 and zone == 9 : # 7, 1
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_scarabrute(randint(40,41),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X+1][Y] == "D" and X+1 == 3 and Y == 6 and zone == 10 : # 3, 6
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_arcanin(randint(49,50),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 6 and Y == 14 and zone == 10 : # 6, 14
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_dracolosse(randint(49,50),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X+1][Y] == "D" and X+1 == 9 and Y == 5 and zone == 10 : # 9, 5
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_ptera(randint(50,51),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X+1][Y] == "D" and X+1 == 1 and Y == 1 and zone == 11 : # 1, 1
                    map[X][Y] = " "
                    print("Hey toi là, viens te battre ! ")
                    time.sleep(2)
                    ennemi_grotadmorv(randint(12,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                
                else:
                    if state_spawn_pkmn == 0: 
                        map[X][Y] = " "
                        X += 1
                        map[X][Y] = "P"
                        state_spawn_pkmn = 0
                        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    elif state_spawn_pkmn == 1:  
                        map[X][Y] = "H"
                        X += 1
                        map[X][Y] = "P"
                        state_spawn_pkmn = 0
                        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
        

            if MoveValue[0] == 3:
                time.sleep(0.1)
                if map[X][Y-1] == "■":
                    Clear()
                    LineByLine(map)
                    print(" Vous êtes dans la Zone",zone,".""\n")
                    print(" Vous ne pouvez pas traverser le mur !""\n") 
                    print(" Compte en banque :",bank_account,"₽""\n")
                    print(" Appuyez sur < i > pour Ouvrir l'Inventaire")
                    print(" Appuyez sur < m > pour Ouvrir le Menu")
                    print(" Appuyez sur < l > pour Ouvrir la Légende")
                
                elif map[X][Y-1] == "H":
                    if state_spawn_pkmn == 0:
                     map[X][Y] = " "
                     Y -= 1
                     map[X][Y] = "P"
                     state_spawn_pkmn = 1
                     fight = 1
                     map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                   
                    elif state_spawn_pkmn == 1:
                     map[X][Y] = "H"
                     Y -= 1
                     map[X][Y] = "P"
                     state_spawn_pkmn = 1
                     fight = 1
                     map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                
                elif map[X][Y-1] == "F":
                    map[X][Y] = " "
                    Clear()
                    map = map_foret
                    X = 7
                    Y = 14
                    zone = 2
                    LineByLine(map)
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y-1] == "E":
                    map[X][Y] = " "
                    Clear()
                    map = map_egout
                    X = 9
                    Y = 4
                    zone = 11
                    LineByLine(map)
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                


                elif map[X][Y-1] == "C":
                    map[X][Y] = " "
                    Clear()
                    map = map_campagne
                    X = 13
                    Y = 14
                    zone = 3
                    LineByLine(map)
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
               
                elif map[X][Y-1] == "D" and X == 14 and Y-1 == 0:
                    map[X][Y] = " "
                    Clear()
                    map = map_desert
                    Y = 14
                    zone = 6
                    LineByLine(map)
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
               


                elif map[X][Y-1] == "V" and zone == 6:
                    map[X][Y] = " "
                    Clear()
                    map = map_ville
                    Y = 14
                    zone = 1
                    LineByLine(map)
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
               

                elif map[X][Y-1] == "V" and zone == 14:
                    map[X][Y] = " "
                    Clear()
                    map = map_ville
                    X = 1
                    Y = 13
                    zone = 1
                    LineByLine(map)
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y-1] == "P":
                    map[X][Y] = " "
                    Clear()
                    map = map_pic
                    Y = 14
                    zone = 12
                    LineByLine(map)
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                

                elif map[X][Y-1] == "R":
                    map[X][Y] = " "
                    Clear()
                    map = qg_racket
                    X = 5
                    Y = 1
                    zone = 14
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "M" and zone == 14:
                    map[X][Y] = " "
                    Clear()
                    print(" Vous voilà dans le Marché Noir. Vous y trouverez des objets très utiles et vous pouvez vendre vos Pokémons pour vous faire un max d'argent.""\n")
                    DarkMarket(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y-1] == "L" and niveau_joueur < 60:                                        
                    Clear()
                    LineByLine(map)
                    print(" Vous êtes dans la Zone",zone,".""\n")
                    print(" Compte en banque :",bank_account,"₽""\n")
                    print(" Appuyez sur < i > pour Ouvrir l'Inventaire")
                    print(" Appuyez sur < m > pour Ouvrir le Menu")
                    print(" Appuyez sur < l > pour Ouvrir la Légende")
                    print("\n"" Vous voyez une forme floue dans la capsule que vous n'arrivez pas à comprendre .""\n") 
                
                elif map[X][Y-1] == "L" and niveau_joueur >= 60:    
                    print("\n"" Quelque chose vous saute dessus !")
                    time.sleep(3)                                      
                    Clear()
                    ennemi_mewtwo(65,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y-1] == "D" and X == 5 and Y-1 == 13 and zone == 1 :
                    map[X][Y] = " "
                    print("\n"" C'est l'heure du duel des Ombres ! ")
                    time.sleep(2)
                    ennemi_roucarnage(randint(8,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 9 and Y-1 == 2 and zone == 1 :
                    map[X][Y] = " "
                    print("\n"" Oh, tu veux te battre  ?")
                    time.sleep(2)
                    ennemi_elcetrode(randint(8,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 13 and Y-1 == 14    and zone == 1 :
                    map[X][Y] = " "
                    print("\n"" Abra ... Kadrabra ... ")
                    time.sleep(2)
                    ennemi_alakazam(randint(9,10),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y-1] == "D" and X == 5 and Y-1 == 14 and zone == 2 :
                    map[X][Y] = " "
                    print("\n"" Herbifesse ! ")
                    time.sleep(2)
                    ennemi_florizarre(randint(11,12),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 9 and Y-1 == 7 and zone == 2 :
                    map[X][Y] = " "
                    print("\n" " Euh... ")
                    time.sleep(2)
                    ennemi_papilusion(randint(11,12),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 10 and Y-1 == 1    and zone == 2 :
                    map[X][Y] = " "
                    print("\n"" BZZZZZ BBZZZZZ eheh ! ")
                    time.sleep(2)
                    ennemi_dardargan(randint(12,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y-1] == "D" and X == 1 and Y-1 == 14 and zone == 3 :
                    map[X][Y] = " "
                    print("\n"" Je suis le king de la zone ! ")
                    time.sleep(2)
                    ennemi_nidoking(randint(14,15),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 5 and Y-1 == 1 and zone == 3 :
                    map[X][Y] = " "
                    print("\n"" Piou piou je suis un oiseau ! ")
                    time.sleep(2)
                    ennemi_nidqueen(randint(14,15),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 14 and Y-1 == 9    and zone == 3 :
                    map[X][Y] = " "
                    print("\n"" Vive les chiens  ! ")
                    time.sleep(2)
                    ennemi_feunard(randint(15,16),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y-1] == "D" and X == 2 and Y-1 == 14 and zone == 4 :
                    map[X][Y] = " "
                    print("\n"" Mon Carabaffe vient d'évoluer ! ")
                    time.sleep(2)
                    ennemi_tortank(randint(16,17),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 11 and Y-1 == 2 and zone == 4 :
                    map[X][Y] = " "
                    print("\n"" Steak Tartard ! ")
                    time.sleep(2)
                    ennemi_tartard(randint(16,17),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 11 and Y-1 == 11    and zone == 4 :
                    map[X][Y] = " "
                    print("\n"" Regardes mon beau coquillage ! ")
                    time.sleep(2)
                    ennemi_crustabri(randint(17,18),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y-1] == "D" and X == 4 and Y-1 == 6 and zone == 5 :
                    map[X][Y] = " "
                    print("\n"" 'Léviator attaque Trempette', nan je rigole je vais te soulever ! ")
                    time.sleep(2)
                    ennemi_leviator(randint(24,25),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 4 and Y-1 == 13 and zone == 5 :
                    map[X][Y] = " "
                    print("\n"" Mon pokémon et moi on va te piquer ! ")
                    time.sleep(2)
                    ennemi_tentacruel(randint(24,25),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 8 and Y-1 == 3    and zone == 5 :
                    map[X][Y] = " "
                    print("\n"" Ah glouglou ! ")
                    time.sleep(2)
                    ennemi_hypocean(randint(25,26),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y-1] == "D" and X == 1 and Y-1 == 14 and zone == 6 :
                    map[X][Y] = " "
                    print("\n"" T'aimes les chamallow ? ")
                    time.sleep(2)
                    ennemi_Dracaufeu(randint(27,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 9 and Y-1 == 9 and zone == 6 :
                    map[X][Y] = " "
                    print("\n"" Guette la puissance ! ")
                    time.sleep(2)
                    ennemi_colossinge(randint(27,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 14 and Y-1 == 4    and zone == 6 :
                    map[X][Y] = " "
                    print("\n"" On va t'empaler ! ")
                    time.sleep(2)
                    ennemi_rhinoferos(randint(28,29),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y-1] == "D" and X == 1 and Y-1 == 2 and zone == 7 :
                    map[X][Y] = " "
                    print("\n"" Il est beau mon caillou ! ")
                    time.sleep(2)
                    ennemi_grolem(randint(31,32),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 8 and Y-1 == 10 and zone == 7 :
                    map[X][Y] = " "
                    print("\n"" Bouh ! ")
                    time.sleep(2)
                    ennemi_ectoplasma(randint(31,32),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 14 and Y-1 == 14    and zone == 7 :
                    map[X][Y] = " "
                    print("\n"" J'aime le castagne ! ")
                    time.sleep(2)
                    ennemi_mackogneur(randint(32,33),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y-1] == "D" and X == 1 and Y-1 == 2 and zone == 9 :
                    map[X][Y] = " "
                    print("\n"" Bousti-Boustiflor ! ")
                    time.sleep(2)
                    ennemi_empiflor(randint(39,40),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 1 and Y-1 == 14 and zone == 9 :
                    map[X][Y] = " "
                    print("\n"" T'aimes les insectes ? ")
                    time.sleep(2)
                    ennemi_insecateur(randint(39,40),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 7 and Y-1 == 1    and zone == 9 :
                    map[X][Y] = " "
                    print("\n"" Je vais te goumer ! ")
                    time.sleep(2)
                    ennemi_scarabrute(randint(40,41),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y-1] == "D" and X == 1 and Y-1 == 2 and zone == 10 :
                    map[X][Y] = " "
                    print("\n"" Mon Arcanin va te graille ! ")
                    time.sleep(2)
                    ennemi_arcanin(randint(49,50),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 1 and Y-1 == 14 and zone == 10 :
                    map[X][Y] = " "
                    print("\n"" T'aime mon short ! ")
                    time.sleep(2)
                    ennemi_ptera(randint(49,50),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y-1] == "D" and X == 7 and Y-1 == 1    and zone == 10 :
                    map[X][Y] = " "
                    print("\n"" Piou Piou je te hagar ! ")
                    time.sleep(2)
                    ennemi_dracolosse(randint(50,51),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y-1] == "D" and X == 1 and Y-1 == 1 and zone == 11 :
                    map[X][Y] = " "
                    print("\n"" Mon Grotadmorv va te manger ! ")
                    time.sleep(2)
                    ennemi_grotadmorv(randint(12,14),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)


                else:
                    if state_spawn_pkmn == 0:
                        map[X][Y] = " "
                        Y -= 1
                        map[X][Y] = "P"
                        state_spawn_pkmn = 0
                        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    elif state_spawn_pkmn == 1:
                        map[X][Y] = "H"
                        Y -= 1
                        map[X][Y] = "P"
                        state_spawn_pkmn = 0
                        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                    
            if MoveValue[0] == 4:
                time.sleep(0.1)
                if map[X][Y+1] == "■":
                    Clear()
                    LineByLine(map)
                    print(" Vous ne pouvez pas traverser le mur !""\n")
                    print(" Vous êtes dans la Zone",zone,".""\n")
                    print(" Compte en banque :",bank_account,"₽""\n")
                    print(" Appuyez sur < i > pour Ouvrir l'Inventaire")
                    print(" Appuyez sur < m > pour Ouvrir le Menu")
                    print(" Appuyez sur < l > pour Ouvrir la Légende")
                
                elif map[X][Y+1] == "H":
                    if state_spawn_pkmn == 0:
                     map[X][Y] = " "
                     Y += 1
                     map[X][Y] = "P"
                     state_spawn_pkmn = 1
                     fight = 1
                     map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    elif state_spawn_pkmn == 1:
                     map[X][Y] = "H"
                     Y += 1
                     map[X][Y] = "P"
                     state_spawn_pkmn = 1
                     fight = 1
                     map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                
                elif map[X][Y+1] == "F":
                    map[X][Y] = " "
                    Clear()
                    map = map_foret
                    X = 13
                    Y = 1
                    zone = 2
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y+1] == "V" and zone == 2:
                    map[X][Y] = " "
                    Clear()
                    map = map_ville
                    X = 7
                    Y = 1
                    zone = 1
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                 
                elif map[X][Y+1] == "V" and zone == 11:
                    map[X][Y] = " "
                    Clear()
                    map = map_ville
                    X = 14
                    Y = 2
                    zone = 1
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y+1] == "Z":
                    map[X][Y] = " "
                    Clear()
                    map = map_desert
                    Y = 1
                    zone = 6
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y+1] == "G":
                    map[X][Y] = " "
                    Clear()
                    map = map_grotte
                    Y = 1
                    zone = 7
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                

                elif map[X][Y+1] == "R" and zone == 13 or map[X][Y+1] == "E" and zone == 13 or map[X][Y+1] == "D" and zone == 13:
                    print("\n""...")
                    time.sleep(3)                                      
                    Clear()
                    ennemi_pikachu(80,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                
                elif map[X][Y+1] == "R" and zone == 1:
                    map[X][Y] = " "
                    Clear()
                    map = qg_racket
                    X = 5
                    Y = 1
                    zone = 14
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y+1] == "E":
                    map[X][Y] = " "
                    print("\n"" KRIIIII !!!")
                    time.sleep(2)
                    ennemi_electhor(60,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    
                elif map[X][Y+1] == "R" and zone == 12:
                    map[X][Y] = " "
                    Clear()
                    map = map_red
                    Y = 1
                    zone = 13
                    map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y+1] == "M" and zone == 14:
                    map[X][Y] = " "
                    Clear()
                    print(" Vous voilà dans le Marché Noir. Vous y trouverez des objets très utiles et vous pouvez vendre vos Pokémons pour vous faire un max d'argent.""\n")
                    DarkMarket(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y+1] == "T" and niveau_joueur < 40:                                         # on vérifie si la prochaine case est un mur 
                    Clear()
                    LineByLine(map) 
                    print(" Compte en banque :",bank_account,"₽""\n")
                    print(" Vous êtes dans la Zone",zone,".""\n")
                    print(" Appuyez sur < i > pour Ouvrir l'Inventaire")
                    print(" Appuyez sur < m > pour Ouvrir le Menu")
                    print(" Appuyez sur < l > pour Ouvrir la Légende")
                    print("\n"" Un camion banal .")
                
                elif map[X][Y+1] == "T" and niveau_joueur >= 40:    
                    print(" Quelque chose vous saute dessus !")
                    time.sleep(3)                                     # on vérifie si la prochaine case est un mur 
                    Clear()
                    ennemi_mew(50,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y+1] == "L" and niveau_joueur < 60:                                        
                    Clear()
                    LineByLine(map)
                    print(" Vous êtes dans la Zone",zone,".""\n")
                    print(" Compte en banque :",bank_account,"₽""\n")
                    print(" Appuyez sur < i > pour Ouvrir l'Inventaire")
                    print(" Appuyez sur < m > pour Ouvrir le Menu")
                    print(" Appuyez sur < l > pour Ouvrir la Légende")
                    print("\n"" Vous voyez une forme floue dans la capsule que vous n'arrivez pas à comprendre .") 
                
                elif map[X][Y+1] == "L" and niveau_joueur >= 60:    
                    print("\n"" Quelque chose vous saute dessus !")
                    time.sleep(3)                                      
                    Clear()
                    ennemi_mewtwo(65,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y+1] == "D" and X == 5 and Y+1 == 13 and zone == 1 :
                    map[X][Y] = " "
                    print("\n"" C'est l'heure du duel des Ombres ! ")
                    time.sleep(2)
                    ennemi_roucarnage(randint(8,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 9 and Y+1 == 2 and zone == 1 :
                    map[X][Y] = " "
                    print("\n"" Oh, tu veux te battre  ?")
                    time.sleep(2)
                    ennemi_elcetrode(randint(8,9),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 13 and Y+1 == 14    and zone == 1 :
                    map[X][Y] = " "
                    print("\n"" Abra ... Kadrabra ... ")
                    time.sleep(2)
                    ennemi_alakazam(randint(9,10),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y+1] == "D" and X == 5 and Y+1 == 14 and zone == 2 :
                    map[X][Y] = " "
                    print("\n"" Herbifesse ! ")
                    time.sleep(2)
                    ennemi_florizarre(randint(11,12),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 9 and Y+1 == 7 and zone == 2 :
                    map[X][Y] = " "
                    print("\n" " Euh... ")
                    time.sleep(2)
                    ennemi_papilusion(randint(11,12),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 10 and Y+1 == 1    and zone == 2 :
                    map[X][Y] = " "
                    print("\n"" BZZZZZ BBZZZZZ eheh ! ")
                    time.sleep(2)
                    ennemi_dardargan(randint(12,13),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y+1] == "D" and X == 1 and Y+1 == 14 and zone == 3 :
                    map[X][Y] = " "
                    print("\n"" Je suis le king de la zone ! ")
                    time.sleep(2)
                    ennemi_nidoking(randint(14,15),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 5 and Y+1 == 1 and zone == 3 :
                    map[X][Y] = " "
                    print("\n"" Piou piou je suis un oiseau ! ")
                    time.sleep(2)
                    ennemi_nidqueen(randint(14,15),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 14 and Y+1 == 9    and zone == 3 :
                    map[X][Y] = " "
                    print("\n"" Vive les chiens  ! ")
                    time.sleep(2)
                    ennemi_feunard(randint(15,16),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y+1] == "D" and X == 2 and Y+1 == 14 and zone == 4 :
                    map[X][Y] = " "
                    print("\n"" Mon Carabaffe vient d'évoluer ! ")
                    time.sleep(2)
                    ennemi_tortank(randint(16,17),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 11 and Y+1 == 2 and zone == 4 :
                    map[X][Y] = " "
                    print("\n"" Steak Tartard ! ")
                    time.sleep(2)
                    ennemi_tartard(randint(16,17),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 11 and Y+1 == 11    and zone == 4 :
                    map[X][Y] = " "
                    print("\n"" Regardes mon beau coquillage ! ")
                    time.sleep(2)
                    ennemi_crustabri(randint(17,18),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y+1] == "D" and X == 4 and Y+1 == 6 and zone == 5 :
                    map[X][Y] = " "
                    print("\n"" 'Léviator attaque Trempette', nan je rigole je vais te soulever ! ")
                    time.sleep(2)
                    ennemi_leviator(randint(24,25),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 4 and Y+1 == 13 and zone == 5 :
                    map[X][Y] = " "
                    print("\n"" Mon pokémon et moi on va te piquer ! ")
                    time.sleep(2)
                    ennemi_tentacruel(randint(24,25),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 8 and Y+1 == 3    and zone == 5 :
                    map[X][Y] = " "
                    print("\n"" Ah glouglou ! ")
                    time.sleep(2)
                    ennemi_hypocean(randint(25,26),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y+1] == "D" and X == 1 and Y+1 == 14 and zone == 6 :
                    map[X][Y] = " "
                    print("\n"" T'aimes les chamallow ? ")
                    time.sleep(2)
                    ennemi_Dracaufeu(randint(27,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 9 and Y+1 == 9 and zone == 6 :
                    map[X][Y] = " "
                    print("\n"" Guette la puissance ! ")
                    time.sleep(2)
                    ennemi_colossinge(randint(27,28),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 14 and Y+1 == 4    and zone == 6 :
                    map[X][Y] = " "
                    print("\n"" On va t'empaler ! ")
                    time.sleep(2)
                    ennemi_rhinoferos(randint(28,29),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y+1] == "D" and X == 1 and Y+1 == 2 and zone == 7 :
                    map[X][Y] = " "
                    print("\n"" Il est beau mon caillou ! ")
                    time.sleep(2)
                    ennemi_grolem(randint(31,32),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 8 and Y+1 == 10 and zone == 7 :
                    map[X][Y] = " "
                    print("\n"" Bouh ! ")
                    time.sleep(2)
                    ennemi_ectoplasma(randint(31,32),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 14 and Y+1 == 14    and zone == 7 :
                    map[X][Y] = " "
                    print("\n"" J'aime le castagne ! ")
                    time.sleep(2)
                    ennemi_mackogneur(randint(32,33),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                elif map[X][Y+1] == "D" and X == 1 and Y+1 == 2 and zone == 9 :
                    map[X][Y] = " "
                    print("\n"" Bousti-Boustiflor ! ")
                    time.sleep(2)
                    ennemi_empiflor(randint(39,40),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 1 and Y+1 == 14 and zone == 9 :
                    map[X][Y] = " "
                    print("\n"" T'aimes les insectes ? ")
                    time.sleep(2)
                    ennemi_insecateur(randint(39,40),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 7 and Y+1 == 1    and zone == 9 :
                    map[X][Y] = " "
                    print("\n"" Je vais te goumer ! ")
                    time.sleep(2)
                    ennemi_scarabrute(randint(40,41),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y+1] == "D" and X == 1 and Y+1 == 2 and zone == 10 :
                    map[X][Y] = " "
                    print("\n"" Mon Arcanin va te graille ! ")
                    time.sleep(2)
                    ennemi_arcanin(randint(49,50),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 1 and Y+1 == 14 and zone == 10 :
                    map[X][Y] = " "
                    print("\n"" T'aime mon short ! ")
                    time.sleep(2)
                    ennemi_ptera(randint(49,50),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif map[X][Y+1] == "D" and X == 7 and Y+1 == 1    and zone == 10 :
                    map[X][Y] = " "
                    print("\n"" Piou Piou je te hagar ! ")
                    time.sleep(2)
                    ennemi_dracolosse(randint(50,51),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                elif map[X][Y+1] == "D" and X == 1 and Y+1 == 1 and zone == 11 :
                    map[X][Y] = " "
                    print("\n"" Mon Grotadmorv va te manger ! ")
                    time.sleep(2)
                    ennemi_grotadmorv(randint(12,14),zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

                else:
                    if state_spawn_pkmn == 0:
                        map[X][Y] = " "
                        Y += 1
                        map[X][Y] = "P"
                        state_spawn_pkmn = 0
                        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    elif state_spawn_pkmn == 1:
                        map[X][Y] = "H"
                        Y += 1
                        map[X][Y] = "P"
                        state_spawn_pkmn = 0
                        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
            
            # sauvegarde de la partie.
            
            if MoveValue[0] == 7:
                Clear()
                i = 0 
                list_choice_menu = ["1","2","3","4"]
                while i < 10000 :


                    print("""
                1 -- Sauvegarder

                2 -- Commandes

                3 -- Crédits

                4 -- Quitter Menu

                
                """)
                    choice_menu = input()

                    if choice_menu == list_choice_menu[0] :
                        list_choice_saved = ["1","2"]
                        print("""
                            Voulez-vous écraser l'ancienne sauvegarde ? 
                                1 -- Oui            2 -- Non
                        """)
                        choice_Yes_No = input()
                        clear = system('cls')

                        if choice_Yes_No == list_choice_saved[0] :

                            zone_out = open("zone_save.pickle", "wb")
                            pickle.dump(zone, zone_out)
                            zone_out.close()

                            niveau_joueur_out = open("niveau_joueur_save.pickle", "wb")
                            pickle.dump(niveau_joueur, niveau_joueur_out)
                            niveau_joueur_out.close()

                            stats_vie_joueur_out = open("stats_vie_joueur_save.pickle", "wb")
                            pickle.dump(stats_vie_joueur, stats_vie_joueur_out)
                            stats_vie_joueur_out.close()

                            stats_vie_total_joueur_out = open(
                                "stats_vie_total_joueur_save.pickle", "wb")
                            pickle.dump(stats_vie_total_joueur, stats_vie_total_joueur_out)
                            stats_vie_total_joueur_out.close()

                            stats_attaque_joueur_out = open("stats_attaque_joueur_save.pickle", "wb")
                            pickle.dump(stats_attaque_joueur, stats_attaque_joueur_out)
                            stats_attaque_joueur_out.close()

                            stats_defense_joueur_out = open("stats_defense_joueur_save.pickle", "wb")
                            pickle.dump(stats_defense_joueur, stats_defense_joueur_out)
                            stats_defense_joueur_out.close()

                            attaque1_out = open("attaque1_save.pickle", "wb")
                            pickle.dump(attaque1, attaque1_out)
                            attaque1_out.close()

                            effet1_out = open("effet1_save.pickle", "wb")
                            pickle.dump(effet1, effet1_out)
                            effet1_out.close()

                            attaque2_out = open("attaque2_save.pickle", "wb")
                            pickle.dump(attaque2, attaque2_out)
                            attaque2_out.close()

                            effet2_out = open("effet2_save.pickle", "wb")
                            pickle.dump(effet2, effet2_out)
                            effet2_out.close()

                            xp_joueur_out = open("xp_joueur_save.pickle", "wb")
                            pickle.dump(xp_joueur, xp_joueur_out)
                            xp_joueur_out.close()

                            xp_prochain_niveau_out = open("xp_prochain_niveau_save.pickle", "wb")
                            pickle.dump(xp_prochain_niveau, xp_prochain_niveau_out)
                            xp_prochain_niveau_out.close()

                            cooldown_out = open("cooldown_save.pickle", "wb")
                            pickle.dump(cooldown, cooldown_out)
                            cooldown_out.close()

                            map_out = open("map_save.pickle", "wb")
                            pickle.dump(map, map_out)
                            map_out.close()

                            X_out = open("X_save.pickle", "wb")
                            pickle.dump(X, X_out)
                            X_out.close()

                            Y_out = open("Y_save.pickle", "wb")
                            pickle.dump(Y, Y_out)
                            Y_out.close()

                            map_ville_out = open("map_ville_save.pickle", "wb")
                            pickle.dump(map_ville, map_ville_out)
                            map_ville_out.close()

                            map_foret_out = open("map_foret_save.pickle", "wb")
                            pickle.dump(map_foret, map_foret_out)
                            map_foret_out.close()

                            map_plage_out = open("map_plage_save.pickle", "wb")
                            pickle.dump(map_plage, map_plage_out)
                            map_plage_out.close()

                            map_ocean_out = open("map_ocean_save.pickle", "wb")
                            pickle.dump(map_ocean, map_ocean_out)
                            map_ocean_out.close()

                            map_campagne_out = open("map_campagne_save.pickle", "wb")
                            pickle.dump(map_campagne, map_campagne_out)
                            map_campagne_out.close()


                            map_safari_out = open("map_safari_save.pickle", "wb")
                            pickle.dump(map_safari, map_safari_out)
                            map_safari_out.close()


                            qg_racket_out = open("qg_racket_save.pickle", "wb")
                            pickle.dump(qg_racket, qg_racket_out)
                            qg_racket_out.close()

                            state_spawn_pkmn_out = open("state_spawn_pkmn_save.pickle", "wb")
                            pickle.dump(state_spawn_pkmn, state_spawn_pkmn_out)
                            state_spawn_pkmn_out.close()

                            fight_out = open("fight_save.pickle", "wb")
                            pickle.dump(fight, fight_out)
                            fight_out.close()

                            ListPokemonInBag_out = open("ListPokemonInBag_save.pickle","wb")
                            pickle.dump(ListPokemonInBag, ListPokemonInBag_out)
                            ListPokemonInBag_out.close()

                            bank_account_out = open("bank_account_save.pickle","wb")
                            pickle.dump(bank_account, bank_account_out)
                            bank_account_out.close()

                            list_item_out = open("list_item_save.pickle","wb")
                            pickle.dump(list_item, list_item_out)
                            list_item_out.close()

                            stats_vie_ennemi_out = open("stats_vie-ennemi_save.pickle","wb")
                            pickle.dump(stats_vie_ennemi, stats_vie_ennemi_out)
                            stats_vie_ennemi_out.close()

                            stats_attaque_ennemi_out = open("stats_attaque_ennemi_save.pickle","wb")
                            pickle.dump(stats_attaque_ennemi, stats_attaque_ennemi_out)
                            stats_attaque_ennemi_out.close()

                            stats_defense_ennemi_out = open("stats_defense_ennemi_save.pickle","wb")
                            pickle.dump(stats_defense_ennemi, stats_defense_ennemi_out)
                            stats_defense_ennemi_out.close()

                            nom_ennemi_out = open("nom_ennemi_save.pickle","wb")
                            pickle.dump(nom_ennemi, nom_ennemi_out)
                            nom_ennemi_out.close()

                            niveau_ennemi_out = open("niveau_ennemi_save.pickle","wb")
                            pickle.dump(niveau_ennemi, niveau_ennemi_out)
                            niveau_ennemi_out.close()

                            attaque_ennemi_1_out = open("attaque_ennemi_1_save.pickle","wb")
                            pickle.dump(attaque_ennemi_1, attaque_ennemi_1_out)
                            attaque_ennemi_1_out.close()

                            attaque_ennemi_2_out = open("attaque_ennemi_2_save.pickle","wb")
                            pickle.dump(attaque_ennemi_2, attaque_ennemi_2_out)
                            attaque_ennemi_2_out.close()

                            effet_attaque_ennemi1_out = open("effet_attaque_ennemi1_save.pickle","wb")
                            pickle.dump(effet_attaque_ennemi1, effet_attaque_ennemi1_out)
                            effet_attaque_ennemi1_out.close()

                            effet_attaque_ennemi2_out = open("effet_attaque_ennemi2_save.pickle","wb")
                            pickle.dump(effet_attaque_ennemi2, effet_attaque_ennemi2_out)
                            effet_attaque_ennemi2_out.close()

                            xp_ennemi_out = open("xp_ennemi_save.pickle","wb")
                            pickle.dump(xp_ennemi, xp_ennemi_out)
                            xp_ennemi_out.close()

                            cooldown_ennemi_out = open("cooldown_ennemi_save.pickle","wb")
                            pickle.dump(cooldown_ennemi, cooldown_ennemi_out)
                            cooldown_ennemi_out.close()


                            return ""


                        elif choice_Yes_No == list_choice_saved[1] : 
                            return ""

                        elif choice_Yes_No != list_choice_saved[:] :
                            print("erreur")
                            clear = system('cls')
                    
                    elif choice_menu == list_choice_menu[1] :
                        print("""
                        
                        Les commandes sont exclusivement liées à votre clavier (pour le moment.... A l'avenir, on souhaite vous proposer une expérience liée à la Kinect lol) :
                        - Avancer devant : ↑
                        - Avancer en arrière : ↓
                        - Avancer vers la droite : → 
                        - Avancer vers la gauche : ←

                        """)
                        input(delay_print(" < Appuyez sur Entrée pour Quitter > "))

                        clear = system('cls')
                    
                    elif choice_menu == list_choice_menu[2] :
                        print("""
                    
                        Ce superbe jeu a été développé par Billy l'ultime boss, Anthony The master, Ewan le Président et Louis Le Dieu des Dieux !! 
            
                        """)
                        input(delay_print(" < Appuyez sur Entrée pour Quitter > "))

                        clear = system('cls')


                    elif choice_menu == list_choice_menu[3] :
                        map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                    
                    
                    elif choice_menu != list_choice_menu[:] :
                        print("Erreur, séléctionner une option comprise entre 1 et 4 !")
                        input(print(" < Appuyez sur Entrée pour Quitter > "))
                        
                        clear = system('cls')


                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)





            if MoveValue[0] == 5:           # si la touche i est utilisée , alors on ouvre l'inventaire
                Clear()
                inventaire(0,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,0,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,0)
            
            if MoveValue[0] == 6:           # si la touche l est utilisée , alors on montre la légende 
                print("""
                
                Zone 1 : Villeblanche (NIV Moyen : 5)

                 H = Herbe (Zine d'apparition de Pokémon)
                 D = Dresseur

                 R = QG Team Racket
                 T = Un camion 
                

                 E = Les Égouts de Villeblanche ( Zone 11 - NIV Moyen : 18 )
                 F (Gauche) = La Forêt Vertefeuille (Zone 2 - NiV Moyen : 8 )
                 F (Haut) = La Forêt Sombrechêne ( Zone 9 -- NIV Moyen : 35 )
                 P = La Plage Clairgrain ( Zone 4 -- NIV Moyen : 14 )
                 Z = Le Désert de Rochesombre ( Zone 6 -- NIV Moyen : 24 )



                Zone 2 : La Forêt Vertefeuille (NiV Moyen : 8 )

                 H = Herbe (Zine d'apparition de Pokémon)
                 D = Dresseur

                 ■ ■ ■
                 ■ L ■ =  Le Lac Brillant
                 ■ ■ ■

                 V = Villeblanche (Zone 1 -- NIV Moyen : 5)
                 C = Le Village de Noisetiel ( Zone 3 -- NIV Moyen 11)



                Zone 3  : Le Village de Noisetiel (NIV Moyen 11)
                 
                 H = Herbe (Zine d'apparition de Pokémon)
                 D = Dresseur

                 F = La Forêt Vertefeuille (Zone 2 - NiV Moyen : 8 )
                 S = Le Safari (Zone 8 -- NIV 15 - 50)



                Zone 4 : La Plage Clairgrain ( NIV Moyen : 14 )

                 H = Herbe (Zine d'apparition de Pokémon)
                 D = Dresseur

                 V = Villeblanche (Zone 1 -- NIV Moyen : 5)
                 O = La Grande Mer (Zone 5 -- NIV Moyen 20)

                

                Zone 5 : La Grande Mer ( NIV Moyen 20)

                 H = Herbe (Zine d'apparition de Pokémon)
                 D = Dresseur

                 P = La Plage Clairgrain ( Zone 4 -- NIV Moyen : 14 )



                Zone 6 : Le Désert de Rochesombre ( NIV Moyen : 24 )
                 
                 H = Herbe (Zine d'apparition de Pokémon)
                 D = Dresseur

                 G = La Grotte Rochesombre ( Zone 7 -- NIV Moyen 28 )



                Zone 7 : La Grotte Rochesombre ( NIV Moyen : 28 )
                 
                 H = Herbe (Zine d'apparition de Pokémon)
                 D = Dresseur

                 D = Le Désert de Rochesombre ( Zone 6 -- NIV Moyen 24 )



                Zone 8 : Le Safari ( NIV Moyen : 15 - 50 )
                 
                 H = Herbe (Zine d'apparition de Pokémon)
                 D = Dresseur

                 C = Le Village de Noisetiel ( Zone 3 -- NIV Moyen 11)


                
                Zone 9 : La Forêt Sombrechêne ( NIV Moyen : 35 )

                 H = Herbe ( Z0ne d'apparition de Pokémon)
                 D = Dresseur

                 V = Villeblanche ( Zone 1 -- NIV Moyen : 5)
                 M = Le Mont Glasang ( Zone 10 -- NIV Moyen 45)



                Zone 10 : Le Mont Glasang ( NIV Moyen : 45 )

                 H = Herbe ( Z0ne d'apparition de Pokémon)
                 D = Dresseur

                 F = La Forêt Sombrechêne ( Zone 9 -- NIV Moyen : 35)
                 P = Le Pic Glasang ( Zone 12 -- NIV Moyen 60)



                Zone 11 : Les Égouts de Villeblanche (NIV Moyen : 18)

                 H = Herbe ( Z0ne d'apparition de Pokémon)
                 D = Dresseur

                 V = Villeblanche (Zone 1 -- NIV Moyen : 5)



                Zone 12 : Le Pic Glasang ( NIV Moyen : 60 )

                 H = Herbe ( Z0ne d'apparition de Pokémon)
                 D = Dresseur

                 S = Sulfura
                 A = Artikodin
                 E = Électhor

                 M = Le Mont Glasang ( Zone 10 -- NIV Moyen 45)
                 R = RED ( Zone 13 -- NIV 70 )



                Zone 13 : RED ( NIV 70)
                 
                 RED = ...
                 P = Le Pic Glasang ( Zone 12 -- NIV Moyen 60)



                Zone 14 : QG Team Racket 
                 
                 M = Marché Noir
                 L = Caspsule Secrète

                 V = Villeblanche (Zone 1 -- NIV Moyen : 5)



                 < Appuyez sur Entrée pour Quitter >

                
                """)
                z = input()
                map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)


#-------------------------------------------------------------------------------------FONCTIONS BLACK MARKET --------------------------------------------------------------------------------------------------------------------

# Fonction qui permet d'afficher les mots petit a petit comme dans les jeux Pokémon

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    return ""




# Fonction pour vendre les pokémons en notre possession

def SellPoke(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    # Listes catégorisant les Pokémons et attribuant une valeur marchande en fonction de ces catégories
    
    list_low_pkmn = ["Bulbizarre","Salamèche","Carapuce","Chenipan","Aspicot","Roucool","Rattata","Piafabec","Abo","Sabelette","Nidoran (F)","Nidoran (M)","Goupix","Rondoudou","Nosferapti","Mystherbe","Paras","Mimitoss","Taupiqueur","Psykokwak","Férosinge","Ptitard","Abra","Machoc","Chetiflor","Tentacool","Racaaillou","Ponyta","Ramoloss","Magnéti","Doduo","Otaria","Tadmorv","Kokiyas","Fantominus","Krabby","Voltorbe","Noeunoeuf","Osselait","Smogo","Saquedeneu","Hypotrempe","Poissirène","Stari","Magicarpe","Évoli","Amonita","Kabuto","Minidraco"]
    price_low = 10

    list_medium_pkmn = ["Herbizarre","Reptincel","Carabaffe","Chrysacier","Coconfort","Roucoups","Rattatac","Rapasdepic","Arbok","Sablaireau","Nidorina","Nidorino","Mélofée","Grodoudou","Nosferalto","Ortide","Parasect","Aéromite","Persian","Caninos","Têtarte","Kadabra","Machopeur","Boustiflor","Magnéton","Canarticho","Dodrio","Spectrum","Soporifik","Excelangue","Rhinocorne","Poissoroy","M.Mime","Scarabrute","Tauros","Métamorph","Porygon","Amonistar"]
    price_medium = 25

    list_high_pkmn = ["Papilusion","Dardargnan","Roucarnage","Raichu","Mélodelfe","Feunard","Rafflesia","Triopiqueur","Akwakwak","Colossinge","Mackogneur","Empiflor","Tentacruel","Gravalanch","Galopa","Flagadoss","Lamantine","Grotadmorv","Crustabri","Ectoplasma","Onix","Hypnomade","Krabboss","Électrode","Noadkoko","Ossatueur","Kicklee","Tygnon","Smogogo","Rhinoféros","Leveinard","Kangourex","Hypocéan","Staross","Insécateur","Lippoutou","Élektek","Magmar","Aquali","Voltali","Pyroli","Kabutops","Ptéra","Draco"]
    price_high = 50

    list_premium_pkmn = ["Florizarre","Dracaufeu","Tortank","Nidoking","Nidoqueen","Arcanin","Tartard" ,"Alakazam","Grolem","Leviator","Lockhlass","Ronflex","Dracolosse"]
    price_premium = 100

    list_legend_pkmn = ["Mew","Mewtwo,","Sulfura","Électhor","Artikodin"]
    price_legend = 250
 
    number_own_pokemon = len(ListPokemonInBag)  # calcule le nombre de pokémon en notre possession
    
    
    if number_own_pokemon > 0:      # si on a des Pokémons , alors on affiche le menu de vente sinon on retourne au menu Marché Noir
        print(" Vous avez {} Pokémon(s) en votre possession, vous pouvez en donner à Giovanni pour qu'il vous donne une prime !".format(
                number_own_pokemon))

        print(" Quel Pokémon faut-il vendre ?                    ",bank_account,"₽")
        print()
        print("                    0 - Retour")
        j = 0
        while j < len(ListPokemonInBag):                                         # on affiche les Pokémons en notre possession
         print("                   ",j + 1,"-",''.join(ListPokemonInBag[j]))
         j += 1
        
        sell_pok = int(input())

        if sell_pok == 0: # si on entre 0 alors on retourne au menu Marché Noir
            Clear()
            DarkMarket(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
        # Partie de la fonction qui nous donne de l'argent en fonction de la catégorie du Pokémon vendu
        
        elif ListPokemonInBag[sell_pok-1] in list_low_pkmn:
            print()
            print(" Vous vendez",''.join(ListPokemonInBag[sell_pok-1]),"et gagnez",price_low,"₽")
            time.sleep(2)
            Clear()
            bank_account += 10
            del ListPokemonInBag[sell_pok-1]             # une fois vendu , on le retire de notre liste et on retourne au menu vente de Pokémon
            SellPoke(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

        elif ListPokemonInBag[sell_pok-1] in list_medium_pkmn:
            print()
            print(" Vous vendez",''.join(ListPokemonInBag[sell_pok-1]),"et gagnez",price_medium,"₽")
            time.sleep(2)
            Clear()
            bank_account += 25
            del ListPokemonInBag[sell_pok-1]
            SellPoke(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

        elif ListPokemonInBag[sell_pok-1] in list_high_pkmn:
            print()
            print(" Vous vendez",''.join(ListPokemonInBag[sell_pok-1]),"et gagnez",price_high,"₽")
            time.sleep(2)
            Clear()
            bank_account += 50
            del ListPokemonInBag[sell_pok-1]
            SellPoke(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

        elif ListPokemonInBag[sell_pok-1] in list_premium_pkmn:
            print()
            print(" Vous vendez",''.join(ListPokemonInBag[sell_pok-1]),"et gagnez",price_premium,"₽")
            time.sleep(2)
            Clear()
            bank_account += 100
            del ListPokemonInBag[sell_pok-1]
            SellPoke(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

        elif ListPokemonInBag[sell_pok-1] in list_legend_pkmn:
            print()
            print(" Vous vendez",''.join(ListPokemonInBag[sell_pok-1]),"et gagnez",price_legend,"₽")
            time.sleep(2)
            Clear()
            bank_account += 250
            del ListPokemonInBag[sell_pok-1]
            SellPoke(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
    else: 
        print(" Vous n'avez pas de Pokémon à vendre .")
        time.sleep(3)
        Clear()
        DarkMarket(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)




# fonction pour achater des items dans le Marché Noir

def buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    Clear()
    i = 0
    list_number_item = ["1", "2", "3", "4", "5"]                                        # on affiche le menu item avec le prix de chacun 
    while True:
        print(" Que voulez-vous acheter ?                     ",bank_account,"₽")
        print("""
                    1 -- Filet  10 ₽
                    2 -- Potion (20 PV) 15 ₽
                    3 -- Super Potion (50 PV) 25 ₽
                    4 -- Hyper Potion (200 PV) 50 ₽
                    5 -- Retour

        """)
        choice_buy_item = input()

        if choice_buy_item == list_number_item[0]:                                       # on choisit l'item                       
            x = int(input(" Combien voulez-vous en acheter ? "))                         # on demande combien on veut on acheter
            price = x * 10
            print(" Êtes-vous sûr de vouloir acheter",x,"Filet(s) ? Cela vous coûtera",price,"₽")
            y = input(" Oui ou Non ? ")                                                  # vérification
            while y.lower() != "oui" and y.lower() != "non":
                y = input(" Oui ou Non ? ")
            else:
                if y.lower() == "oui":                                                   # on vérifie que le joueur a assez d'argent sinon retour au menu
                    if price > bank_account:
                     print(" Vous n'avez pas assez d'argent .")
                     time.sleep(2)
                     buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                    print(" Vous venez d'acheter",x,"Filet(s)")                           # sinon le joueur achète et on ajoute le nombre d'item achetés dans l'inventaire en retirant le prix * le nombre a notre compte en banque
                    i = 0
                    while i < x:
                     list_item.append("Filet") 
                     i += 1
                    bank_account -= 10 * x
                    buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif y.lower() == "non":
                    buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
            

        elif choice_buy_item == list_number_item[1]:                                        # exactement la même chose pour tout les autres items
            x = int(input(" Combien voulez-vous en acheter ? "))
            price = x * 15
            print(" Êtes-vous sûr de vouloir acheter",x,"Potion(s) ? Cela vous coûtera",price,"₽")
            y = input(" Oui ou Non ? ")
            while y.lower() != "oui" and y.lower() != "non":
                y = input(" Oui ou Non ? ")
            else:
                if y.lower() == "oui":
                    if price > bank_account:
                     print(" Vous n'avez pas assez d'argent .")
                     time.sleep(2)
                     buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                    print(" Vous venez d'acheter",x,"Potion(s)")
                    i = 0
                    while i < x:
                     list_item.append("Potion") 
                     i += 1
                    bank_account -= 15 * x
                    buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif y.lower() == "non":
                    buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)


        elif choice_buy_item == list_number_item[2]:
            x = int(input(" Combien voulez-vous en acheter ? "))
            price = x * 25
            print(" Êtes-vous sûr de vouloir acheter",x,"Super Potion(s) ? Cela vous coûtera",price,"₽")
            y = input(" Oui ou Non ? ")
            while y.lower() != "oui" and y.lower() != "non":
                y = input(" Oui ou Non ? ")
            else:
                if y.lower() == "oui":
                    if price > bank_account:
                     print(" Vous n'avez pas assez d'argent .")
                     time.sleep(2)
                     buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                    print(" Vous venez d'acheter",x,"Super Potion(s)")
                    i = 0
                    while i < x:
                     list_item.append("Super Potion") 
                     i += 1
                    bank_account -= 25 * x
                    buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif y.lower() == "non":
                    buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

        elif choice_buy_item == list_number_item[3]:
            x = int(input(" Combien voulez-vous en acheter ? "))
            price = x * 50
            print(" Êtes-vous sûr de vouloir acheter",x,"Hyper Potion(s) ? Cela vous coûtera",price,"₽")
            y = input(" Oui ou Non ? ")
            while y.lower() != "oui" and y.lower() != "non":
                y = input(" Oui ou Non ? ")
            else:
                if y.lower() == "oui":
                    if price > bank_account:
                     print(" Vous n'avez pas assez d'argent .")
                     time.sleep(2)
                     buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                
                    print(" Vous venez d'acheter",x,"Hyper Potion(s)")
                    i = 0
                    while i < x:
                     list_item.append("Hyper Potion") 
                     i += 1
                    bank_account -= 50 * x
                    buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
                elif y.lower() == "non":
                    buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

        elif choice_buy_item == list_number_item[4]: # si on choisit Retour , retour au menu
            Clear()
            DarkMarket(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)

        elif choice_buy_item != list_number_item[:]:
            print("Erreur de saisie. Refaite une séléction")


# fonction qui appelle toutes les fonctions liées au Marché Noir


def DarkMarket(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    list_choice_Dark_Market = ["1", "2", "3"]

    while True:
        print(" Que voulez-vous faire :                    ",bank_account,"₽")   # le même principe que pour la vente de Pokémon
        print("""
                    1 -- Donner Pokémon à Giovanni
                    2 -- Acheter Objet
                    3 -- Quitter
    """)
        print()
        choice_Dark_Market = input()
        clear = system('cls')

        if choice_Dark_Market == list_choice_Dark_Market[0]:           # si on choisit 1 , on appelle la fonction Vente de Pokémon 
            SellPoke(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
            

        elif choice_Dark_Market == list_choice_Dark_Market[1]:         # si on choisit 2 , on appelle la foncton Achat d'objet
            buy_item(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
            

        elif choice_Dark_Market == list_choice_Dark_Market[2]:         # si on choisit 3 on retourne sur la map
            print()
            print("Vous allez quitter le Marché Noir, au revoir !")
            time.sleep(3)
            map_fonction(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item)
            

        elif choice_Dark_Market != list_choice_Dark_Market[:]:    # si une valeur incorrecte est donnée = redemande 
            print()
            print("Erreur de saisie, refaite une séléction")
            time.sleep(2)
            clear = system('cls')





#-------------------------------------------------------------------------------------FONCTIONS POKEMON --------------------------------------------------------------------------------------------------------------------    


def ennemi_builbizarre(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Bulbizarre"   # on définit le nom , ses stats et les noms de ses attaques et on lance le combat 
    money_battle = 0
    
    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 ="Charge"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 ="Fouet Liane"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_herbizarre(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Herbizarre"
    money_battle = 0

    
    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Fouet Liane"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Tranches Herbes"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_florizarre(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Florizarre"
    money_battle = 100

    
    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Tranches Herbes"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Lance Soleil"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_salameche(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Salamèche"
    money_battle = 0

    
    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Charge"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Flamèche"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_reptincel(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Reptincel"
    money_battle = 0

    
    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Flamèche"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Lance Flamme"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_Dracaufeu(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Dracaufeu"
    money_battle = 100


    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Lance Flamme"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Déflagration"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_carapuce(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Carapuce"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Charge"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Bulle d'Eau"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_carabaffe(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Carabaffe"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Bulle d'Eau"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Pistolet à Eau"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_tortank(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Tortank"
    money_battle = 100

    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Pistolet à Eau"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Hydrocanon"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_chenipan(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Chenipan"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Charge"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Sécrétion"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_chrysacier(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Chrysacier"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Sécrétion"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Armure"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
    

def ennemi_papilusion(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Papilusion"
    money_battle = 100

    
    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Armure"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Poudre Dodo"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_aspicot(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Aspicot"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Charge"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Sécrétion"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_coconfort(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Coconfort"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Armure"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Boule Armure"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_dardargan(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Dardargnan"
    money_battle = 100

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Survinsect"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Coupe Croix"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_roucool(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Roucool"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Tornade"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Picpic"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_roucoups(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Roucoups"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Lame d'Air"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Cru-Ailes"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_roucarnage(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Roucarnage"
    money_battle = 100

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Rapace"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Lame d'Air"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_rattata(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Rattata"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Morsure"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Charge"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_rattatac(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Rattatac"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Croc de Mort"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Machouille"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_piafabec(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Piafabec"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Tornade"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Picpic"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_rapasdepic(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Rapasdepic"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Lame d'Air"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Rapace"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_abo(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Abo"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Morsure"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Charge"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_arbok(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Arbok"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ligotage"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Croc Toxik"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_pikachu(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Pikachu"
    money_battle = 500

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Fatal Foudre"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Elektacle"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_raichu(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Raichu"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Tonnerre"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Queue de Fer"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_sabelette(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Sabelette"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Jet de Pierre"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Tunnel"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_sablaireau(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Sablaireau"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Seisme"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Rock Boulet"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_nidoran_f(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Nidoran (F)"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Morsure"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Poison"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_nidorina(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Nidorina"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Dard Venin"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Poison Croix"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_nidqueen(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Nidoqueen"
    money_battle = 100

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ultralaser"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Direct Toxik"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_nidoran_m(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Nidoran (M)"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Crochet Venin"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Morsure"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_nidorino(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Nidorino"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Direct Toxik"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Croc Poison"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_nidoking(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Nidoking"
    money_battle = 100

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ultralaser"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Direct Toxik"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_melofee(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Mélofée"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Métronome"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Eclat Magique"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_melodelfe(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Mélodelfe"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Pouvoir Lunaire"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Attraction"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_goupix(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Goupix"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Flamèche"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Roue de Feu"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_feunard(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Feunard"
    money_battle = 100

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Déflagration"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Rafale Feu"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_rondoudou(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Rondoudou"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Métronome"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Eclat Magique"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_grodoudou(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Grodoudou"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Calinerie"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Pouvoir Lunaire"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_nosferapti(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Nosferapti"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Cru-Ailes"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Onde Folie"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_nosferalto(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Nosferalto"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Vent Violent"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Machouille"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_mystherbe(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Mystherbe"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Fouet Liane"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Charge"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_ortide(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Ortide"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Tranche Herbe"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Détris Canon"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_rafflesia(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
  
    nom_ennemi = "Rafflesia"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Lance Soleil"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Feuille Magik"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_paras(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Paras"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Coupe"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Eclat Rock"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_parasect(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Parasect"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Survinsect"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Morsure"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_mimitoss(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Mimitoss"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Psycho"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Onde Folie"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_aeromite(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Aéromite"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Rafale Psy"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Papillodanse"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_taupiqueur(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Taupiqueur"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Tunnel"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Jet de Pierre"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_triopiqueur(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Triopiqueur"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Seisme"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Tombe Roche"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_persian(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Persian"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Jackpot"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Rayon Gemme"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_psykokwak(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Psykokwak"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Spatio Rift"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Choc Mental"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_akwakwak(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Akwakwak"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Bulle d'Eau"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Ecume"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_ferosinge(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Férosinge"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Casse Brique"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Poing Furieux"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_colossinge(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Colossinge"
    money_battle = 100

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Close Combat"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Frappe Atlas"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_caninos(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Caninos"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Roue de Feu"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Lance Flamme"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_arcanin(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Arcanin"
    money_battle = 100

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Déflagration"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Vitesse Extrême"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_ptitard(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Ptitard"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Bulle d'O"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Ecras Face"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_tetarte(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Tétarte"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Torgnole"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Vibraqua"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_tartard(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Tartard"
    money_battle = 200

    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Close Combat"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Bluff"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_abra(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Abra"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Psyko"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Teleport"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_kadabra(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Kadabra"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Rafale Psy"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Tilikinisi"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_alakazam(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Alakazam"
    money_battle = 100

    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Choc Mental"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Elecanon"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_machoc(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Machoc"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Eclat Roc"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Casse Brique"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_machopeur(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Machopeur"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Poing Karaté"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Frappe Atlas"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_mackogneur(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Mackogneur"
    money_battle = 200

    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Close Combat"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Corps Perdu"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_chetiflor(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Chétiflor"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Vanpigraine"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Balle Graine"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_boustiflor(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Boustiflor"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Tranch'Herbes"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Vol Vie"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_empiflor(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Empiflor"
    money_battle = 100

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Giga Sangsue"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Lance Soleil"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_tentacool(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Tentacool"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Swag"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Ligotage"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_tentacruel(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Tentacruel"
    money_battle = 75

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Hydrocanon"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Rafale Eau"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_racaillou(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Racaillou"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Coup de Boule"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Jet de Caillou"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_gravalanch(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Gravalanch"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ampleur 3/4"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Avalanch de Pierre"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_grolem(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Grolem"
    money_battle = 200

    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ampleur 1 milion %"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Seisme"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_ponyta(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Ponyta"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Roue de Feu"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Flamèche"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_galopa(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Galopa"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Vitesse Extême"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Déflagration"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_ramoloss(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Ramoloss"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Baillement"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Léchouille"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_flagadoss(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Flagadoss"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Surf"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Cascade"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_magneti(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Magnéti"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Luminocanon"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Eclair"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_magneton(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Magnéton"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Sonic Boom"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Tonerre"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_canarticho(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Canarticho"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Articho Magique"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Canard WC"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_doduo(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Doduo"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Bec Vrille"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Picpic"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_dodrio(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
   
    nom_ennemi = "Dodrio"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    

    attaque_ennemi_1 = "Vol"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Hâte"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_otaria(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Otaria"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Onde Boréal"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Croc Givre"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_lamantine(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Lamantine"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Blizare"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Laser Glace"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_tadmorv(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Tadmorv"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Avaltout"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Jugement"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_grotadmorv(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Grotadmorv"
    money_battle = 75

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Stockage"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Destockage"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_kokiyas(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Kokiyas"
    money_battle = 0

    xp_base_ennemi = 30
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 40
    stats_base_defense_ennemi = 20
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Croc Givre"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Pistolet à Eau"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_crustabri(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Crustabri"
    money_battle = 75

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Eclat Glace"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Ball Ombre"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_fantominus(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Fantominus"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ball Ombre"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Onde Folie"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_Spectrum(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Spectrum"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Malédiction"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Léchouille"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_ectoplasma(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Ectoplasma"
    money_battle = 200

    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Vibroscur"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Poing Ombre"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_onix(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Onix"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Queue de Fer"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Tomberoche"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_soporifik(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Soporifik"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Onde de Choc"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Psycho"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_hypnomade(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Hypnomade"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Onde de Choc"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Psycho"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_krabby(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Krabby"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Pince Masse"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Bulle d'O"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_krabboss(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Krabboss"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Vibraque"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Ecras Face"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_voltorbe(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Voltorbe"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Surcharge"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Tonerre"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_elcetrode(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Électrode"
    money_battle = 75

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Explosion"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Fatal Foudre"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_noeunoeuf(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Noeunoeuf"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Rafale Psy"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Vanpigraine"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_noadkoko(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Noadkoko"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Lance Soleil"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Psycho"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_osselait(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Osselait"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Tomberoche"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Jet de Sable"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_ossatueur(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Ossatueur"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Boomerang"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Tempête Sable"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_kicklee(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Kicklee"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)


    attaque_ennemi_1 = "Pied Voltige"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Tacle Assassin"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_tygnon(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Tygnon"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Giga Poing"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Mach Punch"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_excelangue(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Excelangue"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Léchouille"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Coup De Krane"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_smogo(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Smogo"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Bomb Beurk"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Gaz Toxik"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_smogogo(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Smogogo"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Destruction"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Detrit Canon"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_rhinocorne(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Rhinocorne"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Empale Corne"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Seisme"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_rhinoferos(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Rhinoféros"
    money_battle = 100

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ampleur 8"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Mitra Poing"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_leveinard(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Leveinard"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Oeuf Coque"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Eclat Magique"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_saquedeneu(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Saquedeneu"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Fouet Liane"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Eclat Magique"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_abo(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Abo"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ligotage"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Poison"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_kangourex(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Kangourex"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Mitra Poing"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Bélier"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_hypotrempe(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Hypotrempe"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Bulle d'O"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Pistolet à Eau"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_hypocean(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Hypocéan"
    money_battle = 100

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Hydrocanon"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Laser Glace"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_poissirene(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Poissirène"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Surf"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Cascade"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_poissoroy(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Poissoroy"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Hydrocanon"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Empale Corne"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_stari(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Stari"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Bulle d'O"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Surf"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_Staross(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Staross"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Surf"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Eclat Magique"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_mr_mime(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Mr.Mime"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Torgnole"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Psycho"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_insecateur(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Insécateur"
    money_battle = 75

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Lame Feuille"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Plaie Croix"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_lippoutou(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Lippoutou"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Laser Glace"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Bisous"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_elektek(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Élektek"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Fatale Foudre"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Boule Elek"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_magmar(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Magmar"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Surchauffe"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Poing Feu"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_scarabrute(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Scarabrute"
    money_battle = 75

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Plaie Croix"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Survinsecte"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_tauros(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Tauros"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ultralaser"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Bélier"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_magicarpe(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Magicarpe"
    money_battle = 0

    xp_base_ennemi = 10
    stats_base_vie_ennemi = 10
    stats_base_attaque_ennemi = 10
    stats_base_defense_ennemi = 10
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Draco-Ascencion"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Distorsion"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_leviator(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Léviator"
    money_battle = 200


    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ultralaser"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Draco-Souffle"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_lockhlass(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Lockhlass"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Surf"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Laser Glace"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_metamorph(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Métamorph"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Copie"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Métarmophose"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_evoli(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Évoli"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Câlin"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Meilleur Copain"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_aquali(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Aquali"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Surf"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Aqua Jet"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_voltali(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Voltali"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Tonerre"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Electacle"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_pyroli(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Pyroli"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Lance Flamme"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Nitrocharge"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_porygon(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Porygon"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    

    attaque_ennemi_1 = "Ultralaser"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Eclair"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_amonita(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Amonita"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Pistolet à Eau"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Jet de Pierre"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)
def ennemi_amonistar(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):


    nom_ennemi = "Amonistar"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Hydrocanon"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Pouvoir Antique"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_kabuto(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Kabuto"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Pistolet à Eau"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Jet de Pierre"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_kabutops(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Kabutops"
    money_battle = 0

    xp_base_ennemi = 50
    stats_base_vie_ennemi = 50
    stats_base_attaque_ennemi = 50
    stats_base_defense_ennemi = 50
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Pouvoir Antique"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Surf"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_ptera(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Ptéra"
    money_battle = 150

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Tomberoche"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Pouvoir Antique"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_ronflex(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Ronflex"
    money_battle = 0

    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Cognobidon"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Ultralaser"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_artikodin(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Artikodin"
    money_battle = 0

    xp_base_ennemi = 150
    stats_base_vie_ennemi = 150
    stats_base_attaque_ennemi = 150
    stats_base_defense_ennemi = 150
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Vent Glacé"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Blizard"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_electhor(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):
    
    nom_ennemi = "Électhor"
    money_battle = 0

    xp_base_ennemi = 150
    stats_base_vie_ennemi = 150
    stats_base_attaque_ennemi = 150
    stats_base_defense_ennemi = 150
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Fatale Foudre"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Surcharge"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_sulfura(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Sulfura"
    money_battle = 0

    xp_base_ennemi = 150
    stats_base_vie_ennemi = 150
    stats_base_attaque_ennemi = 150
    stats_base_defense_ennemi = 150
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Rapace"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Surchauffe"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_minidraco(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Minidraco"
    money_battle = 0

    xp_base_ennemi = 25
    stats_base_vie_ennemi = 25
    stats_base_attaque_ennemi = 25
    stats_base_defense_ennemi = 25
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Draco Souffle"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Pistolet à Eau"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_draco(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Draco"
    money_battle = 0

    xp_base_ennemi = 100
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Dracochoc"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Surf"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_dracolosse(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Dracolosse"
    money_battle = 200

    xp_base_ennemi = 125
    stats_base_vie_ennemi = 125
    stats_base_attaque_ennemi = 125
    stats_base_defense_ennemi = 125
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ultralaser"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Dracogriffe"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_mewtwo(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Mewtwo"
    money_battle = 0

    xp_base_ennemi = 150
    stats_base_vie_ennemi = 150
    stats_base_attaque_ennemi = 150
    stats_base_defense_ennemi = 150
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)

    attaque_ennemi_1 = "Ball Ombre"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Exploforce"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)

def ennemi_mew(niveau_ennemi,zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,xp_joueur,xp_prochain_niveau,cooldown,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item):

    nom_ennemi = "Mew"
    money_battle = 0

    xp_base_ennemi = 150
    stats_base_vie_ennemi = 100
    stats_base_attaque_ennemi = 100
    stats_base_defense_ennemi = 100
    
    xp_ennemi = xp_base_ennemi + ((xp_base_ennemi//10)*niveau_ennemi)
    stats_vie_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    stats_attaque_ennemi = stats_base_attaque_ennemi + ((stats_base_attaque_ennemi//10)* niveau_ennemi)
    stats_defense_ennemi = stats_base_defense_ennemi + ((stats_base_defense_ennemi//10)* niveau_ennemi)
    stats_vie_total_ennemi = stats_base_vie_ennemi + ((stats_base_vie_ennemi//10)* niveau_ennemi)
    

    attaque_ennemi_1 = "Psycho"
    effet_attaque_ennemi1 = 20 + (20//10 * (stats_attaque_ennemi//10))
    attaque_ennemi_2 = "Rafale Psy"
    effet_attaque_ennemi2 = 10 + (10//10 * (stats_attaque_ennemi//10))
    cooldown_ennemi = 1

    _ = system('cls')
    print(" ")
    print(" Vous êtes attaqué par un",nom_ennemi,"NIV",niveau_ennemi,"! (",stats_vie_ennemi," PV"" )")
    time.sleep(2.5)
    choix_action(zone,niveau_joueur,stats_vie_joueur,stats_vie_total_joueur,stats_attaque_joueur,stats_defense_joueur,attaque1,effet1,attaque2,effet2,stats_vie_ennemi,stats_vie_total_ennemi,stats_attaque_ennemi,stats_defense_ennemi,nom_ennemi,niveau_ennemi,attaque_ennemi_1,attaque_ennemi_2,effet_attaque_ennemi1,effet_attaque_ennemi2,xp_joueur,xp_prochain_niveau,xp_ennemi,cooldown,cooldown_ennemi,map,X,Y,map_ville,map_foret,state_spawn_pkmn,fight,ListPokemonInBag,bank_account,list_item,money_battle)