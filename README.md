# ✈ Airline Flight Delay Analysis & Prediction

---

## 📌 Project Objective

Analyze flight delay patterns across airports and airlines, identify key delay drivers, and build predictive models to determine flights most likely to be delayed.

---

## 🛫 Problem Statement

Airlines frequently experience delays due to operational inefficiencies, weather disruptions, air traffic congestion, and aircraft rotation issues.  
This project aims to analyze large-scale flight data and develop predictive models to identify delay risk and improve operational planning.

---

## 📊 Dataset Description

The dataset includes:

- FL_DATE  
- AIRLINE  
- FL_NUMBER  
- ORIGIN / DEST  
- CRS_DEP_TIME / DEP_TIME  
- DEP_DELAY  
- ARR_TIME / ARR_DELAY  
- TAXI_OUT / TAXI_IN  
- AIR_TIME  
- DISTANCE  
- CANCELLED  
- DIVERTED  
- DELAY_DUE_CARRIER  
- DELAY_DUE_WEATHER  
- DELAY_DUE_NAS  
- DELAY_DUE_SECURITY  
- DELAY_DUE_LATE_AIRCRAFT  

**Total Records:** ~100,000+

---

## 🛠 Tools & Technologies Used

- Python (Pandas, NumPy)
- Matplotlib & Seaborn
- Scikit-learn
- MySQL
- Power BI

---

## 🔎 Step 1: Data Cleaning

- Analyzed missing values across delay-related columns  
- Filled null values with 0 for operational consistency  
- Created cleaned dataset (`Cleaned_flights_data.csv`)  
- Ensured dataset was structured for modeling and database integration  

---

## 📈 Step 2: Exploratory Data Analysis (EDA)

Performed:

- Arrival delay distribution analysis  
- Airline-wise flight count comparison  
- Cancellation frequency analysis  
- Delay contribution breakdown (Weather, Carrier, NAS, Security, Late Aircraft)  
- Correlation heatmap of operational variables  
- Distance vs Arrival Delay relationship study  

---

## 🤖 Step 3: Predictive Modeling

### 📌 Linear Regression

**Target Variable:**  
ARR_DELAY (Arrival Delay in Minutes)

**Evaluation Metrics:**  
- Mean Squared Error (MSE)  
- R² Score  

**Objective:**  
Predict arrival delay using operational variables such as departure delay, distance, air time, and taxi-out time.

---

### 📌 Logistic Regression

**Target Variable:**  
DELAYED (1 if ARR_DELAY > 15 minutes, else 0)

**Evaluation Metrics:**  
- Accuracy  
- Confusion Matrix  
- Classification Report  
- ROC Curve  

**Objective:**  
Classify flights likely to be delayed beyond 15 minutes.

---

## 🗄 Step 4: Database Integration

- Designed MySQL database schema for flight records  
- Created `airline` database  
- Inserted cleaned dataset into MySQL  
- Enabled SQL-based delay and airline performance analysis  

---

## 📊 Step 5: Power BI Dashboard

Created an interactive dashboard including:

- Delay frequency by airline  
- Cancellation trends  
- Delay cause contribution analysis  
- Average delay by airport  
- Predictive delay risk visualization  

**Dashboard File:**  
Located in `/dashboard/Flight_Delay_Dashboard.pbix`

---

## 📌 Key Business Insights

- Departure delays strongly influence arrival delays.
- Weather and late aircraft contribute significantly to total delay minutes.
- Taxi-out time and congestion increase delay probability.
- Delay patterns vary across airlines, indicating operational performance differences.
- Predictive modeling enables proactive delay risk identification and improved passenger communication.

---

## 🚀 Future Enhancements

- Integration with real-time weather APIs  
- Advanced ensemble models for improved prediction accuracy  
- Deployment of predictive model as a web application  
- Route-level delay forecasting  

---

## 📂 Project Structure

Airline-Flight-Delay-Analysis/  
│  
├── data/  
├── notebooks/  
├── database/  
├── dashboard/  
├── requirements.txt  
└── README.md  

---

## ▶ How to Run the Project

1. Clone the repository  
2. Install required libraries:

   ```
   pip install -r requirements.txt
   ```

3. Open `notebooks/Flight_Delay_Analysis.ipynb`  
4. Run all cells  

---

## 🎯 Project Impact

This project demonstrates the complete data analytics lifecycle:

- Data Cleaning  
- Exploratory Data Analysis  
- Machine Learning Modeling  
- SQL Integration  
- Business Insights Generation  
- Interactive Dashboard Creation  

The analysis highlights how data-driven strategies can reduce operational inefficiencies and improve airline performance.
