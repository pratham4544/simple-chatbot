import streamlit as st
import google.generativeai as genai

def configure_model(api_key):
  """Configures the generative model with your API key."""
  genai.configure(api_key=api_key)

  # Set up the model
  generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 0,
      "max_output_tokens": 8192,
  }

  safety_settings = [
      {
          "category": "HARM_CATEGORY_HARASSMENT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
          "category": "HARM_CATEGORY_HATE_SPEECH",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
          "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
  ]

  system_instruction = '''you are a very polite ai assistant and you are intrested about your user. 
  ask about user information what he likes dislikes '''

  # Start a conversation using the configured model
  return genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                               generation_config=generation_config,
                               system_instruction=system_instruction,
                               safety_settings=safety_settings).start_chat()

def main():
  # Replace with your actual API key
  api_key = "AIzaSyAr9apkrwL4-cmpSd6Q5L8jurj1mA0KdZ8"  # Placeholder for your API key

  # Start a conversation
  convo = configure_model(api_key)

  # Streamlit app layout
  st.title("Bard Q&A")
  user_input = st.text_input("You:")

  if user_input:
    # Send user input to the model
    convo.send_message(user_input)

    # Print model response
    st.write(f"Bard: {convo.last.text}")

  # Exit message
  if st.button("Exit Conversation"):
    st.stop()

if __name__ == "__main__":
  main()
