import openai

openai.api_key = "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"
print('öppnar')
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.2,
    max_tokens = 1000,
    messages = [
        {"role": "system", "content": "Du är en yrkesvägledare, beskriv yrket och förutspå framtiden för yrket."},
        {"role": "user", "content": "frisör."}])
print('kör')
print(completion.choices[0].message.content)
print('klart')
     