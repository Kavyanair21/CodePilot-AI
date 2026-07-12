import streamlit as st
from dotenv import load_dotenv

from agent import (
    explain_agent,
    bug_agent,
    optimization_agent,
    complexity_agent,
    security_agent,
    fix_agent,
    review_code
)

from quality import calculate_score
from orchestrator import orchestrate

# -------------------------
# Load Environment
# -------------------------
load_dotenv()
# Load Custom CSS
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="CodePilot AI",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:

    st.title("🤖 CodePilot AI")

    st.markdown("""
### 🚀 Multi-Agent Intelligent Code Review Platform

Analyze, Review, Optimize and Secure your source code using specialized AI Agents.
""")

    st.divider()
    # ==========================================
# Dashboard Cards
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    quality_display = "--"
with col1:
    st.metric(
        "⭐ Quality",
        "--"
    )

with col2:
    st.metric(
        "🤖 Agents",
        "6"
    )

with col3:
    st.metric(
        "📂 Files",
        "1"
    )

with col4:
    st.metric(
        "💻 Language",
        "--"
    )

    st.divider()

    

    st.markdown("### 🚀 Features")

    st.write("📖 Explain Code")
    st.write("🐞 Detect Bugs")
    st.write("⚡ Optimize Code")
    st.write("📈 Complexity Analysis")
    st.write("🔒 Security Review")
    st.write("🛠 Auto Fix")
    st.write("🚀 Overall Review")

    st.markdown("---")

    st.info("""
Built Using

• Streamlit

• Groq Llama 3.3

• Agentic AI

• Python
""")

    st.markdown("---")

    st.caption("Version 1.0")

# -------------------------
# Header
# -------------------------
st.title("🤖 CodePilot AI")

st.markdown("""
### Multi-Agent AI Code Review Assistant

Analyze, review and improve your source code using specialized AI agents.

Supported Languages:

- Python
- Java
- C
- C++
- JavaScript
""")

# -------------------------
# Language
# -------------------------
language = st.selectbox(
    "Programming Language",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript"
    ]
)

# -------------------------
# Upload File
# -------------------------
uploaded_file = st.file_uploader(
    "📂 Upload Source Code",
    type=[
        "py",
        "java",
        "c",
        "cpp",
        "js",
        "html",
        "css"
    ]
)

if uploaded_file:

    code = uploaded_file.read().decode("utf-8")

    st.success(f"Uploaded : {uploaded_file.name}")

    st.text_area(
        "Code Preview",
        value=code,
        height=350
    )

else:

    code = st.text_area(
        "Paste your code here",
        height=350,
        placeholder="Paste Python, Java, C, C++, JavaScript..."
    )

# -------------------------
# Code Quality
# -------------------------
if code.strip():

    score = calculate_score(code)

    st.markdown("## 📊 Code Quality")

    st.metric(
        "Overall Score",
        f"{score}/100"
    )

    st.progress(score / 100)

st.divider()

# -------------------------
# Buttons
# -------------------------
col1, col2 = st.columns(2)

with col1:
    explain = st.button(
        "📖 Explain Code",
        use_container_width=True
    )

with col2:
    bugs = st.button(
        "🐞 Detect Bugs",
        use_container_width=True
    )

col3, col4 = st.columns(2)

with col3:
    optimize = st.button(
        "⚡ Optimize Code",
        use_container_width=True
    )

with col4:
    complexity = st.button(
        "📈 Complexity",
        use_container_width=True
    )

col5, col6 = st.columns(2)

with col5:
    security = st.button(
        "🔒 Security Review",
        use_container_width=True
    )

with col6:
    auto_fix = st.button(
        "🛠 Auto Fix",
        use_container_width=True
    )

st.divider()

review = st.button(
    "🚀 Review My Code",
    type="primary",
    use_container_width=True
)
# =====================================================
# Explain Code
# =====================================================

if explain:

    if not code.strip():
        st.warning("Please paste or upload some code.")
    else:

        with st.spinner("Explaining your code..."):

            result = explain_agent(code)

        st.success("Explanation Complete!")

        st.markdown(result)

# =====================================================
# Bug Detection
# =====================================================

if bugs:

    if not code.strip():
        st.warning("Please paste or upload some code.")
    else:

        with st.spinner("Detecting bugs..."):

            result = bug_agent(code)

        st.success("Bug Detection Complete!")

        st.markdown(result)

# =====================================================
# Optimization
# =====================================================

if optimize:

    if not code.strip():
        st.warning("Please paste or upload some code.")
    else:

        with st.spinner("Optimizing code..."):

            result = optimization_agent(code)

        st.success("Optimization Complete!")

        st.markdown(result)

# =====================================================
# Complexity
# =====================================================

if complexity:

    if not code.strip():
        st.warning("Please paste or upload some code.")
    else:

        with st.spinner("Analyzing complexity..."):

            result = complexity_agent(code)

        st.success("Complexity Analysis Complete!")

        st.markdown(result)

# =====================================================
# Security
# =====================================================

if security:

    if not code.strip():
        st.warning("Please paste or upload some code.")
    else:

        with st.spinner("Performing security review..."):

            result = security_agent(code)

        st.success("Security Review Complete!")

        st.markdown(result)

# =====================================================
# Auto Fix
# =====================================================

if auto_fix:

    if not code.strip():
        st.warning("Please paste or upload some code.")
    else:

        with st.spinner("Fixing code using AI..."):

            fixed_code = fix_agent(code)

        st.success("Code Fixed Successfully!")

        st.code(
            fixed_code,
            language=language.lower()
        )

        extension = {
            "Python": "py",
            "Java": "java",
            "C": "c",
            "C++": "cpp",
            "JavaScript": "js"
        }.get(language, "txt")

        st.download_button(
            label="📥 Download Fixed Code",
            data=fixed_code,
            file_name=f"fixed_code.{extension}",
            mime="text/plain"
        )

# =====================================================
# Master Review
# =====================================================

if review:

    if not code.strip():
        st.warning("Please paste or upload some code.")
    else:

        with st.spinner("🧠 Planner Agent is deciding which AI agents to execute..."):

            report = orchestrate(
    "review",
    code
)

        st.success("Review Completed Successfully!")

        with st.expander("📖 Code Explanation", expanded=True):
         if "Explanation" in report:
                   st.markdown(report["Explanation"])
        with st.expander("🐞 Bug Detection"):
            if "Bug Detection" in report:
                st.markdown(report["Bug Detection"])

        with st.expander("⚡ Optimization"):
           if "Optimization" in report:
               st.markdown(report["Optimization"])
        with st.expander("📈 Complexity"):
            if "Complexity" in report:
                st.markdown(report["Complexity"])
        with st.expander("🔒 Security Review"):
            if "Security" in report:
               st.markdown(report["Security"])

# =====================================================
# Footer
# =====================================================

st.divider()

st.caption(
    "🚀 CodePilot AI | Multi-Agent AI Code Review Assistant | Built with Streamlit + Groq"
)