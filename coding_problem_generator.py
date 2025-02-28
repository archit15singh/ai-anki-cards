
import requests
import json
import os
from dotenv import load_dotenv
import openai

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)


def fetch_openai_response(prompt, response_format=None):
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "user", "content": prompt}],
        response_format=response_format,
    )
    return response.choices[0].message.content


def generate():
    with open("problem_statement.txt", "r", encoding="utf-8") as f:
        problem_statement = f.read()
    
    if not problem_statement.strip():
        e = "Error: empty problem statement file"
        print(e)
        return e, e, e

    try:
        rephrase_prompt_template = """
this is a coding problem statement, rephrase and reformat it properly without missing out any information at all.

# coding problem statement
{}
"""
        explanation_prompt_template = """
Explain the solution, thought process, and intuition behind this concept in a way that helps me recognize patterns and deeply understand the underlying principles.
I want to develop strong intuition and problem-solving skills to apply this knowledge across different scenarios.  
However, don't just use words and assume I already understand them—break it down thoroughly.
Explain why this solution even works, the core idea behind it, and how each step connects.
Provide a clear step-by-step breakdown, along with code examples, to illustrate the approach effectively.
Additionally, include strategies on how to recognize similar problems and master this concept over time.

Start with a Brute Force Approach: Develop a simple, correct solution as a baseline, even if it's inefficient.
Identify Inefficiencies: Analyze the solution to find performance bottlenecks.
Incrementally Optimize: Replace inefficient parts with more efficient algorithms or data structures
Explain Each Change: Provide a brief rationale for each optimization, focusing on performance improvements.
Iterate Until Optimal: Continue refining until the solution is as efficient as possible.

# coding problem statement
{}
"""
        tags_prompt_template = """
I will provide a coding problem, and I want you to generate **precise Anki flashcard tags** that act as **memory aids** by emphasizing the problem's fundamental pattern and solving approach.

### **Objective:**
Generate concise, **high-signal** tags that quickly remind me of the problem-solving framework.
The tags should align with **common coding interview problem patterns** and help in **quick recognition & recall.**

### **Tagging Approach:**
1. **Identify the Core Pattern** - What category does this problem fit into? (e.g., Sliding Window, Two Pointers, Backtracking, Graph Traversal)
2. **Key Algorithm/Technique Used** - What is the dominant technique required? (e.g., Recursion, Dynamic Programming, Greedy, Divide and Conquer)
3. **Optimization & Variants** - Does this problem involve a common optimization or variation? (e.g., Memoization, Bitmasking, Prefix Sum, Kadane’s Algorithm)
4. **Problem Type** - What kind of problem is this structurally? (e.g., Subsets, Intervals, Palindromes, Graph Paths)
5. **Complexity Insight** *(optional if significant)* - Are there important complexity considerations? (e.g., O(n log n) for sorting-based approaches)
6. easy, medium, hard or others

### **Output Format:**
Provide a JSON object with the most relevant tags, following a **minimalist but effective** format.
The tags should always use pythonic format, for example, two_pointers

# **Example Output JSON:**
{{
    "tags": []
}}

# **Coding Problem:**
{}
"""

        rephrase_prompt = rephrase_prompt_template.format(problem_statement)
        explanation_prompt = explanation_prompt_template.format(problem_statement)
        tags_prompt = tags_prompt_template.format(problem_statement)

        print("\n========== Generating Rephrased Question ==========")
        rephrased_response = fetch_openai_response(rephrase_prompt)
        print("\n[Rephrased-Question]\n")
        print(rephrased_response)
        print("\n============================================================")

        print("\n========== Generating Problem-Solving Explanation ==========")
        explanation_response = fetch_openai_response(explanation_prompt)
        print("\n[Problem-Solving Explanation]\n")
        print(explanation_response)
        print("\n============================================================")

        print("\n========== Generating Anki Flashcard Tags ==========")
        tags_response = fetch_openai_response(
            tags_prompt, response_format={"type": "json_object"}
        )
        tags_response = json.loads(tags_response)["tags"]
        print("\n[Anki Flashcard Tags]\n")
        print(tags_response)
        print("\n=====================================================")
        return rephrased_response, explanation_response, tags_response
    except Exception as e:
        print(f"\n[Error] Failed to process request: {e}")
        return str(e), str(e), str(e)


def create_flashcard(deck_name, front, back, tags, api_url="http://localhost:8765"):
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": "KaTeX and Markdown Basic",
                "fields": {
                    "Front": front,
                    "Back": back,
                },
                "tags": tags,
                "options": {"allowDuplicate": False},
            }
        },
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        result = response.json()

        if result.get("error") is None:
            print(f"Card added successfully: {result}")
        else:
            print(f"Error: {result['error']}")
    except requests.RequestException as e:
        print(f"Failed to connect to Anki: {e}")


if __name__ == "__main__":
    deck_name = "coding problems"
    rephrased_question, explanation, tags = generate()
    create_flashcard(deck_name, front=rephrased_question, back=explanation, tags=tags)
