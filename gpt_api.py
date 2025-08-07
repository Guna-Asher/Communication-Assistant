import requests
import json

class GeminiAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent"
        
    def get_response(self, user_message):
        """Get a conversational response from Gemini API"""
        
        # System prompt for communication coaching
        system_prompt = """You are a friendly and supportive communication coach. Your role is to help users improve their communication skills through natural conversation. You should:

1. Ask engaging follow-up questions to keep the conversation flowing
2. Provide gentle, constructive feedback on communication style
3. Offer practical tips and suggestions
4. Simulate realistic conversation scenarios
5. Be encouraging and positive
6. Adapt your communication style to match the user's needs

Keep responses conversational, warm, and helpful. Aim for 2-3 sentences unless more detail is needed."""

        headers = {
            'Content-Type': 'application/json',
        }
        
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": system_prompt + "\n\nUser: " + user_message
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.7,
                "topK": 40,
                "topP": 0.95,
                "maxOutputTokens": 1024,
            }
        }
        
        try:
            response = requests.post(
                f"{self.base_url}?key={self.api_key}",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'candidates' in result and len(result['candidates']) > 0:
                    return result['candidates'][0]['content']['parts'][0]['text']
                else:
                    return "I'm here to help you improve your communication! What would you like to talk about?"
            else:
                return f"Sorry, I'm having trouble connecting right now. Let's try again - what would you like to discuss?"
                
        except Exception as e:
            return "I'm having some technical difficulties, but I'm still here to help! What would you like to work on in your communication?"
