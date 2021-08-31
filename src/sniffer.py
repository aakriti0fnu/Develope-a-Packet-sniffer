import subprocess
import sys
import csv
import os

directory="data"
if not os.path.exists(directory):
    os.makedirs(directory)

try:
        try:
            from scapy.all import *

        except ImportError:
            sys.exit("Scapy package for python is not installed on your system.\nExiting...\n")

        #Message to run as ROOT for users
        print("\n! Please run the program as ROOT !")
        if not os.geteuid() == 0:
            sys.exit("\nOnly root can run this.\nExiting...\n")

        #setting the interface to run the sniffer
        net_iface = input("Please enter the Network Interface on which you want to sniffer packets from: ")

        try:
            subprocess.call(["ifconfig", net_iface, "promisc"], stdout = None, stderr = None, shell = False)

        except:
            sys.exit("Failed to configure interface as promiscuous.\nExiting...\n")

        else:
            print("Interface %s was set to PROMISC mode." % net_iface)

        #number of packets to sniff with value 0 equal to infinity
        pkt_to_sniff = 0

        #setting timeout to 30 seconds
        time_to_sniff = 30
        print("The program will capture packets for %d seconds." % time_to_sniff)

        #Creating a .csv file according to user input of experiment number
        exp_num = int(input("Please enter the experiment number (1, 2 or 3): "))
        if exp_num == 1:
            file_name = "data/aakriti_exp_1.csv"
            sniffer_log = open(file_name, "w")
        elif exp_num == 2:
            file_name = "data/aakriti_exp_2.csv"
            sniffer_log = open(file_name, "w")
        elif exp_num == 3:
            file_name = "data/aakriti_exp_3.csv"
            sniffer_log = open(file_name, "w")
        else:
            sys.exit("Incorrect Experiment number entered.\nExiting...\n")

        #Printing logging message to the screen
        print("\n** Packet Capture started...\n")
        print("-------Packet Capture Results-------")

        #Running the sniffer process
        packet = sniff(iface = net_iface, count = pkt_to_sniff, timeout = time_to_sniff)

        tcp_packets = packet[TCP]
        udp_packets = packet[UDP]

        ip = len(packet[IP])
        print("IP = ", ip)
        tcp = len(packet[TCP])
        print("TCP = ", tcp)
        udp = len(packet[UDP])
        print("UDP = ", udp)
        dns = len(packet[DNS])
        print("DNS = ", dns)
        icmp = len(packet[ICMP])
        print("ICMP = ", icmp)

        http = 0
        https = 0
        for i in range(tcp):
            if tcp_packets[i][TCP].sport == 80:
                http += 1
            elif tcp_packets[i][TCP].sport == 443:
                https += 1
        print("HTTP = ",http)
        print("HTTPS = ",https)

        quic = 0
        for i in range(udp):
            if udp_packets[i][UDP].sport == 443:
                quic += 1
        print("QUIC = ", quic)

        writer = csv.writer(sniffer_log)
        writer.writerow(["protocol","count"])
        writer.writerow(["ip",ip])
        writer.writerow(["tcp",tcp])
        writer.writerow(["udp",udp])
        writer.writerow(["dns",dns])
        writer.writerow(["icmp",icmp])
        writer.writerow(["http",http])
        writer.writerow(["https",https])
        writer.writerow(["quic",quic])

        print("------------------------------------\n")
        #Printing the closing message
        print("*** Please check the %s file to see the results." % file_name)

        #Closing the log file
        sniffer_log.close()

        #Exiting the program
        print("Packet Sniffer program exits.\n")
        sys.exit()

except KeyboardInterrupt:
        sys.exit('\nProgram Interrupted\nExiting...\n')

#************************************ END OF CODE ************************************
