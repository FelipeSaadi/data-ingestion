import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime
from marshmallow  import Schema, fields, validate, ValidationError

class MovieSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    year = fields.Int(required=True)
    genre = fields.List(
        fields.Str(),
        required=True,
        validate=validate.Length(min=1,max=10)
    )
    rating = fields.Float(required=True)
    director = fields.Str(required=True)
    actors = fields.List(
        fields.Str(),
        required=True,
        validate=validate.Length(min=1,max=10)
    )
    plot = fields.Str(required=True)
    poster = fields.Str(required=True)
    trailer = fields.Str(required=True)
    runtime = fields.Int(required=True)
    awards = fields.Str(required=True)
    country = fields.Str(required=True)
    language = fields.Str(required=True)
    boxOffice = fields.Str(required=True)
    production = fields.Str(required=True)
    website = fields.Str(required=True)
    
def validate_data(data):
    movie_schema = MovieSchema()
    
    if not data:
        return False
    
    try:
        for movie in data:
            movie_schema.load(movie)
        return data
    except ValidationError as e:
        return False

def process_data(data):
    # Criar DataFrame e salvar como Parquet
    df = pd.DataFrame([data])
    filename = f"raw_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
    table = pa.Table.from_pandas(df)
    pq.write_table(table, filename)
    return filename

def prepare_dataframe_for_insert(df):
    df['date_ingestion'] = datetime.now()
    df['data_row'] = df.apply(lambda row: row.to_json(), axis=1)
    df['tag'] = 'example_tag'
    return df[['date_ingestion', 'data_row', 'tag']]