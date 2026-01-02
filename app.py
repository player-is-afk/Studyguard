from flask import Flask, render_template, request
from gpt4all import GPT4All

app = Flask(__name__)

# Load local AI model (downloads automatically the first time)
model = GPT4All("gpt4all-falcon-q4_0.gguf")

SYSTEM_RULES = """
You are StudyGuard AI, an ethical AI study assistant.

Rules:
- Do NOT give direct answers to homework, tests, or quizzes
- Teach concepts step by step
- Ask the student to attempt the problem before continuing
- Generate practice questions
- Explain common mistakes
- Be supportive and encouraging
"""

def studyguard_ai(user_input):
    prompt = f"{SYSTEM_RULES}\n\nStudent question:\n{user_input}\n\nStudyGuard AI response:"
    with model.chat_session():
        return model.generate(prompt, max_tokens=300)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["question"]
        response_text = studyguard_ai(user_input)

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
