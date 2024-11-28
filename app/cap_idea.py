from functools import lru_cache
from database import Movie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# cache para disponibilidad
recommendations_cache = {}
preferences_cache = {}

# mas conexiones !!
DATABASES = {
    'primary': 'sqlite:///./primary.db',
    'secondary': 'sqlite:///./secondary.db'
}

engines = {name: create_engine(url) for name, url in DATABASES.items()}
sessions = {name: sessionmaker(bind=engine) for name, engine in engines.items()}

def get_recommendations(user_id: int):
    # guardar en cache
    if user_id in recommendations_cache:
        return recommendations_cache[user_id]
    
    # insertar en bd - priorizamos orden
    for db_name in ['primary', 'secondary']:
        try:
            db = sessions[db_name]()
            recommendations = db.query(Movie).limit(5).all()
            recommendations_cache[user_id] = recommendations
            return recommendations
        except:
            continue
    
    # si todo falla, gg se pasa lo de cache
    return cached_recommendations.get(user_id, [])