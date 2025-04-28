'''Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, 
print both of your lists to show that the original list has retained its messages.'''

def send_message(message:list):
    for itemes in message:
        return message

message=["hello","ciao", "world"]
message1 = []
message1.extend(message)
message1.sort()
print(f"lista1: {message}")
print(f"lista2: {message1}")
