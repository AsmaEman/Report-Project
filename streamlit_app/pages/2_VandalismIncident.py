import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


# Display Title and Description
st.title("Vandalism Incident Report (PC 594)")
st.header("Riverside County Sheriff Department")
st.markdown("Enter the details below.")

# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing data
existing_data1 = conn.read(worksheet="VandalismIncident" , ttl =10)
existing_data1 = existing_data1.dropna(how="all")

with st.form(key="report_form"):
    report_number = st.text_input(label="Report Number")
    report_date = st.date_input(label="Report Date")
    report_officer = st.text_input(label="Report Officer")
    assignment = st.text_input(label="Assignemnt")


    submit_button = st.form_submit_button(label="Submit Details")

    # If the submit button is pressed
    if submit_button:

            report_data1 = pd.DataFrame(
                [
                    {
                        "ReportNumber": report_number,
                        "ReportDate": report_date,
                        "ReportOfficer": report_officer,
                        "Assignment": assignment,
                       
                    }
                ]
            )

            # Add the new data to the existing data
            updated_df1 = pd.concat([existing_data1, report_data1], ignore_index=True)

            # Update Google Sheets with the new incident data
            conn.update(worksheet="VandalismIncident", data=updated_df1)

            st.success("Vandalism Incident Report successfully submitted!")
