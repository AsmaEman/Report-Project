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

@app.route('/summarize_evidence', methods=['POST'])
def summarize_evidence():
    if request.content_type.startswith('multipart/form-data'):
        file = request.files.get('file')
        if file and file.filename:
            if file.content_type.startswith('image/'):
                summary = bot.summarize_image_evidence(file.read())
            else:
                summary = bot.summarize_text_evidence(file.read())
        else:
            return jsonify({'error': 'No file provided'}), 400
    elif request.content_type.startswith('application/json'):
        text_data = request.json.get('text_data', '')
        summary = bot.summarize_text_evidence(text_data)
    else:
        return jsonify({'error': 'Unsupported Media Type'}), 415

    return jsonify({'summary': summary})
if __name__ == '__main__':
    app.run(debug=True, port=5000)