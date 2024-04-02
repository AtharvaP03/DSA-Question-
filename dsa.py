from flask import Flask, render_template
import random
import openai

app = Flask(__name__)

openai.api_key = "-----------"  # Replace with your OpenAI API Key

dsa_topics = {
    "Arrays": [
        "Dynamic Programming (DP) problems related to arrays.",
        "Sorting algorithms for arrays.",
        "Search algorithms for arrays."
    ],
    "Linked Lists": [
        "Dynamic Programming (DP) problems related to linked lists.",
        "Insertion and deletion operations in linked lists.",
        "Cyclic detection and removal in linked lists."
    ],
    "Stacks and Queues": [
        "Implementing stacks and queues using arrays or linked lists.",
        "Applications of stacks and queues in algorithm design.",
        "Optimizing stack and queue operations for efficiency."
    ],
    "Trees": [
        "Dynamic Programming (DP) problems related to trees.",
        "Traversal algorithms for trees (e.g., inorder, preorder, postorder).",
        "Balancing techniques for binary search trees."
    ]
}

def generate_dsa_question(topic):
    prompt = f"""
Generate a question related to the following topic:

**Topic:** {topic}

**Instructions:**
- This question is commonly encountered in programming competitions and assessments.
- The problem statement should revolve around a concept or problem related to {topic}.
- Provide a concise description of the problem or concept, ensuring clarity and accuracy.
- Include examples or test cases to illustrate the problem statement effectively.
- Ensure proper formatting and punctuation for clear presentation.

Write a question that adheres to the provided instructions.
"""
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=120,
        temperature=0.5,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

def generate_test_cases(question, num_test_cases=5):
    prompt = f"""
Generate numerical test cases for the following question:

**Question:** {question}

Instructions:
- Generate {num_test_cases} test cases where input and/or output are numerical values.
- Each test case should include numerical input values and the expected numerical output.
- Ensure that the test cases cover various scenarios related to the given question.
- Use proper formatting and punctuation for readability.

Example Test Cases:
Input: [Specify numerical input values here]
Output: [Specify expected numerical output here]

Write {num_test_cases} test cases that thoroughly test the problem related to the given question.
"""
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=200,
        temperature=0.5,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

def generate_random_dsa_question():
    topic = random.choice(list(dsa_topics.keys()))
    question = generate_dsa_question(topic)
    test_cases = generate_test_cases(question)
    return f"DSA Question: {question}\n(Topic: {topic})\n\nTest Cases:\n{test_cases}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_question')
def generate_question():
    return generate_random_dsa_question()

if __name__ == '__main__':
    app.run(debug=True)
