import streamlit as st
from flask import Flask, request, jsonify
import threading
import requests 
import pickle
from pages.File_Report import Chatbot, process_file
import base64

file = open('LLM_Index', 'rb')


LLM_Index = pickle.load(file)

file.close()
bot = Chatbot("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", index=LLM_Index)
app = Flask(__name__)
@app.route('/summarize_evidence', methods=['POST'])
def summarize_evidence():
    # Check if there is a file in the request
    if 'file' in request.files:
        file = request.files['file']

        # Ensure the file is not empty
        if file and file.filename:
            
            if file.content_type.startswith('image/'):
                # Process image file
                summary = bot.evidence_image(process_file(file))
            else:
                # Process other file types (e.g., PDF, DOCX)
                summary = bot.generate_evidence_summary(process_file(file))
        else:
            return jsonify({'error': 'No file provided'}), 400
    else:
        return jsonify({'error': 'No file part in the request'}), 400

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
