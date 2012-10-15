from razor import base

class ActiveModel(base.Resource):
	"""
	A active model is a model that is currently bound to a node
	"""

	def __repr__(self):
		return "<Active Model: %s>" % self.name

	def delete(self):
		"""
		Delete this active model
		"""
		self.manager.delete(self)

class ActiveModelManager(base.ManagerWithFind):
	"""
	Manage :class:`ActiveModel` resources
	"""

	resource_class = ActiveModel

	def list(self):
		"""
		Get a list of all models

		:rtype: list of :class:`ActiveModel`.
		"""

		return self._list("/active_model", "active_model")

	def get(self, uuid):
		"""
		Get a specific active model instance
		:param uuid: The uuid of the :class:`ActiveModel` to get.
		:rtype: :class:`ActiveModel`
		"""

		return self._get("/active_model/%s" % base.getid(uuid), "active_model")

	def delete(self, uuid):
		"""
		Deletes a specific active model

		:param uuid: The uuid of the :class:`ActiveModel' to delete.
		"""

		return self._delete("/active_model/%s" % base.getid(uuid), "active_model")
