import logging 
import os
from dotenv import load_dotenv
_ = load_dotenv(override = True)

logger = logging.getLogger("dial-agent")
logger.setLevel(logging.INFO)

from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions
from livekit.agents.llm import LLM
from livekit.agents.stt import STT
from livekit.agents.tts import TTS
from livekit.agents.vad import VAD

# Import API keys from config
from config import OPENAI_API_KEY, ELEVENLABS_API_KEY

# Set environment variables from config
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["ELEVENLABS_API_KEY"] = ELEVENLABS_API_KEY

class Assistant(Agent):
    def __init__(self) -> None:
        print("✅ API Keys configured:")
        print(f"   • OpenAI: {'✅ Set' if OPENAI_API_KEY else '❌ Missing'}")
        print(f"   • ElevenLabs: {'✅ Set' if ELEVENLABS_API_KEY else '❌ Missing'}")
        
        # Initialize the components with proper configuration
        llm = LLM()  # This will use OpenAI with the configured API key
        stt = STT()  # This will use default configuration
        tts = TTS()  # This will use ElevenLabs with the configured API key
        vad = VAD()  # This will use default configuration

        super().__init__(
            instructions = """
            You are a helpful AI assistant communicating via voice. 
            Be conversational, friendly, and provide accurate information.
            Keep responses concise and natural for voice interaction.
            """,
            stt = stt,
            llm = llm,
            tts = tts,
            vad = vad,
        )

async def entrypoint(ctx: JobContext):
    await ctx.connect()

    session = AgentSession()

    await session.start(
        room = ctx.room,
        agent = Assistant()
    )

def check_environment():
    """Check if all required environment variables are set"""
    required_vars = {
        "OPENAI_API_KEY": "OpenAI API key for language model",
        "ELEVENLABS_API_KEY": "ElevenLabs API key for text-to-speech",
        "LIVEKIT_URL": "LiveKit server URL",
        "LIVEKIT_API_KEY": "LiveKit API key",
        "LIVEKIT_API_SECRET": "LiveKit API secret"
    }
    
    missing_vars = []
    for var, description in required_vars.items():
        if not os.getenv(var):
            missing_vars.append(f"  - {var}: {description}")
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(var)
        print("\n📝 Update the config.py file with your LiveKit server details")
        return False
    else:
        print("✅ All required environment variables are set!")
        return True

if __name__ == "__main__":
    print("🤖 LiveKit Voice Assistant")
    print("=" * 40)
    
    # Check environment setup
    env_ok = check_environment()
    
    if env_ok:
        print("\n🚀 Ready to start voice assistant!")
        print("Available components:")
        print("- LLM: Language model for processing conversations")
        print("- STT: Speech-to-text for voice input")
        print("- TTS: Text-to-speech for voice output")
        print("- VAD: Voice activity detection")
        print("\n💡 To run the assistant, you'll need to:")
        print("1. Set up a LiveKit server or use a hosted service")
        print("2. Update config.py with your LiveKit server details")
        print("3. Run the agent with proper LiveKit configuration")
    else:
        print("\n❌ Please set up the required environment variables first.")
        print("   Update the config.py file with your LiveKit server details.")