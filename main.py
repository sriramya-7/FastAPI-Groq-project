from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Prompt API")

# mount all our endpoints under /api
app.include_router(router, prefix="/api")
