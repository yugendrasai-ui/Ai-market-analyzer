import httpx
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def test_analyze_endpoint():
    url = "http://127.0.0.1:8000/api/v1/analyze/pharmaceuticals"
    print(f"Testing endpoint: {url}")
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.get(url)
            print(f"Status Code: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"Sector: {data['sector']}")
                print("\n--- Report Preview ---\n")
                print(data['report_markdown'][:500] + "...")
            else:
                print(f"Error: {response.text}")
        except Exception as e:
            print(f"Connection failed: {e}")

if __name__ == "__main__":
    # Note: Requires the server to be running in another process
    # asyncio.run(test_analyze_endpoint())
    print("Verification script ready. Run the server first using: uvicorn app.main:app --reload")
