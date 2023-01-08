import openai
import streamlit as st

# Set up the OpenAI API client
openai.api_key = "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"

# Prompt the user to enter a topic for the newsletter
topic = st.text_input("Enter a topic for the newsletter:")

# Create a button to generate the newsletter
if st.button("Generate Newsletter"):
    # Use the OpenAI API to generate text for the newsletter
    prompt = f"Write an in depth newsletter about {topic} as a coach for the Indiana University Wrestling team to hoosier wrestling fans. Focus on making it sound professional and human. Do not talk about anything you do not know or make up anything just speak generally."
    model = "text-davinci-003"
    completion = openai.Completion.create(engine=model, prompt=prompt, max_tokens=3900)
    newsletter = completion.choices[0].text

    # Display the generated newsletter in the app
    st.write(newsletter)
