# 🥗 NutriSmart – Food Nutrition Analyzer

NutriSmart is a web-based Food Nutrition Analyzer built using Flask that helps users analyze food nutrition, calculate health scores, compare food items, and compute BMI with daily calorie recommendations. The project integrates real nutrition data with rule-based AI logic and interactive data visualization.

---

## 📌 Project Overview

Maintaining a healthy diet requires understanding the nutritional value of foods. NutriSmart addresses this problem by providing an easy-to-use web application that analyzes food nutrition and presents insights in a clear and visual manner. The system is designed as an academic project with a clean user interface and reliable backend logic.

---

## ✨ Features

- Food Nutrition Analysis  
  - Calories, Protein, Carbohydrates, and Fat  
  - Real nutrition data with fallback support  

- Health Score Calculation  
  - AI-based score (0–100)  
  - Color-coded badges (Healthy / Moderate / Poor)  
  - Visual progress bar  

- Nutrition Visualization  
  - Interactive bar charts using Chart.js  

- BMI Calculator  
  - Calculates Body Mass Index  
  - Determines BMI category  
  - Suggests recommended daily calorie intake  

- Food Comparison  
  - Compare two food items side by side  
  - Displays nutrition values for both foods  
  - Highlights the healthier option with a verdict banner  

- Clean & Responsive UI  
  - Card-based layout  
  - User-friendly design suitable for academic evaluation  

---

## 🛠️ Technologies Used

Frontend: HTML, CSS, JavaScript  
Backend: Python, Flask  
Data Visualization: Chart.js  
API Integration: USDA FoodData Central API  
Environment Management: python-dotenv  

---

## 📂 Project Structure

NutriSmart/
│
├── app.py  
├── src/  
│   ├── main.py  
│   └── ai_model.py  
│
├── templates/  
│   └── index.html  
│
├── static/  
│   └── style.css  
│
├── data/  
│   └── foods.json  
│
├── .env  
└── requirements.txt  

---

## ⚙️ Installation & Setup

1. Clone the repository  
git clone https://github.com/your-username/NutriSmart.git  
cd NutriSmart  

2. Create virtual environment (optional but recommended)  
python -m venv venv  
source venv/bin/activate  
(On Windows: venv\Scripts\activate)  

3. Install dependencies  
pip install -r requirements.txt  

4. Set up environment variables  
Create a .env file and add:  
USDA_API_KEY=your_api_key_here  

5. Run the application  
python app.py  

6. Open in browser  
http://127.0.0.1:5000  

---

## 🧠 How It Works

The system first checks a local food dataset.  
If data is unavailable, it fetches nutrition data from the USDA API.  
A fallback mechanism ensures results are always returned.  
Health scores are calculated using rule-based AI logic.  
Charts and UI components display results visually.

---

## 🎓 Academic Use

This project is suitable for:  
- Mini projects  
- Final year projects  
- Flask-based web application demonstrations  
- AI & data-driven system examples  

---

## 🚀 Future Enhancements

- User authentication  
- Personalized diet planning  
- Disease-specific diet recommendations  
- PDF export of nutrition reports  
- Mobile-first responsive design  

---

## 👨‍💻 Author

NutriSmart – Food Nutrition Analyzer  
Developed as an academic project using Flask and Python.

---

## 📜 License

This project is intended for educational purposes only.
