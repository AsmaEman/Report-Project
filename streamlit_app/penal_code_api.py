import streamlit as st
from flask import Flask, request, jsonify
import threading
import requests 
import pickle
from pages.File_Report import Chatbot


file = open('LLM_Index', 'rb')


LLM_Index = pickle.load(file)

file.close()
bot = Chatbot("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", index=LLM_Index)


app = Flask(__name__)
@app.route('/')
def home():
    return "API Service"
@app.route('/find_penal_code', methods=['POST'])
def find_penal_code():
    data = request.json
    incident_description = data.get('incident_description')
    penal_code = bot.generate_response_from_text(incident_description)
    return jsonify({'penal_code': penal_code})
if __name__ == '__main__':
    app.run(debug=True, port=5000)


# Json
# {
#   "incident_description": "Theft"
# }