A Packet sniffer tool.


------

How to run the code:

1. Clone this repo!

   `git clone https://github.com/aakriti0fnu/Develope-a-packet-sniffer.git`

2. In [project directory](./) create a virtual enviroment using `virtualenv` to have package dependencies of this python codebase.
    
   First, install external package `virtualenv` on system python.  
    - if on python(version 2.x) :`pip install virtualenv`, 
    - if on python(version 3.x) : `python3 -m pip install virtualenv`
   
   Second, create new project virtual environment: `packet_sniffer_env`

   - **create environment** : `virtualenv --python=3.8 packet_sniffer_env38`
   - **source it**          : `source packet_sniffer_env38/bin/activate`
   
      
      install project specific dependencies: `pip install scapy matplotlib`

      [scapy source](https://github.com/secdev/scapy), 
      [scapy docs](https://scapy.readthedocs.io/en/latest/introduction.html)
      Scapy is a well-known packet manipulation tool which allows to create, modify, send and capture network packets.

   
   - **freeze it to file** : `pip freeze > requirements.txt`
   - **load from file**    : `pip install -r requirements.txt`
   


3. 
   - Specific to `Ubuntu 20.04.3 LTS (Focal Fossa)`, you need to install [tcpdump](http://manpages.ubuntu.com/manpages/trusty/man8/tcpdump.8.html)
 
     `sudo apt-get install tcpdump`

   - you need to check the network-interface, you'll be using is enabled [promiscuous mode](https://www.thegeekdiary.com/how-to-configure-interface-in-promiscuous-mode-in-centos-rhel/). [How to check?](https://tots.1o24.org/how-to-check-if-promiscuous-mode-is-enabled-on-network-interface-in-linux/)
     
     to check : `netstat -i`

     to set promiscuous mode: `ip link set wlp108s0 promisc on`

      - by default `ip` command is used, but if you want to use `ifconfig`, Ubuntu 20.04 (Focal Fossa) doesn’t have `ifconfig` command pre-installed. 

         Note: [ip vs ifconfig](https://computingforgeeks.com/ifconfig-vs-ip-usage-guide-on-linux/)

         `sudo apt install net-tools`
         
         then, to set promiscuous mode: `ifconfig eth0 promisc`
      
      Note: for [debugging purpose](https://askubuntu.com/questions/430355/configure-a-network-interface-into-promiscuous-mode)    
   - Now, you're ready to run the program.

      `sudo ./packet_sniffer_env38/bin/python src/sniffer.py `
   
     Note:
      - The important Modules used in the code which helped in the successful run are as follows:**

            1) `subprocess` - It helped to establish the network interface to promiscuous mode which helps in capturing all the packets without discarding any unnecessary packets.
            2) `sys` - used to exit the tool gracefully
            3) `csv` - used to create CSV file
            4) `scapy.all` - used to import necessary functions of the scapy module

   - results are in [results/](./results/)   

Future work:
- to use [scapy-unroot](https://github.com/scapy-unroot/scapy_unroot), scapy without root permissions
  or [pcapy](https://github.com/helpsystems/pcapy) [without root permissions](https://medium.com/@badbot/safe-packet-capture-python-without-sudo-b08c4c4e531).
----

Team Members:

Aakriti

Ashwin Kumar Munniswamy

