# LiveKit Voice Assistant Practice

This is a practice project for creating a voice assistant using LiveKit agents.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Variables
Create a `.env` file in the Practice directory with the following variables:

```
# LiveKit Configuration
LIVEKIT_URL=wss://your-livekit-server.com
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key

# ElevenLabs Configuration
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

### 3. Required API Keys
- **LiveKit**: You need a LiveKit server instance and API credentials
- **OpenAI**: Get an API key from https://platform.openai.com/
- **ElevenLabs**: Get an API key from https://elevenlabs.io/

### 4. Running the Application
```bash
python practice.py
```

## Issues Fixed
- Fixed `logger.setLive()` to `logger.setLevel()`
- Fixed import syntax errors
- Added proper main execution block
- Created requirements.txt with necessary dependencies

## Note
This is a basic setup. You'll need to configure your LiveKit server and obtain the necessary API keys for the voice assistant to work properly.
