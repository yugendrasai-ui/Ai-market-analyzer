from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.v1.endpoints import router as api_router
from app.core.rate_limit import init_rate_limiting
import os
import logging

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Market Analysis Service",
    description="Analyze market sectors in India using AI and Web Search",
    version="1.0.0"
)

# Initialize Rate Limiting
init_rate_limiting(app)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Router
app.include_router(api_router, prefix="/api/v1")

# Serve Frontend Static Files
# Get the absolute path to the project root (one level up from 'backend')
current_dir = os.path.dirname(os.path.abspath(__file__)) # backend/app
project_root = os.path.dirname(os.path.dirname(current_dir)) # f:/Assignment_Webscrap
frontend_path = os.path.join(project_root, "frontend")

if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
else:
    # Log a warning if frontend is missing
    logger.warning(f"Frontend path not found at: {frontend_path}")

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
