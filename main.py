from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from databases.db import init_db, close_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["http://localhost:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Vous pouvez spécifier les méthodes HTTP autorisées
    allow_headers=["*"],  # Vous pouvez spécifier les en-têtes autorisés
)
# Configurer la base de données au démarrage de l'application
@app.on_event("startup")
async def startup_event():
    await init_db()

# Fermer proprement la base de données à l'arrêt de l'application
@app.on_event("shutdown")
async def shutdown_event():
    await close_db()

# Importer et utiliser les routeurs pour les utilisateurs et les notes
from routes import user, note

app.include_router(note.router, prefix="/api")
app.include_router(user.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
