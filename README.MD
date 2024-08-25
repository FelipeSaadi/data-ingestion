# Como rodar
Abra a pasta data_pipeline no terminal

Crie o .env e troque para os dados corretos
```
cp .env.example .env
```

Rode o comando para iniciar a infra:
```
make up
```

Abra um novo terminal

Rode o comando para rodar o projeto:
```
make all
```

Teste os endpoints:
```
GET http://localhost:5000/getData
Content-Type: application/json
```

```
POST http://localhost:5000/ingestion
Content-Type: application/json

[
  {
    "id": 1,
    "title": "The Shawshank Redemption",
    "year": 1994,
    "genre": [
      "Drama"
    ],
    "rating": 9.3,
    "director": "Frank Darabont",
    "actors": [
      "Tim Robbins",
      "Morgan Freeman"
    ],
    "plot": "Two imprisoned men bond over several years, finding solace and eventual redemption through acts of common decency.",
    "poster": "https://fakeimg.pl/220x310/ff0000",
    "trailer": "https://example.com/shawshank_redemption_trailer.mp4",
    "runtime": 142,
    "awards": "Nominated for 7 Oscars",
    "country": "USA",
    "language": "English",
    "boxOffice": "$28.3 million",
    "production": "Columbia Pictures",
    "website": "http://www.warnerbros.com/movies/shawshank-redemption"
    },
]
```