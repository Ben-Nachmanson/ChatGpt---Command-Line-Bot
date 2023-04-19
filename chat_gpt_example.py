import openai
import os

openai.api_key = "INSERT_API_KEY_HERE"

def chat_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the ChatGPT command line bot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        prompt = f"User: {user_input}\nAI:"
        response = chat_gpt(prompt)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
