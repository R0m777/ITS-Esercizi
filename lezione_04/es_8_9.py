'''Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.'''


def show_message(text_message:list) -> list:
    for message in text_message:
        print(message)
    
text_message:list = ["Ciao",
                      "Come Stai?",
                      "Che fai?"]
show_message(text_message)