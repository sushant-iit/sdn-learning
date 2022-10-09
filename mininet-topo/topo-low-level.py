from mininet.node import OVSSwitch,Host,Controller
from mininet.link import Link

h1 = Host('h1')
h2 = Host('h2')
h3 = Host('h3')
h4 = Host('h4')

s1 = OVSSwitch('s1', inNamespace=False)
c0 = Controller('c0', inNamespace=False)

Link(h1, s1)
Link(h2, s1)
Link(h3, s1)
Link(h4, s1)

h1.setIP('172.24.0.1/16')
h2.setIP('172.24.0.2/16')
h3.setIP('172.24.0.4/16')
h4.setIP('172.24.0.4/16')

c0.start()
s1.start([c0])

print("")
print("host h1 IP:", h1.IP)
print("host h2 IP:", h2.IP)
print("host h3 IP:", h3.IP)
print("host h4 IP:", h4.IP)
print("")

print("ping test between h1 and h2")
print(h1.cmd("ping -c2", h2.IP()))
print()

s1.stop()
c0.stop()