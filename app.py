from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="YOUR_API_KEY")  # Replace with your OpenAI API key

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

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )

        response_text = response.choices[0].message.content

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
