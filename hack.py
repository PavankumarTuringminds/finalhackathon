# -*- coding: utf-8 -*-
"""hack.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yP5j0sgtwADyMXdcwcUpIQx5IJNkrUMe
"""

import subprocess
subprocess.call(['pip', 'install', 'streamlit'])

import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('/content/drive/MyDrive/data set/train1.csv')
st.write('###### Telecom Customer Detail')
st.write('## Dataset')
st.write(df)

df = df.drop(['customerID'], axis=1)

le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
df['TotalCharges'] = le.fit_transform(df['TotalCharges'])
df['Partner'] = le.fit_transform(df['Partner'])
df['Dependents'] = le.fit_transform(df['Dependents'])
df['PhoneService'] = le.fit_transform(df['PhoneService'])
df['MultipleLines'] = le.fit_transform(df['MultipleLines'])
df['InternetService'] = le.fit_transform(df['InternetService'])
df['OnlineSecurity'] = le.fit_transform(df['OnlineSecurity'])
df['OnlineBackup'] = le.fit_transform(df['OnlineBackup'])
df['DeviceProtection'] = le.fit_transform(df['DeviceProtection'])
df['TechSupport'] = le.fit_transform(df['TechSupport'])
df['StreamingTV'] = le.fit_transform(df['StreamingTV'])
df['StreamingMovies'] = le.fit_transform(df['StreamingMovies'])
df['Contract'] = le.fit_transform(df['Contract'])
df['PaperlessBilling'] = le.fit_transform(df['PaperlessBilling'])
df['PaymentMethod'] = le.fit_transform(df['PaymentMethod'])
df['Churn'] = le.fit_transform(df['Churn'])
df['MonthlyCharges'] = df['MonthlyCharges'].astype(float)


X = df.drop('Churn', axis=1)
y = df['Churn']

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNN model on the training set
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = lr_model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import pickle
from sklearn.neighbors import KNeighborsClassifier

# Train your KNN model
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

import pickle
# Saving the model
with open('logistic_regression_model.pkl', 'wb') as f:
    pickle.dump(lr_model, f)

with open('logistic_regression_model.pkl', 'rb') as f:
    lr_model = pickle.load(f)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('/content/drive/MyDrive/data set/train1.csv')

# Define the columns to display
columns = ['tenure', 'MonthlyCharges', 'TotalCharges', 'gender', 'SeniorCitizen', 'Partner']

# Create a selectbox to choose a column to display
selected_column = st.selectbox('Select a column to display', columns)

# Display a bar chart of the selected column
fig, ax = plt.subplots()
ax.bar(df[selected_column].unique(), df[selected_column].value_counts())
plt.title(selected_column)
plt.xlabel(selected_column)
plt.ylabel('Count')
st.pyplot(fig)

# Display a histogram of the selected column
fig, ax = plt.subplots()
ax.hist(df[selected_column], bins=30)
plt.title(selected_column)
plt.xlabel(selected_column)
plt.ylabel('Frequency')
st.pyplot(fig)

# Display a scatter plot of MonthlyCharges vs. TotalCharges
if selected_column == 'MonthlyCharges':
    fig, ax = plt.subplots()
    ax.scatter(df['MonthlyCharges'], df['TotalCharges'])
    plt.title('MonthlyCharges vs. TotalCharges')
    plt.xlabel('MonthlyCharges')
    plt.ylabel('TotalCharges')
    st.pyplot(fig)

import matplotlib.pyplot as plt
# Define a function to get new data from the user
def get_new_data():
    
    st.sidebar.write('# Enter the new data point:')
    gender = st.sidebar.selectbox('gender', ['Male', 'Female'])
    SeniorCitizen = st.sidebar.radio('SeniorCitizen', [0, 1])
    Partner = st.sidebar.selectbox('Partner', ['Yes', 'No'])
    Dependents = st.sidebar.selectbox('Dependents', ['Yes', 'No'])
    tenure = st.sidebar.number_input('tenure', min_value=0)
    PhoneService = st.sidebar.selectbox('PhoneService', ['Yes', 'No'])
    MultipleLines = st.sidebar.selectbox('MultipleLines', ['No phone service', 'No', 'Yes'])
    InternetService = st.sidebar.selectbox('InternetService', ['DSL', 'Fiber optic', 'No'])
    OnlineSecurity = st.sidebar.selectbox('OnlineSecurity', ['No internet service', 'No', 'Yes'])
    OnlineBackup = st.sidebar.selectbox('OnlineBackup', ['No internet service', 'No', 'Yes'])
    DeviceProtection = st.sidebar.selectbox('DeviceProtection', ['No internet service', 'No', 'Yes'])
    TechSupport = st.sidebar.selectbox('TechSupport', ['No internet service', 'No', 'Yes'])
    StreamingTV = st.sidebar.selectbox('StreamingTV', ['No internet service', 'No', 'Yes'])
    StreamingMovies = st.sidebar.selectbox('StreamingMovies', ['No internet service', 'No', 'Yes'])
    Contract = st.sidebar.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
    PaperlessBilling = st.sidebar.selectbox('PaperlessBilling', ['Yes', 'No'])
    PaymentMethod = st.sidebar.selectbox('PaymentMethod', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    MonthlyCharges = st.sidebar.number_input('MonthlyCharges', min_value=0)
    TotalCharges = st.sidebar.number_input('TotalCharges', min_value=0)
    
    # Convert the input values to a dataframe
    input_dict = {'tenure': tenure,
                  'gender': gender,
                  'SeniorCitizen': SeniorCitizen,
                  'Partner': Partner,
                  'Dependents': Dependents,
                  'PhoneService': PhoneService,
                  'MultipleLines': MultipleLines,
                  'InternetService': InternetService,
                  'OnlineSecurity': OnlineSecurity,
                  'OnlineBackup': OnlineBackup,
                  'DeviceProtection': DeviceProtection,
                  'TechSupport': TechSupport,
                  'StreamingTV': StreamingTV,
                  'StreamingMovies': StreamingMovies,
                  'Contract': Contract,
                  'PaperlessBilling': PaperlessBilling,
                  'PaymentMethod': PaymentMethod,
                  'MonthlyCharges': MonthlyCharges,
                  'TotalCharges': TotalCharges}
    input_df = pd.DataFrame.from_dict([input_dict])

    # Show the filtered dataset
    st.write('## Filtered Data')
    st.write(input_df)

    # Encode input features
    le = LabelEncoder()
    for column in input_df.columns:
        input_df[column] = le.fit_transform(input_df[column])
    
   # Make predictions and display results
    st.write('## Predictions')
    if st.sidebar.button('Predict'):
        X_pred = input_df.values
        y_pred = lr_model.predict(X_pred)

        if y_pred == 0:
           st.success('The customer is not likely to churn.')
    else:
           st.error('The customer is likely to churn.')  

 
# Run the Streamlit app
get_new_data()

from google.colab import drive
drive.mount('/content/drive')