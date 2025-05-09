class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Apre il file e restituisce l'oggetto file
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Chiude il file, se è stato aperto
        if self.file:
            self.file.close()
        # Se si è verificata un'eccezione, non la sopprime (ritorna False)
        return False

with FileManager('example.txt', 'w') as f:
    f.write('Hello, world!')

    