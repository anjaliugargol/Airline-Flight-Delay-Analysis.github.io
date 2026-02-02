import os
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error, accuracy_score, auc, classification_report, confusion_matrix, roc_curve, RocCurveDisplay

df = pd.read_csv('flights_data_100k.csv')
#print(df.head())
#print(df.tail())
#print(df.info())
#print(df.shape)

print(df.isnull().sum())


# List of columns to fill null values with 0
cols_to_fill = [
    "DEP_TIME", "DEP_DELAY", "TAXI_OUT", "WHEELS_OFF",
    "WHEELS_ON", "TAXI_IN", "ARR_TIME", "ARR_DELAY",
    "CANCELLATION_CODE", "CRS_ELAPSED_TIME", "ELAPSED_TIME",
    "AIR_TIME", "DELAY_DUE_CARRIER", "DELAY_DUE_WEATHER",
    "DELAY_DUE_NAS", "DELAY_DUE_SECURITY", "DELAY_DUE_LATE_AIRCRAFT"
]

# Fill null values with 0 for the specified columns
df[cols_to_fill] = df[cols_to_fill].fillna(0)

# Save the updated dataset
df.to_csv("Cleaned_flights_data.csv", index=False)

print("Null values filled with 0 and file saved successfully.")

'''print(df.isnull().sum())
print(df.nunique())'''
print(df.columns.to_list())


#EDA Analysis
# Univariate Analysis
#Arrrival Delay Distribution
'''sns.histplot(df['ARR_DELAY'], bins=50, kde=True)
plt.xlabel("Arrival Delay (minutes)")
plt.ylabel("Number of Flights")
plt.title("Distribution of Arrival Delay")
plt.show()
'''

#Airline-wise Flight Count

'''sns.countplot(x='AIRLINE', data=df)
plt.xlabel("Airline")
plt.ylabel("Number of Flights")
plt.title("Flights per Airline")
plt.xticks(rotation=45)
plt.show()'''


#Cancelled vs Non-Cancelled Flights
'''sns.countplot(x='CANCELLED', data=df)
plt.xlabel("Cancelled (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.title("Cancelled vs Non-Cancelled Flights")
plt.show()'''

#Flight Distance Distribution
'''sns.histplot(df['DISTANCE'], bins=40, kde=True)
plt.xlabel("Distance (miles)")
plt.ylabel("Flights Count")
plt.title("Flight Distance Distribution")
plt.show()
'''

#Bivariate Analysis
#Average Arrival Delay by Airline
'''plt.figure(figsize=(10,5))
sns.barplot(x='AIRLINE', y='ARR_DELAY', data=df, estimator='mean')
plt.xlabel("Airline")
plt.ylabel("Average Arrival Delay")
plt.title("Average Arrival Delay by Airline")
plt.xticks(rotation=45)
plt.show()
'''

#Distance vs Arrival Delay
'''sns.scatterplot(x='DISTANCE', y='ARR_DELAY', data=df, alpha=0.3)
plt.xlabel("Distance")
plt.ylabel("Arrival Delay")
plt.title("Distance vs Arrival Delay")
plt.show()'''

#Average Delay by Day of Week
'''df['FL_DATE'] = pd.to_datetime(df['FL_DATE'])
df['DAY_OF_WEEK'] = df['FL_DATE'].dt.day_name()

plt.figure(figsize=(10,5))
sns.barplot(x='DAY_OF_WEEK', y='ARR_DELAY', data=df, estimator='mean')
plt.xlabel("Day of Week")
plt.ylabel("Average Arrival Delay")
plt.title("Average Delay by Day of Week")
plt.xticks(rotation=45)
plt.show()
'''

#Cancellation Reason vs Count
'''sns.countplot(x='CANCELLATION_CODE', data=df)
plt.xlabel("Cancellation Code")
plt.ylabel("Count")
plt.title("Cancellation Reasons")
plt.show()'''


#Multi-variate Analysis
#Delay Reasons Contribution

'''delay_cols = [
    'DELAY_DUE_CARRIER',
    'DELAY_DUE_WEATHER',
    'DELAY_DUE_NAS',
    'DELAY_DUE_SECURITY',
    'DELAY_DUE_LATE_AIRCRAFT'
]

delay_sum = df[delay_cols].sum().reset_index()
delay_sum.columns = ['Delay_Type', 'Total_Delay']

sns.barplot(x='Delay_Type', y='Total_Delay', data=delay_sum)
plt.xlabel("Delay Type")
plt.ylabel("Total Delay (minutes)")
plt.title("Contribution of Different Delay Reasons")
plt.xticks(rotation=45)
plt.show()
'''

#Distance + Arrival Delay + Airline
'''sample_df = df.sample(5000)

sns.scatterplot(
    x='DISTANCE',
    y='ARR_DELAY',
    hue='AIRLINE',
    data=sample_df,
    alpha=0.6,
    legend=False
)
plt.xlabel("Distance")
plt.ylabel("Arrival Delay")
plt.title("Distance vs Arrival Delay Across Airlines")
plt.show()
'''


#Correlation Heatmap
'''numeric_cols = [
    'DEP_DELAY','ARR_DELAY','TAXI_OUT','TAXI_IN',
    'AIR_TIME','DISTANCE','ELAPSED_TIME'
]

corr = df[numeric_cols].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()'''


#Cancelled vs Delay vs Distance
'''cancel_summary = df.groupby('CANCELLED')[['ARR_DELAY','DISTANCE']].mean().reset_index()

sns.barplot(x='CANCELLED', y='ARR_DELAY', data=cancel_summary)
plt.title("Average Arrival Delay by Cancellation Status")
plt.show()
'''


#Linear Regression
'''X = df[['DEP_DELAY', 'DISTANCE', 'AIR_TIME', 'TAXI_OUT']]
y = df['ARR_DELAY']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
r2_score=r2_score(y_test,y_pred)

print('Mean Squared Error:',mse)
print('R2 Score:',r2_score)
'''

#Logistic Regression
'''df['DELAYED'] = (df['ARR_DELAY'] > 15).astype(int)

X = df[['DEP_DELAY', 'DISTANCE', 'AIR_TIME', 'TAXI_OUT']]
y = df['DELAYED']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# ROC curve
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)'''






#Connection to MySQL Database
'''db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anjali@sql'
)
mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS airline") 
db.close()'''


# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anjali@sql",
    database="airline"
)

if db.is_connected():
    print("✅ Connected to MySQL successfully")

db.close()







import csv
import mysql.connector

def to_bool(value):
    return 1 if str(value).strip().lower() in ('1', 'true', 'yes') else 0

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anjali@sql",
    database="airline"
)

cursor = db.cursor()

sql = '''
INSERT INTO flights (
    FL_DATE, AIRLINE, AIRLINE_DOT, AIRLINE_CODE, DOT_CODE, FL_NUMBER,
    ORIGIN, ORIGIN_CITY, DEST, DEST_CITY,
    CRS_DEP_TIME, DEP_TIME, DEP_DELAY,
    TAXI_OUT, WHEELS_OFF, WHEELS_ON, TAXI_IN,
    CRS_ARR_TIME, ARR_TIME, ARR_DELAY,
    CANCELLED, CANCELLATION_CODE, DIVERTED,
    CRS_ELAPSED_TIME, ELAPSED_TIME, AIR_TIME, DISTANCE,
    DELAY_DUE_CARRIER, DELAY_DUE_WEATHER, DELAY_DUE_NAS,
    DELAY_DUE_SECURITY, DELAY_DUE_LATE_AIRCRAFT
)
VALUES (
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s,
    %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s, %s,
    %s, %s
)
'''

with open("Cleaned_flights_data.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        # Boolean columns
        row[20] = to_bool(row[20])  # CANCELLED
        row[22] = to_bool(row[22])  # DIVERTED

        cursor.execute(sql, row)

db.commit()
cursor.close()
db.close()

print("Flight data inserted into MySQL successfully!")
