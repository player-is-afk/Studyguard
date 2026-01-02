from flask import Flask, render_template, request
from gpt4all import GPT4All
import os

app = Flask(__name__)

# Use the local model
MODEL_PATH = os.path.join("models", "gpt4all-lora-quantized.bin")
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

        response = ai_model.chat_completion(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )

        response_text = response['message'] if 'message' in response else str(response)

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
