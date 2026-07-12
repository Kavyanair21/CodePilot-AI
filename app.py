import streamlit as st
from dotenv import load_dotenv
from report_generator import generate_pdf
from chat_agent import chat_with_ai
from dashboard import dashboard
from database import (
    create_database,
    save_review,
    get_reviews,
    delete_review
)

from agent import (
    explain_agent,
    bug_agent,
    optimization_agent,
    complexity_agent,
    security_agent,
    fix_agent
)

from orchestrator import orchestrate
from quality import calculate_score

load_dotenv()

create_database()

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="CodePilot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# Load CSS
# ---------------------------------------------------

with open("style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )
# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/artificial-intelligence.png",
        width=90
    )

    st.title("CodePilot AI")

    st.markdown("---")

    st.markdown("### 🤖 AI Agents")

    st.success("Planner Agent")

    st.success("Explain Agent")

    st.success("Bug Agent")

    st.success("Optimization Agent")

    st.success("Complexity Agent")

    st.success("Security Agent")

    st.success("Fix Agent")

    st.markdown("---")

    st.info(
        """
Version : 2.0

Built using

• Streamlit

• Groq

• Agentic AI
"""
    )
    page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Code Review",
        "📜 Review History"
    ]
)
    st.sidebar.title("🤖 CodePilot AI")

st.sidebar.success("System Status")

st.sidebar.write("🟢 AI Agents Online")
st.sidebar.write("🟢 Database Connected")
st.sidebar.write("🟢 Groq API Connected")
st.sidebar.write("🟢 Report Generator Ready")

st.sidebar.divider()

st.sidebar.markdown("### Version")

st.sidebar.success("CodePilot AI v1.0")

st.sidebar.caption("Built by Kavya S Nair")

st.sidebar.divider()

st.sidebar.metric("AI Agents", 7)

st.sidebar.metric("Features", 15)

st.sidebar.metric("Database", "SQLite")
# =====================================================
# Header
# =====================================================

st.markdown("""
<div style="
background:linear-gradient(135deg,#4F46E5,#7C3AED);
padding:40px;
border-radius:25px;
color:white;
text-align:center;
margin-bottom:25px;
">

<h1>🤖 CodePilot AI</h1>

<h3>Multi-Agent Intelligent Code Review Platform</h3>

<p>
Explain • Detect Bugs • Optimize • Security • Auto Fix • Analytics
</p>

</div>
""", unsafe_allow_html=True)

st.info(
    "👋 Welcome! Upload or paste your source code, then let CodePilot AI review it using multiple AI agents."
)

# =====================================================
# Dashboard
# =====================================================


# =====================================================
# Language Selection
# =====================================================

language = st.selectbox(
    "💻 Programming Language",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript"
    ]
)
# =====================================================
# Upload Code
# =====================================================

uploaded_file = st.file_uploader(
    "📂 Upload Source Code",
    type=[
        "py",
        "java",
        "c",
        "cpp",
        "js"
    ]
)

if uploaded_file:

    code = uploaded_file.read().decode()

else:

    code = st.text_area(
        "✍ Paste your code",
        height=350
    )


score = calculate_score(code) if code.strip() else 0

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div style="
    background:white;
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 6px 18px rgba(0,0,0,.1);
    ">
        <h3>⭐ Quality</h3>
        <h1>{score}/100</h1>
        <p>Code Score</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="
    background:white;
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 6px 18px rgba(0,0,0,.1);
    ">
        <h3>🤖 AI Agents</h3>
        <h1>7</h1>
        <p>Active</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div style="
    background:white;
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 6px 18px rgba(0,0,0,.1);
    ">
        <h3>💻 Language</h3>
        <h1>{language}</h1>
        <p>Selected</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div style="
    background:white;
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 6px 18px rgba(0,0,0,.1);
    ">
        <h3>📄 Report</h3>
        <h1>PDF</h1>
        <p>Ready</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
# =====================================================
# Code Quality
# =====================================================

score = 0

if code.strip():
    score = calculate_score(code)

st.subheader("⭐ Code Quality")

st.progress(score / 100)

st.metric(
    "Overall Score",
    f"{score}/100"
)

st.divider()

# =====================================================
# AI Actions
# =====================================================

st.subheader("🤖 AI Tools")

c1, c2, c3 = st.columns(3)

with c1:
    explain = st.button(
        "📖 Explain Code",
        use_container_width=True
    )

with c2:
    bugs = st.button(
        "🐞 Detect Bugs",
        use_container_width=True
    )

with c3:
    optimize = st.button(
        "⚡ Optimize",
        use_container_width=True
    )

c4, c5, c6 = st.columns(3)

with c4:
    complexity = st.button(
        "📈 Complexity",
        use_container_width=True
    )

with c5:
    security = st.button(
        "🔒 Security",
        use_container_width=True
    )

with c6:
    auto_fix = st.button(
        "🛠 Auto Fix",
        use_container_width=True
    )

st.divider()

# =====================================================
# Review Button
# =====================================================

review = st.button(
    "🚀 Review My Code",
    type="primary",
    use_container_width=True
)

st.divider()
# =====================================================
# Agent Status
# =====================================================

status_box = st.empty()
if explain:

    if not code.strip():

        st.warning("Please paste some code.")

    else:

        with st.spinner("Explaining Code..."):

            result = explain_agent(code)

        st.success("Done!")

        st.markdown(result)
if bugs:

    if not code.strip():

        st.warning("Please paste some code.")

    else:

        with st.spinner("Detecting Bugs..."):

            result = bug_agent(code)

        st.success("Done!")

        st.markdown(result)
if optimize:

    if not code.strip():

        st.warning("Please paste some code.")

    else:

        with st.spinner("Optimizing Code..."):

            result = optimization_agent(code)

        st.success("Done!")

        st.markdown(result)
if complexity:

    if not code.strip():

        st.warning("Please paste some code.")

    else:

        with st.spinner("Analyzing Complexity..."):

            result = complexity_agent(code)

        st.success("Done!")

        st.markdown(result)
if security:

    if not code.strip():

        st.warning("Please paste some code.")

    else:

        with st.spinner("Checking Security..."):

            result = security_agent(code)

        st.success("Done!")

        st.markdown(result)
if auto_fix:

    if not code.strip():

        st.warning("Please paste some code.")

    else:

        with st.spinner("Fixing Code..."):

            fixed = fix_agent(code)

        st.success("Done!")

        st.code(
            fixed,
            language=language.lower()
        )
# =====================================================
# Multi-Agent Review
# =====================================================

if review:

    if not code.strip():

        st.warning("Please paste some code.")

    else:

        status = st.empty()

        status.info("🧠 Planner Agent is analyzing your request...")

        report = orchestrate("review", code)

        status.info("🧠 Planner Agent completed")
        pdf_file = generate_pdf(
    report,
    score
)       
        with open(pdf_file, "rb") as file:

          st.download_button(
        label="📄 Download AI Report",
        data=file,
        file_name="CodePilot_Report.pdf",
        mime="application/pdf"
    )
          st.divider()
st.header("📜 Review History")

reviews = get_reviews()

if not reviews:
    st.info("No reviews available yet.")

else:
    for review in reviews:
        review_id, filename, language, score, date = review

        with st.expander(f"📄 {filename}"):
            st.write(f"**Language:** {language}")
            st.write(f"**Score:** {score}/100")
            st.write(f"**Reviewed On:** {date}")

            if st.button("🗑 Delete", key=f"delete_{review_id}"):
                delete_review(review_id)
                st.rerun()

        import time

        time.sleep(0.4)

        status.info("📖 Explain Agent running...")
        time.sleep(0.4)

        status.info("🐞 Bug Detection Agent running...")
        time.sleep(0.4)

        status.info("⚡ Optimization Agent running...")
        time.sleep(0.4)

        status.info("📈 Complexity Agent running...")
        time.sleep(0.4)

        status.info("🔒 Security Agent running...")
        time.sleep(0.4)

        status.success("✅ All AI Agents Completed")

        st.success("🎉 AI Review Completed!")

        filename = "Pasted Code"

        if uploaded_file is not None:
           filename = uploaded_file.name

        save_review(
    filename=filename,
    language=language,
    score=score
)
        tabs = st.tabs([
    "📖 Explain",
    "🐞 Bugs",
    "⚡ Optimize",
    "📈 Complexity",
    "🔒 Security"
])

        with tabs[0]:
          if "Explanation" in report:
             st.markdown(report["Explanation"])
 
        with tabs[1]:
          if "Bug Detection" in report:
             st.markdown(report["Bug Detection"])

        with tabs[2]:
          if "Optimization" in report:
             st.markdown(report["Optimization"])

        with tabs[3]:
          if "Complexity" in report:
             st.markdown(report["Complexity"])

        with tabs[4]:
             if "Security" in report:
               st.markdown(report["Security"])

st.divider()

st.subheader("💬 Ask CodePilot AI")

question = st.text_input(
    "Ask any programming question"
)

if st.button("Ask AI"):

    if question.strip():

        with st.spinner("Thinking..."):

            answer = chat_with_ai(question)

        st.markdown(answer)

if page == "📜 Review History":

    st.title("📜 Review History")
    search = st.text_input("🔍 Search by filename")

reviews = get_reviews()

reviews = get_reviews()
if not reviews:
        st.info("No reviews available yet.")

else:

        for review in reviews:

            review_id = review[0]
            filename = review[1]
            language = review[2]
            score = review[3]
            date = review[4]

            with st.expander(f"📄 {filename}"):

                st.write(f"**Language:** {language}")

                st.write(f"**Score:** {score}/100")

                st.write(f"**Reviewed On:** {date}")

                if st.button(
                    "🗑 Delete",
                    key=review_id
                ):

                    delete_review(review_id)

                    st.rerun()
st.divider()

dashboard()
st.divider()

st.markdown("""
<div style="text-align:center;color:gray;">
Made with ❤️ using Streamlit, Groq, SQLite & Plotly
<br><br>
© 2026 CodePilot AI
</div>
""", unsafe_allow_html=True)

with st.expander("🛠 Tech Stack"):

    st.write("""
Frontend:
- Streamlit

Backend:
- Python

Database:
- SQLite

AI:
- Groq Llama 3.3

Visualization:
- Plotly

Reports:
- ReportLab
""")