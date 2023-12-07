import streamlit as st

st.set_page_config(
    page_title= "Police Report Generation",
    page_icon = ":cop:"

)


st.title("Police Report Generation")

st.write("""
A web app for filing police reports allows users to input incident details, suspect and witness 
information, and upload supporting evidence. It features a user-friendly interface with clear 
instructions, automated report generation, and auto-extraction of penal code based on incident details.
""")

st.info("👈 Select **File Report** from the sidebar to get started!")
