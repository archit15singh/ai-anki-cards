
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

    try:
        rephrase_prompt_template = """
this is a coding problem statement, rephrase and reformat it properly without missing out any information at all.

# coding problem statement
{}
"""
        explanation_prompt_template = """
I will provide a coding problem, and I want you to guide me through the most effective thought process for solving it.
Focus on building deep problem-solving intuition, ensuring that I understand why each step is taken, not just how to implement it.

Approach:
1. Decompose the problem conceptually - Identify its type, underlying patterns, and constraints before jumping into a solution.
2. Develop a structured approach - Walk me through a logical step-by-step breakdown, ensuring clarity at each stage.
3. Progressively refine solutions:
    - Naive approach - The simplest, most intuitive solution (even if inefficient).
    - Intermediate optimization - Identifying inefficiencies and improving step by step.
    - Optimal approach - Arriving at the most efficient solution while maintaining clarity and simplicity.
4. Emphasize thought frameworks - Guide me using:
    - Pattern recognition - Relating this problem to broader classes of problems.
    - Meta-thinking - Teaching how to break down, analyze, and reason about problems in general.
    - Chain-of-thought reasoning - Explaining the rationale behind each step, avoiding leaps in logic.
5. Provide heuristics & generalizable insights - Help me internalize problem-solving strategies that can be applied to other problems, not just this one.

Goal: I don't just want to solve the problem—I want to develop a mindset that allows me to recognize similar problems, intuitively recall the right approaches, and refine solutions with confidence.

**answer concisely, reduce redundancy**

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
