from openai import OpenAI
from config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def read_prompt(filename: str) -> str:
    with open(f"prompts/{filename}", "r", encoding="utf-8") as f:
        return f.read()

def get_coffee_fortune(image_url: str, is_pro: bool) -> str:
    user_type = "PRO" if is_pro else "FREE"
    prompt = read_prompt("coffee.txt").replace("{user_type}", user_type)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content