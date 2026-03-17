from fastapi import APIRouter, Depends, HTTPException, Query
from app.services.scraper import scraper
from app.services.analyzer import analyzer
from app.core.security import get_current_user
from app.core.rate_limit import limiter
from fastapi import Request

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,
    sector: str,
    # current_user: str = Depends(get_current_user) # Uncomment for mandatory auth
):
    """
    Accepts a sector name and returns a structured market analysis report.
    """
    try:
        # Step 1: Collect Data
        clean_sector = sector.strip()
        raw_data = await scraper.search_sector_news(clean_sector)
        
        # Step 2: Analyze Data
        report = await analyzer.analyze_sector(clean_sector, raw_data)
        
        return {
            "sector": sector,
            "report_markdown": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
