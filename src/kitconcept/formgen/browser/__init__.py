# -*- coding: utf-8 -*-
from plone.rest import Service
from plone.restapi.deserializer import json_body

import json
import transaction


class GetSchema(Service):
    def render(self):
        self.request.response.setStatus(200)
        self.request.response.setHeader("Content-Type", "application/json+schema")
        return json.dumps(self.context.schema)


class PostSchema(Service):
    def render(self):
        self.context.schema = self.request.get("BODY", "{}")
        transaction.commit()
        return self.request.response.setStatus(201)


class PatchSchema(Service):
    def render(self):
        self.context.schema = self.request.get("BODY", "{}")
        transaction.commit()
        return self.request.response.setStatus(204)


class DeleteSchema(Service):
    def render(self):
        self.context.schema = u"{}"
        transaction.commit()
        return self.request.response.setStatus(204)


class SubmitForm(Service):
    def render(self):
        # todo: data needs to be appended
        self.context.data = json_body(self.request)
        transaction.commit()
        return self.request.response.setStatus(201)
