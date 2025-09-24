class Pagamento:
    def __init__(self):
        self.__importo = 0.0

    def set_importo(self, importo):
        if importo >= 0:
            self.__importo = round(importo, 2)
        else:
            raise ValueError("L'importo non può essere negativo.")

    def get_importo(self):
        return self.__importo

    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.__importo:.2f}")


class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()

    def dettagliPagamento(self):
        importo = self.get_importo()
        print(f"Pagamento in contanti di: €{importo:.2f}")
        self.inPezziDa()

    def inPezziDa(self):
        importo = self.get_importo()
        pezzi = {
            500: "banconota",
            200: "banconota",
            100: "banconota",
            50: "banconota",
            20: "banconota",
            10: "banconota",
            5: "banconota",
            2: "moneta",
            1: "moneta",
            0.50: "moneta",
            0.20: "moneta",
            0.10: "moneta",
            0.05: "moneta",
            0.01: "moneta"
        }

        print(f"{importo:.2f} euro da pagare in contanti con:")
        for valore, tipo in pezzi.items():
            count = int(importo // valore)
            if count > 0:
                print(f"{count} {tipo}{'e' if count > 1 else ''} da {valore:.2f} euro")
                importo = round(importo - (count * valore), 2)


class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome, scadenza, numero):
        super().__init__()
        self.nome = nome
        self.scadenza = scadenza
        self.numero = numero

    def dettagliPagamento(self):
        print(f"Pagamento di: €{self.get_importo():.2f} effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.nome}")
        print(f"Data di scadenza: {self.scadenza}")
        print(f"Numero della carta: {self.numero}")