CREATE TABLE IF NOT EXISTS working_data (
    date_ingestion DateTime,
    data_row String,
    tag String
) ENGINE = MergeTree()
ORDER BY date_ingestion;