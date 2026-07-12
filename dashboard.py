import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

DATABASE = "reviews.db"


def load_reviews():
    """Load all reviews from the database."""

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(
        "SELECT * FROM reviews",
        conn
    )

    conn.close()

    return df


def dashboard():

    st.header("📊 Analytics Dashboard")

    df = load_reviews()

    if df.empty:
        st.info("No review data available.")
        return

    # KPI Cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Total Reviews", len(df))

    with col2:
        st.metric("⭐ Average Score", f"{df['score'].mean():.1f}")

    with col3:
        st.metric("🏆 Highest Score", df["score"].max())

    st.divider()

    # Language Distribution
    st.subheader("💻 Language Distribution")

    language_chart = px.bar(
        df["language"].value_counts().reset_index(),
        x="language",
        y="count",
        labels={
            "language": "Language",
            "count": "Reviews"
        },
        title="Reviews by Language"
    )

    st.plotly_chart(
        language_chart,
        use_container_width=True
    )

    # Score Distribution
    st.subheader("📈 Score Distribution")

    score_chart = px.histogram(
        df,
        x="score",
        nbins=10,
        title="Code Quality Scores"
    )

    st.plotly_chart(
        score_chart,
        use_container_width=True
    )

    st.subheader("📋 Raw Review Data")

    st.dataframe(
        df,
        use_container_width=True
    )