
class Invoice:
    def __init__(self, descricao):
      self.numeroItem = 0
      self.descricaoItem = descricao
      self.quantidade = 0
      self.preco = 0


    def set_numeroItem(self):
        numeroItem = int(input("Insira o número do item: "))
        return numeroItem

    def set_descricaoItem(self):
        descricaoItem = input("Insira a descrição do item: ")
        return descricaoItem

    def set_quantidade(self):
        quantidade =int(input("Insira a quantidade do pedido: "))
        return quantidade

    def set_preco(self):
        preco = float(input("Insira o preço unitário do produto: "))
        return preco
      
    def getInvoiceAmount (self, quantidade, preco):
        total = preco * quantidade
        return total