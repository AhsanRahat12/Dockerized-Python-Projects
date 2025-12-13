# Alien Invasion - Dockerized

A containerized version of the Alien Invasion game from "Python Crash Course" by Eric Matthes, demonstrating real-world Docker deployment with persistent data storage.

## 🎮 Features

- **Docker Containerized** - Consistent runtime across any Linux system
- **Persistent High Scores** - Scores saved to JSON file, survive container restarts
- **Configurable Display** - Environment variables for screen resolution and fullscreen mode
- **Optimized Build** - Minimal image size (~150-200MB) with layer caching
- **Cross-Platform** - Works on any Linux distribution with Docker

## 📋 Prerequisites

- Docker and Docker Compose
- X11 display server (pre-installed on most Linux distros)
- `xorg-xhost` package for X11 access control

### Installation - Arch Linux
```bash
sudo pacman -S docker docker-compose xorg-xhost
sudo systemctl start docker
```

### Installation - Ubuntu/Debian
```bash
sudo apt update
sudo apt install docker.io docker-compose x11-xserver-utils
sudo systemctl start docker
```

## 🚀 Quick Start
```bash
# Clone the repository
git clone https://github.com/AhsanRahat12/Dockerized-Python-Projects.git
cd Dockerized-Python-Projects/Alien_Invasion

# Enable X11 access for Docker
xhost +local:docker

# Run the game
sudo docker compose up
```

## 🎯 Usage

### Running the Game
```bash
# Enable X11 access (once per session)
xhost +local:docker

# Start the game
sudo docker compose up

# Stop with Q key in-game or Ctrl+C in terminal
```

### Controls

- **Arrow Keys** - Move ship left/right
- **Spacebar** - Fire bullets
- **Q** - Quit game (saves high score)

### Viewing High Scores
```bash
# High scores saved in data/high_score.json
cat data/high_score.json
```

## ⚙️ Configuration

Environment variables can be modified in `docker-compose.yml`:
```yaml
environment:
  - FULLSCREEN=true          # Enable/disable fullscreen mode
  - SCREEN_WIDTH=1200        # Window width (if fullscreen=false)
  - SCREEN_HEIGHT=800        # Window height (if fullscreen=false)
  - HIGH_SCORE_FILE=/app/data/high_score.json
```

## 📁 Project Structure
```
Alien_Invasion/
├── alien_invasion.py      # Main game loop (modified)
├── game_stats.py          # Game statistics with JSON persistence (modified)
├── scoreboard.py          # Score display with auto-save (modified)
├── settings.py            # Game settings with env vars (modified)
├── alien.py               # Alien sprite
├── bullet.py              # Bullet sprite
├── button.py              # UI button
├── ship.py                # Player ship
├── images/                # Game assets
│   ├── alien.bmp
│   └── ship.bmp
├── Dockerfile             # Container definition
├── docker-compose.yml     # Service orchestration
├── requirements.txt       # Python dependencies
├── .dockerignore          # Build optimization
└── data/                  # Persistent storage (auto-created)
    └── high_score.json
```

## 🐳 Docker Details

### Image Optimization

- **Base:** `python:3.11-slim` for minimal size
- **Runtime libraries only:** No development packages
- **Layer caching:** Dependencies cached separately from code
- **Final size:** ~150-200MB

### Build Process
```bash
# Build the image
sudo docker compose build

# Rebuild without cache
sudo docker compose build --no-cache
```

### Data Persistence

High scores persist via Docker volume mount:
```yaml
volumes:
  - ./data:/app/data
```

Data survives container restarts and rebuilds.

## 🔒 Security Considerations

### Running as Root

This container currently runs as root for simplicity and to avoid X11 permission issues with the display. 

**Why this is acceptable for this project:**
- Local-only execution (not exposed to internet)
- No sensitive data processing
- Educational/portfolio project
- Simplified X11 display access

**For production deployments**, consider:
- Running as non-root user
- Implementing proper user permissions
- Using security scanning tools
- Following Docker security best practices

### Production Hardening

If deploying this as a web service or multi-user environment, implement:
```dockerfile
# Create non-root user
RUN useradd -m -u 1000 gameuser && \
    chown -R gameuser:gameuser /app

# Switch to non-root
USER gameuser
```

## 🔧 Development

### Modifying the Game

1. Edit Python files locally
2. Rebuild the image: `sudo docker compose build`
3. Run to test: `sudo docker compose up`

### Running Without Docker

The code works natively with Python:
```bash
pip install pygame
python alien_invasion.py
```

All Docker modifications are backward-compatible.

## 🌐 Cross-Platform Notes

### Linux (Full Support)

Works on all major distributions:
- Arch Linux ✅
- Ubuntu/Debian ✅  
- Fedora ✅
- OpenSUSE ✅

### Windows

**Option 1: WSL2 (Recommended)**
```bash
# Install WSL2 and Docker Desktop
# Then run in WSL2 Ubuntu terminal
git clone <repo>
docker compose up
```

**Option 2: Native Python**
```bash
pip install pygame
python alien_invasion.py
```

### macOS

Requires XQuartz for X11 support:
```bash
brew install xquartz
# Configure XQuartz, then use docker compose
```

## 🐛 Troubleshooting

### "cannot open display" Error
```bash
# Enable X11 access
xhost +local:docker
```

### "Docker daemon not running"
```bash
# Start Docker service
sudo systemctl start docker
```

### "permission denied" on Docker Socket
```bash
# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Or use sudo
sudo docker compose up
```

### High Score Not Saving

Verify volume mount in `docker-compose.yml`:
```yaml
volumes:
  - ./data:/app/data
```

Check file was created:
```bash
ls -la data/
cat data/high_score.json
```

### Game Runs Too Fast (Windowed Mode)

Use fullscreen mode for proper frame rate:
```yaml
environment:
  - FULLSCREEN=true
```

## 📝 Technical Implementation

### Code Modifications

**Minimal changes to original game code:**
- `game_stats.py`: Added JSON persistence (~30 lines)
- `scoreboard.py`: Added auto-save trigger (1 line)
- `settings.py`: Added environment variable support (4 lines)
- `alien_invasion.py`: Added display mode selection (~15 lines)

**Total:** ~50 lines of code added/modified

### Docker Optimizations

1. **Layer Caching** - Dependencies installed before code copy
2. **Runtime Libraries** - No dev packages (~50% size reduction)
3. **Build Context** - `.dockerignore` excludes unnecessary files
4. **No Cache Flag** - `pip install --no-cache-dir`

### Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `DISPLAY` | X11 display target | From host |
| `FULLSCREEN` | Enable fullscreen | `true` |
| `SCREEN_WIDTH` | Window width | `1200` |
| `SCREEN_HEIGHT` | Window height | `800` |
| `HIGH_SCORE_FILE` | Save location | `/app/data/high_score.json` |

## 📚 Learning Objectives

This project demonstrates:

- ✅ Docker containerization of GUI applications
- ✅ X11 display forwarding in containers
- ✅ Volume mounts for data persistence
- ✅ Environment variable configuration
- ✅ Multi-stage Docker optimization
- ✅ Backward-compatible code modifications

## 🙏 Credits

- **Original Game:** Eric Matthes - [Python Crash Course, 3rd Edition](https://nostarch.com/python-crash-course-3rd-edition)
- **Docker Implementation:** Rahat (AhsanRahat12)

## 📄 License

Educational project based on "Python Crash Course" by Eric Matthes.

## 🔗 Related Projects

Part of the [Dockerized-Python-Projects](https://github.com/AhsanRahat12/Dockerized-Python-Projects) repository - a collection of Python projects containerized for learning Docker deployment.

---

**Portfolio Project** - Demonstrating Docker containerization skills through practical application.
