import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time
import pickle
import openai
from langchain.llms import OpenAI
import openai
from langchain import FewShotPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from docx import Document
import io
from PIL import Image
import PyPDF2

st.set_page_config(
    page_title= "Report",
    page_icon = ":page_with_curl:"

)

class Chatbot:
    def __init__(self, api_key, index):
        self.index = index
        openai.api_key = api_key

    def generate_response_from_text(self, user_input):
        prompt = f"""
        Incident Summary: {user_input}

                As a criminal law expert, understand the incident and try to find relevant penal code.

                Only return the penal code without heading. Do not write any filler text.

                If you can't find the penal code, return "N/A".
        """
        query_engine = self.index.as_query_engine()  # Use self.index instead of index
        response = query_engine.query(prompt)  # Use prompt instead of user_input

        message = {"content": response.response}
        return message
    def generate_report_response(self, user_input):
        # open a file, where you stored the pickled data
        file = open('few_shot_prompt_template', 'rb')

        # dump information to that file
        data = pickle.load(file)

        # close the file
        file.close()
   
        report_prompt = data.format(query=f"""
        Incident Report: {user_input} Generate a summary of an incident report involving the case. Include information about the date, location,
        individuals involved, actions taken by law enforcement, and the current case status just remove extra symbols from query?
        """)
        
        query_engine = self.index.as_query_engine()  # Use self.index instead of index
        report_response= query_engine.query(report_prompt)  # Use prompt instead of user_input


        return report_response
    def evidence_image(self,image_path):
        
        result = openai.chat.completions.create(
            model = "gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text",
                        "text": "Analyze the visual content of the provided image file, creating a brief summary that highlights crucial details while excluding irrelevant information. Aim for accuracy and clarity in your analysis. If summarization poses challenges or specific details are unclear, kindly mention 'N/A' in your response."},
                        {"type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{image_path}"},
                    ]
                },
            ],
            max_tokens=300,
            )
        return result.choices[0].message.content
    def generate_evidence_summary(self, evidence_input):
        prompt = f"""
        Evidence Summary: {evidence_input}

               Examine the contents of the attached files and craft a concise summary, 
               emphasizing essential details while excluding irrelevant information. 
               Strive for precision and coherence in your analysis. If summarizing proves challenging or certain details are unclear,
               please indicate 'N/A'.
        """
        query_engine = self.index.as_query_engine()
        response = query_engine.query(prompt)
        return response
    
    
 

report_numbers = {}
if 'report_numbers' in st.session_state:
    report_numbers = st.session_state.report_numbers

st.image("logo.png" , width=200)
# Display Title and Description
st.title("Online Report Form")
# st.caption("Riverside County Sheriff Department")
st.write("Enter the details below:")

# Establishing a Google Sheets connection
# conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing data
# existing_data = conn.read(worksheet="ReportDetails" , ttl =10)
# existing_data = existing_data.dropna(how="all")

# open a file, where you stored the pickled data
file = open('LLM_Index', 'rb')

# dump information to that file
LLM_Index = pickle.load(file)

# close the file
file.close()

bot = Chatbot("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", index=LLM_Index)

with st.form(key="report_form" , clear_on_submit = True):
    st.caption("1. General Information")
    report_number = st.text_input(label="**Report Number**")
    report_date = st.date_input(label="**Report Date**")
    report_officer = st.text_input(label="**Report Officer**")
    assignment = st.text_input(label="**Assignment**")

    st.caption("2. Incident Details")
    incident_date = st.date_input(label="**Incident Date**")
    incident_location = st.text_input(label="**Incident Location**")
    incident_nature = st.text_input(label="**Incident Nature**")
    injuries_observed = st.text_area(label="**Injuries Observed**")
    inital_observation = st.text_area(label="**Initial Observation**")

    st.caption("3. Victim Information")
    victim_name = st.text_input(label="**Victim Name**")
    victim_address = st.text_input(label="**Victim Address**")
    victim_contact= st.text_input(label="**Victim Conatct (Email / Phone)**")
    victim_statement = st.text_area(label="**Victim's Statement**")

    st.caption("4. Witness Information")
    witness_name = st.text_input(label="**Witness Name**")
    witness_address = st.text_input(label="**Witness Address**")
    witness_contact= st.text_input(label="**Witness Conatct (Email / Phone)**")
    witness_relation = st.selectbox('**Relationship to Victim**', ['--', 'Neighbor','Bystander','Other'])
    witness_statement = st.text_area(label="**Witness's Statement**")

    st.caption("5. Suspect Information")
    suspect_name = st.text_input(label="**Suspect's Name**")
    suspect_description= st.text_area(label="**Suspect Description**")
    suspect_location = st.text_input(label="**Suspect's Current Location**")

    st.caption("6. Evidence Collected")
    evidence_files = st.file_uploader(
    label="**Photographs / Reports / Footage**",
    type=["jpg", "jpeg", "png", "pdf", "docx"],
    accept_multiple_files=True
    )


    
    physical_evidence = st.text_area(label="**Details of Evidence**")

    st.caption("7. Investigation Summary")
    scene_processing = st.text_area(label="**Crime Scene**")
    background_checks = st.text_area(label="**Suspect's Background Check**")
    add_investigate_actions = st.text_area(label="**Other Actions**")
    
    st.caption("8. Final Remarks")
    add_observations = st.text_area(label="**Additional Observations**")
    # officer_narrative = st.text_area(label="**Reporting Officer's Statement**")

    case_status = st.text_input(label = "**Case Status**")
    completion_date = st.date_input(label = "**Report Completion Date**")
    review_date = st.date_input(label = "**Review Date**")

    submit_button = st.form_submit_button(label="**Submit Report**")
    # If the submit button is pressed
    if submit_button:
            evidence_summary = 'N/A'
            if evidence_files:
                for file_num, file in enumerate(evidence_files, start=1):
                    try:
                        if file.type.startswith("image"):
                            encoded_image = base64.b64encode(file.read()).decode('utf-8')
                            summary = bot.evidence_image(encoded_image)
                        elif file.type == "application/pdf":
                            pdf_content = ""
                            pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(file.read()))
                            for page_num in range(pdf_reader.numPages):
                                pdf_content += pdf_reader.getPage(page_num).extractText()
                            summary = bot.generate_evidence_summary(pdf_content)
                        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                            doc = Document(io.BytesIO(file.read()))
                            paragraphs = [paragraph.text for paragraph in doc.paragraphs]
                            input_text = "\n".join(paragraphs)
                            summary = bot.generate_evidence_summary(input_text)
                        else:
                            st.warning(f"Unsupported file type for File {file_num}. Please upload a supported file type.")
                            continue

                        evidence_summary = summary

                    except Exception as e:
                        st.error(f"Error processing File {file_num}: {str(e)}")
            else:
                # Handle the case when no evidence files are uploaded
                evidence_summary = 'N/A'
            penal_code = 'N/A'
            Officer_Statement = 'N/A'
            
            # Generate a response using a 'bot' object
            if incident_nature or inital_observation or victim_statement:
                while penal_code == 'N/A':
                    user_input = incident_nature# ' '.join([incident_nature, inital_observation, victim_statement])
                    print(user_input)
                    response = bot.generate_response_from_text(user_input)
                    penal_code = response['content'].split('Penal Code: ')[-1]

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
                        "PhysicalEvidence": physical_evidence,
                        "SceneProcessing":scene_processing,
                        "BackgroundChecks": background_checks,
                        "AddInvestigateActions" : add_investigate_actions,
                        "AddObservations": add_observations,
                        "PenalCode": penal_code,
                        "OfficerStatement":Officer_Statement,
                        "EvidenceSummary" : evidence_summary,
                        "CaseStatus" : case_status,
                        "CompletionDate": completion_date,
                        "ReviewDate": review_date
                    }
            if report_data:
                while Officer_Statement == 'N/A':
                    response = bot.generate_report_response(report_data)
                    Officer_Statement = response
                report_data["OfficerStatement"] = Officer_Statement
            report_numbers[report_number] = report_data
            st.session_state.report_data = report_data
            st.session_state.report_numbers = report_numbers


            st.success("File Reported Successfully!")


