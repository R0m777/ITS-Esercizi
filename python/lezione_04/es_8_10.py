'''Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.'''

def show_message(text_message:list) -> list:
    for message in text_message:
        print(f"Show Message: {message}")
    
        

def send_message(sent_message:list) -> list:
    for message in text_message:
        sent_message.append(message)
        print(f"Send message: {message}") 
    

text_message:list = ["Ciao",
                      "Come Stai?",
                      "Che fai?"]
sent_message = []
show_message(text_message)
print("-------")
send_message(sent_message)
