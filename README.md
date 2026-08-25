# 💼 Employee Salary Prediction

### 🤖 Machine Learning Web Application

> Predict an employee's estimated salary based on their years of professional experience.

---

## 🌟 About the Project

**Employee Salary Prediction** is a Machine Learning project that predicts an employee's salary based on their years of experience.

The project uses **Linear Regression** and integrates the trained model with a **Flask web application**, allowing users to enter their experience and instantly receive a salary prediction.

---

## ✨ Features

- 📊 Salary prediction based on experience
- 🤖 Linear Regression Machine Learning model
- 📈 Model evaluation using MAE and R² Score
- 🌐 Flask-based web application
- 🎨 Modern and responsive user interface
- ⚡ Real-time salary prediction
- 💾 Trained model saved using Joblib

---

## 🧠 Machine Learning Workflow

```text
        📂 Dataset
           │
           ▼
     📊 Data Loading
           │
           ▼
    ✂️ Train/Test Split
           │
           ▼
   🤖 Linear Regression
           │
           ▼
     📈 Model Evaluation
           │
           ▼
       💾 model.pkl
           │
           ▼
     🌐 Flask Web App
           │
           ▼
     💰 Salary Prediction

📊 Dataset

The dataset contains 25 employee records with two main attributes:

Feature	Description
YearsExperience	Years of professional experience
Salary	Employee salary
🤖 Machine Learning Model
Linear Regression

Linear Regression is used to learn the relationship between:

Years of Experience → Salary

The model is trained using 80% of the data and tested on the remaining 20%.

📈 Model Performance
Metric	Result
Mean Absolute Error	6010.94
R² Score	0.93
🎯 R² Score

An R² score of approximately 0.93 means that the model explains around 93% of the variation in the test data.

🌐 Web Application

The trained Machine Learning model is integrated with Flask.

Users can:

Enter their years of experience.
Click Predict My Salary.
Get the estimated annual salary.
🔄 Application Flow
👤 User Input
     ↓
🌐 Flask
     ↓
🤖 Trained ML Model
     ↓
💰 Salary Prediction
     ↓
🖥️ Result Displayed
🛠️ Technologies Used
Technology	Purpose
🐍 Python	Programming
🐼 Pandas	Data handling
🤖 Scikit-learn	Machine Learning
📐 Linear Regression	Prediction
🌐 Flask	Web application
🎨 HTML & CSS	Frontend
💾 Joblib	Model saving/loading
📁 Project Structure
Employee_Salary_Prediction/
│
├── 📄 app.py
├── 📄 train_model.py
├── 📄 Salary_Data.csv
├── 📦 model.pkl
├── 📖 README.md
│
├── 📂 templates/
│   └── 📄 index.html
│
└── 📂 static/
    └── 🎨 style.css
🚀 How to Run
1️⃣ Install Required Libraries
pip install pandas scikit-learn flask joblib
2️⃣ Train the Model
python train_model.py

This will train the model and generate:

model.pkl
3️⃣ Start Flask Application
python app.py
4️⃣ Open in Browser
http://127.0.0.1:5000
🎨 Project Preview

The application provides a clean interface where users can enter their experience and receive an estimated salary.

💡 What I Learned

Through this project, I learned:

Data loading and handling using Pandas
Train/Test splitting
Linear Regression
Model evaluation
Saving and loading ML models
Flask integration
Connecting Machine Learning with a web interface
Basic frontend development
👨‍💻 Author
Lokpal Singh Solanki

💻 Python | Machine Learning | Flask

⭐ If you found this project useful, feel free to star the repository!
