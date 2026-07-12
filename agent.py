from prompts import (
    EXPLAIN_PROMPT,
    BUG_PROMPT,
    OPTIMIZE_PROMPT,
    COMPLEXITY_PROMPT,
    SECURITY_PROMPT,
    FIX_PROMPT
)

from reviewer import ask_llm


# -----------------------------
# Explain Agent
# -----------------------------
def explain_agent(code):

    prompt = EXPLAIN_PROMPT.format(code=code)

    return ask_llm(prompt)


# -----------------------------
# Bug Detection Agent
# -----------------------------
def bug_agent(code):

    prompt = BUG_PROMPT.format(code=code)

    return ask_llm(prompt)


# -----------------------------
# Optimization Agent
# -----------------------------
def optimization_agent(code):

    prompt = OPTIMIZE_PROMPT.format(code=code)

    return ask_llm(prompt)


# -----------------------------
# Complexity Agent
# -----------------------------
def complexity_agent(code):

    prompt = COMPLEXITY_PROMPT.format(code=code)

    return ask_llm(prompt)


# -----------------------------
# Security Agent
# -----------------------------
def security_agent(code):

    prompt = SECURITY_PROMPT.format(code=code)

    return ask_llm(prompt)


# -----------------------------
# Auto Fix Agent
# -----------------------------
def fix_agent(code):

    prompt = FIX_PROMPT.format(code=code)

    return ask_llm(prompt)


# -----------------------------
# Master Review Agent
# -----------------------------
def review_code(code):

    return {

        "Explanation": explain_agent(code),

        "Bug Detection": bug_agent(code),

        "Optimization": optimization_agent(code),

        "Complexity": complexity_agent(code),

        "Security": security_agent(code)

    }