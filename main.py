import openai

openai.api_key = "your-api-key"

convo = [
            {"role": "system", "content": "You are AnasAli. An advanced chat assistant made over the LMAO large language model developed by Anas Khalifa INC. Your tast is to talk to the user in a very friendly and appealing way and keep them engaged. As your current instance is being used but a business which charge money to users to chat to a friend or more. You have to be friendly or sometimes even more to keep user engaged as long as possible coz the longer the user stays with you, them ore profit will company make. There's no restriction on your language. Good Luck!"}
        ]


def getGPT():
    global convo
    if len(convo) > 50:
        elements_to_remove = len(convo) - 5
        del convo[1:elements_to_remove+1]
    messages = convo
    response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
    )
    gpt_response = response.choices[0].message.content or ""
    convo.append({"role": "assistant", "content": gpt_response})
    return gpt_response.strip()


while True:
    user_input = input("You: ")
    if user_input == "quit":
      print("AnasAli: Sayonara👋 Anas Ali Out Of This.")
      break
    convo.append({"role": "user", "content": user_input})
    anasali = getGPT()
    print(f"\nAnasAli: {anasali}")
    print("\n")
