import select
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db, Movie, UserPreference, init_database
from sqlalchemy import select
import logging
from datetime import datetime

app = FastAPI()

# Cache in memory
recommendations_cache = {}

log_filename = f"log_{datetime.now().strftime('%d_%m_%Y')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.on_event("startup")
async def startup_event():
    init_database()

@app.get("/")
async def root():
    return {
        "message": "Examen final de Ingenieria de Software - 2024.2",
        "team": ["Kalos Lazo", "Lenin Chavez"]
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "metrics": {
            "availability": 100.0,
            "reliability": 100.0
        }
    }

@app.get("/movies/")
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        movies = db.query(Movie).offset(skip).limit(limit).all()
        logging.info("Exito en Ejecucion")
        return movies
    except Exception as e:
        logging.error("Error en Ejecucion")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/preferences/")
def create_preference(preference: dict, db: Session = Depends(get_db)):
    try:
        db_preference = UserPreference(**preference)
        db.add(db_preference)
        db.commit()
        db.refresh(db_preference)
        logging.info("Exito en Ejecucion")
        return db_preference
    except Exception as e:
        db.rollback()
        logging.error("Error en Ejecucion")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: int, db: Session = Depends(get_db)):
    try:
        # Check cache
        cache_key = f"user_{user_id}"
        if cache_key in recommendations_cache:
            logging.info("Exito en Ejecucion")
            return recommendations_cache[cache_key]

        # Get preferences
        user_pref = db.execute(
            select(UserPreference)
            .where(UserPreference.user_id == user_id)
            .limit(1)
        ).scalar_one_or_none()
        if not user_pref:
            logging.info("Exito en Ejecucion")
            return []

        # Search movies
        movies = db.query(Movie)\
            .filter(
                Movie.genre == user_pref.movie_genre,
                Movie.rating >= user_pref.movie_min_rating
            )\
            .order_by(Movie.rating.desc())\
            .limit(5)\
            .all()

        # Save to cache
        recommendations_cache[cache_key] = movies
        logging.info("Exito en Ejecucion")
        return movies
    except Exception as e:
        logging.error("Error en Ejecucion")
        return []