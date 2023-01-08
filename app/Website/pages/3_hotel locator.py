import streamlit as st
import openai

#google maps key AIzaSyDJX3ccQ2Q5JpombdNQenUfCVELxvki2TM

openai.api_key = "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"




# Look up a place using the Google Maps Geocoding API
place = st.text_input('Enter the location of the event:')


if st.button('Look up hotels'):
    # Use the OpenAI API to generate text based on the location
    prompt = f"Find five hotels near {place}. List them on seperate lines in bullet points. State them simply and focus on being closest to the location."
    model = "text-davinci-003"
    completion = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024)
    restaurant_list = completion.choices[0].text

# Display the generated text in the app
    st.write(restaurant_list)

