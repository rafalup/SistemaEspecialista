from random import *
class Pergunta:
	def __init__(self):
		self.level = [
			['Voce esta vendo o imovel?', 'imovel'],
		    ['Imovel localiza em zona urbana?','zonaurbana'],
		    #['Imovel localiza em zona rural?','zonarural'],
		    ['O Acabamento do imovel é de alvenaria?','alvenaria'],
		    #['O Acabamento do imovel é de Madeira?','madeira'],	
		    ['Imovel se encontra na posicao de esquina?','esquina'],
		    #['Imovel se encontra na posicao dentro da quadra?','quadra'],
		    #['Documentacao do imovel está em dias?','documentsimovel'],
		    ['Está quitado o imovel?','quitadoImovel'],
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string

