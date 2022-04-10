import csv
import json
import consolemenu as cm
import consolemenu.items as cmi
import consolemenu.format as cmf
from colorama import Fore, init


def back():
    input(Fore.WHITE + "Presione una tecla para regresar: ")


def Releases_2021():
    """Esta funcion imprime solo los nombres de las peliculas de 2021, a partir del contenido de un archivo cvs"""
    movies = open("movies_2021.csv", "r", encoding='utf-8')
    csvreader = csv.reader(movies, delimiter=',')
    for ln in csvreader:
        print('\n', Fore.WHITE + ln[2], "\n")
        print(Fore.CYAN + "<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    movies.close()
    back()


def Countries_most_common():
    """Esta funcion imprime el contenido de un archivo en formato json, de acuerdo al contexto"""
    countries = open("countries_most_common.txt", "r", encoding='utf-8')
    c = json.load(countries)
    countries.close()
    for country in c:
        print(Fore.CYAN + country, Fore.WHITE + "con" + Fore.GREEN,
              c[country], Fore.WHITE + "producciones", '\n')
    back()


# para poder imprimir a color
init()

# Configuracion del formato del menu
menu_format = cm.MenuFormatBuilder().set_border_style_type(cmf.MenuBorderStyleType.HEAVY_BORDER) \
    .set_prompt(Fore.RED + "OPCION>") \
    .set_title_align('center') \
    .set_subtitle_align('center') \
    .set_left_margin(10) \
    .set_right_margin(10) \
    .show_header_bottom_border(True)


menu = cm.ConsoleMenu(title=Fore.RED + "Datos sobre Netflix",
                      epilogue_text="Alumna: Cuenca Antonella", formatter=menu_format, exit_option_text=Fore.RED + "Salir")


function_item_1 = cmi.FunctionItem(
    Fore.MAGENTA + "Peliculas del 2021.", Releases_2021)

function_item_2 = cmi.FunctionItem(
    Fore.MAGENTA + "Los 5 paises con mas producciones.", Countries_most_common)


menu.append_item(function_item_1)
menu.append_item(function_item_2)

menu.show()
