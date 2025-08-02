import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_recommendation(user_profile):
    prompt = f"""
    User Profile:
    Name: {user_profile.name}
    Age: {user_profile.age}
    Health Conditions: {", ".join(user_profile.health_conditions)}
    Dietary Preferences: {", ".join(user_profile.dietary_preferences)}
    Preferred Cuisines: {", ".join(user_profile.preferred_cuisines)}
    
    Suggest a healthy meal that suits their profile.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful diet assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error generating recommendation: {str(e)}"
