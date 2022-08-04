from pytest_bdd import scenario, given, when, then, parsers
from testinfra import host

serviceConfigs = {
    'basic': ['NetworkManager.service', 'sshd.service'],
    'extra': ['NetworkManager.service', 'sshd.service', 'testservice']
}

@given(parsers.parse('Klaus configured a {role} Host'), target_fixture='role')
def klaus_configured_a_basic_host(role):
    return role

@when('the host is provisioned')
def the_host_is_provisioned():
    return

@then('all basic services are running')
def all_basic_services_are_running(role):
    assert (role in serviceConfigs)
    for service in serviceConfigs[role]:
        assert host.get_host("local://").service(service).is_running, f'Service "{service}" is not running'
