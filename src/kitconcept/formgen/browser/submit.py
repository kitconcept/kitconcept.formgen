from plone.rest import Service


class GetSchema(Service):

    def render(self):
        self.request.response.setStatus(200)
        return '{"message": "GET: Schema"}'


class PostSchema(Service):

    def render(self):
        self.request.response.setStatus(201)
        return '{"message": "POST: Schema"}'


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
