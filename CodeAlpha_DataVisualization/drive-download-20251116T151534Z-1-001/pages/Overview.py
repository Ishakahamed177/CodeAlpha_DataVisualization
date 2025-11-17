import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📌 HR Overview Dashboard")

df = pd.read_csv("data/HR_Analytics.csv")

# Filters
col1, col2, col3 = st.columns(3)
dept = col1.selectbox("Select Department", ["All"] + list(df["Department"].unique()))
gender = col2.selectbox("Select Gender", ["All"] + list(df["Gender"].unique()))
role = col3.selectbox("Select Job Role", ["All"] + list(df["JobRole"].unique()))

filtered = df.copy()
if dept != "All":
    filtered = filtered[filtered["Department"] == dept]
if gender != "All":
    filtered = filtered[filtered["Gender"] == gender]
if role != "All":
    filtered = filtered[filtered["JobRole"] == role]

# KPIs
total_employees = len(filtered)
attrition_count = filtered[filtered["Attrition"] == "Yes"].shape[0]
attrition_rate = round((attrition_count / total_employees) * 100, 2)
avg_age = round(filtered["Age"].mean(), 1)
avg_salary = round(filtered["MonthlyIncome"].mean(), 1)
avg_years = round(filtered["YearsAtCompany"].mean(), 1)

k1, k2, k3, k4, k5, k6 = st.columns(6)
k1.metric("Total Employees", total_employees)
k2.metric("Attrition Count", attrition_count)
k3.metric("Attrition Rate (%)", attrition_rate)
k4.metric("Average Age", avg_age)
k5.metric("Avg Salary", avg_salary)
k6.metric("Avg Years", avg_years)

# Charts
st.subheader("Attrition by Gender")
fig1 = px.bar(filtered, x="Gender", color="Attrition", barmode="group")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Attrition by Department")
fig2 = px.bar(filtered, x="Department", color="Attrition")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Salary by Job Level")
fig3 = px.box(filtered, x="JobLevel", y="MonthlyIncome")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Age Distribution")
fig4 = px.histogram(filtered, x="Age", nbins=30)
st.plotly_chart(fig4, use_container_width=True)