import g4f

import random 

import asyncio

PROVIDERS_LIST = [
    g4f.Provider.ChatBase,
    g4f.Provider.Aura,
    g4f.Provider.GeminiProChat,
    g4f.Provider.You
]

# chat gpt 3.5 turbo
async def make_promt_gpt_3_5(text_prompt: str):

    try:
        response = await request_chat_gpt_3_5(text_prompt)
        return response
    except:
        response = await request_chat_gpt_3_5(text_prompt, provider=random.choice(PROVIDERS_LIST))
        return response


async def request_chat_gpt_3_5(text_prompt: str, provider=g4f.Provider.Aura):
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_35_turbo,
        messages=[{
            "role": "user",
            "content": f"{text_prompt}"
        }],
        provider=provider
    )
    return response




# async def main():
    
#     print(await make_promt_gpt_3_5("Сколько раз турция воевала с россией?"))



# asyncio.run(main())























