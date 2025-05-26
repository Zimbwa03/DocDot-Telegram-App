import openai
import json
import sqlite3
import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OPENROUTER_API_KEY = "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"

CATEGORIES = {
    "Anatomy": [
        "Head and Neck",
        "Upper Limb",
        "Thorax",
        "Lower Limb",
        "Pelvis and Perineum",
        "Neuroanatomy",
        "Abdomen"
    ],
    "Physiology": [
        "Cell",
        "Nerve and Muscle",
        "Blood",
        "Endocrine",
        "Reproductive",
        "Gastrointestinal Tract",
        "Renal",
        "Cardiovascular System",
        "Respiratory",
        "Medical Genetics",
        "Neurophysiology"
    ]
}

REFERENCE_BOOKS = {
    "Anatomy": [
        "Snell Clinical Anatomy",
        "Gray's Anatomy",
        "Keith Moore's Clinical Anatomy",
        "Barr's Human Nervous System"
    ],
    "Physiology": [
        "Ganong's Review of Medical Physiology",
        "Guyton and Hall Textbook of Medical Physiology",
        "Vander's Human Physiology",
        "Boron Medical Physiology"
    ]
}

def generate_question(category: str, subcategory: str) -> Optional[Dict]:
    """Generate a question using AI with references to standard texts."""
    if not OPENROUTER_API_KEY:
        logger.error("OpenRouter API key is not set")
        return None

    prompt = f"""Create a detailed true/false medical question about {subcategory} in {category}.
    Include:
    1. A clear question statement
    2. The correct answer (true/false)
    3. A concise explanation
    4. A detailed AI-generated explanation with clinical relevance
    5. Specific page references from: {', '.join(REFERENCE_BOOKS[category])}

    Format as JSON with keys: question, answer, explanation, ai_explanation, references"""

    try:
        client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
            default_headers={
                "HTTP-Referer": "https://replit.com",
                "X-Title": "Medical Question Generator"
            }
        )

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat:67b",
            messages=[{"role": "user", "content": prompt}]
        )

        if not response.choices:
            logger.error("No response received from API")
            return None

        content = response.choices[0].message.content
        question_data = json.loads(content)
        question_data['category'] = subcategory
        return question_data

    except Exception as e:
        logger.error(f"Error generating question: {str(e)}")
        return None

def save_to_database(question_data: Dict) -> bool:
    """Save a question to the SQLite database."""
    try:
        conn = sqlite3.connect('questions.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO questions
            (question, answer, explanation, ai_explanation, reference_json, category)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            question_data['question'],
            question_data['answer'],
            question_data['explanation'],
            question_data['ai_explanation'],
            json.dumps(question_data.get('references', {})),
            question_data['category']
        ))

        conn.commit()
        conn.close()
        return True

    except Exception as e:
        logger.error(f"Error saving to database: {str(e)}")
        return False

if __name__ == "__main__":
    try:
        print("Starting question generation...")
        for category in CATEGORIES:
            print(f"\nGenerating questions for {category}:")
            for subcategory in CATEGORIES[category]:
                print(f"\nProcessing {subcategory}...")
                question_data = generate_question(category, subcategory)
                if question_data:
                    if save_to_database(question_data):
                        print(f"Successfully generated and saved question for {subcategory}")
                    else:
                        print(f"Failed to save question for {subcategory}")
                else:
                    print(f"Failed to generate question for {subcategory}")
    except KeyboardInterrupt:
        print("\nStopping question generation...")
import openai
import json
import sqlite3
import logging
from typing import Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OPENROUTER_API_KEY = "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"

REFERENCE_BOOKS = {
    "Anatomy": [
        "Snell Clinical Anatomy",
        "Gray's Anatomy",
        "Keith Moore's Clinical Anatomy",
        "Barr's Human Nervous System"
    ],
    "Physiology": [
        "Ganong's Review of Medical Physiology",
        "Guyton and Hall Textbook of Medical Physiology",
        "Vander's Human Physiology",
        "Boron Medical Physiology"
    ]
}

def generate_question(category: str, subcategory: str) -> Optional[Dict]:
    if not OPENROUTER_API_KEY:
        logger.error("OpenRouter API key is not set")
        return None

    prompt = f"""Create a detailed true/false medical question about {subcategory} in {category}.
    Include:
    1. A clear question statement
    2. The correct answer (true/false)
    3. A concise explanation
    4. A detailed AI-generated explanation with clinical relevance
    5. Specific page references from: {', '.join(REFERENCE_BOOKS[category])}

    Format as JSON with keys: question, answer, explanation, ai_explanation, references"""

    try:
        client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
            default_headers={
                "HTTP-Referer": "https://replit.com",
                "X-Title": "Medical Question Generator"
            }
        )

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat:67b",
            messages=[{"role": "user", "content": prompt}]
        )

        if not response.choices:
            logger.error("No response received from API")
            return None

        content = response.choices[0].message.content
        question_data = json.loads(content)
        question_data['category'] = subcategory
        return question_data

    except Exception as e:
        logger.error(f"Error generating question: {str(e)}")
        return None

def save_to_database(question_data: Dict) -> bool:
    try:
        conn = sqlite3.connect('questions.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO questions
            (question, answer, explanation, ai_explanation, reference_json, category)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            question_data['question'],
            question_data['answer'],
            question_data['explanation'],
            question_data['ai_explanation'],
            json.dumps(question_data.get('references', {})),
            question_data['category']
        ))

        conn.commit()
        conn.close()
        return True

    except Exception as e:
        logger.error(f"Error saving to database: {str(e)}")
        return False

def get_question_count(category: str) -> int:
    try:
        conn = sqlite3.connect('questions.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM questions WHERE category = ?', (category,))
        count = cursor.fetchone()[0]
        conn.close()
        return count
    except Exception as e:
        logger.error(f"Error getting question count: {str(e)}")
        return 0
