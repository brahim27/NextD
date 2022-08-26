
"""
envoyer une resuqets.get(https://api.themoviedb.org/3/discover/movie?api_key=5d6a7f84d2b33e215034f1c46625910b&_genres=2)
2 et letest
"""
#coding:utf-8

import random
import requests

ListFilm = 0

Action = 28
Adventure = 12
Animation = 16
Comedy = 35
Crime = 80
Documentary = 99
Drama = 18
Family = 10751
Fantasy = 14
History = 36
Horror = 27
Music = 10402
Mystery = 9648
Romance = 10749
Science_Fiction = 878
TV_Movie = 10770
Thriller = 53
War = 10752
Western = 37
Genras = {"Action","Adventure","Animation","Comedy","Crime","Documentary","Drama","Family","Fantasy","History","Horror","Music","Mystery","Romance","Science_Fiction","TV_Movie","Thriller","War","Western"}
print (Genras)


genra = input("What's your favorite genra:")

if genra == "Action":
	genra_id = 28
if genra == "Adventure":
	genra_id = 12
if genra == "Animation":
	genra_id = 16
if genra == "Comedy":
	genra_id = 35
if genra == "Crime":
	genra_id = 80
if genra == "Documentary":
	genra_id = 99
if genra == "Drama":
	genra_id = 18
if genra == "Family":
	genra_id = 10751
if genra == "Fantasy":
	genra_id = 14
if genra == "History":
	genra_id = 36
if genra == "Horror":
	genra_id = 27
if genra == "Music":
	genra_id = 10402
if genra == "Mystery":
	genra_id = 9648
if genra == "Romance":
	genra_id = 10749
if genra == "Science_Fiction":
	genra_id = 878
if genra == "TV_Movie":
	genra_id = 10770
if genra == "Thriller":
	genra_id = 53
if genra == "War":
	genra_id = 10752
if genra == "Western":
	genra_id = 37
ListFilmValue = 0
ListeValue = 0
IdValue = 0
dic_genra = {
	
	0:	{"g_name": "Action",
		"g_id": "28",
		"IdValue": 0
		},
	1:	{"g_name": "Adventure",
		"g_id": "12",
		"IdValue": 0
		},
	2:	{"g_name": "Animation",
		"g_id": "16",
		"IdValue": 0
		},
	3:	{"g_name": "Comedy",
		"g_id": "35",
		"IdValue": 0
		},
	4:	{"g_name": "Crime",
		"g_id": "80",
		"IdValue": 0
		},
	5:	{"g_name": "Documentary",
		"g_id": "99",
		"IdValue": 0
		},
	6:	{"g_name": "Drama",
		"g_id": "18",
		"IdValue": 0
		},
	7:	{"g_name": "Family",
		"g_id": "10751",
		"IdValue": 0
		},
	8:	{"g_name": "Fantasy",
		"g_id": "14",
		"IdValue": 0
		},
	9:	{"g_name": "History",
		"g_id": "36",
		"IdValue": 0
		},
    10:	{"g_name": "Horror",
		"g_id": "27",
		"IdValue": 0
		},
    11:	{"g_name": "Music",
		"g_id": "10402",
		"IdValue": 0
		},
	12:	{"g_name": "Mystery",
		"g_id": "9648",
		"IdValue": 0
		},
	13:	{"g_name": "Romance",
		"g_id": "10749",
		"IdValue": 0
		},
	14:	{"g_name": "Science_Fiction",
		"g_id": "878",
		"IdValue": 0
		},
	15:	{"g_name": "TV_Movie",
		"g_id": "10770",
		"IdValue": 0
		},
	16:	{"g_name": "Thriller",
		"g_id": "53",
		"IdValue": 0
		},
	17:	{"g_name": "War",
		"g_id": "10752",
		"IdValue": 0
		},
	18:	{"g_name": "Western",
		"g_id": "37",
		"IdValue": 0
		}

}
discover_url = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=5d6a7f84d2b33e215034f1c46625910b&with_genres="+str(genra_id))
"""
GenraIds = discover_url.json()["results"][ListFilmValue]["genre_ids"][ListeValue]
len_genra = len(discover_url.json()["results"][ListFilmValue]["genre_ids"])
"""
id_discover = discover_url.json()["results"][0]["id"]
All_ids = [id_discover]
print (All_ids)

NameFilm_url = requests.get("https://api.themoviedb.org/3/movie/"+str(id_discover)+"?api_key=5d6a7f84d2b33e215034f1c46625910b")
NameFilm = (NameFilm_url.json()["original_title"])
print (NameFilm)

Watched = input("Did you watched" +NameFilm+ "Yes or No:")

if Watched == "Yes" or "yes":
	ListFilm +=	1
 
if Watched == "No" or "no":
	ListFilm == ListFilm

discover_url = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=5d6a7f84d2b33e215034f1c46625910b&with_genres="+str(genra_id))
id_discover = discover_url.json()["results"][IdValue]["id"]

while id_discover in All_ids and ListFilm != 0:
	genra = input("What's your favorite genra:")
	discover_url = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=5d6a7f84d2b33e215034f1c46625910b&with_genres="+str(genra_id))
	IdValue += 1
	id_discover = discover_url.json()["results"][IdValue]["id"]
	All_ids = [id_discover]
	print(id_discover)
	NameFilm_url = requests.get("https://api.themoviedb.org/3/movie/"+str(id_discover)+"?api_key=5d6a7f84d2b33e215034f1c46625910b")
	NameFilm = (NameFilm_url.json()["original_title"])
	print (NameFilm)
















"""
Les réponses informatives (100 - 199)
Les réponses de succès (200 - 299)
Les messages de redirection (300 - 399)
Les erreurs du client (400 - 499)
Les erreurs du serveur (500 - 599)

"""

