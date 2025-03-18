from openai import AzureOpenAI
client = AzureOpenAI(
    api_key="42c19dfbd58e4959b004e61187ae9a8e",
    api_version="2023-03-15-preview",
    azure_endpoint="https://basegpt4turbov.openai.azure.com/"
)

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
MAX_TOKENS = 15000
MODEL_NAME = "basegpt-4o-mini"
# Temperature controls the randomness of the response
# Lower values make the model more deterministic, 
# while higher values make it more creative
TEMPERATURE = 0.4

def chat_with_openai(prompt):
    response = client.chat.completions.create(
        model = MODEL_NAME,
        messages = prompt,
        max_tokens = MAX_TOKENS,
        temperature = TEMPERATURE,
        n=1,
        stop=None,
    )

    return response.choices[0].message.content

conversation = [
    {
        "role": "system",
        "content": "君はベース社員専用のチャットボットです。ここでベース株式会社は、主にシステムインテグレーション（SI）やITソリューションを提供する企業です。企業向けのシステム開発や運用、コンサルティングなどを行っており、さまざまな業界においてITを活用したビジネスの支援をしています。他に必要な情報はこのウェブサイトから取得できます: https://www.basenet.co.jp/"
    }
]

def terminalChat():
    print("ようこそ！私はベース社員専用のチャットボットです。")
    print("お手伝いできることはありますか？")

    while True:
        user_input = input("あなた: ")

        if user_input.lower() == 'exit':
            print("お疲れ様でした！")
            break

        conversation.append({"role": "user", "content": user_input})

        response = chat_with_openai(conversation)
        conversation.append({"role": "assistant", "content": response})

        print(f"ボット： {response}")

def apiChat(user_input):
    while True:
        if user_input.lower() == 'exit':
            print("お疲れ様でした！")
            break

        conversation.append({"role": "user", "content": user_input})

        response = chat_with_openai(conversation)
        conversation.append({"role": "assistant", "content": response})

        return response

if __name__ == '__main__':
    terminalChat()