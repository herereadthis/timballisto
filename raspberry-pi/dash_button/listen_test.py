"""Takeen from KeanWong."""

import datetime

import logging
from scapy.all import sniff
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def button_pressed_dash1():
    """Don't know what this does."""
    current_time = datetime.datetime.strftime(
        datetime.datetime.now(),
        '%Y-%m-%d %H:%M:%S'
    )
    print('Dash button pressed at %s' % (current_time))


def udp_filter(pkt):
    """Don't know either."""
    options = pkt['DHCP'].options
    for option in options:
        if isinstance(option, tuple):
            if 'requested_addr' in option:
                # we've found the IP address, which means its the second and
                # final UDP request, so we can trigger our action
                mac_to_action[pkt.src]()
                break


if __name__ == "__main__":
    # main()

    mac_to_action = {'68:37:e9:9c:78:7c': button_pressed_dash1}
    mac_id_list = list(mac_to_action.keys())

    print("Waiting for a button press...")
    sniff(
        prn=udp_filter,
        store=0,
        filter="udp",
        lfilter=lambda d: d.src in mac_id_list
    )
