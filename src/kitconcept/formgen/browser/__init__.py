from plone.rest import Service

import json
import transaction


class GetSchema(Service):

    def render(self):
        self.request.response.setStatus(200)
        return '{"message": "GET: Schema"}'


class PostSchema(Service):

    def render(self):
        self.context.schema = self.request.get('BODY', '{}')
        transaction.commit()
        return self.request.response.setStatus(201)


class PatchSchema(Service):

    def render(self):
        self.request.response.setStatus(204)
        return '{"message": "PATCH: Schema"}'


class DeleteSchema(Service):

    def render(self):
        self.request.response.setStatus(204)
        return '{"message": "DELETE: Schema"}'


class SubmitForm(Service):

    def render(self):
        self.request.response.setStatus(201)
        return '{"message": "POST: Form submitted!"}'
