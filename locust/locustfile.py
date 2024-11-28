from locust import HttpUser, task, between, events
import random

class MovieAPIUser(HttpUser):
    wait_time = between(1, 2)
    
    def on_start(self):
        self.user_id = random.randint(1, 1000)
        
        self.preference = {
            "user_id": self.user_id,
            "movie_min_rating": 8.5,
            "movie_genre": "Action"
        }
        
        try:
            response = self.client.post("/preferences/", json=self.preference)
            if response.status_code == 200:
                self.preference_id = response.json()["id"]
        except Exception as e:
            print(f"Error creando preferencia: {e}")

    @task
    def get_recommendations(self):
        if hasattr(self, 'user_id'):
            self.client.get(f"/recommendations/{self.user_id}")