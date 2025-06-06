class ContactManager:
    def __init__(self, contacts:dict[str,list[str]]):
        self.contacts = contacts

    def create_contact(self,name:str, phone_numbers:list[str])->dict:
        if name is self.contacts:
            return "Errore: il contatto esiste già."
        else:
            self.contacts[name] = phone_numbers
        return self.contacts
    
    def add_phone_number(self, contact_name:str, phone_number:str)->dict:
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste." 
        if phone_number is self.contacts[contact_name]:
            return "Errore: il numero di telefono esiste già."
        else:
            self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number(self, contact_name:str, phone_number:str) ->dict:
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        if phone_number not in self.contacts[contact_name]:
            return "Errore: il numero di telefono non è presente."
        else:
            self.contacts[contact_name].remove(phone_number)
        return {contact_name:self.contacts[contact_name]}

    def update_phone_number(self,contact_name:str, old_phone_number:str, new_phone_number:str)->dict:
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."  
        if old_phone_number not in self.contacts[contact_name]:
            return "Errore: il numero di telefono non è presente."
        else:
            update_numbers = []
            for number in self.contacts[contact_name]:
                if number == old_phone_number:
                    update_numbers.append(new_phone_number)
                else:
                    update_numbers.append(number)
        self.contacts[contact_name] = update_numbers
        return {contact_name: update_numbers}
    
    def list_contacts(self) -> list[str]:
        return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name:str)-> list[str] | str:
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        return self.contacts[contact_name]
    
    def search_contact_by_phone_number(self,phone_number:str) -> list[str] | str:
        result = []
        for name in self.contacts:
            if phone_number in self.contacts[name]:
                result.append(name)
        
        if not result:
            return "Nessun contatto trovato con questo numero di telefono."
        
        return result
