from pox.core import core
from pox.lib.addresses import IPAddr, EthAddr
import pox.openflow.libopenflow_01 as of
import os

class Switch:
    def __init__(self, connection):
        self.connection = connection
        self.macToPort = {}
        connection.addListeners(self)

    def _handle_PacketIn(self, event):
        in_port = event.port
        dpid = event.dpid

        packet = event.parse
        eth = packet().find("ethernet")
        self.macToPort[eth.src] = in_port
        if eth.dst in self.macToPort:
            out_port = self.macToPort[eth.dst]
            msg = of.ofp_flow_mod()
            msg.match = of.ofp_match()
            msg.match.dl_dst = eth.dst
            # msg.match.in_port = in_port
            msg.idle_timeout = 10
            msg.hard_timeout = 30
        else:
            out_port = of.OFPP_FLOOD
            msg = of.ofp_packet_out()

        msg.actions.append(of.ofp_action_output(port = out_port))
        msg.data = event.ofp
        self.connection.send(msg)

def _handle_ConnectionUp (event):
    policyFile = "/prog/pox/pox/forwarding/firewall-mac-policies.csv"
    rulesFile = open(policyFile, 'r')
    rules = [rule.strip() for rule in rulesFile]
    for rule in rules:
        parsed_rule = rule.split(',')
        new_rule = of.ofp_flow_mod()
        new_rule.match = of.ofp_match()
        new_rule.match.dl_src = EthAddr(parsed_rule[0])
        new_rule.match.dl_dst = EthAddr(parsed_rule[1])
        event.connection.send(new_rule)
    Switch(event.connection)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
