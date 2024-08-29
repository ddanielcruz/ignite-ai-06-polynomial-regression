import requests
import streamlit as st

st.title("Salary Prediction Model")

st.write("Please enter the number of months of experience of the employee.")
months_of_experience = st.slider(
    "Months of Experience",
    min_value=1,
    max_value=120,
    step=1,
)

st.write("Please enter the level of the employee.")
level = st.slider(
    "Level",
    min_value=1,
    max_value=10,
    step=1,
)

# Create the request body
request_body = {
    "time_in_company": months_of_experience,
    "level": level,
}

if st.button("Predict Salary"):
    # Make a POST request to the API
    response = requests.post("http://localhost:8000/predict_salary", json=request_body)

    # Parse the JSON response
    response_data = response.json()

    # Display the prediction
    st.subheader("Prediction")
    st.write(
        f"The predicted salary is {response_data['salary']:.2f} {response_data['currency']}."
    )
