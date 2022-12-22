from mininet.topo import Topo  
from mininet.link import TCLink

class MyTopo( Topo ):  
  
    def __init__( self ):
      


        Topo.__init__( self )

        # Add hosts and switches
        client = self.addHost( 'h1' )
        server = self.addHost( 'h2' )
        router1 =self.addSwitch("r1")
        router2 =self.addSwitch("r2")
        router3 =self.addSwitch("r3")
        router4 =self.addSwitch("r4")
        router5 =self.addSwitch("r5")
        router6 =self.addSwitch("r6")
        router7 =self.addSwitch("r7")
        router8 =self.addSwitch("r8")
    
        # Add links
        self.addLink(client,router1)
        self.addLink(client,router2)
        self.addLink(router1,router3)
        self.addLink(router1,router4)

        self.addLink(router2,router3)
        self.addLink(router2,router5)

        self.addLink(router3,router4)
        self.addLink(router3,router5)
        
        self.addLink(router4,router6)
        self.addLink(router4,router7)

        self.addLink(router5,router6)
        self.addLink(router5,router8)

        self.addLink(router6,router7)
        self.addLink(router6,router8)
        self.addLink(router7,server)
        self.addLink(router8,server)
        


topos = { 'mytopo': ( lambda: MyTopo() ) } 

