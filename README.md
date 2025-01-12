# AI Voice Assistant

This project is an AI-powered voice assistant that listens for the wake word "JARVIS," processes user queries using OpenAI's ChatGPT, and responds using a text-to-speech engine. It includes a limit on the number of API calls to manage usage.

---

## Features

- **Wake Word Detection**: Activates the assistant when "JARVIS" is detected.
- **Speech Recognition**: Converts user speech to text using `speech_recognition`.
- **AI-Powered Responses**: Generates intelligent responses using OpenAI's GPT-3.5-turbo model.
- **Text-to-Speech**: Converts AI responses into speech with `pyttsx3`.
- **Usage Tracking**: Limits the number of API calls with configurable limits.

---

## Prerequisites

Before running the program, ensure you have the following installed:

- Python 3.7 or later
- Required Python libraries (see [Installation](#installation))

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Nezgova/AI-Assitant
    cd AI-Assitant
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create an OpenAI API key by signing up at [OpenAI](https://platform.openai.com/).

5. Replace the placeholder in the code with your API key:
    ```python
    client = OpenAI(api_key="your-api-key-here")
    ```

---

## Requirements

Save the following dependencies in a file named `requirements.txt`:

```text
speechrecognition
pyttsx3
openai
```

Install them using:
```bash
pip install -r requirements.txt
```

---

## How to Run

Run the script:
```bash
python nez-assistant.py
```

The assistant will listen for the wake word "JARVIS". Once detected, it will respond to your questions. You can ask any query, and the assistant will provide an answer and speak it back to you.

---

## Customization

1. **Wake Word**:
   Change the wake word by modifying this line in the code:
   ```python
   if text and "JARVIS" in text.upper().split():
   ```

2. **API Call Limit**:
   Adjust the API call limit by modifying the `MAX_CALLS` variable:
   ```python
   MAX_CALLS = 10
   ```

3. **Text-to-Speech Settings**:
   Customize the speech rate, volume, and voice in the `pyttsx3` setup:
   ```python
   engine.setProperty('rate', 150)  # Speed of speech
   engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[1].id)  # Use a different voice
   ```

---

## Troubleshooting

1. **Speech Recognition Issues**:
   - Ensure your microphone is connected and recognized by your system.
   - Adjust the ambient noise settings in the `listen` function:
     ```python
     recognizer.adjust_for_ambient_noise(source)
     ```

2. **OpenAI Errors**:
   - Check your API key and ensure it has not expired.
   - Verify your API usage limits on the OpenAI dashboard.

3. **Text-to-Speech Problems**:
   - Verify your `pyttsx3` installation.
   - Ensure the system has the required TTS voices installed.

---

## Acknowledgments

- OpenAI for the GPT-3.5-turbo model
- Python community for the libraries used in this project

