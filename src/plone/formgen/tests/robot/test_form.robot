# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s plone.formgen -t test_form.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src plone.formgen.testing.PLONE_FORMGEN_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_form.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open chrome browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Form
  Given a logged-in site administrator
    and an add form form
   When I type 'My Form' into the title field
    and I submit the form
   Then a form with the title 'My Form' has been created

Scenario: As a site administrator I can view a Form
  Given a logged-in site administrator
    and a form 'My Form'
   When I go to the form view
   Then I can see the form title 'My Form'


*** Keywords *****************************************************************

# --- Setup ------------------------------------------------------------------

Open chrome browser
  ${options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
  Call Method  ${options}  add_argument  disable-extensions
  Call Method  ${options}  add_argument  disable-web-security
  Call Method  ${options}  add_argument  window-size\=1280,1024
  # Call Method  ${options}  add_argument  remote-debugging-port\=9223
  Create WebDriver  Chrome  chrome_options=${options}


# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add form form
  Go To  ${PLONE_URL}/++add++Form

a form 'My Form'
  Create content  type=Form  id=my-form  title=My Form


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the form view
  Go To  ${PLONE_URL}/my-form
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a form with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the form title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
