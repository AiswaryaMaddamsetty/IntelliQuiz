import google.generativeai as genai
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_quiz_questions(pdf_text, selected_difficulty):
    try:
        prompt = f"""
        You are an intelligent quiz generator.
        Based on the following study material, create 5 {selected_difficulty} multiple-choice questions.
        Each question must have 4 options and clearly specify the correct answer.
        
        Return the output strictly in JSON format like this:
        [
            {{
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Rome"],
                "answer": "Paris"
            }}
        ]

        Study material:
        {pdf_text[:4000]}
        """

        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

        # Extract text safely
        text_output = ""
        if hasattr(response, "text"):
            text_output = response.text
        elif hasattr(response, "candidates"):
            text_output = response.candidates[0].content.parts[0].text
        else:
            print("[WARN] Empty Gemini response.")
            return []

        # --- 🧹 Clean the output ---
        # Remove markdown-style code fences like ```json ... ```
        cleaned_text = re.sub(r"```(?:json)?", "", text_output, flags=re.IGNORECASE).strip()

        # --- 🧠 Try parsing JSON ---
        try:
            questions = json.loads(cleaned_text)
            return questions
        except json.JSONDecodeError:
            print("[WARN] Could not parse Gemini response as JSON.")
            print("Raw output:\n", cleaned_text)
            return []

    except Exception as e:
        print(f"[ERROR] Failed to generate quiz questions: {e}")
        return []
