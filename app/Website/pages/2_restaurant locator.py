import streamlit as st
import openai

openai.api_key = "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"


# Prompt the user to enter a location
location = st.text_input("Enter location of event:")

# Use the OpenAI API to generate text based on the location
if st.button('Look up restaurants'):
    prompt = f"Find restaurants near {location}. Give multiple options for breakfast, lunch, and dinner. For breakfast focus on finding a type of breakfast diner. For lunch find a chipotle, qdoba, or something similar. For dinner find an outback steakhouse or something similar. Seperate them by meal and list each resturant in bullet points."
    model = "text-davinci-003"
    completion = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024)
    restaurant_list = completion.choices[0].text

# Display the generated text in the app
    st.write(restaurant_list)
