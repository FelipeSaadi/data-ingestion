from core import __version__
from core.data_processing import validate_data, process_data, prepare_dataframe_for_insert

def test_validate_data_valid():
    valid_data = [
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
        }
    ]
    
    assert  validate_data(valid_data) == valid_data

    
def test_validate_data_without_some_atribute(): 
    invalid_data = [
        {
        "id": 1,
        "title": "The Shawshank Redemption",
        "year": 1994,
        "rating": 9.3,
        "trailer": "https://example.com/shawshank_redemption_trailer.mp4",
        "runtime": 'abc',
        "awards": "Nominated for 7 Oscars",
        "country": "USA",
        "language": "English",
        "boxOffice": "$28.3 million",
        "production": "Columbia Pictures",
        "website": "http://www.warnerbros.com/movies/shawshank-redemption"
        }
    ]
    
    assert validate_data(invalid_data) == False
    
def test_validate_data_with_empty_list(): 
    invalid_data = [
        {
            "id": 1,
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genre": [],
            "rating": 9.3,
            "director": "Frank Darabont",
            "actors": [],
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
        }
    ]
    
    assert validate_data(invalid_data) == False
    
def test_validate_data_with_wrong_types(): 
    invalid_data = [
        {
            "id": 'abc',
            "title": 1231241,
            "year": '1994',
            "genre": ['Test'],
            "rating": 'abc',
            "director": "Frank Darabont",
            "actors": ["Actor"],
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
        }
    ]
    
    assert validate_data(invalid_data) == False
    
def test_validate_data_without_data():
    invalid_data = None
    
    assert validate_data(invalid_data) == False
    