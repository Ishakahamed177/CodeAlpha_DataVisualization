import streamlit as st
import pandas as pd
import plotly.express as px

st.title("👥 Employee Demographics")

df = pd.read_csv("data/HR_Analytics.csv")

st.subheader("Gender Distribution")
fig1 = px.pie(df, names="Gender")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Marital Status")
fig2 = px.bar(df, x="MaritalStatus")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Age Group Distribution")
fig3 = px.histogram(df, x="AgeGroup")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Education Field")
fig4 = px.bar(df, x="EducationField")
st.plotly_chart(fig4, use_container_width=True)