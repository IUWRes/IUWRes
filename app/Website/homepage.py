import streamlit as st
import openai
import time
import getpass

st.set_page_config(
      page_title="Indiana Wrestling Admin",
      page_icon="wrestlers"
    )

password = "Hoosiers"

input_text = st.text_input("Please Enter the Password:")

if input_text == password:
    st.write("Access granted.")
    # Add content to the page here
    

    st.title("Indiana Wrestling Virtual Assistant")
    st.sidebar.success("Select a page above.")
    st.image('https://scontent-ord5-1.xx.fbcdn.net/v/t39.30808-6/324552622_700654058334663_4904241222776850418_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=tLTpH75M7LsAX9MIXHu&_nc_ht=scontent-ord5-1.xx&oh=00_AfB5GV9kXJ3O6j9zQ81FIDrp6IY6HV6qfMqNeCQRTW2S8A&oe=63BFB218')


    openai.api_key = "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"

    st.markdown(
        """
        <style>
        h1 {
          font-family: 'Georgia';
          font-size: 35px;
          color: crimson;
        }
    
    
        """,
        unsafe_allow_html=True,
    )


    def generate_quote():
      prompt = (
          "Generate a motivational quote:\n"
          "Motivational quotes are short phrases or sentences that provide inspiration, encouragement, or guidance to help people achieve their goals and live happier, more fulfilling lives. They can be about any topic, including success, love, friendship, perseverance, and more.\n"
          "Examples:\n"
          "- "
          "Believe you can and you're halfway there. -Theodore Roosevelt\n"
          "- "
          "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. As with all matters of the heart, you'll know when you find it. -Steve Jobs\n"
          "- "
          "Don't let yesterday take up too much of today. -Will Rogers"
          "Try to make a different quote every time and focus it on achieving greatness and stuff like that."
      )
  
      completions = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=400,
          n=1,
          stop=None,
          temperature=0.9,
      )

      message = completions.choices[0].text
      return message


    quote = generate_quote()
    st.write(quote)

    st.title('Check Ins:')


    tasks = [
        "Prep work for next competition",
        "Strength Training - Coach Dustin",
        "Coordinate with RTC",
        "Weight Checks",
        "Individual Meetings",
    ]

    st.markdown("- " + "\n- ".join(tasks))


else:
    st.write(" ")




