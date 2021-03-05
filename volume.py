#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Calcule des volumes
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
from math import pi


# --- Function Section ---
def volume_cone(rayon_value, hauteur_value):
    """
    Calcule le volume d'un cône droit à partir de la saisie d'un rayon et d'une hauteur exprimés en mètre

    :param rayon_value: Valeur du rayon du cône exprimé en mètre
    :type rayon_value: float

    :param hauteur_value: Valeur de la hauteur du cône exprimé en mètre
    :type hauteur_value: float

    :return: Valeur du volume du cone droit
    :rtype: float
    """

    volume_value = (pi * rayon_value * rayon_value * hauteur_value) / 3.0

    return volume_value


def volume_cube(cote_value):
    """
    Calcule le volume d'un cube à partir de la saisie d'un côté exprimé en mètre

    :param cote_value: Valeur du rayon du cône exprimé en mètre
    :type cote_value: float

    :return: Valeur du volume du cube
    :rtype: float
    """

    volume_value = cote_value * cote_value * cote_value

    return volume_value


# --- Main Program ---
if __name__ == '__main__':

    print('Menu')
    print('----')
    print('1 : Cube')
    print('2 : Cône droit')
    print('')
    choix = input('Choississez le volume que vous désirez calculer : ')

    if choix == '1':
        cote = float(input("Côté du cube (m) : "))

        print("Volume du cube =", volume_cube(cote), "m3")

    else:

        rayon = float(input("Rayon du cône (m) : "))
        hauteur = float(input("Hauteur du cône (m) : "))

        print("Volume du cône =", volume_cone(rayon, hauteur), "m3")
