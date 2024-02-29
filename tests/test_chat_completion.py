def print_chat_completion(model, client):
    prompt="Draw your favorite animal."
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an amazing ascii art generator bot, no text just art."},
            {"role": "user", "content": prompt}
        ]
    )
    print(f'prompt> {prompt}')
    print(f'artist-{model}>\n{response.choices[0].message.content}')

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an amazing ascii art generator bot, no text just art."},
            {"role": "user", "content": prompt}
        ],
        stream=True
    )
    print(f"prompt> {prompt}")
    print(f"artist-{model}>")
    for part in response:
        if part.choices[0].finish_reason is not None:
            break
        print(part.choices[0].delta.content, end="")


def test_chat_completion_gpt4(openai_client):
    model="gpt-4-1106-preview"
    print_chat_completion(model, openai_client)

def test_chat_completion_gpt3_5(openai_client):
    model="gpt-3.5-turbo"
    print_chat_completion(model, openai_client)

def test_chat_completion_cohere(openai_client):
    model="cohere/command"
    print_chat_completion(model, openai_client)

def test_chat_completion_perp_mixtral(openai_client):
    model="perplexity/mixtral-8x7b-instruct"
    print_chat_completion(model, openai_client)

def test_chat_completion_claude(openai_client):
    model="anthropic.claude-v2"
    print_chat_completion(model, openai_client)

def test_chat_completion_gemini_pro(openai_client):
    model="gemini/gemini-pro"
    print_chat_completion(model, openai_client)
