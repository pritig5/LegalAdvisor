from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Set the Google API key here
GOOGLE_API_KEY = "**"

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('inner-page.html')

# Route to handle the API request
@app.route('/get_info', methods=['POST'])
def get_info():
    try:
        data = request.json
        user_query = data['user_query']

        # Configure and generate text using Google Generative AI
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-pro")
        complete_prompt = """The Indian legal system is vast and complex. It includes the Indian Constitution, various legal acts, judicial precedents, and more. This application can provide summaries of relevant legal information.In the output , provide a structured text and do not make any part of sentence bold. Make sure it is organized in point form and has no * in it."""+ user_query

        response = model.generate_content(complete_prompt)
        answer = response.text

        # Example summarized answer (you may adjust this as needed)
        summarized_answer = f"According to Indian Constitution , {answer}."

        return jsonify({"answer": summarized_answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
