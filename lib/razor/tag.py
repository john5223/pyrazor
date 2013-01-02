from razor import base
import urllib

class Tag(base.Resource):
	"""
	A Tag is a string label that can be applied to one or more nodes within Razor
	"""

	def __repr__(self):
		return "<Tag: %s>" % self.name

class TagManager(base.ManagerWithFind):
	"""
	Manage :class:`Tag` resources
	"""

	resource_class = Tag

	def list(self):
		"""
		Get a list of all tags

		:rtype: list of :class:`Tag`.
		"""

		return self._list("/tag", "tag")

	def get(self, uuid):
		"""
		Get a specific tag
		:param uuid: The uuid of the :class:`Tag` to get.
		:rtype: :class:`Tag`
		"""

		return self._get("/tag/%s" % base.getid(uuid), "tag")

	def create(self, name, tag):
		"""
		Creates a new tag
		:param name: The name of tag
		:param tag: The flag to match the tag to, ex: nics_4, cpus_3
		"""

		url_json = urllib.urlencode({"name": name, "tag": tag})
		return self._create("/tag?json_hash=%s" % url_json, "tag")

	def update(self, name=None, tag=None):
		"""
		Updates a existing tag

		:param name: The name of the tag
		:param tag: The flag to math the tag to. ex: nics_4, cpus_3
		"""

		json_hash = {}
		if name != None:
			json_hash['name'] = name
		if tag != None:
			json_hash['tag'] = tag

		url_json = urllib.urlencode(json_hash)
		return self._update("/tag?json_hash=%s" % url_json, "tag")

	def delete(self, uuid):
		"""
		Deletes a specific tag

		:param uuid: The uuid of the :class:`Tag' to delete.
		"""

		return self._delete("/tag/%s" % base.getid(uuid), "tag")