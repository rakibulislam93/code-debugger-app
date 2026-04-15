from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def code_debugger(images, options):
    if options == "Hints":
        prompt = """
You are an expert code debugger. Your task is to analyze the provided code image and identify any bugs or issues.

INSTRUCTIONS:
- Carefully examine the code for logical errors, syntax issues, or bad practices
- Provide concise, actionable hints that guide the user toward the fix WITHOUT giving away the solution
- Each hint should address a specific issue
- Do NOT show corrected code

Respond strictly in this format:

HINTS:
- [Hint 1: Brief, targeted clue pointing to the issue]
- [Hint 2: Another clue if multiple issues exist]
- [Add more hints as needed]
"""
    else:
        prompt = """
You are an expert code debugger. Your task is to analyze the provided code image, identify all bugs, and provide a complete fix.

INSTRUCTIONS:
- Carefully examine the code for logical errors, syntax issues, runtime errors, or bad practices
- Be thorough — identify ALL issues, not just the most obvious one
- Explain bugs clearly so the user understands WHY it was wrong
- Provide fully corrected, clean code

Respond strictly in this format:

HINTS:
- [Hint 1: Brief clue about the first issue]
- [Hint 2: Brief clue about the second issue, if any]

EXPLANATION:
[Clear explanation of what the bug(s) are, why they occur, and what impact they have on the program]

SOLVED_CODE:
[The complete corrected code with the fix(es) applied — no partial snippets]
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text



# parse response and display results tab-wise in the Streamlit app
def parse_debugger_response(response_text):
    """Parse the response into separate sections."""
    hints = ""
    explanation = ""
    solved_code = ""
    
    # Extract HINTS section
    if "HINTS:" in response_text:
        start = response_text.find("HINTS:") + len("HINTS:")
        end = response_text.find("EXPLANATION:") if "EXPLANATION:" in response_text else len(response_text)
        hints = response_text[start:end].strip()
    
    # Extract EXPLANATION section
    if "EXPLANATION:" in response_text:
        start = response_text.find("EXPLANATION:") + len("EXPLANATION:")
        end = response_text.find("SOLVED_CODE:") if "SOLVED_CODE:" in response_text else len(response_text)
        explanation = response_text[start:end].strip()
    
    # Extract SOLVED_CODE section
    if "SOLVED_CODE:" in response_text:
        start = response_text.find("SOLVED_CODE:") + len("SOLVED_CODE:")
        solved_code = response_text[start:].strip()
    
    return hints, explanation, solved_code