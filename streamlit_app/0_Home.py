import streamlit as st

st.set_page_config(
    page_title= "Peter Police Report Project",
    page_icon = ":cop:"

)


st.title("Peter Police Report ")

st.header("Riverside County Sheriff Department")

text = '<p style="font-family:sans-serif; color:Blue; font-size: 18px;">Select relevant template to file a report</p>'
st.markdown(text, unsafe_allow_html=True)
