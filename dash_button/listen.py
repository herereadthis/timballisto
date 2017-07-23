"""Attempt to listen for dash button presses."""

from scapy.all import *


def arp_display(pkt):
    """Don't know how this works yet."""
    if pkt[ARP].op == 1:  # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0':  # ARP Probe
            print("ARP Probe from: %s" % (pkt[ARP].hwsrc))

print(sniff(prn=arp_display, filter="arp", store=0, count=10))
