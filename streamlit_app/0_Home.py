import streamlit as st

st.set_page_config(

    page_title= "Police Report Generation",
    page_icon = ":cop:"

)


st.image("logo.png" , width=200)

#st.title("RIVERSIDE COUNTY SHERIFF")

st.title("Police Report Generation")

st.write("""
A web app for filing police reports allows users to input incident details, suspect and witness 
information, and upload supporting evidence. It features a user-friendly interface with clear 
instructions, automated report generation, and auto-extraction of penal code based on incident details.
""")

# Set the custom background color and text color
custom_background_color = "#2b3923"  # Background color
custom_text_color = "#d2ad63"  # Text color

# Use st.markdown with HTML styling to set the background color
st.markdown(
    f"""
    <div style="background-color:{custom_background_color}; padding:15px 0px 05px 10px; border-radius: 5px;">
        <p style="color:{custom_text_color};">👈 Select <strong>File Report</strong> from the sidebar to get started!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

