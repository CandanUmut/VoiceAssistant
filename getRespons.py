
import openai
import pyttsx3
openai.api_key = "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"

def get_response_from_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n = 1,
        stop=None,
        temperature=0.5,

    )
    text = response["choices"][0]["text"]
    return text