from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import os
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
DEV_URL = os.getenv("DEV_URL", "http://localhost:3000/")

app = FastAPI()


# if in production then serve the nuxt generated html file (presumed it exists)
if ENVIRONMENT == "prod":
    app.mount("/", StaticFiles(directory="../dashboard/dist", html=True), name="static")
# if in dev then redirect to the dev server
elif ENVIRONMENT == "dev":
    @app.get("/")
    def read_root():
        return RedirectResponse(DEV_URL)
