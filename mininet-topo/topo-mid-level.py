from mininet.net import Mininet
from mininet.cli import CLI

net=Mininet()

h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
h4 = net.addHost('h4')

s1 = net.addSwitch('s1')
c0 = net.addController('c0')

net.addLink(h1, s1)
net.addLink(h2, s1)
net.addLink(h3, s1)
net.addLink(h4, s1)

net.start()

h1.setIP('172.24.0.1/16')
h2.setIP('172.24.0.2/16')
h3.setIP('172.24.0.3/16')
h4.setIP('172.24.0.4/16')

print("")
CLI(net)
net.stop()