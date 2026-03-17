# AI Market Analyzer - India

A high-performance FastAPI service that provides real-time market analysis for various sectors in the Indian economy. The system uses a hybrid AI approach (Gemini 1.5 & DeepSeek R1) combined with live web search to deliver structured, data-driven reports.

![Market Insights UI](https://via.placeholder.com/800x400.png?text=Market+Insights+India+Dashboard)

## 🚀 Features

- **Real-time Data**: Scrapes the latest 2024-2025 news and trends specifically for the Indian market.
- **Hybrid AI Engine**: Primary analysis via **Google Gemini 1.5 Flash** with an automatic fallback to **DeepSeek R1** (via OpenRouter) for 100% uptime.
- **Premium UI**: A sleek, dark-themed dashboard with glassmorphism aesthetics.
- **Async Architecture**: Fully asynchronous data pipeline for low-latency responses.
- **Security**: Built-in rate limiting (SlowAPI) and sanitization to protect against abuse.
- **Developer Friendly**: Structured folder organization, easy-to-read reports, and PDF/Markdown export ready.

## 🛠️ Tech Stack

- **Backend**: FastAPI, Pydantic, HTTPX, BeautifulSoup4
- **AI**: Google Generative AI (Gemini), OpenRouter (DeepSeek)
- **Frontend**: Vanilla HTML5, CSS3 (Modern Flexbox/Grid), JavaScript (ES6+)
- **Documentation**: Swagger UI / ReDoc

## 📦 Project Structure

```text
├── backend/            # FastAPI Application
│   ├── app/
│   │   ├── api/        # Endpoints & Routing
│   │   ├── core/       # Config, Security, Rate Limiting
│   │   └── services/   # Scraper & AI Analyzer Logic
│   ├── main.py         # Application Entry & Static Serving
│   └── requirements.txt
├── frontend/           # UI Implementation
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md
```

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.9+
- API Keys for Google Gemini or OpenRouter

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/yugendrasai-ui/Ai-market-analyzer.git
cd Ai-market-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the `backend/` directory:
```env
GEMINI_API_KEY=your_gemini_key_here
OPENROUTER_API_KEY=your_openrouter_key_here
SECRET_KEY=your_random_secret_string
```

### 4. Running the Application
```bash
cd backend
uvicorn app.main:app --reload
```
The application will be available at: **http://127.0.0.1:8000**

## 🧪 API Documentation
Interative documentation is automatically generated:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 🔒 Security
- **Rate Limiting**: 5 requests per minute per IP.
- **CORS**: Configured for secure cross-origin communication.
- **Inputs**: All sector names are sanitized and URL-encoded.

---
Built as part of an Advanced Market Analysis Technical Assignment.
