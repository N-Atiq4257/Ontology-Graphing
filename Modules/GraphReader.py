import math
import threading

import requests
import time
import pandas
from . import OntoPlotter as ontoPlotter
from . import Util

# set up the session.
session = requests.Session()

'''
A function that calls to my instance in order to get a json result that is then turned into a pandas dataframe.
'''


def getGraph(ontology='GO:0030421', clusterName='SCD', clusterNum=3, minRange=100, maxRange=105):
    print("calling the cherrypy server...")
    # call the cherrypy server.
    r = session.get("http://scd.ustcomputing.org:8012/scd/get_graph/",
                    params={'Ontology': ontology, 'Cluster': clusterName, 'Repetition': clusterNum,
                            'LengthMin': minRange,
                            'LengthMax': maxRange})
    if not (r.text == "NO PATH" or r.status_code == 502):

        # get the json :)
        graphFile = r.json()
        # now get the dataframe!
        return pandas.DataFrame.from_dict(graphFile)
    else:
        return pandas.DataFrame()


'''
This function will parse through the dataframe from the above function and then
send a post request to cherrypy in order to get it to generate the necessary graphs for plotting.
'''
def graphResult(ontology='GO:0030421', clusterName='SCD', clusterNum=3, minRange=100, maxRange=105,
                correctionMethod=Util.defaultCorrection):

    correction = Util.correctionNameConversions[correctionMethod]
    book = getGraph(ontology, clusterName, clusterNum, minRange, maxRange)

    # for the ones that the server might wanna generate.
    foundLengths = []
    missingDefs = []

    # if the dataframe exists, we'll read through it to see.
    if not book.empty:

        for index, line in book.iterrows():

            # we're in the cluster now?
            if line['cluster'] == clusterName:
                # we are!
                # is this the number we like?
                if line['number_clusters'] == clusterNum:
                    # it is!
                    # if the length is inbetween the min and max, we'll add it!
                    if minRange <= line['length'] <= maxRange:
                        foundLengths.append(line['length'])
                        # we're having a list of integers since that's the one part that differs for the graph, really.

                    # end of the num of clusters
                # end of the cluster
            # end of the loop

    # now that we have parsed through the dataframe to see which ones are defined, let's find the missing ones!
    print("MISSING DEFINITIONS:: ")
    for i in range(minRange, maxRange + 1):
        if i not in foundLengths:
            missingDef = str(clusterNum) + " " + clusterName + " " + str(i)
            missingDefs.append(missingDef)
            print(" " + missingDef)

    if not len(missingDefs) == 0:
        print("a")
        # send a post request to deal with the missing ones now.
        r = session.post("http://scd.ustcomputing.org:8012/scd/generate_graphs/",
                         params={'Definitions': missingDefs,
                                 'Ontology': ontology,
                                 'Organism': 9606,
                                 'Cluster': clusterName,
                                 'Repetition': clusterNum,
                                 'MinRange': minRange,
                                 'MaxRange': maxRange,
                                 'Correction': correction
                                 }
                         )

        print(r.text)

    else:
        # now this is where we plot it.
        print("PERFECT.")
        ontoPlotter.parseAndPlot(ontology, clusterName, clusterNum, minRange, maxRange, correction, book)
