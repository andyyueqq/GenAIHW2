# HW2 – Build and Evaluate a Simple GenAI Workflow

**Course:** BU.330.760 · Spring 2026
**Author:** Xiangyu Yue

## Video Walkthrough

> [https://youtu.be/ZfxgjgKQ3GQ](https://youtu.be/ZfxgjgKQ3GQ)

---

## Workflow: Customer Support Response Drafting

| Field | Description |
|---|---|
| **Workflow** | Drafting first-pass customer support email responses |
| **User** | Customer support agent at a SaaS company |
| **Input** | Raw customer complaint or inquiry (plain text) |
| **Output** | A professional, empathetic, and actionable reply email |
| **Why automate** | Support teams handle hundreds of similar tickets daily; LLM-generated drafts cut response time and reduce agent cognitive load while keeping a human in the loop for final review |

---

## Repository Structure

```
hw2-genai-workflow/
├─ README.md        ← this file
├─ app.py           ← Python prototype (Gemini API)
├─ prompts.md       ← prompt versions v1 / v2 / v3 with analysis
├─ eval_set.json    ← 5 test cases with expected behavior notes
└─ report.md        ← written report
```

## Setup

```bash
pip3 install google-genai
export GEMINI_API_KEY="your_key_here"
```

Get a free API key at https://aistudio.google.com/app/apikey

## Running

```bash
# Run all 5 eval cases and save results
python3 app.py

# Run a single custom input
python3 app.py --input "My order hasn't arrived after 3 weeks."

# Use a specific prompt version (v1, v2, v3)
python3 app.py --prompt-version v2
```

Results are printed to the terminal and saved to `outputs/`.
