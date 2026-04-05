Reasoning Agent - Advanced Logic & Reasoning App
An interactive AI-powered reasoning system that explains how answers are derived, not just what the answer is. Built using Google Gemini Pro, this agent performs structured, step-by-step logical analysis before delivering conclusions.
________________________________________
Features

•	Step-by-step reasoning for every query 

•	Logical analysis and problem breakdown 

•	Fallacy and misconception detection 

•	Interactive CLI chat interface 

•	Lightweight and easy to run (Colab or local) 

•	Preloaded example puzzles for quick testing 
________________________________________
How It Works

The agent enforces a strict reasoning structure:

1. Thought Process

•	Breaks down the problem 

•	Identifies variables and constraints 

•	Checks assumptions and logical traps 

•	Verifies consistency 

2. Final Answer

•	Provides a concise, accurate conclusion 

•	Highlights key results clearly 

________________________________________
Installation

Option 1: Run in Google Colab

•	Open the script in Colab 

•	Add your API key in Colab Secrets (GOOGLE_API_KEY) 

•	Run all cells 

Option 2: Run Locally

pip install google-generativeai

python app.py
________________________________________

API Key Setup

You need a Google AI API key:

https://makersuite.google.com/app/apikey

Important: Never share your API key publicly.

________________________________________
Usage

Run the application:

python app.py

Then interact:

You: A bat and a ball cost $1.10...

Agent: [Step-by-step reasoning + answer]

To exit:

exit / quit / bye

________________________________________

Example Problems

•	Bat and ball pricing puzzle 

•	Machine production logic 

•	Survival/counting riddles 

________________________________________

Project Structure

├── app.py              # Main application

├── README.md           # Project documentation

________________________________________

Use Cases

•	Students learning problem-solving 

•	Educators demonstrating reasoning 

•	Developers exploring explainable AI 

•	Puzzle and logic enthusiasts 

________________________________________

Notes

•	Requires internet connection 

•	Gemini Pro access must be enabled 

•	Performance depends on API response 

________________________________________

Contributing

Contributions are welcome.
Feel free to fork, improve and submit a pull request.

