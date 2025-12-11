# Dockerized Python Projects

A collection of Python projects inspired by *Python Crash Course* by Eric Matthes, enhanced with Docker containerization for improved portability, longevity, and ease of deployment.

## Overview

These projects are based on exercises and projects from the Python Crash Course book, but have been modified and dockerized to demonstrate real-world DevOps practices. Each project runs in its own isolated container, ensuring consistent behavior across different systems and eliminating dependency conflicts.

## Why Docker?

The original projects have been containerized to provide:

- **Portability** - Run anywhere Docker is installed, regardless of host system configuration
- **Consistency** - Same environment every time, no "works on my machine" issues
- **Longevity** - Projects remain executable years later without dependency rot
- **Isolation** - Each project has its own dependencies without conflicts
- **Easy Setup** - No manual installation of Python packages or system dependencies

## Modifications

The code has been adapted for containerization with enhancements including:
- Docker configuration files (Dockerfile, docker-compose where applicable)
- Volume persistence for data that needs to survive container restarts
- Container-friendly configurations and file paths
- Optimized dependencies in requirements.txt

## Projects

- [**Alien Invasion**](./Alien_Invasion) - A Pygame-based space shooter game, fully containerized with display forwarding for Linux systems

*(More projects coming soon...)*

## Requirements

- Docker installed on your system
- For GUI applications: X11 server (Linux) or XQuartz (macOS)

## Credits

Projects inspired by [*Python Crash Course, 3rd Edition*](https://nostarch.com/python-crash-course-3rd-edition) by Eric Matthes. Dockerization and modifications are my own work to demonstrate containerization skills and DevOps best practices.

---

Each project folder contains its own README with specific setup instructions and technical details.
