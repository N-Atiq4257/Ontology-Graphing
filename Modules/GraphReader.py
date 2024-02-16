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
    if not (r.text == "NO PATH" or r.status_code == 502 or r.status_code == 503):

        # get the json :)
        graphFile = r.json()
        # now get the dataframe!
        return pandas.DataFrame.from_dict(graphFile)
    elif r.status_code == 502 or r.status_code == 503:
        # if the instance is off or website is not on, return this.
        Util.log.updateText("The server is either off or encountered an error. :(\nCheck the status of the server "
                            "here: http://scd.ustcomputing.org:8012/scd/ ")
        return None
    elif r.text == "NO PATH":
        return pandas.DataFrame()


'''
    A function that gets the missing lengths needed for the SCD graphs to generate.
'''
def getMissingLengths(book, clusterName='SCD', clusterNum=3, minRange=100, maxRange=105):
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
                        print(line)
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

    return missingDefs


'''
    A function that checks whether or not the graph files for all fo these functions exist.
    If they don't they'll do some process to generate them all :)
'''
def generateGraphs(ontology='GO:0030421', clusterName='SCD', clusterNum=3, minRange=100, maxRange=105,
                   correctionMethod=Util.defaultCorrection):
    book = getGraph(ontology, clusterName, clusterNum, minRange, maxRange)
    if book is None:
        return "The server is either off or encountered an error. :("

    missingDefs = getMissingLengths(book, clusterName, clusterNum, minRange, maxRange)
    correction = Util.correctionNameConversions[correctionMethod]

    if not len(missingDefs) == 0:
        message = "Sending a request to the server to generate graphs for the following ontologies: " + str(missingDefs)
        Util.log.updateText(message)

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

        return "^_^"
    else:
        message = "The generation of graphs is already complete :)"
        Util.log.updateText(message)


'''
This function will parse through the dataframe from the above function and then
send a post request to cherrypy in order to get it to generate the necessary graphs for plotting.
'''
def graphResult(ontology='GO:0030421', clusterName='SCD', clusterNum=3, minRange=100, maxRange=105,
                correctionMethod=Util.defaultCorrection):
    book = getGraph(ontology, clusterName, clusterNum, minRange, maxRange)
    if book is None:
        Util.log.updateText("The server is either off or encountered an error. :(\nCheck the status of the server "
                            "here: "
                            "http://scd.ustcomputing.org:8012/scd/ ")
        return

    missingDefs = getMissingLengths(book, clusterName, clusterNum, minRange, maxRange)
    correction = Util.correctionNameConversions[correctionMethod]

    if not len(missingDefs) == 0:
        message = "We're still missing these definitions:\n" + str(missingDefs)

        Util.log.updateText(message)
    else:
        # now this is where we plot it.
        message = "Now plotting! ^_^"
        Util.log.updateText(message)

        ontoPlotter.parseAndPlot(ontology, clusterName, clusterNum, minRange, maxRange, correction, book)
