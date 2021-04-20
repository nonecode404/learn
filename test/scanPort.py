import socket
import _thread
import threading

def connScan(host, port):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((host, port))
        print("tcp open port: " + str(port))

    except:
        print("tcp closed:" +str(port))

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host "% tgtHost)
        return

    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: '+ tgtIP)
        socket.setdefaulttimeout( 1 )

        for tgtPort in tgtPorts:
            print('Scanning port '+ str(tgtPort))
            t =  threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
            t.start()

portScan('172.17.229.11', [2222, 80, 443])