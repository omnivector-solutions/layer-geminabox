from charms.reactive import (
    when, when_not, set_state
)

from charmhelpers.core.hookenv import (
    open_port, status_set, unit_private_ip
)


PORT = 9292


@when_not('geminabox.available')
def open_port_set_avail():
    open_port(PORT)
    status_set(
        "active", "Geminabox Available at http://{}:{}".format(
            unit_private_ip(), PORT))
    set_state('geminabox.available')


@when('http.available', 'geminabox.available')
def configure_http_interface(http):
    http.configure(port=PORT)
