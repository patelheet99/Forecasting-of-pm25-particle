# Objective
To forecast the pm25 particle which cause low visibility in Delhi, for next 24 hour

# Data
data consist two columns:one datetime and another is pm25 value 

# Data preprocessing
this one is forecasting project so for data visualisation lag plot,seasonal components were plotted. for better visualisation scroll bar plot is plotted so anyone can see value of pm25 particle for exact specific datatime and hour.
Here null values should not be filled with mean or median of data so null values filled by Optimal Interpolation method.

# Model building
built different model using data driven approaches, method based approaches, ARIMA and FBProphet.
got best accuracy which was, RMSE value around 0.10 using FBProphet

# Deployment
deploy the model using Streamlit.There user have only upload the preprocessed dataset and have to select only time period for forecasting.
Then appplication return the forecasted result on hourly basis with visualisation .
