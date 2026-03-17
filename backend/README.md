# FastAPI Market Analysis Service

A FastAPI-based service that analyzes market sectors in India using web search (DuckDuckGo) and Google Gemini AI to provide structured trade opportunity reports.

## Features
- **Sector Analysis**: Comprehensive market reports for various sectors.
- **AI-Powered**: Uses Google Gemini Pro for intelligent data synthesis.
- **Security**: Basic authentication and rate limiting implemented.
- **Clean Architecture**: Decoupled services for scraping, analysis, and API handling.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd Assignment_Webscrap
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Create a `.env` file based on `.env.example`:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   SECRET_KEY=your_app_secret_key
   ```

4. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Usage

### Analyze Sector
`GET /analyze/{sector}`

Returns a structured markdown report for the specified sector.

## Project Structure
- `app/`: Source code
  - `api/`: Route handlers
  - `core/`: Config, security, and rate limiters
  - `services/`: Scraping and AI logic
  - `schemas/`: Data validation models
- `tests/`: Automated tests
