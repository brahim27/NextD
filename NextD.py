
"""
envoyer une resuqets.get(https://api.themoviedb.org/3/discover/movie?api_key=5d6a7f84d2b33e215034f1c46625910b&_genres=2)
2 et letest
"""
#coding:utf-8

from lib2to3.pgen2.pgen import generate_grammar
import random
from re import X
import requests

ListFilm = 0
genres = {"action": 28, "adventure": 12, "animation": 16, "comedy": 35, "crime": 80, "documentary": 99, "drama": 18, "family": 10751, "fantasy": 14, "history": 36, "horror": 27, "music": 10402, "mystery": 9648, "romance": 10749, "science_fiction": 878, "tv_movie": 10770, "thriller": 53, "war": 10752, "western": 37}

for x, y in genres.items():
	print(f"{x}-{y}")

while True:
	input_genre = input("What's your favorite genre: ").lower().strip()
	
	if input_genre in genres:
		print("yes its true")
		break
	
	print("Please type a valid genre!")

genre_id = genres[input_genre]

genra_idValue = {
	"action": 0,
	"adventure": 0,	
	"animation": 0,
	"comedy": 0,
	"crime": 0,
	"documentary": 0,
	"drama": 0,
	"family": 0,
	"fantasy": 0,
	"history": 0,
	"horror": 0,
	"music": 0,
	"mystery": 0,
	"romance": 0,
	"science_fiction": 0,
	"tv_movie": 0,
	"thriller": 0,
	"war": 0,
	"western": 0,
}

discover_url = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=5d6a7f84d2b33e215034f1c46625910b&with_genres=" + str(genres[input_genre]))

id_discover = discover_url.json()["results"][0]["id"]
All_ids = [id_discover]
print (All_ids)

NameFilm_url = requests.get("https://api.themoviedb.org/3/movie/" + str(id_discover) + "?api_key=5d6a7f84d2b33e215034f1c46625910b")
NameFilm = (NameFilm_url.json()["original_title"])
print (NameFilm)

Watched = input("Did you watched" +NameFilm+ "Yes or No:")

if Watched == "Yes" or "yes":
	ListFilm +=	1
 

discover_url = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=5d6a7f84d2b33e215034f1c46625910b&with_genres=" + str(genres[input_genre]))
id_discover = discover_url.json()["results"][genra_idValue[input_genre]]["id"]

while id_discover in All_ids and ListFilm != 0:
	genra = input("What's your favorite genra:")
	discover_url = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=5d6a7f84d2b33e215034f1c46625910b&with_genres=" + str(genres[input_genre]))
	genra_idValue[input_genre] += 1
	id_discover = discover_url.json()["results"][genra_idValue[input_genre]]["id"]
	All_ids = [id_discover]
	print(id_discover)
	NameFilm_url = requests.get("https://api.themoviedb.org/3/movie/" + str(id_discover) + "?api_key=5d6a7f84d2b33e215034f1c46625910b")
	NameFilm = NameFilm_url.json()["original_title"]
	print (NameFilm)
