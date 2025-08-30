import logging 
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
_ = load_dotenv(override = True)

logger = logging.getLogger("web-voice-assistant")
logger.setLevel(logging.INFO)

# Import API keys from config
from config import OPENAI_API_KEY, ELEVENLABS_API_KEY

# Set environment variables from config
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["ELEVENLABS_API_KEY"] = ELEVENLABS_API_KEY

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('voice_assistant.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        # Simple response for now (you can integrate with OpenAI here)
        response = f"Hello! I received your message: '{user_message}'. This is your voice assistant responding!"
        
        return jsonify({
            'success': True,
            'response': response,
            'message': 'Voice assistant is working!'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/status')
def status():
    return jsonify({
        'status': 'running',
        'openai_configured': bool(OPENAI_API_KEY),
        'elevenlabs_configured': bool(ELEVENLABS_API_KEY),
        'message': 'Voice Assistant is ready!'
    })

if __name__ == '__main__':
    print("🎯 Starting Web Voice Assistant...")
    print("=" * 50)
    print("✅ API Keys Status:")
    print(f"   • OpenAI: {'✅ Configured' if OPENAI_API_KEY else '❌ Missing'}")
    print(f"   • ElevenLabs: {'✅ Configured' if ELEVENLABS_API_KEY else '❌ Missing'}")
    print("\n🌐 Access your voice assistant at:")
    print("   http://localhost:5000")
    print("\n📱 You can also access it from other devices on your network:")
    print("   http://[your-ip-address]:5000")
    print("\n🚀 Starting server...")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
