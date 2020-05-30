.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
kitconcept.formgen
==============================================================================

.. image:: https://travis-ci.org/kitconcept/kitconcept.formgen.svg?branch=master
    :target: https://travis-ci.org/kitconcept/kitconcept.formgen

.. image:: https://img.shields.io/pypi/status/kitconcept.formgen.svg
    :target: https://pypi.python.org/pypi/kitconcept.formgen/
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/v/kitconcept.formgen.svg
    :target: https://pypi.python.org/pypi/kitconcept.formgen
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/kitconcept.formgen.svg
    :target: https://pypi.python.org/pypi/kitconcept.formgen
    :alt: License

|

.. image:: https://raw.githubusercontent.com/kitconcept/kitconcept.formgen/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/

kitconcept.formgen allows to generate forms through the web (TTW).

Features
--------

- Add, updated and delete form definitions (JSON schema)
- Submit a form
- Send an email as form action
- Store data of the form submissions as JSON/CSV

Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

kitconcept.formgen adds a "Form" content type with title, description, schema and data field.

GET form schema::

    GET
    /Plone/my-form
    Accept: Application/json

Response::

    {
        "title": "Form",
        "type": "object",
        "properties": {
            "email": {"type": "string"},
            "subject": {"type": "string"},
            "comments": {"type": "string"},
        },
        "required": ["email", "subject", "comments"],
    }

POST form schema::

    POST
    /Plone/my-form
    Accept: Application/json
    Content-Type: application/schema-instance+json
    {
        "title": "Form",
        "type": "object",
        "properties": {
            "email": {"type": "string"},
            "subject": {"type": "string"},
            "comments": {"type": "string"},
        },
        "required": ["email", "subject", "comments"],
    }

PATCH form schema::

    PATCH
    /Plone/my-form
    Accept: Application/json
    Content-Type: application/schema-instance+json
    {
        "title": "Form",
        "type": "object",
        "properties": {
            "email": {"type": "string"},
            "subject": {"type": "string"},
            "comments": {"type": "string"},
        },
        "required": ["email", "subject", "comments"],
    }

DELETE form schema::

    DELETE
    /Plone/my-form
    Accept: Application/json

Submit form data::

    POST
    /Plone/my-form/submit
    Accept: Application/json
    Content-Type: application/schema-instance+json

    {
        "email": "jane@example.com",
        "subject": "hi from jane",
        "comment": "hi there",
    }

To submit form data do a POST request on the form content object::


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install kitconcept.formgen by adding it to your buildout::

    [buildout]

    ...

    eggs =
        kitconcept.formgen


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/kitconcept.formgen/issues
- Source Code: https://github.com/collective/kitconcept.formgen
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
Send us an email at info@kitconcept.com.


License
-------

The project is licensed under the GPLv2.
