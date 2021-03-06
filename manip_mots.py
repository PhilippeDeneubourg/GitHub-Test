#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Joue avec les lettres
"""


#
__author__ = "Nom de l'étudiant auteur du code"
__copyright__ = "Année scolaire 2020-2021, The Python Project - IPES Ath"
__credits__ = ["Philippe Deneubourg", "Laurence Lahaise"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Nom de l'étudiant modificateur du code"
__email__ = "ipesttinfo@gmail.com"
__status__ = "Development - Test - Production"
#


# --- Import Section ---
# from math import pi


# --- Function Section ---
def longueur(mot_value):
    """
    Indique le nombre de caractères contenus dans un mot

    :param mot_value: Mot à analyser
    :type mot_value: string

    :return: Nombre de caractères contenus dans le mot
    :rtype: integer
    """

    nbr_car_value = len(mot_value)

    return nbr_car_value


def gauche(mot_value, nbr_value):
    """
    Extrait les X premiers caractères d'un mot

    :param mot_value: Mot à analyser
    :type mot_value: string

    :param nbr_value: Nombre de caractères à extraire à partir du début du mot
    :type nbr_value: integer

    :return: Chaîne des X premiers caractères d'un mot
    :rtype: string
    """

    x_prem_car = mot_value[:nbr_value]

    return x_prem_car


def droite(mot_value, nbr_value):
    """
    Extrait les X derniers caractères d'un mot

    :param mot_value: Mot à analyser
    :type mot_value: string

    :param nbr_value: Nombre de caractères à extraire à partir de la fin du mot
    :type nbr_value: integer

    :return: Chaîne des X derniers caractères d'un mot
    :rtype: string
    """

    x_dern_car = mot_value[(-1 * nbr_value):]

    return x_dern_car


def milieu_gauche(mot_value, nbr_value, pos_value):
    """
    Extrait les X caractères d'un mot avant une position donnée dans ce mot

    :param mot_value: Mot à analyser
    :type mot_value: string

    :param nbr_value: Nombre de caractères à extraire
    :type nbr_value: integer

    :param pos_value: position dans le mot avant extraction
    :type pos_value: integer

    :return: Chaîne des X caractères extrait d'un mot.
    :rtype: string

    La fonction ne retourne rien si pos_value vaut 0
    """

    if nbr_value > pos_value:
        nbr_value = pos_value

    x_car = mot_value[(pos_value - nbr_value):pos_value]

    return x_car


def milieu_droite(mot_value, nbr_value, pos_value):
    """
    Extrait les X caractères d'un mot après une position donnée dans ce mot

    :param mot_value: Mot à analyser
    :type mot_value: string

    :param nbr_value: Nombre de caractères à extraire
    :type nbr_value: integer

    :param pos_value: position dans le mot avant extraction
    :type pos_value: integer

    :return: Chaîne des X caractères extrait d'un mot.
    :rtype: string

    La fonction ne retourne rien si pos_value est plus grand que la longueur du mot
    """

    x_car = mot_value[(pos_value - 1):(pos_value - 1 + nbr_value)]

    return x_car


# --- Main Program ---
if __name__ == '__main__':

    print('Menu')
    print('----')
    print('1 : Afficher le nombre de caractères d\'un mot')
    print('2 : Afficher les X premiers caractères d\'un mot')
    print('3 : Afficher les X derniers caractères d\'un mot')
    print('4 : Afficher les X caractères précédents à partir d\'une position donnée dans un mot')
    print('5 : Afficher les X caractères suivants à partir d\'une position donnée dans un mot')
    print('')
    choix = input('Choisissez l\'action que vous désirez mener : ')

    mot = input('Introduisez le mot à analyser : ')

    if choix == '1':

        print("Le mot <", mot, "> contient", longueur(mot), "caratère(s)")

    elif choix == '2':

        nbr = int(input('Combien de caracères souhaitez-vous extraire : '))
        print("Les", nbr, "premiers caractères du mot <", mot, "> sont <", gauche(mot, nbr), ">")

    elif choix == '3':

        nbr = int(input('Combien de caracères souhaitez-vous extraire : '))
        print("Les", nbr, "derniers caractères du mot <", mot, "> sont <", droite(mot, nbr), ">")

    elif choix == '4':

        nbr = int(input('Combien de caracères souhaitez-vous extraire : '))
        pos = int(input('A partir de quelle position souhaitez-vous commencer l\'extraction : '))
        print("Les", nbr, "caractères du mot <", mot, "> après la position", pos, "sont <",
              milieu_gauche(mot, nbr, pos), ">")

    else:

        nbr = int(input('Combien de caracères souhaitez-vous extraire : '))
        pos = int(input('A partir de quelle position souhaitez-vous commencer l\'extraction : '))
        print("Les", nbr, "caractères du mot <", mot, "> avant la position", pos, "sont <",
              milieu_droite(mot, nbr, pos), ">")
