
from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PacketIn (event):
    packet = event.parsed
    msg = of.ofp_flow_mod()
    msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
    event.connection.send(msg)

def launch ():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    # log.info("Hub application is running...")

# launch()