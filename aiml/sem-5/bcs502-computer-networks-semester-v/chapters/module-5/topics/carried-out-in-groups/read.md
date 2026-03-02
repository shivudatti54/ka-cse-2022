bash
        Router> enable
        Router# configure terminal
        Router(config)# interface gigabitethernet 0/0
        Router(config-if)# ip address 192.168.1.1 255.255.255.0
        Router(config-if)# no shutdown