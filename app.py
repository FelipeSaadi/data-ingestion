from flask import Flask, request, jsonify
from datetime import datetime
from core.minio_client import create_bucket_if_not_exists, upload_file, download_file
from core.clickhouse_client import execute_sql_script, get_client, insert_dataframe
from core.data_processing import process_data, prepare_dataframe_for_insert, validate_data
import pandas as pd
import requests

app = Flask(__name__)

# Criar bucket se não existir
create_bucket_if_not_exists("raw-data")

# Executar o script SQL para criar a tabela
execute_sql_script('sql/create_table.sql')

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.route('/ingestion', methods=['POST'])
def ingestion():
    data = request.get_json()
    
    if not data or len(data) < 1:
        return jsonify({"error": "Invalid data"}), 400

    result = validate_data(data)
    print(result)
    
    if not result:
        return jsonify({"error": "Wrong data type"}), 400
    
    # Processar e salvar dados
    filename = process_data(data)
    upload_file("raw-data", filename)

    # Ler arquivo Parquet do MinIO
    download_file("raw-data", filename, f"downloaded_{filename}")
    df_parquet = pd.read_parquet(f"downloaded_{filename}")

    # Preparar e inserir dados no ClickHouse
    df_prepared = prepare_dataframe_for_insert(df_parquet)
    client = get_client()  # Obter o cliente ClickHouse
    insert_dataframe(client, 'working_data', df_prepared)

    return jsonify({"message": "Dados recebidos, armazenados e processados com sucesso"}), 200

@app.route('/getData', methods=['GET'])
def receive_data():
    data = requests.get("https://freetestapi.com/api/v1/movies")
    json = data.json()
    
    if not json or len(json) < 1:
        return jsonify({"error": "Invalid data"}), 400

    result = validate_data(json)
    print(result)
    
    if not result:
        return jsonify({"error": "Wrong data type"}), 400

    # Processar e salvar dados
    filename = process_data(json)
    upload_file("raw-data", filename)

    # Ler arquivo Parquet do MinIO
    download_file("raw-data", filename, f"downloaded_{filename}")
    df_parquet = pd.read_parquet(f"downloaded_{filename}")

    # Preparar e inserir dados no ClickHouse
    df_prepared = prepare_dataframe_for_insert(df_parquet)
    client = get_client()  # Obter o cliente ClickHouse
    insert_dataframe(client, 'working_data', df_prepared)

    return jsonify({"message": "Data successfully received, stored and processed"}), 200

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "An unexpected error occurred!"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)