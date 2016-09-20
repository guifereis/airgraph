import snap, csv

gg = snap.TNGraph.New() # NOTE - single edges.

currentID = 0
airportToID = dict()
allports = set()

for row in csv.reader(open("routes.dat", "rb"), delimiter=","):
	src = row[2]
	if (src not in airportToID):
		airportToID[src] = currentID
		currentID += 1
		gg.AddNode(airportToID[src])
		allports.add(airportToID[src])
	
	dst = row[4]
	if (dst not in airportToID):
		airportToID[dst] = currentID
		currentID += 1
		gg.AddNode(airportToID[dst])
		allports.add(airportToID[dst])
	gg.AddEdge(airportToID[src], airportToID[dst])
	
print "gg: Nodes %d, Edges %d" % (gg.GetNodes(), gg.GetEdges())


SIN_id = airportToID["SIN"]
DXB_id = airportToID["DXB"]


def getOutNeigh(NI, reachable):
	outdeg = NI.GetOutDeg()
	for ii in range(0, outdeg):
		reachable.add(NI.GetOutNId(ii))


reachable = set()
sin = gg.GetNI(SIN_id)
dxb = gg.GetNI(DXB_id)
nextReachable = set()
getOutNeigh(sin, reachable)

for port in reachable:
	ni = gg.GetNI(port)
	getOutNeigh(ni, nextReachable)

allReachable = reachable | nextReachable
unReachable = allports - allReachable
print len(allports)
print len(allReachable)
print len(unReachable)

IDToDeg = dict()

for portID in unReachable:
	
