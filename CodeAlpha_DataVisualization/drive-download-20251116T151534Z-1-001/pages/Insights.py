import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔍 HR Insights")

df = pd.read_csv("data/HR_Analytics.csv")

st.subheader("Attrition by Work Life Balance")
fig1 = px.bar(df, x="WorkLifeBalance", color="Attrition")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Attrition by Overtime")
fig2 = px.bar(df, x="OverTime", color="Attrition")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Years Since Last Promotion vs Attrition")
fig3 = px.box(df, x="Attrition", y="YearsSinceLastPromotion")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Years with Current Manager vs Attrition")
fig4 = px.box(df, x="Attrition", y="YearsWithCurrManager")
st.plotly_chart(fig4, use_container_width=True)