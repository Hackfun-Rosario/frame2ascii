# -*- encoding: utf8 -*-
from os import listdir as ls
from curses import wrapper
from time import sleep

## definimos el directorio de los archivos de texto y los listamos
FRAMESDIR = "transformed"
framelist = ls(FRAMESDIR)
FRAMELEN = len(framelist)

## cargamos los cuadros de animación (frames)
frames = []

for filename in framelist:
  # leemos el contenido de todos los archivos ("r" es READ-ONLY) y lo guardamos en el array de frames
  with open(f"{FRAMESDIR}/{filename}", "r") as file:
    frames.append(file.read().split("\n"))


## función de animación principal. es un callback que se llama desde wrapper (una función de curses)
def animation(stdscr):
    # definimos el puntero al cuadro que se dibuja
    curframe = 0

    # hacemos un loop infinito
    while True:
      stdscr.clear() # limpiamso la pantalla

      try:
        # iteramos por cada línea del frame actual y dibujamos una abajo de la otra
        # i = orden de cada línea, l = el contenido de la línea leída
        # enumerate toma un array y devuelve una tupla así: (índice, datos)
        for i, l in enumerate(frames[n]):
          stdscr.addstr(i, 0, l)
      except:
        # esto no se hace, pero acá no importa
        pass

      # hacemos refresh y mandamos a dormir el proceso por una fracción de segundo
      # sleep traba todo, es una forma rudimentaria de limitar el framerate pero funciona para esto
      stdscr.refresh()
      sleep(1/60)
      
      ## esto aumenta el puntero en 1 y vuelve a 0 si nos pasamos de la longitud de la lista
      n = (n + 1) % FRAMELEN


## wrapper de curses. esto ejecuta la función principal pasándole como parámetro la ventana a escribir
wrapper(animation)