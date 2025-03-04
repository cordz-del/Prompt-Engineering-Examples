import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_product_name(prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=30,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].text.strip()

# Few-shot prompt with examples
prompt = """
You are an expert at generating creative product names. Here are some examples:
Input: "A futuristic electric car"
Output: "ElectraDrive"

Input: "A sleek smartwatch with advanced health tracking"
Output: "VitaWatch"

Now, generate a creative product name for:
Input: "A portable solar-powered charger for smartphones"
Output:"""

product_name = generate_product_name(prompt)
print("Generated Product Name:", product_name)
