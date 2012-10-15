from razorapi import base
from urllib import quote_plus

class Model(base.Resource):
	"""
	A Model is an available hardware + software configuration for a server
	"""

	def __repr__(self):
		return "<Model: %s>" % self.name

class ModelManager(base.ManagerWithFind):
	"""
	Manage :class:`Model` resources
	"""

	resource_class = Model

	def list(self):
		"""
		Get a list of all models
		
		:rtype: list of :class:`Model`.
		"""
		return self._list("/model", "model")

	def get(self, uuid):
		"""
		Get a specific model.

		:param model: The uuid of the :class:`Model` to get.
		:rtype: :class:`Model`
		"""
		return self._get("/model/%s" % base.getid(uuid), "model")

	def templates(self):
		"""
		Get a list of templates

		:rtype: list of :class:`Model`
		"""
		return self.get("/model/templates", "model")

	def create(self, label, image_uuid, template, hostname_prefix, domain_name, root_password):
		"""
		Creates a new model instance

		:param label: Label to give to the new model (ex. 'Test Model')
		:param image_uuid: UUID to give to the new model (ex. 'OTP')
		:param template: Template label to give to the new model (ex. 'ubuntu_precise')
		:param hostname_prefix: Prefix for the hostname (ex. 'test')
		:param domain_name: Domain for host (ex. 'testdomain.com')
		:param root_password: Default root password for host (ex. 'test4321')

		Refer to the CLI / API documentation for Razor for more information
		"""
		
		body = {'label': label, 'image_uuid': image_uuid, 'template': template,
		        'req_metadata_hash': {
		        	'hostname_prefix': hostname_prefix,
		        	'domainname': domain_name,
		        	'root_password': root_password
		        	}
	        	}

    	return self._create("/model?json_hash=%s" % quote_plus(json.dumps(body), body, "model")

	def update(self, uuid, label, image_uuid, hostname_prefix, domain_name, root_password):
		"""
		Updates an existing model instance

		:param label: Label to give to the new model (ex. 'Test Model')
		:param image_uuid: UUID to give to the new model (ex. 'OTP')
		:param hostname_prefix: Prefix for the hostname (ex. 'test')
		:param domain_name: Domain for host (ex. 'testdomain.com')
		:param root_password: Default root password for host (ex. 'test4321')

		Refer to the CLI / API documentation for Razor for more information
		"""

		body = {'label': label, 'image_uuid': image_uuid,
		        'req_metadata_hash': {
		        	'hostname_prefix': hostname_prefix,
		        	'domainname': domain_name,
		        	'root_password': root_password
		        	}
	        	}

    	return self._update("/model/%s?json_hash=%s" % (base.getid(uuid), quote_plus(json.dumps(body))), body)

	def delete(self, uuid):
		"""
		Removes a specific model instance

		:param uuid: The UUID of the model to remove
		"""

		return self._delete("/model/%s" % base.getid(uuid), 'model')