import streamlit as st
st.title("Gross salary calculator")
basic_salary = st.number_input("Enter your basic salary:", min_value=0,step=1)
if st.button("calculate gross salary") :
    hra=0
    da=0
if basic_salary < 10000:
    hra=basic_salary*0.67
    da=basic_salary*0.73
elif basic_salary<20000:
    hra=basic_salary*0.69
    da=basic_salary*0.76
else:
    hra=basic_salary*0.73
    da=basic_salary*0.89
gross_salary=hra+da+basic_salary
st.success(gross_salary)