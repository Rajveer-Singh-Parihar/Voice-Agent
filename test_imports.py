print("Testing LiveKit imports...")

try:
    from livekit.agents import Agent
    print("✅ Agent import successful")
except Exception as e:
    print(f"❌ Agent import failed: {e}")

try:
    from livekit.agents.llm import LLM
    print("✅ LLM import successful")
except Exception as e:
    print(f"❌ LLM import failed: {e}")

try:
    from livekit.agents.stt import STT
    print("✅ STT import successful")
except Exception as e:
    print(f"❌ STT import failed: {e}")

try:
    from livekit.agents.tts import TTS
    print("✅ TTS import successful")
except Exception as e:
    print(f"❌ TTS import failed: {e}")

try:
    from livekit.agents.vad import VAD
    print("✅ VAD import successful")
except Exception as e:
    print(f"❌ VAD import failed: {e}")

print("\nAll imports tested!")
