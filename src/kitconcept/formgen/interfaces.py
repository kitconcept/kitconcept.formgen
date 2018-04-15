# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from kitconcept.formgen import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPloneFormgenLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IForm(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    schema = schema.Text(
        title=_(u"Schema"),
        description=_(u"JSON schema definition of the form"),
        required=False,
    )
