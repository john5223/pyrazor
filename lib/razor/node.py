from razor import base

class Node(base.Resource):
	"""
	A Node is an available hardware + software configuration for a server
	"""

	def __repr__(self):
		return "<Node: %s>" % self.name

class NodeManager(base.ManagerWithFind):
	"""
	Manage :class:`Node` resources
	"""

	resource_class = Node

	def list(self):
		"""
		Get a list of all nodes
		
		:rtype: list of :class:`Node`.
		"""
		return self._list("/node", "node")

	def get(self, uuid):
		"""
		Get a specific node.

		:param node: The uuid of the :class:`Node` to get.
		:rtype: :class:`Node`
		"""
		return self._get("/node/%s" % base.getid(uuid), "node")