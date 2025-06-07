[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nkhajouei/ai-agent-gui/blob/main/AgenticColab.ipynb)

# Math and Joke AI Agent

This project is a simple AI agent built with Python, LangChain, and Google's Gemini model. The agent can perform basic arithmetic (addition and subtraction) and tell jokes.

## Features

- **Tool Use:** The agent is equipped with tools for adding, subtracting, and telling jokes.
- **Web UI:** The notebook includes code to launch a simple web interface using Gradio to easily interact with the agent.

## How to Run

1.  **Open in Colab:** Click the "Open in Colab" badge at the top of this file.
2.  **Set API Key:** Before running, you must set your Google AI Studio API key. In the Colab notebook, go to the "Secrets" tab (key icon on the left) and add a new secret named `GOOGLE_API_KEY` with your key as the value.
3.  **Run All Cells:** Click `Runtime -> Run all` to install the dependencies and launch the Gradio web interface.
