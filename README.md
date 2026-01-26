🚗 Car Price Prediction System

An end-to-end Machine Learning web application that predicts the price of a used car based on user inputs.
The project includes a FastAPI backend for model inference and a Streamlit frontend for user interaction.

📌 Project Overview

This project demonstrates how to take a Machine Learning model from development to deployment by:
Training a regression model using real-world car data
Saving the trained ML pipeline
Exposing predictions via a REST API using FastAPI
Building an interactive UI using Streamlit
Deploying backend and frontend as separate services
The system allows users to input car details and get a predicted price instantly.

🛠 Tech Stack

Programming Language
Python
Machine Learning
scikit-learn
pandas
numpy

Backend

FastAPI
Uvicorn

Frontend

Streamlit

Deployment

Backend: Render
Frontend: Streamlit Cloud

⚙️ How It Works

User enters car details on the Streamlit UI
Streamlit sends a POST request to the FastAPI backend
FastAPI loads the trained ML pipeline
The model predicts the car price
Prediction is returned and displayed on the UI

▶️ How to Run the Project Locally
🔹 Backend (FastAPI)

Clone the backend repository

git clone https://github.com/amits-1729/car-price-backend.git
cd car-price-backend


Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run the FastAPI server

python -m uvicorn main:app --reload --port 8080


Open API docs:

http://127.0.0.1:8080/docs

🔹 Frontend (Streamlit)

Clone the frontend repository

git clone https://github.com/your-username/car-price-frontend.git
cd car-price-frontend


Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py
