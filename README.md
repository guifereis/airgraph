Usage: python airgraph.py SIN

Loads a graph of airline routes onto snap.py. Then takes an airport (IATA or ICAO identifier), and finds largest airports not reachable in 2 hops max (1 stopover).

Largest is defined as largest degree, i.e. biggest number of routes in+out.

You will need snap.py installed for this to work: http://snap.stanford.edu/snappy/index.html#download

Dataset is a couple years out of date so you must double-check there aren't actually valid 1-stop itins.

Code is very quick and rough. Python 2.

Please note that the data (routes.dat) is property of: https://openflights.org/data.html
