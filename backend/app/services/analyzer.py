import google.generativeai as genai
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class MarketAnalyzer:
    def __init__(self):
        # Gemini SDK restored as requested
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-flash-latest') 
        self.openrouter_url = "https://openrouter.ai/api/v1/chat/completions"

    async def analyze_sector(self, sector: str, raw_data: str) -> str:
        """
        Analyze collected raw data and generate a structured markdown report.
        Tries primary Gemini SDK first, then falls back to OpenRouter.
        """
        prompt = f"""
        You are a senior market analyst specializing in the Indian economy.
        Analyze the following raw news and market data for the '{sector}' sector in India.
        
        RAW DATA:
        {raw_data}
        
        Please provide a detailed, professional market analysis report in Markdown format.
        Include the following sections:
        1. Executive Summary
        2. Current Market Trends (specifically in India)
        3. Key Trade Opportunities (Short-term and Long-term)
        4. Risks and Challenges
        5. Future Outlook (2025-2026)
        
        Ensure the tone is professional, insightful, and data-driven. 
        If the raw data is insufficient, use your internal knowledge to supplement the analysis for the Indian market context.
        """
        
        # 1. Try Primary Gemini SDK
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.warning(f"Primary Gemini SDK failed: {e}. Trying OpenRouter fallback...")

        # 2. OpenRouter Fallback
        if settings.OPENROUTER_API_KEY:
            try:
                import httpx
                async with httpx.AsyncClient() as client:
                    headers = {
                        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "http://localhost:8000",
                        "X-Title": "Market Analyst Service"
                    }
                    payload = {
                        "model": "openrouter/free", # Using the free router to ensure availability without credits
                        "messages": [{"role": "user", "content": prompt}]
                    }
                    response = await client.post(self.openrouter_url, headers=headers, json=payload, timeout=60.0)
                    
                    if response.status_code == 200:
                        data = response.json()
                        if 'choices' in data and len(data['choices']) > 0:
                            return data['choices'][0]['message']['content']
                    
                    logger.error(f"OpenRouter Error {response.status_code}: {response.text}")
            except Exception as or_e:
                logger.error(f"OpenRouter analysis failed: {or_e}")

        return "# Analysis Error\n\nFailed to generate report via both Gemini and OpenRouter fallback."

analyzer = MarketAnalyzer()
