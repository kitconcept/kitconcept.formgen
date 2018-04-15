# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import kitconcept.formgen


class PloneFormgenLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=kitconcept.formgen)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'kitconcept.formgen:default')


KITCONCEPT_FORMGEN_FIXTURE = PloneFormgenLayer()


KITCONCEPT_FORMGEN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(KITCONCEPT_FORMGEN_FIXTURE,),
    name='PloneFormgenLayer:IntegrationTesting'
)


KITCONCEPT_FORMGEN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(KITCONCEPT_FORMGEN_FIXTURE, z2.ZSERVER_FIXTURE),
    name='PloneFormgenLayer:FunctionalTesting'
)


KITCONCEPT_FORMGEN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        KITCONCEPT_FORMGEN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PloneFormgenLayer:AcceptanceTesting'
)
