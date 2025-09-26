from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SavvyFinance API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "SavvyFinance API Running!"}

@app.get("/api/health")
async def health():
    return {"status": "healthy"}

@app.post("/api/auth/login")
async def login(credentials: dict):
    if credentials.get("email") == "hello@savvyfinance.com":
        return {
            "access_token": "demo_token",
            "user": {"email": "hello@savvyfinance.com", "role": "admin"}
        }
    return {"error": "Invalid credentials"}
