import snap, csv, sys

gg = snap.TNEANet.New() # Directed multigraph.

srcPort = sys.argv[1]
print srcPort

currentID = 0
airportToID = dict()
IDToAirport = dict()
allports = set() # set of every airport ID

def addToDicts(airportToID, IDToAirport, portName):
	global currentID
	if (portName not in airportToID):
		airportToID[portName] = currentID
		IDToAirport[currentID] = portName
		currentID += 1
		gg.AddNode(airportToID[portName])
		allports.add(airportToID[portName])

for row in csv.reader(open("routes.dat", "rb"), delimiter=","):
	src = row[2] # airport name (IATA or ICAO)
	if (src not in airportToID):
		addToDicts(airportToID, IDToAirport, src)
	
	dst = row[4] # airport name (IATA or ICAO)
	if (dst not in airportToID):
		addToDicts(airportToID, IDToAirport, dst)
		
	gg.AddEdge(airportToID[src], airportToID[dst])
	
print "gg: Nodes %d, Edges %d" % (gg.GetNodes(), gg.GetEdges())

def getOutNeigh(NI, reachable): # add all out-neighbors to reachable
	outdeg = NI.GetOutDeg()
	for ii in range(0, outdeg):
		reachable.add(NI.GetOutNId(ii))

def addNeighborsToReachable(reachable, nextReachable): # for all in reachable, add their neighbors to reachable
	for port in reachable:
		ni = gg.GetNI(port)
		getOutNeigh(ni, nextReachable)

reachable = set() # IDs reachable in 1 hop
nextReachable = set() # IDs reachable in 2 hops

#getOutNeigh(gg.GetNI(airportToID[srcPort]), reachable)

getOutNeigh(gg.GetNI(airportToID["LHR"]), reachable)
getOutNeigh(gg.GetNI(airportToID["LGW"]), reachable)
#getOutNeigh(gg.GetNI(airportToID["JFK"]), reachable)
#getOutNeigh(gg.GetNI(airportToID["SFO"]), reachable)

addNeighborsToReachable(reachable, nextReachable)

allReachable = reachable | nextReachable

unReachable = allports - allReachable # every airport ID that is not reachable in <= 1 hop

print len(allports)
print len(allReachable)
print len(unReachable)

tupList = list()
for portID in unReachable:
	ni = gg.GetNI(portID)
	deg = ni.GetDeg()
	tup = (portID, deg)
	tupList.append(tup)

tupList.sort(key=lambda x: x[1], reverse=True)
print tupList[:10]
for ii in range(0, 10):
	print IDToAirport[tupList[ii][0]] + " : " + str(tupList[ii][1])
