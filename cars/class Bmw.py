class Bmw:
	def __init__(self):
		self.models = ['i8', 'x1', 'x5', 'x6']

	def outModels(self):
		print('These are the models available in BMW')
		for model in self.models:
			print('\t%s', %model)