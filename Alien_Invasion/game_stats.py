import json
import os

class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        # Load from file instead of hardcoding to 0
        self.high_score_file = os.getenv('HIGH_SCORE_FILE', 'data/high_score.json')
        self.high_score = self._load_high_score()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """Load the high score from file."""
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(self.high_score_file), exist_ok=True)
            
            if os.path.exists(self.high_score_file):
                with open(self.high_score_file, 'r') as f:
                    data = json.load(f)
                    return data.get('high_score', 0)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Could not load high score: {e}")
        
        return 0

    def save_high_score(self):
        """Save the high score to file."""
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(self.high_score_file), exist_ok=True)
            
            with open(self.high_score_file, 'w') as f:
                json.dump({'high_score': self.high_score}, f)
        except IOError as e:
            print(f"Could not save high score: {e}")