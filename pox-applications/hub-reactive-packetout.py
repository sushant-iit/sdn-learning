from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _hanlde_PacketIn (event):
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _hanlde_PacketIn)
    log.info("Hub running...")