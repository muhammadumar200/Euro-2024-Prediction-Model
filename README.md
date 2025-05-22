# ⚽ Euro 2024 Prediction Model

This project is a machine learning-based prediction model built to forecast match outcomes of the UEFA Euro 2024 football tournament. It uses historical match data and a Poisson regression model to predict the number of goals each team is likely to score and progress further in the tournament.

---

## 🚀 Project Motivation

As a Computer Science undergraduate passionate about Artificial Intelligence, I developed this project to apply foundational AI and data science techniques in a real-world sports context. This was my first AI-based project, and I took the initiative to learn key tools and concepts to build it from scratch.

---

## 🧠 Technologies & Libraries Used

- **Python 3**
- **Jupyter Notebook**
- **pandas** – data preprocessing & manipulation
- **NumPy** – numerical operations
- **scikit-learn** – Poisson Regression model
- **BeautifulSoup** – web scraping match data

---

## 📂 Project Structure

<pre> EuroPredictionModel/ 
├── euro_2024_fixtures.csv # Group stage fixtures for Euro 2024
├── euro_historical_data.csv # Historical match data from previous Euro tournaments
├── clean_euro_cup_fixtures.csv # Euro 2024 fixtures
├── clean_euro_cup_matches.csv # Euro cup Historical data 
├── HistoricalData.py # Python script for extracting the historical data and EURO 2024 fixtures
├── Euro_data_cleaning.ipynb # Jupyter Notebook with data cleaning for historical data. 
├── get_euro_groupstage_tables.ipynb # Jupyter Notebook with tranforming the data to the dict format and cleaning the fixtures dataset. 
├── Euro_Prediction_2024.ipynb # Jupyter Notebook with full pipeline and predictions
├── .gitignore # Git ignore rules 
└── README.md # Project overview (you are here) </pre>


---

## 📊 Data Collection

- **Historical Data**: Extracted manually using Beautiful Soap from Wikipedia
- **Euro 2024 Fixtures**: Gathered manually and saved in CSV format for prediction.

---

## 🧮 Model Approach

- Cleaned and engineered features like goals, home/away teams,Attack Strengths, Defence Strengths and year.
- Trained a **Poisson Regression model** using historical goal-scoring patterns.
- Predicted the expected number of goals each team would score in a given fixture.
- Used those predictions to simulate match results.

---

## ✅ Features Implemented

- [x] Web scraping using BeautifulSoup 
- [x] Feature engineering on historical match data
- [x] Poisson Regression model training
- [x] Fixture prediction for Euro 2024 group stage
- [x] Fixture prediction for Euro 2024 Knockout stage

---

## 💡 Future Improvements

- Incorporate more advanced models (e.g. XGBoost, Deep Learning)
- Include player statistics, team ratings, or form data
- Deploy predictions as a web app using Streamlit or Flask

---

## 🎓 Learning Outcomes

- Improved my skills in:
  - Data cleaning & preprocessing
  - Regression modeling
  - Handling real-world datasets
  - Using Git and GitHub for project version control
- Gained confidence in applying AI in real-life scenarios

---

## 📬 Contact

**Muhammad Umar**  
- 📧 [Insert your email here]  
- 🔗 [LinkedIn Profile](https://www.linkedin.com/in/muhammad-umar-mu2004/)  
- 💻 [GitHub Profile](https://github.com/muhammadumar200/)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

