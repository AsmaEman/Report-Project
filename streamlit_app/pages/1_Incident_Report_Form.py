import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time



st.set_page_config(
    page_title= "Report",
    page_icon = ":page_with_curl:"

)

# Display Title and Description
st.title("Data Entry for Incident Report")
st.header("Riverside County Sheriff Department")
st.markdown("Enter the details below.")

# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing data
existing_data = conn.read(worksheet="ReportDetails" , ttl =10)
existing_data = existing_data.dropna(how="all")


with st.form(key="report_form" , clear_on_submit = True):
    st.write("General Information")
    report_number = st.text_input(label="Report Number")
    report_date = st.date_input(label="Report Date")
    report_officer = st.text_input(label="Report Officer")
    assignment = st.text_input(label="Assignemnt")
    st.write("1. Incident Details")
    incident_date = st.date_input(label="Incident Date")
    incident_location = st.text_input(label="Incident Location")
    incident_nature = st.text_input(label="Incident Nature")
    injuries_observed = st.text_area(label="Injuries Observed")
    inital_observation = st.text_area(label="Initial Observation")
    st.write("2. Victim Information")
    victim_name = st.text_input(label="Victim Name")
    victim_address = st.text_input(label="Victim Address")
    victim_contact= st.text_input(label="Victim conatct (Email & Phone)")
    victim_statement = st.text_area(label="Summary of Victim's Statement")
    st.write("3. Witness Statement")
    witness_name = st.text_input(label="Witness Name")
    witness_address = st.text_input(label="Witness Address")
    witness_contact= st.text_input(label="Witness conatct (Email & Phone)")
    witness_relation = st.selectbox('Relationship to Incident', ['Neighbor','Bystander','Other'])
    witness_statement = st.text_area(label="Summary of Witness's Statement")
    st.write("4. Suspect Information")
    suspect_name = st.text_input(label="Suspect's Name")
    suspect_description= st.text_area(label="Suspect Description (Gender, Race, Age Range, Height, Weight, Clothing)")
    suspect_location = st.text_input(label="Suspect's Current Location")
    vehicle_info = st.text_input(label = "Vehical Information")
    st.write("5. Evidence Collected")
    photographs = st.text_input(label="Photographs (Details of Injuries,Scenes etc)")
    medical_reports = st.text_input(label="Medical Reports")
    physical_evidence = st.text_area(label="Details of Physical Evidence")
    surveillance_footage = st.text_input(label="Surveillance footage")
    other_evidence = st.text_area(label="Details of Other Relevant Evidence")
    st.write("6. Investigate Actions")
    scene_processing = st.text_area(label="Details of Crime Scene Processing")
    interviews = st.text_area(label="Details of Interviews Conducted (with Victim, Witness, Suspect)")
    background_checks = st.text_area(label="Results of Background Check on Suspect")
    add_investigate_actions = st.text_area(label="Other Actions Taken or Planned")
    st.write("7. Additional Informaton/Follow-up Actions")
    add_observations = st.text_area(label="Additional Observations")
    rec_follow_up_actions = st.text_area(label="Follow-up Actions Recommended")
    assign_investigator = st.text_input(label="Name of Assigned Investigator (if other than Reporting)")
    case_status = st.text_input(label = "Case Status")
    st.write("8. Reporting Officer's Statement")
    officer_narrative = st.text_area(label="Officer's Narrative of the Incident (including obervations, actions taken, and any initial conclusions or Hypotheses")
    officer_signature = st.text_input(label = "Signature of Reporting Officer")
    completion_date = st.date_input(label = "Date of Report Completion")
    supervisor_signature = st.text_input(label = "Supervisor Review and Signature")
    review_date = st.date_input(label = "Date of Review")

    submit_button = st.form_submit_button(label="Submit Details")

    # If the submit button is pressed
    if submit_button:


            report_data = {
                        "ReportNumber": report_number,
                        "ReportDate": report_date,
                        "ReportOfficer": report_officer,
                        "Assignment": assignment,
                        "IncidentDate" : incident_date,
                        "IncidentLocation" : incident_location,
                        "IncidentNature" : incident_nature ,
                        "InjuriesObserved" : injuries_observed, 
                        "InitialObservation" : inital_observation,
                        "VictimName" : victim_name ,
                        "VictimAddress" :victim_address,
                        "VictimContact" : victim_contact,
                        "VictimStatment" : victim_statement,
                        "WitnessName" : witness_name,
                        "WitnessAddress" : witness_address,
                        "WitnessConatct" : witness_contact,
                        "WitnessRelation" : witness_relation,
                        "WitnessStatement" : witness_statement,
                        "SuspectName": suspect_name,
                        "SuspectDescription" : suspect_description,
                        "SuspectLocation": suspect_location,
                        "VehicleInfo" : vehicle_info ,
                        "Photographs": photographs,
                        "MedicalReports": medical_reports,
                        "PhysicalEvidence": physical_evidence,
                        "SurveillanceFootage": surveillance_footage,
                        "OtherEvidence": other_evidence,
                        "SceneProcessing":scene_processing,
                        "Interviews": interviews,
                        "BackgroundChecks": background_checks,
                        "AddInvestigateActions" : add_investigate_actions,
                        "AddObservations": add_observations,
                        "RecFollowupActions": rec_follow_up_actions,
                        "AssignInvestigator": assign_investigator,
                        "CaseStatus" : case_status,
                        "OfficerNarrative": officer_narrative,
                        "OfficerSignature": officer_signature,
                        "CompletionDate": completion_date,
                        "SupervisorSignature": supervisor_signature,
                        "ReviewDate": review_date                   
                    }

                     
            st.session_state.report_data = report_data

            df_report_data = pd.DataFrame([report_data])

            # Add the new data to the existing data
            updated_df = pd.concat([existing_data, df_report_data], ignore_index=True)

            # Update Google Sheets with the new incident data
            conn.update(worksheet="ReportDetails", data=updated_df)

            with st.empty():
                st.success("Report Details successfully submitted!")
                time.sleep(5)
                st.success("")

            
            #alert = st.warning("Report Details successfully submitted!") # Display the alert
            #time.sleep(3) # Wait for 3 seconds
            #alert.empty()

