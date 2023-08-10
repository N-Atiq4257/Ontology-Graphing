import pandas
import os
from matplotlib import pyplot as yae  # i love me some bad naming :)
import numpy as np
from . import Util

'''
    This is the method that's meant to read through the ontology files in order to get the plot.
    The way that the ontology files are sorted is through the cluster name, the number of hits, then the length ranges.
    
    If you overshoot the range then there should be a check for that.
    Also, if min range is more than max range there should be another check for that too.
'''
graphEnabled = False


def testPlot(plotName, plotX, plotY):
    # *sigh* this again.
    global graphEnabled

    # set up some things
    if not graphEnabled:
        yae.title("P Value graph for an Ontology")
        yae.xlabel("Motif")
        yae.ylabel("P Value")
        yae.ylim([0, 1])
        yae.ticklabel_format(style='sci')
        graphEnabled = True

        yae.plot(plotX, plotY, label=plotName)
        yae.draw()
    else:
        yae.plot(plotX, plotY, label=plotName)
        yae.draw()

    yae.legend()
    yae.show()
    print("======")
    if graphEnabled:
        graphEnabled = False
    # switch it once the graph is closed!
    # also do it once :)
    # also this doesn't really work LOL


def parseAndPlot(ontologyID, clusterName, clusterNum, minRange, maxRange, correctionName):
    # TODO: Change this path later
    ontologyPath = os.path.join(os.getcwd(), "test-data", ontologyID + ".csv")
    correctionMethod = Util.correctionNameConversions[correctionName]

    if os.path.exists(ontologyPath) and correctionMethod is not None:
        print("the path exists :)")
        # read through the csv file
        book = pandas.read_csv(ontologyPath)

        # declare these 2 so that they'll be used for iloc
        startIndex = -1
        endIndex = -1

        for index, line in book.iterrows():
            # print("looping: " + str(index))
            # we're in the cluster now?
            if line['cluster'] == clusterName:
                # we are!
                # is this the number we like?
                if line['number_clusters'] == clusterNum:
                    # it is!
                    # is this the minimum range?
                    # TODO: fix these checks since they're super rigid.
                    if line['length'] == minRange:
                        # print("this is the min range")
                        startIndex = index
                    elif line['length'] == maxRange:
                        # print("this is the max range.")
                        endIndex = index + 1
                        break
                    # end of the num of clusters
                # end of the cluster
            # end of the loop

        if not (startIndex == -1 or endIndex == -1):
            result = book.iloc[startIndex:endIndex]
            # now with the result, let's turn it into a graph :)
            motifLengths = result['length'].tolist()
            pValues = result[correctionMethod].tolist()

            # now plot it.
            plotName = str(clusterNum) + clusterName + str(minRange) + "-" + str(maxRange)
            testPlot(plotName, motifLengths, pValues)
        else:
            print("one of ur indices is -1 :(")
            print(startIndex)
            print(endIndex)
    else:
        print("no path or the correction method is none :(")
