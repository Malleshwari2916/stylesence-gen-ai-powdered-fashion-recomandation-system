from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_style_recommendation(skin_tone):
    prompt = f"Give fashion styling tips for {skin_tone} skin tone."

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
