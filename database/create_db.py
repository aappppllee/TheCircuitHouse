import mysql.connector
from config.config import DATABASE_CONFIG

insert_query = """
INSERT INTO Productdetails (pid, Brand_Name, `Price (Rupee)`, Rating, Rating_Count, Review_Count, url)
VALUES (%s,%s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    Brand_Name = VALUES(Brand_Name),
    `Price (Rupee)` = VALUES(`Price (Rupee)`),
    Rating = VALUES(Rating),
    Rating_Count = VALUES(Rating_Count),
    Review_Count = VALUES(Review_Count),
    url = VALUES(url);
"""

def create_database():
    conn = mysql.connector.connect(
        host=DATABASE_CONFIG['host'],
        user=DATABASE_CONFIG['user'],
        password=DATABASE_CONFIG['password']
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ProductDatabase;")
    conn.commit()
    cursor.close()
    conn.close()

def create_tables():
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Productdetails (   
        pid VARCHAR(255) PRIMARY KEY, 
        Brand_Name VARCHAR(255),
        `Price (Rupee)` INT,
        Rating FLOAT,
        Rating_Count INT,
        Review_Count INT,
        Sponsored TINYINT(1) NOT NULL DEFAULT 0,
        Ranking INT AUTO_INCREMENT,
        url TEXT NOT NULL,
        UNIQUE (Ranking)
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database()
    create_tables()
