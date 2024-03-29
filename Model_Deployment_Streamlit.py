#Import streamlit
import streamlit as st
#Import NumPy and Pandas for data manipulation 
import pandas as pd
import numpy as np
from fbprophet import Prophet
from fbprophet.diagnostics import performance_metrics
from fbprophet.diagnostics import cross_validation
from fbprophet.plot import plot_cross_validation_metric
#for encoding binary data to printable ASCII characters and decoding it  #back to binary form
import base64  
st.title('Time Series Forecasting Using Streamlit')
st.write("IMPORT DATA")
st.write("Import the time series CSV file. It should have two columns labelled as 'ds' and 'y'. The 'ds' column should be of DateTime format by Pandas. The 'y' column must be numeric representing the measurement to be forecasted.") 
data = st.file_uploader('Upload here',type='csv')
if data is not None:
    appdata = pd.read_csv(data)  #read the data fro
    appdata['ds'] = pd.to_datetime(appdata['ds'],errors='coerce') 
    st.write(data) #display the data  
    max_date = appdata['ds'].max() #compute latest date in the data
st.write("SELECT FORECAST PERIOD") #text displayed
periods_input = st.number_input('How many hours forecast do you want?',min_value = 1, max_value = 24)
#The minimum number of hours a user can select is one, while the maximum is  #24 (yearly forecast)
if data is not None:
    obj = Prophet() #Instantiate Prophet object
    obj.fit(appdata)  #fit the data 
#text to be displayed
st.write("VISUALIZE FORECASTED DATA")  
st.write("The following plot shows future predicted values. 'yhat' is the  predicted value.")
if data is not None:
    future = obj.make_future_dataframe(periods=periods_input,freq='H')
#Prophet.make_future_dataframe() takes the Prophet model object and   #extends the time series dataframe for specified period for which user needs #the forecast
    fcst = obj.predict(future)  #make prediction for the extended data
    forecast = fcst[['ds', 'yhat']]
#The predict() method assigns each row in the ‘future’ dataframe a predicted #value denoted as yhat
#Choose only the forecasted records (having date after the latest date in #original data)
    forecast_filtered =  forecast[forecast['ds'] > max_date]    
    st.write(forecast_filtered)  #Display some forecasted records
    st.write(" The next visual shows the actual (black dots) and predicted(blue line) values over time.")    
    figure1 = obj.plot(fcst) #plot the actual and predicted values
    st.write(figure1)  #display the plot
 #Plot the trends using Prophet.plot_components()
    st.write("The following plots show a high level trend of predicted values, day of week trends and yearly trends (if dataset contains multiple years’ data).Blue shaded area represents upper and lower confidence intervals.")
    figure2 = obj.plot_components(fcst) 
    st.write(figure2) 
	