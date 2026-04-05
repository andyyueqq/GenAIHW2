"""
HW2 – Customer Support Response Drafting
Uses Google Gemini API to generate first-pass support email replies.

Usage:
  python3 app.py                          # run all eval cases
  python3 app.py --input "My order..."    # run a single custom input
  python3 app.py --prompt-version v2      # use a specific prompt version
"""

import os
import json
import argparse

from google import genai

# ── Prompt versions ────────────────────────────────────────────────────────────

PROMPTS = {
    "v1": (
        "You are a customer support agent. "
        "Reply to the customer message below."
    ),
    "v2": (
        "You are a professional customer support agent for a SaaS company. "
        "Write a concise, empathetic reply to the customer message below. "
        "Acknowledge their concern, apologize if appropriate, and state clear next steps. "
        "Do not make promises you cannot keep. Keep the tone warm and professional."
    ),
    "v3": (
        "You are a senior customer support agent for a SaaS company. "
        "Reply to the customer message below following these rules:\n"
        "1. Open with empathy and acknowledge the specific issue.\n"
        "2. Apologize briefly if the company is at fault.\n"
        "3. State exactly what will happen next (or ask for missing details).\n"
        "4. If you cannot verify a claim (e.g. a promised discount), say you will look into it — never confirm unverified claims.\n"
        "5. Close with an offer to help further.\n"
        "6. Keep the reply under 120 words. Use a professional but human tone."
    ),
}

# ── Core function ──────────────────────────────────────────────────────────────

def generate_reply(customer_message: str, prompt_version: str = "v3") -> str:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")

    client = genai.Client(api_key=api_key)

    system_instruction = PROMPTS[prompt_version]
    full_prompt = f"{system_instruction}\n\nCustomer message:\n{customer_message}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt,
    )
    return response.text.strip()

# ── Run eval set ───────────────────────────────────────────────────────────────

def run_eval(prompt_version: str = "v3"):
    with open("eval_set.json") as f:
        cases = json.load(f)

    os.makedirs("outputs", exist_ok=True)
    output_file = f"outputs/eval_results_{prompt_version}.txt"

    with open(output_file, "w") as out:
        for case in cases:
            header = f"=== Case {case['id']} [{case['type']}] ==="
            print(header)
            out.write(header + "\n")

            print(f"INPUT:  {case['input']}")
            out.write(f"INPUT:  {case['input']}\n")

            reply = generate_reply(case["input"], prompt_version)

            print(f"OUTPUT:\n{reply}")
            out.write(f"OUTPUT:\n{reply}\n")

            note = f"EXPECTED: {case['expected_behavior']}"
            print(note)
            out.write(note + "\n")
            print()
            out.write("\n")

    print(f"Results saved to {output_file}")

# ── CLI ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="Single customer message to reply to")
    parser.add_argument("--prompt-version", type=str, default="v3",
                        choices=["v1", "v2", "v3"], help="Prompt version to use")
    args = parser.parse_args()

    if args.input:
        reply = generate_reply(args.input, args.prompt_version)
        print("\n--- Generated Reply ---")
        print(reply)
    else:
        run_eval(args.prompt_version)
# minor formatting update
