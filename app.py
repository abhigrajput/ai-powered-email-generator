from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DATABASE CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'

db = SQLAlchemy(app)

# EMAIL DATABASE MODEL
class Email(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    prompt = db.Column(db.Text)

    generated_email = db.Column(db.Text)

# CREATE DATABASE
with app.app_context():
    db.create_all()

# NVIDIA NIM API CLIENT
client = OpenAI(

    base_url="https://integrate.api.nvidia.com/v1",

    api_key=""

)

@app.route('/')
def home():

    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_email():

    try:

        data = request.json

        prompt = data.get('prompt')

        email_type = data.get('emailType')

        tone = data.get('tone')

        final_prompt = f"""
Write a professional email in proper email format.

Requirements:
- Include Subject line
- Include Greeting
- Keep email under 150 words
- Use professional language
- Avoid AI sounding language
- End with proper closing

Email Type:
{email_type}

Tone:
{tone}

User Request:
{prompt}
"""

        completion = client.chat.completions.create(

            model="meta/llama-3.3-70b-instruct",

            messages=[
                {
                    "role": "system",
                    "content": "You are a professional AI email assistant."
                },

                {
                    "role": "user",
                    "content": final_prompt
                }
            ],

            temperature=0.7,

            max_tokens=300

        )

        generated_email = completion.choices[0].message.content

        # SAVE EMAIL TO DATABASE
        new_email = Email(

            prompt=prompt,

            generated_email=generated_email

        )

        db.session.add(new_email)

        db.session.commit()

        return jsonify({
            "email": generated_email
        })

    except Exception as e:

        return jsonify({
            "email": str(e)
        })


@app.route('/history')
def history():

    emails = Email.query.all()

    email_list = []

    for email in emails:

        email_list.append({

            "prompt": email.prompt,

            "generated_email": email.generated_email

        })

    return jsonify(email_list)


if __name__ == '__main__':
    app.run(debug=True)