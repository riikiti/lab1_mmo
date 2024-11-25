# Base image
FROM python:3.10-slim

# Install dependencies for Tkinter and Xvfb
RUN apt-get update && \
    apt-get install -y python3-tk libx11-6 tk8.6-dev tcl8.6-dev libxrender1 libxtst6 libxi6 xvfb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files
COPY app/ /app/
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set display environment variable
ENV DISPLAY=:99

# Clean stale lock and start Xvfb, then run the application
CMD ["sh", "-c", "rm -f /tmp/.X99-lock && Xvfb :99 -screen 0 1024x768x16 & python3 app.py"]
