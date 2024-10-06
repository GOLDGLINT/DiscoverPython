def printSCPs(scps):
    for scp in scps:
        printSCP(scp)

def printSCP(scp):
    print("SCP " + scp.id + ": " + scp.state + " | " + scp.dangerosityLevel)