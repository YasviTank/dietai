import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the Gemini model (Gemini 1.5 Flash is great for speed)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_recommendation(user_profile):
    prompt = f"""
User Profile:
Name: {user_profile.name}
Age: {user_profile.age}
Health Conditions: {", ".join(user_profile.health_conditions)}
Dietary Preferences: {", ".join(user_profile.dietary_preferences)}
Preferred Cuisines: {", ".join(user_profile.preferred_cuisines)}
"""

    if hasattr(user_profile, "allergies") and user_profile.allergies:
        prompt += f"Allergies: {', '.join(user_profile.allergies)}\n"

    if hasattr(user_profile, "avoid_foods") and user_profile.avoid_foods:
        prompt += f"Foods to Avoid: {', '.join(user_profile.avoid_foods)}\n"

    prompt += """

Only generate meals for the selected Meal Types provided above — no others.
    
For each meal, follow **this exact format** and nothing else:

## <Meal Type> Meal — <Meal Name>
Explanation:
<short paragraph>

Ingredients:
<each ingredient on a new line>

Instructions:
<step-by-step on new lines or numbered>

Nutrition Highlights:
<new lines or bullets>

Note:
<tips or suggestions>

⚠️ Don't include extra summaries or "Meal" lines. Start each block with ## and label sections exactly as above.
"""


    results = []

    for meal_type in user_profile.meal_types:
        meal_prompt = prompt + f"\nNow suggest a healthy {meal_type} meal that suits their profile.\n"
        try:
            response = model.generate_content(meal_prompt)
            results.append(f"## {meal_type} Meal\n\n" + response.text.strip())
        except Exception as e:
            results.append(f"## {meal_type} Meal\n\nError generating recommendation: {str(e)}")

    return "\n\n".join(results)