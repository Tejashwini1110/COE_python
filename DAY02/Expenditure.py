import streamlit as st
st.title("Shopping bills")
basic_salary = st.number_input("Enter your basic salary:",min_value=0,step=1)
bill1 = st.number_input("Enter the amount of bill1 :",min_value=0,step=1)
bill2 = st.number_input("Enter the amount of bill2 :",min_value=0,step=1)
bill3 = st.number_input("Enter the amount of bill3:",min_value=0,step=1)
st.success(bill1+bill2+bill3)
st.success(basic_salary*(bill1+bill2+bill3)/100)