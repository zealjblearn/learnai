def conversation(message):
    return message   

def conversationfancy():
    #return "Hi", "I'm Bharathi"
    #return "Hi, I'm Bharathi"
    yield "Hi"
    yield "I'm Bharathi"
    yield "From Chennai"
    

# message_stream = conversationfancy()
# print(next(message_stream))
# print(next(message_stream))
# print(next(message_stream))
#print(next(message_stream))

conversation = [
["Hi", "Hi"],
["How are you", "I'm fine & wat about you"],
["I'm good, Bye", "Bye"]
]

# messages = ["How are you", "I'm fine & wat about you"]
# print(messages)

# messages1, messages2 = ["How are you", "I'm fine & wat about you"]
# print(messages1)
# print(messages2)

def displayconversation(conversations):
    for msg1, msg2 in conversations:
        print("Prabhu :", msg1)
        print("Bharahi :", msg2)

# print(displayconversation(conversation))
#print(conversationfancy())

messages = []
message = { "role": "prabhu", "content": "Hi"}
messages.append(message)
message = { "role": "bharathi", "content": "Hi"}
messages.append(message)
message = { "role": "prabhu", "content": "How are you"}
messages.append(message)
message = { "role": "bharathi", "content": "Doing good"}
messages.append(message)

def display_messages(messages):
    for message in messages:
        print(f"{message.get('role')} : {message.get('content')}") #format

print(display_messages(messages))