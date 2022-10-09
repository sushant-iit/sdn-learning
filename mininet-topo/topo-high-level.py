from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class OneSwitchTopo(Topo):
    def build(self, count=1):
        hosts = [self.addHost('h%d' %i) for i in range (1, count+1)]
        s1 = self.addSwitch('s1')
        for host in hosts:
            self.addLink(host, s1)

net = Mininet(topo=OneSwitchTopo(4))
h1,h2,h3,h4 = net.get('h1','h2', 'h3', 'h4')
print("")
net.start()

CLI(net)
net.stop()

