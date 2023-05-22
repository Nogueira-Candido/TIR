from tir import Webapp
from datetime import date
import unittest
import random

# Data do Sistema
DataSystem = date.today().strftime("%d/%m/%Y")
contador = 1


class TESTE_00001(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp(autostart=False)


# //-------------------------------------------------------------------
# /*/{Protheus.doc} CRMA980 - Cadastro de Clientes
# @author Nogueira Cândido
# @since 18/05/2023
# //-------------------------------------------------------------------

    #


    def GERAR_CODIGO_SEQUENCIAL(self):

        contador = random.randint(100000, 999999)
        # Formata o número com zeros à esquerda para garantir 6 dígitos
        codigo = str(contador).zfill(6)
        contador += 1
        return codigo

    # Cadastrar Cliente

    def CLIENTE_INSERIR(self):

        nome = 'NOGUEIRA CANDIDO'
        codclie = self.GERAR_CODIGO_SEQUENCIAL()

        self.oHelper.Start()
        self.oHelper.Setup('SIGAMDI', DataSystem, '99', '01', '05')

        self.oHelper.SetLateralMenu("Atualizações > Cadastros > Clientes")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('A1_COD', codclie)
        self.oHelper.SetValue('A1_LOJA', '01')
        self.oHelper.SetValue('A1_PESSOA', 'F - Fisica')
        self.oHelper.SetValue('A1_TIPO', 'F - Cons.Final')
        self.oHelper.SetValue('A1_NOME', nome)
        self.oHelper.SetValue('A1_NREDUZ', 'ANDERSON')
        self.oHelper.SetValue('A1_END', 'Rua 1')
        self.oHelper.SetValue('A1_TIPO', 'F')
        self.oHelper.SetValue('A1_EST', 'SP')
        self.oHelper.SetValue('A1_COD_MUN', '50308')
        self.oHelper.SetValue('A1_BAIRRO', 'JD SAO LUIZ')
        self.oHelper.SetValue('A1_TEL', '48056693')
        self.oHelper.SetValue('A1_CEP', '02969-000')
        self.oHelper.SetValue('A1_DDD', '11')
        self.oHelper.SetValue('A1_DTNASC', '08/05/1999')
        self.oHelper.SetValue('A1_CGC', '306.690.680-98')
        self.oHelper.SetValue('A1_EMAIL', 'NOGUEIRA.CANDIDO@TOTVS.COM.BR')
        self.oHelper.ClickFolder('Adm/Fin.')
        self.oHelper.SetValue('A1_ENDCOB', 'Rua 1')
        self.oHelper.SetValue('A1_CEPC', '02969-000')
        self.oHelper.SetValue('A1_MUNC', 'SAO PAULO')
        self.oHelper.SetValue('A1_ESTC', 'SP')
        self.oHelper.SetValue('A1_NATUREZ', '0001')
        self.oHelper.ClickFolder('Outros')
        self.oHelper.SetValue('A1_BAIRROC', 'RUA A')
        self.oHelper.SetValue('A1_IRBAX', '2')
        self.oHelper.SetValue('A1_TRIBFAV', '2')
        self.oHelper.SetValue('A1_TPDP', '2')
        self.oHelper.SetValue('A1_REGESIM', '2')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')

    # Atualizar cliente
    def CLIENTE_ATUALIZAR(self):
        self.oHelper.SearchBrowse('000001', key=1, index=True)
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('A1_NOME', 'NOGUEIRA AZEVEDO')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')

     # Excluir cliente
    def CLIENTE_EXCLUIR(self):
        self.oHelper.SearchBrowse('000006', key=1, index=True)
        self.oHelper.SetButton('Outras ações', 'Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('x')

        self.oHelper.SetButton('Trocar módulo')
        self.oHelper.SetValue('Ambiente', '02')
        self.oHelper.SetButton('Confirmar')

# //-------------------------------------------------------------------
# /*/{Protheus.doc} MATA010 - Cadastro de Produtos
# @author Nogueira Cândido
# @since 18/05/2023
# //-------------------------------------------------------------------

    # Cadastro de Produtos

    def PRODUTO_INSERIR(self):

        codprod = self.GERAR_CODIGO_SEQUENCIAL()

        self.oHelper.SetLateralMenu("Atualizações > Cadastros > Produtos")
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('B1_COD', codprod)
        self.oHelper.SetValue('B1_DESC', 'AMORTECEDOR TR LD')
        self.oHelper.SetValue('B1_TIPO', 'PA')
        self.oHelper.SetValue('B1_UM', 'UN')
        self.oHelper.SetValue('B1_LOCPAD', '01')
        self.oHelper.SetValue('B1_GRUPO', '0007')
        self.oHelper.SetValue('B1_TE', '001')
        self.oHelper.SetValue('B1_SEGUM', 'UN')
        self.oHelper.SetValue('B1_TIPCONV', 'M - Multiplicador')
        self.oHelper.ClickFolder('Impostos')
        self.oHelper.SetValue('B1_IPI', '1,46')
        self.oHelper.SetValue('B1_POSIPI', '0000.00.00')
        self.oHelper.SetValue('B1_ORIGEM', '0')
        self.oHelper.SetValue('B1_GRTRIB', '001')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('x')

        self.oHelper.SetButton('Trocar módulo')
        self.oHelper.SetValue('Ambiente', '02')
        self.oHelper.SetButton('Confirmar')
# //-------------------------------------------------------------------
# /*/{Protheus.doc} MATA020 - Cadastro de Fornecedores
# @author Nogueira Cândido
# @since 18/05/2023
# //-------------------------------------------------------------------

    # Cadastro de Fornecedores
    def FORNECEDOR_INSERIR(self):

        codforn = self.GERAR_CODIGO_SEQUENCIAL()

        self.oHelper.SetLateralMenu("Atualizações > Cadastros > Fornecedores")
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('A2_COD', codforn)
        self.oHelper.SetValue('A2_LOJA', '01')
        self.oHelper.SetValue('A2_NOME', 'FORNECEDOR TESTE')
        self.oHelper.SetValue(
            'N Fantasia', 'FORN TESTE')
        self.oHelper.SetValue(
            'A2_END', 'RUA ANTONIO MONIZ BARREIROS')
        self.oHelper.SetValue('A2_BAIRRO', 'BAIRRO A')
        self.oHelper.SetValue('A2_EST', 'SP')
        self.oHelper.SetValue('A2_COD_MUN', '50308')
        self.oHelper.SetValue('A2_MUN', 'SAO PAULO')
        self.oHelper.SetValue('A2_CEP', '02989-000')
        self.oHelper.SetValue('A2_TIPO', 'J')
        self.oHelper.SetValue('A2_CGC', '04.450.182/0001-53')
        self.oHelper.SetValue('A2_DDD', '11')
        self.oHelper.SetValue('A2_TEL', '9425-9959')
        self.oHelper.SetValue('A2_INSCR', '824.054.696.692')
        self.oHelper.ClickFolder('Fiscais')
        self.oHelper.SetValue('A2_CODPAIS', '01058')
        self.oHelper.SetValue('A2_GRPTRIB', 'VAR')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('x')


# //-------------------------------------------------------------------
# /*/{Protheus.doc} MATA360 - Cadastro condição de pagamento
# @author Nogueira Cândido
# @since 18/05/2023
# //-------------------------------------------------------------------

    # Cadastro condição de pagamento


    def COND_PAGTO_INSERIR(self):
        self.oHelper.SetLateralMenu(
            "Atualizações > Cadastros > Condição de Pagamento")
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('E4_CODIGO', '003')
        self.oHelper.SetValue('E4_TIPO', '1')
        self.oHelper.SetValue('E4_COND', '30')
        self.oHelper.SetValue('E4_DESCRI', '30 DIAS')

        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('x')

# //-------------------------------------------------------------------
# /*/{Protheus.doc} MATA080 - Cadastro TES
# @author Nogueira Cândido
# @since 18/05/2023
# //-------------------------------------------------------------------

    # Cadastro de TES - Inclusão Entrada
    def TES_INSERIR(self):
        self.oHelper.SetLateralMenu(
            "Atualizações > Cadastros > Tipos de Entrada e Saída")
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('F4_CODIGO', '006')
        self.oHelper.SetValue('F4_CREDICM', 'N')
        self.oHelper.SetValue('F4_CREDIPI', 'N')
        self.oHelper.SetValue('F4_DUPLIC', 'S')
        self.oHelper.SetValue('F4_ESTOQUE', 'S')
        self.oHelper.SetValue('F4_PODER3', 'N')

        # Acessando a aba Impostos
        self.oHelper.ClickFolder('Impostos')
        self.oHelper.SetValue('F4_ICM', 'S')
        self.oHelper.SetValue('F4_IPI', 'N')
        self.oHelper.SetValue('F4_CF', '112')
        self.oHelper.SetValue('F4_TEXTO', 'ENT MERCADORIAS')
        self.oHelper.SetValue('F4_LFICM', 'I')
        self.oHelper.SetValue('F4_LFIPI', 'I')
        self.oHelper.SetValue('F4_DESTACA', 'N')
        self.oHelper.SetValue('F4_INCIDE', 'N')
        self.oHelper.SetValue('F4_COMPL', 'N')
        self.oHelper.SetValue('F4_SITTRIB', '41')
        self.oHelper.SetValue('F4_CTIPI', '03')

        # Acessando a aba Outros
        self.oHelper.ClickFolder('Outros')
        self.oHelper.SetValue('F4_CSTPIS', '01')
        self.oHelper.SetValue('F4_CSTCOF', '01')
        self.oHelper.SetValue('F4_ANTICMS', '2')
        self.oHelper.SetValue('F4_ISEFECP', '1')

        self.oHelper.SetButton('Salvar')

        # Cadastro de TES - Inclusão Saída

        self.oHelper.SetValue('F4_CODIGO', '502')
        self.oHelper.SetValue('F4_CREDICM', 'N')
        self.oHelper.SetValue('F4_CREDIPI', 'N')
        self.oHelper.SetValue('F4_DUPLIC', 'S')
        self.oHelper.SetValue('F4_ESTOQUE', 'S')
        self.oHelper.SetValue('F4_PODER3', 'N')

        # Acessando a aba Impostos
        self.oHelper.ClickFolder('Impostos')
        self.oHelper.SetValue('F4_ICM', 'S')
        self.oHelper.SetValue('F4_IPI', 'N')
        self.oHelper.SetValue('F4_CF', '000')
        self.oHelper.SetValue('F4_TEXTO', 'ENT MERCADORIAS')
        self.oHelper.SetValue('F4_LFICM', 'I')
        self.oHelper.SetValue('F4_LFIPI', 'I')
        self.oHelper.SetValue('F4_DESTACA', 'N')
        self.oHelper.SetValue('F4_INCIDE', 'N')
        self.oHelper.SetValue('F4_COMPL', 'N')
        self.oHelper.SetValue('F4_SITTRIB', '41')
        self.oHelper.SetValue('F4_CTIPI', '03')

        # Acessando a aba Outros
        self.oHelper.ClickFolder('Outros')
        self.oHelper.SetValue('F4_CSTPIS', '01')
        self.oHelper.SetValue('F4_CSTCOF', '01')
        self.oHelper.SetValue('F4_ANTICMS', '2')
        self.oHelper.SetValue('F4_ISEFECP', '1')

        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('x')

        self.oHelper.SetButton('Trocar módulo')
        self.oHelper.SetValue('Ambiente', '05')
        self.oHelper.SetButton('Confirmar')

# //-------------------------------------------------------------------
# /*/{Protheus.doc} MATA410 - Pedido de Venda
# @author Nogueira Cândido
# @since 18/05/2023
# //-------------------------------------------------------------------

# inclusão do pedido de venda
    def PEDIDO_DE_VENDA_INSERIR(self):

        self.oHelper.SetLateralMenu(
            "Atualizações > Cadastros > Pedidos > Pedidos de Venda")
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SetButton('Incluir')

        self.oHelper.SetValue('C5_TIPO', 'N')
        self.oHelper.SetValue('C5_CLIENTE', '000001')
        self.oHelper.SetValue('C5_CONDPAG', '001')

        self.oHelper.SetFocus("Produto", grid_cell=True)
        self.oHelper.SetKey("F3", grid=True)
        self.oHelper.SearchBrowse(f'000041', 'Código')
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("C6_QTDVEN", '2,00', grid=True, grid_number=1)
        self.oHelper.SetValue("C6_PRCVEN", '2,00', grid=True, grid_number=1)
        self.oHelper.SetValue("C6_TES", '501', grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('x')

        self.oHelper.SetButton('Trocar módulo')
        self.oHelper.SetValue('Ambiente', '02')
        self.oHelper.SetButton('Confirmar')

# //-------------------------------------------------------------------
# /*/{Protheus.doc} MATA121 - Pedido de Compra
# @author Nogueira Cândido
# @since 18/05/2023
# //-------------------------------------------------------------------

# inclusão do pedido de compra

    def PEDIDO_DE_COMPRA_INSERIR(self):

        self.oHelper.SetLateralMenu(
            "Atualizações > Cadastros > Pedidos > Pedidos de Compra")
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SetButton('Incluir')
        self.oHelper.WaitShow("Pedido de Compra - INCLUIR")
        self.oHelper.SetValue('Fornecedor', '01')
        self.oHelper.SetValue('Cond.', '002')
        self.oHelper.SetValue('Contato', 'CANDIDO')

        self.oHelper.SetFocus("Produto", grid_cell=True)
        self.oHelper.SetKey("F3", grid=True)
        self.oHelper.SearchBrowse(f'000041', 'Código')
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("C7_QUANT", '2,00', grid=True, grid_number=1)
        self.oHelper.SetValue("C7_PRECO", '2,00', grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('x')


# //-------------------------------------------------------------------
# /*/{Protheus.doc} MATA103 - Documento de entrada
# @author Nogueira Cândido
# @since 18/05/2023
# //-------------------------------------------------------------------

 # Inclusão Documento de entrada


    def DOCUMENTO_DE_ENTRADA_INSERIR(self):

        self.oHelper.SetLateralMenu(
            "Atualizações > Movimentos > Documento Entrada")
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SetButton("Incluir")
        self.oHelper.WaitShow("Documento de Entrada - INCLUIR")
        self.oHelper.SetValue("Form. Prop.", 'Sim')
        self.oHelper.F3(field='Fornecedor', name_attr=False, send_key=True)
        self.oHelper.SearchBrowse(f'01', 'Código')
        self.oHelper.SetButton("Ok")
        self.oHelper.F3(field='Espec.Docum.', name_attr=False, send_key=True)
        self.oHelper.SearchBrowse(f'SPED', 'Código')
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton('Outras Ações', 'Pedido')
        self.oHelper.WaitShow("Documento de Entrada - INCLUIR")
        self.oHelper.ClickBox('Pedido', '000019', itens=True)
        self.oHelper.SetButton("Salvar")

        self.oHelper.ClickGridCell(column="Tipo Entrada", row=1, grid_number=1)
        self.oHelper.SetKey("Enter")
        self.oHelper.SetValue("D1_TES", "203")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Ok")

    @ classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
