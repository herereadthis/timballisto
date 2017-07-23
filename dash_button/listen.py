"""Attempt to listen for dash button presses."""


from scapy.all import sniff
from pprint import pprint


def arp_display(pkt):
    """Don't know how this works yet."""
    pprint(pkt)
    # if pkt[ARP].op == 1:  # who-has (request)
    #     if pkt[ARP].psrc == '0.0.0.0':  # ARP Probe
    #        print("ARP Probe from: %s" % (pkt[ARP].hwsrc))


print(sniff(prn=arp_display, filter="arp", store=0, count=10))

# from scapy.all import *

# def arp_display(pkt):

#     if pkt.haslayer(ARP):
#         if pkt[ARP].op == 1: #who-has (request)
#             if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
#                 print "ARP Probe from: " + pkt[ARP].hwsrc

# print sniff(prn=arp_display, filter="arp", store=0, count=0)
