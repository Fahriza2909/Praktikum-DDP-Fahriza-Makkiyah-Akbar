import streamlit as st

st.title("Biodata Form")
st.header("Please fill in your details below:")
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "      Female", "Other"])
hobbies = st.multiselect("Hobbies", ["Reading", "Traveling", "Gaming", "Cooking", "Sports"])
if st.button("Submit"):
    st.subheader("Submitted Information:")
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"Hobbies: {', '.join(hobbies)}")

st.sidebar.title("Navigation")
st.sidebar.header("Go to:") 
page = st.sidebar.selectbox("Select Page", ["Home", "About", "Contact"])
if page == "Home":
    st.sidebar.write("Welcome to the Home Page!")
elif page == "About":
    st.sidebar.write("This is an app to collect biodata using Streamlit.")