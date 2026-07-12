import sqlite3
from datetime import datetime
DATABASE = "reviews.db"


def create_database():
    """Create the reviews table if it doesn't exist."""

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        language TEXT,

        score INTEGER,

        review_date TEXT

    )
    """)

    conn.commit()
    conn.close()







def save_review(filename, language, score):
    """Save a review into the database."""

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO reviews
        (filename, language, score, review_date)
        VALUES (?, ?, ?, ?)
    """,
    (
        filename,
        language,
        score,
        datetime.now().strftime("%d-%m-%Y %H:%M")
    ))

    conn.commit()
    conn.close()
def get_reviews():
    """Fetch all reviews ordered by newest first."""

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, filename, language, score, review_date
        FROM reviews
        ORDER BY id DESC
    """)

    reviews = cursor.fetchall()

    conn.close()

    return reviews


def delete_review(review_id):
    """Delete a review by its ID."""

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM reviews WHERE id=?",
        (review_id,)
    )

    conn.commit()
    conn.close()

