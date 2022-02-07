import tornado

def torrc():
    '''with open ('torrc-cli', 'w') as f:
        f.write("SOCKSPORT 32708\n")
        f.write("SocksTimeout 120\n")
        f.write("ClientUseIPv6 0\n")
        f.write("AvoidDiskWrites 1\n")
        f.write("FascistFirewall 1\n")
        f.write("ClientOnly 1")'''
    with open ('torrc', 'w') as f:
        f.write("SOCKSPort 54311\n")
        f.write("DirCache 0\n")
        f.write(f"HiddenServiceDir C:\\Tor\\hidden_service\n")
        f.write(f"DataDirectory C:\\Tor\\hidden_data\n")
        f.write("HiddenServicePort 80 127.0.0.1:1235\n")
        f.write("HiddenServiceVersion 3\n")
        f.write("DoSCircuitCreationEnabled 0\n")
        f.write("DoSCircuitCreationMinConnections 54311\n")
        f.write("DoSRefuseSingleHopClientRendezvous 1\n")
        f.write("HiddenServiceMaxStreams 0\n")
        f.write("NoExec 1\n")
        f.write("ConstrainedSockets 0\n")
        f.write("AvoidDiskWrites 1")