from flask import Flask, render_template, request
from gpt4all import GPT4All
import os

app = Flask(__name__)

# Path to your local Phi-3 Mini model
MODEL_PATH = os.path.join("models", "phi-3-mini.bin")

# Initialize GPT4All with local model
ai_model = GPT4All(model_name=MODEL_PATH, n_threads=os.cpu_count())

SYSTEM_PROMPT = """
You are StudyGuard AI, an ethical AI study assistant.

Rules:
- Do NOT provide direct answers to homework, tests, quizzes, or graded assignments.
- If a user asks for answers, politely refuse and explain why.
- Focus on teaching concepts step-by-step.
- Ask the student to attempt the problem before continuing.
- Generate practice questions instead of solutions.
- Explain common mistakes.
- Be supportive and clear.
- State uncertainty when relevant.

Goal:
Promote learning, not cheating.
"""

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["question"]
        
        # Combine system prompt + user input for local model
        prompt = SYSTEM_PROMPT + "\n\nStudent: " + user_input + "\nStudyGuard AI:"
        
        # Generate response from Phi-3 Mini
        response_text = ai_model.generate(prompt)
        
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
