import httpx
from bs4 import BeautifulSoup
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class MarketScraper:
    def __init__(self):
        self.base_search_url = "https://duckduckgo.com/html/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    async def search_sector_news(self, sector: str) -> str:
        """
        Search for current news and data for a specific sector in India.
        """
        query = f"current market trends and trade opportunities in {sector} sector India 2024 2025"
        params = {"q": query}
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.base_search_url, params=params, headers=self.headers)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, "html.parser")
                results = soup.find_all("div", class_="result__body")
                
                collected_text = []
                for res in results[:5]: # Get top 5 results
                    title = res.find("a", class_="result__a")
                    snippet = res.find("a", class_="result__snippet")
                    if title and snippet:
                        collected_text.append(f"Title: {title.get_text()}\nSnippet: {snippet.get_text()}\n")
                
                if not collected_text:
                    return "No recent news found for this sector."
                    
                return "\n".join(collected_text)
        except Exception as e:
            logger.error(f"Error scraping data: {e}")
            return f"Error collecting data for {sector}: {str(e)}"

scraper = MarketScraper()
