from plone.rest import Service

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
        self.context.schema = self.request.get('BODY', '{}')
        transaction.commit()
        return self.request.response.setStatus(204)


class DeleteSchema(Service):

    def render(self):
        self.context.schema = u"{}"
        transaction.commit()
        return self.request.response.setStatus(204)


class SubmitForm(Service):

    def render(self):
        # todo: call adapters
        return self.request.response.setStatus(201)
