# Prompt Versions

## v1 – Initial Version

```
You are a customer support agent.
Reply to the customer message below.
```

**What changed:** Baseline. Minimal instruction, no constraints.

**What we observed:**
- Case 1–4: Outputs were reasonable — polite, empathetic, asked for needed info.
- Case 5 (failure): The model said "I'll ensure the discount is applied promptly" — it accepted an unverified claim at face value and implicitly promised to honor it. This is a real business risk (false commitments, legal liability).
- Tone was generally good but responses were long and sometimes included placeholder text like `[Your Name]`.

---

## v2 – Revision 1: Add Role + Constraints

```
You are a professional customer support agent for a SaaS company.
Write a concise, empathetic reply to the customer message below.
Acknowledge their concern, apologize if appropriate, and state clear next steps.
Do not make promises you cannot keep. Keep the tone warm and professional.
```

**What changed:** Added company context, conciseness instruction, and "do not make promises you cannot keep."

**What improved:**
- Responses became shorter and more focused.
- Placeholder text (`[Your Name]`) was mostly eliminated.
- Case 5 improved slightly: the model asked for verification info before committing. But it still leaned toward confirming the discount was "likely" valid.

**What stayed the same / got worse:**
- Case 5 still did not explicitly say the claim could not be verified — it implied it would be honored after checking.
- Case 3 (angry customer) remained well-handled.

---

## v3 – Revision 2: Add Explicit Verification Rule + Length Cap

```
You are a senior customer support agent for a SaaS company.
Reply to the customer message below following these rules:
1. Open with empathy and acknowledge the specific issue.
2. Apologize briefly if the company is at fault.
3. State exactly what will happen next (or ask for missing details).
4. If you cannot verify a claim (e.g. a promised discount), say you will look into it — never confirm unverified claims.
5. Close with an offer to help further.
6. Keep the reply under 120 words. Use a professional but human tone.
```

**What changed:** Added explicit rule 4 about unverified claims, added 120-word limit.

**What improved:**
- Case 5: The model now explicitly said it could not confirm the discount without checking records — no implicit promise. This is the correct behavior for a support agent.
- All responses became tighter and more action-oriented.
- Length was more consistent and appropriate for email replies.

**What stayed the same / still requires human review:**
- Case 5 still requires a human to actually look up whether Sarah made that promise — the model correctly flags it but cannot resolve it.
- Case 3 (legal threat) should always be escalated to a manager; the model handles tone well but a human must own the outcome.
