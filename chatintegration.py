import openai

# use your own API
openai.api_key = "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"

def get_description(yrke):
    print('matching job..')
    completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.2,
    max_tokens = 1000,
    messages = [
        {"role": "system", "content": "Du är en yrkesvägledare, beskriv yrket och förutspå framtiden för yrket."},
        {"role": "user", "content": yrke}])
    return(completion.choices[0].message.content)

#print(completion.choices[0].message.content)

#yrke = 'arborist'
 

#get_description(yrke)