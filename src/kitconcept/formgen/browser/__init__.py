# -*- coding: utf-8 -*-
from plone.rest import Service
from plone.restapi.deserializer import json_body

import json
import transaction


class SubmitForm(Service):
    def render(self):
        # todo: data needs to be appended
        self.context.data = json_body(self.request)
        transaction.commit()
        return self.request.response.setStatus(201)
