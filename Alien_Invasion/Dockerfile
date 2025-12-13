FROM python:3.11-slim

# Install system dependencies (cached unless this layer changes)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements.txt FIRST (before code)
# This layer is cached unless requirements.txt changes
COPY requirements.txt .

# Install Python dependencies (cached unless requirements.txt changes)
RUN pip install --no-cache-dir -r requirements.txt

# Copy game files LAST
# Code changes won't trigger dependency reinstall
COPY *.py /app/
COPY images/ /app/images/

# Create data directory
RUN mkdir -p /app/data

# Set environment variables
ENV SCREEN_WIDTH=1200 \
    SCREEN_HEIGHT=800 \
    FULLSCREEN=false \
    HIGH_SCORE_FILE=/app/data/high_score.json \
    SDL_VIDEODRIVER=x11 \
    DISPLAY=:0

CMD ["python", "alien_invasion.py"]