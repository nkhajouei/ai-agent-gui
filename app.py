# app.py
import os
import gradio as gr
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

# This is the crucial line that securely gets your API key 
# from the Hugging Face "Secrets" manager.
API_KEY = os.environ.get("GOOGLE_API_KEY")

def run_agent(user_input):
    """
    Defines and runs the AI agent.
    """
    if not API_KEY:
        return "Error: The GOOGLE_API_KEY secret is not set on the server. The app developer needs to configure this in the Hugging Face Space settings."
    
    # Set the API key for the langchain library to use
    os.environ['GOOGLE_API_KEY'] = API_KEY

    # --- Agent Tool Definitions ---
    @tool
    def add(a: int, b: int) -> int:
        """Adds two numbers."""
        return a + b

    @tool
    def subtract(a: int, b: int) -> int:
        """Subtracts two numbers."""
        return a - b

    @tool
    def tell_a_joke() -> str:
        """Tells a random joke."""
        jokes = ["Why did the scarecrow win an award? Because he was outstanding in his field!"]
        import random
        return random.choice(jokes)

    tools = [add, subtract, tell_a_joke]
    
    # --- Agent Initialization ---
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    prompt = hub.pull("hwchase17/react-json")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
        handle_parsing_errors=True
    )
    
    # --- Agent Invocation ---
    response = agent_executor.invoke({"input": user_input})
    return response['output']

# --- Gradio Interface Definition ---
iface = gr.Interface(
    fn=run_agent,
    inputs=gr.Textbox(lines=2, placeholder="Ask your agent anything..."),
    outputs="text",
    title="Math and Joke AI Agent",
    description="This agent can perform addition and subtraction, or tell you a joke. Built with LangChain and Google's Gemini model."
)

# --- Launch the App ---
iface.launch()
