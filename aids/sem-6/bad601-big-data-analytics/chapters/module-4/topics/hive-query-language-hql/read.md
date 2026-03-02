sql
    CREATE EXTERNAL TABLE IF NOT EXISTS student_logs (
        student_id INT,
        action STRING,
        timestamp BIGINT
    )
    COMMENT 'Table for student activity logs'
    PARTITIONED BY (date STRING)
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    STORED AS TEXTFILE
    LOCATION '/user/hive/warehouse/student_logs';