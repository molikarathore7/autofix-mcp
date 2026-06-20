from dotenv import load_dotenv
load_dotenv()

import os
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


# =====================================
# FILE PATHS
# =====================================

LOG_FILE = "app/logs/error.log"
SOURCE_FILE = "app/main.py"

# =====================================
# READ ERROR LOG
# =====================================

try:
    with open(LOG_FILE, "r") as file:
        log_data = file.read()

except Exception as e:
    print("Failed to read error log.")
    print(e)
    exit()

# =====================================
# READ SOURCE CODE
# =====================================

try:
    with open(SOURCE_FILE, "r") as file:
        source_code = file.read()

except Exception as e:
    print("Failed to read source code.")
    print(e)
    exit()

# =====================================
# CHECK LOG CONTENT
# =====================================

if not log_data.strip():
    print("No errors found in error.log")
    exit()

# =====================================
# CREATE PROMPT
# =====================================

prompt = f"""
You are a senior Python software engineer.

Analyze the following application.

ERROR LOG:
{log_data}

SOURCE CODE:
{source_code}

Tasks:

1. Identify the exact bug.
2. Explain why it occurred in short one line.
3. Suggest the fix in short one line.
4. Return the corrected code snippet.

Do not use markdown.
Do not use triple backticks.
Return plain text only.
"""

# =====================================
# SEND TO GEMINI
# =====================================

try:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\n========== GEMINI FIX ==========\n")
    print(response.text)

    # Save Gemini output
    with open("ai/fix_suggestion.txt", "w") as file:
        file.write(response.text)

    print("\nFix suggestion saved to ai/fix_suggestion.txt")

except Exception as e:

    print("\nGemini Error:")
    print(e)