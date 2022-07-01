from classes import *

if __name__ == '__main__':
    testInvoice = Invoice(descricao='none')
    num = testInvoice.set_numeroItem()
    descricao = testInvoice.set_descricaoItem()
    qtde = testInvoice.set_quantidade()
    preco = testInvoice.set_preco()
    fatura = testInvoice.getInvoiceAmount(qtde,preco)

    print("-------------------------------\nFatura\n")
    print(f'Produto: {descricao}\nQuantidade do pedido:{qtde}\n'
          f'Preço Unitário:{preco}\n---------------------------\n'
          f'Total da fatura: R${fatura}\n---------------------------')