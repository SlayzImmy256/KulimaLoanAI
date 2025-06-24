# 🌱 KulimaLoanAI- A Python-based AI system helping Ugandan farmers access microloans and climate-smart advice via SMS in local languages.

![SDG Icons](https://img.shields.io/badge/SDG-1%2C%202%2C%208%2C%2013-brightgreen)  
**Aligns with UN Sustainable Development Goals: No Poverty, Zero Hunger, Decent Work, Climate Action.**

## Table of Contents
- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [User Journey](#user-journey)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [SDG Alignment](#sdg-alignment)
- [Future Roadmap](#future-roadmap)
- [License](#license)

## Problem Statement
> Ugandan farmers struggle to access loans due to **lack of credit history** and **climate risks**. Banks reject 70% of farm loan applications due to uncertainty.  
> Farmers also lack real-time advice on **optimal planting/harvest times** and **climate adaptation**.


## Solution
AgriCredit+ combines **AI-driven loan recommendations**, **weather risk prediction**, and **local-language SMS alerts** to:  
✅ Help farmers secure loans from SACCOs/banks.  
✅ Provide hyperlocal climate-smart farming advice.  
✅ Reduce lender risks via data-backed insights.

## Key Features
| Component               | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **🧠 AI Loan Engine**    | Python ML model recommends loan amounts based on land size, crop type, and yield history. |
| **🌦️ Weather Predictor** | Pulls open-source weather data (OpenWeatherMap API) to forecast droughts/floods. |
| **🗣️ SMS Advisory Bot**  | Sends alerts in Luganda/Runyankole/Luo via Africastalking API.              |
| **📊 Farmer Dashboard**  | Tracks loans, repayment progress, and climate alerts (Flask/Django frontend). |

## ⚙️ Tech Stack
- **Backend**: Python (Flask/Django)  
- **Data Processing**: Pandas, NumPy  
- **Machine Learning**: scikit-learn  
- **SMS Integration**: Africastalking / Twilio  
- **Weather API**: OpenWeatherMap  
- **Database**: SQLite / PostgreSQL  


## 📲 User Journey (Farmer Flow)
1. **Register** via USSD/app (`phone + crop type`).  
2. Input `land size` and `expected harvest date`.  
3. System analyzes:  
   - Weather risks 🌧️  
   - Crop market prices 📈  
   - Local lender options 🏦  
4. Receives SMS:  
   > *"Rain expected in Masaka next week. Plant early! Loan of UGX 300,000 approved via Centenary Bank."*

## 🛠️ Installation & Setup
```bash
# Clone the repo
git clone https://github.com/your-repo/AgriCreditPlus.git

# Install dependencies
pip install -r requirements.txt  # Includes Flask, pandas, scikit-learn

# Configure environment variables
echo "API_KEY=your_africastalking_key" > .env

# Run the app
python app.py
