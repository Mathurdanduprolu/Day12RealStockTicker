# Day12RealStockTicker — Django Real-Time Stock Ticker (Alpha Vantage)

A simple **Django web app** that lets you enter a stock ticker (like `AAPL`, `TSLA`) and fetches the **latest quote** using the **Alpha Vantage** API (`GLOBAL_QUOTE`).

---

## ✨ Features

- Search any stock symbol (e.g., `AAPL`, `MSFT`, `NVDA`)
- Shows:
  - Current price
  - Change + change percent
  - Latest trading day (last updated)
- Basic Django template UI (`base.html` + `tracker.html`)
- Uses Alpha Vantage `GLOBAL_QUOTE` endpoint

---

## 🧱 Tech Stack

- Python
- Django
- Requests (HTTP client)
- Alpha Vantage API

---

## 📁 Project Structure (Important Paths)

```
myproject/
  static/
    css/style.css
  templates/
    base.html
  stock_tracker/stock_tracker/
    manage.py
    stock_project/
      settings.py
      urls.py
    tracker/
      views.py
      urls.py
      templates/tracker/tracker.html
```

---

## ✅ Prerequisites

- Python 3.10+ (works with newer Python too)
- Django installed
- Alpha Vantage API key (free)

---

## 🔑 Get an Alpha Vantage API Key

1. Create/get your free API key from Alpha Vantage.
2. Put it into your Django settings.

In your project, API key is currently configured here:

`myproject/stock_tracker/stock_tracker/stock_project/settings.py`

```py
ALPHA_VANTAGE_API_KEY = "your_api_key_here"
```

---

## 🚀 Setup & Run Locally

### 1) Clone the repo
```bash
git clone https://github.com/Mathurdanduprolu/Day12RealStockTicker.git
cd Day12RealStockTicker
```

### 2) Create & activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
```

### 3) Install dependencies
If you don’t have a `requirements.txt` yet, install directly:
```bash
pip install django requests
```

(Optional) You can generate a requirements file:
```bash
pip freeze > requirements.txt
```

### 4) Run migrations
Go to the folder that contains `manage.py`:

```bash
cd myproject/stock_tracker/stock_tracker
python manage.py migrate
```

### 5) Start the server
```bash
python manage.py runserver
```

Open:
- http://127.0.0.1:8000/

---

## 🧪 How to Use

1. Open the homepage
2. Enter a stock symbol (example: `TSLA`)
3. Submit
4. You’ll see quote details like:
   - Price
   - Change (%)
   - Latest trading day

---

## 🛠️ Notes / Improvements (Optional)

If you want to make this more production-ready:
- Move `ALPHA_VANTAGE_API_KEY` to an environment variable (instead of hardcoding)
- Add a `requirements.txt`
- Add better UI form layout + error messages (invalid symbol / API limit)
- Add caching (Alpha Vantage has rate limits)
- Handle API errors gracefully (timeouts, empty quotes)

---

## 📌 Alpha Vantage Rate Limits

Alpha Vantage free tier has rate limits (commonly 5 requests/minute and 500/day).
If you hit limits, you may see empty responses until the limit resets.

---

## 📄 License

This project is open for learning and personal use.  
(If you want, add an MIT License file.)

---

## 👤 Author

**Mathur Danduprolu**  
GitHub: https://github.com/Mathurdanduprolu