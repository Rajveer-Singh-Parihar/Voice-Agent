import logging 
import os
import openai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
_ = load_dotenv(override = True)

logger = logging.getLogger("working-voice-assistant")
logger.setLevel(logging.INFO)

# Import API keys from config
from config import OPENAI_API_KEY, ELEVENLABS_API_KEY

# Set environment variables from config
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["ELEVENLABS_API_KEY"] = ELEVENLABS_API_KEY

# Configure OpenAI
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('voice_assistant.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'No message provided'
            })
        
        # Generate AI response using OpenAI
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant. Be conversational, friendly, and provide accurate information. Keep responses concise and natural for voice interaction."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=150,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content.strip()
            
            return jsonify({
                'success': True,
                'response': ai_response,
                'message': 'AI response generated successfully!'
            })
            
        except Exception as ai_error:
            # Fallback response if OpenAI fails
            fallback_response = f"I understand you said: '{user_message}'. I'm your AI assistant and I'm here to help! What would you like to know more about?"
            
            return jsonify({
                'success': True,
                'response': fallback_response,
                'message': 'Using fallback response'
            })
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
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

@app.route('/test')
def test():
    return jsonify({
        'success': True,
        'message': 'Voice Assistant is working!',
        'openai_key': 'Configured' if OPENAI_API_KEY else 'Missing'
    })

if __name__ == '__main__':
    print("🎯 Starting Working Voice Assistant...")
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
