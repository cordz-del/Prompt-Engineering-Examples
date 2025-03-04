import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_answer(prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].text.strip()

# Chain-of-thought prompt encouraging step-by-step reasoning
prompt = """
You are a thoughtful assistant that explains its reasoning step-by-step.
Question: What is the sum of the first 10 positive integers?
Let's think step-by-step:
"""

answer = generate_answer(prompt)
print("Model's Reasoning and Answer:", answer)
