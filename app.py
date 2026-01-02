from flask import Flask, render_template, request
from gpt4all import GPT4All
import os

app = Flask(__name__)

# Load GPT4All model (first time it may download ~119MB)
MODEL_NAME = "ggml-gpt4all-j-v1.3-groovy"
ai_model = GPT4All(model_name=MODEL_NAME, n_threads=os.cpu_count())

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

Goal: Promote learning, not cheating.
"""

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["question"]

        # Check for homework/quiz/test keywords
        lower_input = user_input.lower()
        if any(keyword in lower_input for keyword in ["homework", "quiz", "test", "assignment"]):
            response_text = (
                "I’m here to help you learn, but I won’t give direct answers to graded work. "
                "Can you try solving it first? I can guide you step-by-step or create practice questions."
            )
        else:
            prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nAI:"
            response_text = ai_model.generate(prompt)

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
