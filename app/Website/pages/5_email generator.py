import streamlit as st
import openai

# Set the API key
openai.api_key = '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'

def main():
  st.title('Email Generator')

  # Create a list of options
  options = ['Head Coach, Angel Escobedo', 'Associate Head Coach, Mike Dixon', 'Assistant Coach, Riley Lefever','Volunteer Assistant Coach, Chad Red Jr.']
  weightclasses = ['125','133', '141', '149', '157', '165', '174', '184', '197', 'Heavyweight']
  # Create the dropdown menu
  coach = st.selectbox('Which Coach is writing this email? ', options)
  name = st.text_input ('Recruit name: ')
  weight = st.selectbox('Potential College Weight', weightclasses)
  grade = st.text_input ('What is his current grade level? ')
  gpa = st.text_input ('What is his gpa? ')
  hometown = st.text_input('What is his hometown? ')
  worries = st.text_input('What are his specific worries about coming to IU or college? ')
  interest_lvl = st.text_input ('How interested are we in this athlete? (High, Medium, Low) ')
  
  
  # Give prompt to AI
  prompt = ("Write an email to a prospective student athlete wrestler named "+name+" with a GPA of " +gpa+". He is currently in his "+grade+" year of high school and we have a "+interest_lvl+" interest in him coming to Indiana University to wrestle for us. We are looking to have him wrestle at "+weight+" . His hometown is "+hometown+". Write it in the name of "+coach+". With this particular recruit, he is worried or thinking specifically about "+worries+" so try to work a remedy to that in your email. Focus on making it sound like a human wrote it.")


  # Send the prompt to Chat GPT and get the response
  if prompt:
    completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,stop=None,
    temperature=0.9)
  
    response = completions.choices[0].text
  
    st.write(response)

  
  

main()





    

