import sqlite3


DATABASE_NAME = "moving.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            email TEXT,
            pickup_address TEXT,
            dropoff_address TEXT,
            moving_date TEXT,
            moving_time TEXT,
            quote REAL,
            status TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_booking(
    name,
    phone,
    email,
    pickup_address,
    dropoff_address,
    moving_date,
    moving_time,
    quote
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO bookings (
            name,
            phone,
            email,
            pickup_address,
            dropoff_address,
            moving_date,
            moving_time,
            quote,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        phone,
        email,
        pickup_address,
        dropoff_address,
        moving_date,
        moving_time,
        quote,
        "Pending"
    ))

    connection.commit()

    booking_id = cursor.lastrowid

    connection.close()

    return booking_id