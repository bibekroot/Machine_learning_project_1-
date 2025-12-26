import streamlit as st 
import joblib
st.title ('Lab1:Iris Flower Classifier')
model = joblib.load('model.joblib')
sp_length= st.number_input("enter sepal length")
sp_width = st.number_input("Enter sepal width")
petal_length= st.number_input("Enter petal length")
petal_width= st.number_input("Enter petal width")


if (st.button("Predict")):
    pred = model.predict([[sp_length, sp_width, petal_length, petal_width]])[0]
    st.success(f"Predicted species is {pred}")




