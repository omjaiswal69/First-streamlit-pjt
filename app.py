import streamlit as st
st.title("this is my first project on streamlit")
st.write("Hello, world!")
st.write("This is a simple Streamlit app.")
# for slidebar
slider_value = st.slider("Select a value", 0, 100, 50)
st.write(f"You selected: {slider_value}!")
# for checkbox
checkbox_value = st.checkbox("Check me!")
if checkbox_value:
    st.write("Checkbox is checked!")    
else:
    st.write("Checkbox is not checked!")