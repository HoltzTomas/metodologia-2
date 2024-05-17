# correr el siguiente comando para instalar requests
# python -m pip install requests

import requests

#Codigo para pedirle al usuario que elija un actor
#Doy un par de opciones de actores
#Justificacion: Si el prototipo con pocos actores logra el objetivo, se pueden agregar todos en un futuro
#Con un una lista de busqueda mas avanzada
print("Los actores disponibles son:")
print("Leonardo DiCaprio")
print("Los actores disponibles son:")
print("Los actores disponibles son:")
actorUsuario = input("Escribe el nombre de un actor: ")

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_people=${actorUsuario}"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjOTE1ZGU3MjY5YjU3ZmIzODdhZGYzNzgzODNhYTc1MyIsInN1YiI6IjYyYmNiYzdhZTFmYWVkMWRjNzc2YmFhNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fyh6VEqtDM5AAuIk6g0_4CnCbAKHmQ5ttqnq0Ia-lcM"
}

#Add query params
response = requests.get(url, headers=headers)

print(response.text)