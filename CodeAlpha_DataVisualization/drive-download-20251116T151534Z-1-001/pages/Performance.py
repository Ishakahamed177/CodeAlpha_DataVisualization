import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Performance & Salary Analysis")

df = pd.read_csv("data/HR_Analytics.csv")

st.subheader("Performance Rating Distribution")
fig1 = px.histogram(df, x="PerformanceRating")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Monthly Income Distribution")
fig2 = px.histogram(df, x="MonthlyIncome")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Salary vs Job Level")
fig3 = px.box(df, x="JobLevel", y="MonthlyIncome")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Overtime vs Attrition")
fig4 = px.bar(df, x="OverTime", color="Attrition")
st.plotly_chart(fig4, use_container_width=True)