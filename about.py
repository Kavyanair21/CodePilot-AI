import streamlit as st

def about_page():

    st.header("👨‍💻 About CodePilot AI")

    st.write("""
CodePilot AI is a multi-agent intelligent code review platform.

It helps developers by:

• 📖 Explaining code

• 🐞 Detecting bugs

• ⚡ Suggesting optimizations

• 📈 Analyzing complexity

• 🔒 Finding security issues

• 🛠 Automatically fixing code

• 📊 Providing analytics

• 📄 Generating PDF reports

Built using:

- Python
- Streamlit
- Groq LLM
- SQLite
- Plotly
""")