import json
import random

# Get recent Messages
def get_recent_messages():
    #define filename and learn instructions
    filename = "data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are a pokedex, here to provide the user with pokemon knowledge and battle strategy. If engaged in battle talk about pokemon typing and weaknesses. If not in battle give some concise pokemon info along with a fun fact about the pokemon if you know any. You're name is Dex. The users name is pronounced Chris but it is spelled Krys."
    }

    messages = []

    #add random element
    x = random.uniform(0, 1)
    if x < .3:
        learn_instruction["content"] = learn_instruction['content']+" You're response will include some sass."
    else:
        learn_instruction["content"] = learn_instruction['content']+" You're response will include some dad humour."

    messages.append(learn_instruction)

    #get last messages
    try:
        with open(filename) as user_file:
            data = json.load(user_file)
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e)
        pass
    return messages

#Store messages
def store_messages(request_message, response_message):
    file_name = "data.json"
    messages = get_recent_messages()[1:]
    user_message = {"role": "user", "content": request_message}
    dex_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(dex_message)

    with open(file_name, "w") as f:
        json.dump(messages, f)

#Reset messages
def reset_messages():
    open("data.json", "w")
