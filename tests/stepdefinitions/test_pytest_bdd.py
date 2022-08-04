from pytest_bdd import scenario, given, when, then, parsers
from testinfra import host

@given("Klaus configured a basic Host")
def klaus_configured_a_basic_host():
    return "test"

@when("the host is provisioned")
def the_host_is_provisioned():
    return

@then("all basic services are running")
def all_basic_services_are_running():
    pass
