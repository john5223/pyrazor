__version__ = '1.0'

from razor.client import RazorApiClient
from razor.activemodel import ActiveModelManager, ActiveModel
from razor.model import ModelManager, Model

class Razor(object):
	"""
	Top-level object to access the Razor API.

	Create an instace with url and port::
		>>> razor = Razor(URL, PORT)

	Then call methods on its managers::
		>>> razor.model.list()
		...
		>>> razor.activemodels.list()
		...
	"""

	def __init__(self, url, port=8026):
		self.client = RazorApiClient(self, url, port)
		self.models = ModelManager(self)
		self.activemodels = ActiveModelManager(self)
