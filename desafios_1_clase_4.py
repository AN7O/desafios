from collections import Counter
import csv
import json


def country_counter(countries):
    """Esta funcion retorna, en un diccionario, la cantidad de producciones por pais"""
    cant = []
    for country in countries:
        # En caso de tener mas de un pais en la lista, se agregan cada uno de ellos
        for c in country:
            cant.append(c.strip())
    return Counter(cant)


netflix_csv = open("netflix_titles.csv", "r", encoding='utf-8')
movies_2021_csv = open("movies_2021.csv", "w",  encoding='utf-8', newline='')
csvreader = csv.reader(netflix_csv, delimiter=',')
csvwriter = csv.writer(movies_2021_csv)
csvwriter.writerow(next(csvreader))
countries = []

for ln in csvreader:
    if ln[7] == "2021":
        csvwriter.writerow(ln)
    if ln[5] != '':
        # Si la produccion cuenta con mas de un pais, se separa en una lista de mas de 1 elemento
        countries.append(ln[5].lower().split(','))

netflix_csv.close()
movies_2021_csv.close()

cant = country_counter(countries)
print("Los cinco (5) países con más producciones en Netflix: ")
print(dict(cant.most_common()[0:5]), "\n")
# Guardo los resultados en un archivo de texto
cmc = open("countries_most_common.txt", "w")
json.dump(dict(cant.most_common()[0:5]), cmc, indent=4)
cmc.close()
