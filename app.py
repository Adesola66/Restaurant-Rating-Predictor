import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib 

st.set_page_config(layout= "wide")

scaler = joblib.load("scaler.pkl")

st.title("Restaurant Rating Predictor App")

st.caption("This app help you to predict the restaurant review category")

st.divider()

averagecost = st.number_input("please enter estimated average cost for two", min_value=50, max_value=99999,value=1000, step=200)

tablebooking = st.selectbox("Restaurant has table booking?", ["Yes", "No"])

onlinedelivery = st.selectbox("Restaurand has online delivery?", ["Yes", "No"])

pricerange = st.selectbox("what is the price range (1 cheapest, 4 most expensive)",[1,2,3,4])

predictbutton = st.button("predict the review!")

st.divider()

model = joblib.load("mlmodel.pkl")

bookingstatus = 1 if tablebooking == "Yes" else 0 

deliverystatus = 1 if onlinedelivery == "Yes" else 0

# Has table booking 0 is no 1 is yes
# Has online delivery 0 is no 1 is yes 

#averagecost = scaler.fit_transform(averagecost)
#bookingstatus = scaler.fit_transform(averagecost)
#deliverystatus = scaler.fit_transform(deliverystatus)
#pricerange = scaler.fit_transform(pricerange)

values = [[averagecost, bookingstatus, deliverystatus, pricerange]]

my_x_values = np.array(values)

x = scaler.transform(my_x_values)

if predictbutton:
    st.snow()

prediction = model.predict(x)    

st.write(prediction)

#Above 2 below 2.5 Poor
#Above 2.5 below 3.5 Average
#Above 3.5 below 4.0 Good
#Above 4.5 Excellent

if prediction < 2.5:
    st.write("poor")
elif prediction < 3.5:
    st.write("average")
elif prediction < 4.0:
    st.write("Good")
elif prediction <= 4.5:
    st.write("Very Good")
else:
    st.write("Excellent")
    