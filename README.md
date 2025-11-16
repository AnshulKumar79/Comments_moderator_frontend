# Comments_moderator_frontend
Creating a decoupled ML system by calling the FastAPI deployed on render(acting as backend) from the light-weight frontend created using streamlit.
## Comment Moderator Frontend
This is a simple Streamlit web app that provides a user interface for a (separate) ML-powered comment moderation API.

It allows a user to enter any text and instantly check it for both spam and profanity in a single click.

## Live Demo: https://commentsmoderatorfrontend-byanshulkumarchauhan.streamlit.app/

## System Architecture
This is a decoupled application. This repository only contains the frontend UI code.

Frontend (This Repo): A lightweight Streamlit app. It handles user input and displays results.

Backend (Separate API): A FastAPI running on Render. It hosts the scikit-learn models, performs the NLP, and returns a JSON prediction.

This Streamlit app makes an HTTP POST request to the FastAPI endpoint to get its results.

Link to Backend API Repo:  https://github.com/AnshulKumar79/Comments_Filter_API.git

💻 Tech Stack
Streamlit: For building the interactive web UI.

Requests: For making API calls to the ML backend.

Python 3
