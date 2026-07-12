# ----------------------------
# Explain Code Prompt
# ----------------------------

EXPLAIN_PROMPT = """
You are an expert software engineer.

Explain the following code in simple language.

Include:

1. Purpose
2. Working
3. Important functions
4. Expected output

Code:

{code}
"""

# ----------------------------
# Bug Detection Prompt
# ----------------------------

BUG_PROMPT = """
You are an expert debugging assistant.

Analyze the following code.

Find:

- Syntax errors
- Logical errors
- Runtime issues
- Edge cases

Suggest improvements.

Code:

{code}
"""

# ----------------------------
# Optimization Prompt
# ----------------------------

OPTIMIZE_PROMPT = """
You are an expert software engineer.

Optimize the following code.

Focus on:

- Performance
- Readability
- Best Practices
- Memory Usage

Code:

{code}
"""

# ----------------------------
# Complexity Prompt
# ----------------------------

COMPLEXITY_PROMPT = """
Analyze this code.

Provide:

- Time Complexity
- Space Complexity

Explain why.

Code:

{code}
"""

# ----------------------------
# Security Prompt
# ----------------------------

SECURITY_PROMPT = """
You are a Cyber Security Expert.

Review the code.

Find:

- Vulnerabilities
- SQL Injection
- XSS
- Unsafe Input
- Authentication Issues
- Hardcoded Secrets

Suggest fixes.

Code:

{code}
"""

# ----------------------------
# Auto Fix Prompt
# ----------------------------

FIX_PROMPT = """
You are an expert software engineer.

Fix all syntax errors.

Fix logical errors.

Improve readability.

Return ONLY corrected code.

Do not explain anything.

Code:

{code}
"""