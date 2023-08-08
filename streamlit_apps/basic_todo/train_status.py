import streamlit as st 



import requests

url = "https://train-running-status-indian-railways.p.rapidapi.com/trainman/12345"

headers = {
	"X-RapidAPI-Key": "07fd3549bemshdeffdc65b0598aap11450djsneff6c3e08e9e",
	"X-RapidAPI-Host": "train-running-status-indian-railways.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

st.title("Live Train Status Application 🚉")

train = st.text_input("Enter Train Number")
st.write(response.json())