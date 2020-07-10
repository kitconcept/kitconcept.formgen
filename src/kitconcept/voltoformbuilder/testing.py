# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import kitconcept.voltoformbuilder


class PlonevoltoformbuilderLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=kitconcept.voltoformbuilder)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "kitconcept.voltoformbuilder:default")


KITCONCEPT_voltoformbuilder_FIXTURE = PlonevoltoformbuilderLayer()


KITCONCEPT_voltoformbuilder_INTEGRATION_TESTING = IntegrationTesting(
    bases=(KITCONCEPT_voltoformbuilder_FIXTURE,),
    name="PlonevoltoformbuilderLayer:IntegrationTesting",
)


KITCONCEPT_voltoformbuilder_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(KITCONCEPT_voltoformbuilder_FIXTURE, z2.ZSERVER_FIXTURE),
    name="PlonevoltoformbuilderLayer:FunctionalTesting",
)


KITCONCEPT_voltoformbuilder_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        KITCONCEPT_voltoformbuilder_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="PlonevoltoformbuilderLayer:AcceptanceTesting",
)
