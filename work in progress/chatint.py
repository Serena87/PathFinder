import openai

openai.api_key = "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"
print('öppnar')
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.2,
    max_tokens = 1000,
    messages = [
        {"role": "system", "content": "beskriv och förutspå framtiden för yrket, avsluta med 3 bra saker med yrket."},
        {"role": "user", "content": "maskinoperatör, fisk."}])
print('kör')
print(completion.choices[0].message.content)
print('klart')
     