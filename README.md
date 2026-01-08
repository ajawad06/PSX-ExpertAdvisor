# 🤖 PSX ExpertAdvisor: An Intelligent Trading System

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![Market](https://img.shields.io/badge/Market-PSX-green.svg)](https://www.psx.com.pk/)


**PSX ExpertAdvisor** is a rule-based expert system providing explainable, logic-driven investment recommendations for the **Pakistan Stock Exchange**. By encoding financial heuristics into a computational engine, it analyzes market data to categorize stocks as Buy, Sell, or Hold, offering a transparent and professional alternative to "black-box" models.

> **Course:** Artificial Intelligence

---

## 🚀 Key Features
*   **Real-time Data Integration:** Fetches historical and live ticker data using the `yfinance` API.
*   **Knowledge-Based Engine:** Uses a robust rule-set including Moving Average Crossovers, RSI (Relative Strength Index), and Volume Analysis.
*   **Interactive Dashboard:** A modern UI built with a Python-based Streamlit backend and a clean frontend interface.
*   **Explainable AI (XAI):** Every recommendation is accompanied by the specific logic/rule that triggered it, ensuring transparency for the user.

---

## 🧠 AI Methodology: Expert System
This project implements a **Knowledge-Based System (KBS)**, a branch of Artificial Intelligence that mimics the decision-making ability of a human expert. The AI logic is divided into:

1.  **Fact Base:** Current market price, trading volume, and calculated technical indicators.
2.  **Rule Base:** A collection of "IF-THEN" statements derived from technical analysis strategies.
3.  **Inference Engine:** The core logic that matches current market "Facts" against the "Rules" to generate actionable insights.

---

## 🛠️ Tech Stack
### Backend
*   **Language:** Python
*   **Framework:** Flask
*   **Data Analysis:** pandas, numpy
*   **Market Data:** yfinance (Yahoo Finance API)
*   **Web Scraping & Feeds:** beautifulsoup4, feedparser, requests
### Frontend
* **Core:** Vanilla JavaScript (ES6+), HTML5, CSS3
* **Data Visualization:** Chart.js with chartjs-chart-financial for candlestick charts
* **Networking:** Axios for API communication
  
---

## 💻 Installation & Setup

### Prerequisites
*   Python 3.10 or higher installed.
*   Git installed.

### 1. Clone the Repository
```bash
git clone https://github.com/ajawad06/PSX-IntelliTrade.git
cd PSX-IntelliTrade
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# Activate on Windows:
.\venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```
