import unittest

from TESTE_00001 import TESTE_00001


suite = unittest.TestSuite()

suite.addTest(TESTE_00001('CLIENTE_INSERIR'))
suite.addTest(TESTE_00001('CLIENTE_ATUALIZAR'))
suite.addTest(TESTE_00001('CLIENTE_EXCLUIR'))
suite.addTest(TESTE_00001('PRODUTO_INSERIR'))
suite.addTest(TESTE_00001('FORNECEDOR_INSERIR'))
suite.addTest(TESTE_00001('COND_PAGTO_INSERIR'))
suite.addTest(TESTE_00001('TES_INSERIR'))
suite.addTest(TESTE_00001('PEDIDO_DE_VENDA_INSERIR'))
suite.addTest(TESTE_00001('PEDIDO_DE_COMPRA_INSERIR'))
suite.addTest(TESTE_00001('DOCUMENTO_DE_ENTRADA_INSERIR'))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
