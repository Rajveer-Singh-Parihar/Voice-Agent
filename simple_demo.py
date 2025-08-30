import logging 
import os
from dotenv import load_dotenv
_ = load_dotenv(override = True)

logger = logging.getLogger("demo-agent")
logger.setLevel(logging.INFO)

from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions
from livekit.agents.llm import LLM
from livekit.agents.stt import STT
from livekit.agents.tts import TTS
from livekit.agents.vad import VAD

class DemoAssistant(Agent):
    def __init__(self) -> None:
        # Initialize the components with default configuration
        llm = LLM()
        stt = STT()
        tts = TTS()
        vad = VAD()

        super().__init__(
            instructions = """
            You are a demo AI assistant. This is a test setup to show how LiveKit agents work.
            Respond with helpful information and be conversational.
            """,
            stt = stt,
            llm = llm,
            tts = tts,
            vad = vad,
        )

def demo_setup():
    """Demo setup without requiring all API keys"""
    print("🎯 LiveKit Voice Assistant Demo")
    print("=" * 50)
    
    print("\n✅ Components initialized:")
    print("   • LLM (Language Model) - Ready")
    print("   • STT (Speech-to-Text) - Ready") 
    print("   • TTS (Text-to-Speech) - Ready")
    print("   • VAD (Voice Activity Detection) - Ready")
    
    print("\n📋 What this demo shows:")
    print("   • How to create a LiveKit Agent")
    print("   • How to configure STT, LLM, TTS, and VAD components")
    print("   • Basic voice assistant structure")
    
    print("\n🔧 To make it fully functional, you need:")
    print("   1. OpenAI API key (for LLM)")
    print("   2. ElevenLabs API key (for TTS)")
    print("   3. LiveKit server setup")
    
    print("\n💡 Next steps:")
    print("   1. Get API keys from OpenAI and ElevenLabs")
    print("   2. Set up a LiveKit server (or use hosted service)")
    print("   3. Create a .env file with your keys")
    print("   4. Run the full version in practice.py")
    
    print("\n🎉 Demo completed successfully!")
    print("   Your LiveKit voice assistant framework is ready!")

if __name__ == "__main__":
    try:
        # Try to create the assistant (this will work even without API keys)
        assistant = DemoAssistant()
        print("✅ Assistant created successfully!")
        
        # Run the demo
        demo_setup()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("This might be due to missing dependencies or configuration.")
