#Dado especial para Monopoly Gamer con microbit
from microbit import *
import random

#Crear imágenes
poww = Image("55555:"
             "09990:"
             "09990:"
             "09000:"
             "55555")

greenshell = Image("05550:"
             "50005:"
             "50005:"
             "50005:"
             "05550")

redshell = Image("09990:"
             "90009:"
             "90009:"
             "90009:"
             "09990")

coins = Image("00990:"
             "00990:"
             "00000:"
             "99099:"
             "99099")

blooper = Image("00900:"
             "09990:"
             "90909:"
             "99999:"
             "90909")

#Crear lista con nombres de imágenes
dado_especial=[poww,greenshell,redshell,coins,blooper]
#Mostrar uno de los elementos de forma aleatoria
display.show(random.choice(dado_especial))
