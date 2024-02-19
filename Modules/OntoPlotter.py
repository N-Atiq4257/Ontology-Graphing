import pandas
import os
from matplotlib import pyplot as plt  # i love me some bad naming :)
import numpy as np
from . import Util

'''
    This is the method that's meant to read through the ontology files in order to get the plot.
    The way that the ontology files are sorted is through the cluster name, the number of hits, then the length ranges.
    
    If you overshoot the range then there should be a check for that.
    Also, if min range is more than max range there should be another check for that too.
'''
graphEnabled = False


def testPlot(plotName, plotX, plotY, goID, correction):
    # *sigh* this again.
    global graphEnabled

    # set up some things
    # really quickly lets set the limit.
    max = 1.1
    for point in plotY:
        if point > max:
            max = point


    if not graphEnabled:
        plt.title("Graph for GO Ontology " + goID)
        plt.xlabel("Motif")
        plt.ylabel("P Value (" + correction + ")")
        plt.ylim([-.5, max + .33])
        plt.ticklabel_format(style='sci')
        graphEnabled = True

        plt.plot(plotX, plotY, label=plotName)
        plt.draw()
    else:
        plt.plot(plotX, plotY, label=plotName)
        plt.draw()

    plt.legend()
    plt.show()
    print("======")
    if graphEnabled:
        graphEnabled = False
    # switch it once the graph is closed!
    # also do it once :)
    # also this doesn't really work LOL


def parseAndPlot(ontologyID, clusterName, clusterNum, minRange, maxRange, correctionName, dataframe):
    # TODO: Change this path later
    ontologyPath = os.path.join(os.getcwd(), "test-data", ontologyID + ".csv")
    correctionMethod = correctionName

    if correctionMethod is not None:
        print("the path exists :)")
        # declare these 2 so that they'll be used for iloc

        # let's not :)
        #startIndex = -1
        #endIndex = -1

        pValues = []
        motifLengths = []

        sortedFrame = dataframe.sort_values(by=['cluster','number_clusters','length'])

        for index, line in sortedFrame.iterrows():
            # print("looping: " + str(index))
            # we're in the cluster now?
            if line['cluster'] == clusterName:
                # we are!
                # is this the number we like?
                if line['number_clusters'] == clusterNum:
                    # it is!
                    # is this the minimum range?

                    '''
                    # TODO: fix these checks since they're super rigid.
                    if line['length'] == minRange:
                        # print("this is the min range")
                        startIndex = int(index)
                    elif line['length'] == maxRange:
                        # print("this is the max range.")
                        endIndex = int(index) + 1
                        break
                    '''
                    if minRange <= line['length'] <= maxRange:
                        pValues.append(line[correctionMethod])
                        motifLengths.append(line['length'])

                    # end of the num of clusters
                # end of the cluster
            # end of the loop

        plotName = str(clusterNum) + clusterName + str(minRange) + "-" + str(maxRange)
        testPlot(plotName, motifLengths, pValues, ontologyID, correctionName)
        '''
        if not (startIndex == -1 or endIndex == -1):
            #result = dataframe.iloc[startIndex:endIndex]
            # now with the result, let's turn it into a graph :)
            motifLengths = result['length'].tolist()
            pValues = result[correctionMethod].tolist()

            # now plot it.
            plotName = str(clusterNum) + clusterName + str(minRange) + "-" + str(maxRange)
            testPlot(plotName, motifLengths, pValues, ontologyID, correctionName)
        else:
            print("one of ur indices is -1 :(")
            print(startIndex)
            print(endIndex)
        '''

    else:
        print("no path or the correction method is none :(")
