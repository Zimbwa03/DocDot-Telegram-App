import sqlite3
import json

def setup_database():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer BOOLEAN NOT NULL,
        explanation TEXT NOT NULL,
        ai_explanation TEXT,
        reference_json TEXT,
        category TEXT NOT NULL
    )
    ''')

    # Sample questions
    ANATOMY_REFERENCES = ["Snell Clinical Anatomy", "Gray's Anatomy", "Keith Moore", "Barr's The Human Nervous System"]
    PHYSIOLOGY_REFERENCES = ["Ganong Physiology", "Vander's Human Physiology", "Guyton & Hall", "Boron Medical Physiology"]
    
    sample_questions = [
        (
            "The facial nerve innervates muscles of facial expression.",
            True,
            "CN VII (facial nerve) controls all muscles of facial expression.",
            "The facial nerve exits the skull through the stylomastoid foramen and provides motor innervation to the muscles of facial expression.",
            json.dumps({
                "Snell Clinical Anatomy": "Chapter 11, p.347",
                "Gray's Anatomy": "Chapter 28, p.456",
                "Keith Moore": "Chapter 8, p.912"
            }),
            "Head and Neck"
        ),
        (
            "The median nerve passes through the carpal tunnel.",
            True,
            "The median nerve passes through the carpal tunnel with the flexor tendons.",
            "The median nerve travels with the flexor tendons through the carpal tunnel, making it vulnerable to compression in carpal tunnel syndrome.",
            json.dumps({"Moore's Anatomy": "Upper Limb Chapter"}),
            "Upper Limb"
        )
    ]

    cursor.executemany('''
    INSERT OR IGNORE INTO questions 
    (question, answer, explanation, ai_explanation, reference_json, category)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', sample_questions)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()