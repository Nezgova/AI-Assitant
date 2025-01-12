import speech_recognition as sr
import pyttsx3
from openai import OpenAI  # Import the new OpenAI client

# Initialize SpeechRecognition for voice input
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize the OpenAI client
client = OpenAI(api_key="your-api-key-here")  # Replace with your API key

# Track the number of API calls or tokens used
MAX_CALLS = 10  # Set your limit here
remaining_calls = MAX_CALLS

# Function to generate AI response using ChatGPT
def generate_response(prompt):
    global remaining_calls
    if remaining_calls <= 0:
        return "You have no remaining chances. Please reset the counter."

    try:
        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use ChatGPT model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50  # Limit the response length
        )

        # Extract the generated text
        generated_text = response.choices[0].message.content

        # Decrease the remaining calls
        remaining_calls -= 1
        return generated_text
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."

# Function to listen to user voice input
def listen():
    with sr.Microphone() as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except Exception as e:
            print("Sorry, I couldn't understand.")
            return None

# Function to speak the AI's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to detect the wake word "JARVIS"
def detect_wake_word():
    print("Listening for 'JARVIS'...")
    text = listen()
    if text and "JARVIS" in text.upper().split():  # Check for "JARVIS" as a separate word
        print("Wake word detected!")
        return True
    return False

# Main loop
print("AI Assistant is running. Say 'JARVIS' to activate...")

while True:
    # Wait for the wake word "JARVIS"
    if detect_wake_word():
        print("How can I help you?")
        speak("How can I help you?")

        # Listen for the user's question
        question = listen()
        if question and len(question.split()) > 1:  # Ensure the question is complete
            # Generate and speak the AI's response
            response = generate_response(question)
            print(f"AI: {response}")
            speak(response)

            # Display remaining chances
            print(f"Remaining chances: {remaining_calls}")
            if remaining_calls <= 3:
                speak(f"You have {remaining_calls} chances left.")
        else:
            print("Please ask a complete question.")
            speak("Please ask a complete question.")