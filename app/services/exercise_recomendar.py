import openai
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")
openai.api_key = os.getenv("openapi_apikey")



def get_chatgpt_response(sex, age, height, weight, hypertension, diabetes, injuries, body_fat, primary_fitness_goal, preferred_fitness_type, experience_level, Days, gym_access, available_equipment, workout_duration):
    prompt= f"Act as a professional Coach, \
    Generate a Workout plan for \
    Basic Profile: A {sex} , {age} years of age, {height} cm tall, Weighs {weight} kg\
    Hypertension : {hypertension}, Diabetes : {diabetes}, Injuries: {injuries}\
    Body Metrics : {body_fat} \
    Primary Fitness Goal:{primary_fitness_goal}, Preferred Fitness Type: {preferred_fitness_type}, Experience Level: {experience_level}, Days per Week You Can Train: {Days} \
    Access to a gym: {gym_access}, Available equipment: {available_equipment} Preferred workout duration per session: {workout_duration}"
    try:
        # Send a request to the OpenAI API with the model, prompt, and max tokens
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify model name (e.g., "gpt-3.5-turbo" or "gpt-4")
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # Optional system prompt
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # Set token limit for response length
            temperature=0.7  # Adjust the creativity level (0.0 to 1.0)
        )

        # Extract and return the assistant's reply from the response
        return response.choices[0].message["content"]

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
