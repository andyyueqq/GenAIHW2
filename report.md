# Report – Customer Support Response Drafting

**Author:** Xiangyu Yue
**Course:** BU.330.760 · Spring 2026

---

## Business Use Case

Customer support teams at SaaS companies routinely handle hundreds of email tickets per day. Many of these messages follow predictable patterns: shipping delays, billing errors, angry complaints, or unverifiable claims. Drafting a professional, empathetic first response is time-consuming but does not always require human creativity. This prototype uses an LLM to generate a draft reply that a human agent can review, edit, and send — reducing response time while keeping a human in the loop.

## Model Choice

I used **Gemini 2.5 Flash** via the Google AI Studio API (free tier). I chose it because it is free, fast, and the newest available model on my account. I did not compare other models in this prototype, but based on the outputs, Gemini 2.5 Flash produced fluent, well-structured email responses with minimal hallucination in most cases.

## Baseline vs. Final Design

| Dimension | v1 (Baseline) | v3 (Final) |
|---|---|---|
| Role definition | Generic "customer support agent" | Senior agent for a SaaS company |
| Tone guidance | None | Warm, professional, human |
| Length | Uncontrolled (often too long) | Capped at 120 words |
| Unverified claims | Model accepted and implicitly confirmed claims | Explicit rule: flag and do not confirm |
| Placeholder text | Sometimes included `[Your Name]` | Eliminated |

The most important improvement was in **Case 5** (unverified discount claim). The v1 prompt produced a response that implied the discount would be honored after a quick check — a real business risk. The v3 prompt produced a response that acknowledged the claim but explicitly stated it needed to be verified before any commitment could be made.

## Where the Prototype Still Fails

- **Case 5** can never be fully resolved by the LLM. It correctly flags the claim but a human must actually look up the conversation history with Sarah.
- **Case 3** (legal threat) is handled with appropriate tone, but any message involving legal threats should be escalated to a manager — the model cannot make that judgment reliably.
- **Case 4** (empty input) is handled gracefully, but a production system would benefit from input validation before calling the API.

## Deployment Recommendation

I would recommend deploying this as a **draft-assist tool only** — the LLM generates a first-pass reply that a human agent reviews before sending. I would not recommend fully automated replies without human review, for two reasons:

1. The model occasionally makes subtle errors (implicit commitments, missed context).
2. Edge cases involving legal threats, fraud, or high-value accounts require human judgment that no prompt revision can fully address.

With a human-in-the-loop workflow, this prototype could meaningfully reduce agent response time and cognitive load.
