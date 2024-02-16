import tkinter
from Modules.TextInput import TextInput
from Modules import Util
from Modules import GraphReader as grapher
import Modules.OntoPlotter as oPlot

# yeah i still can't believe it, when i was coding ~4 years ago
# i used to name my variables weird stuff like 'butts'
# 'poop', 'pee' and all the likeness. weiiiiiiiird.
# i also had my code organized in the most odd ways out there
# like entire functions in one line sorta odd.
# nowadays the worst i do is just giving them character names, a good bit different


'''
>>>>Setting up a tkinter widget ==============================================================
'''
window = tkinter.Tk()
window.geometry("500x500")
window.title("Ontology Grapher!")
window.tk_setPalette("#fffafa")  # i like it slightly pink :)

'''
>>>>Setting up some variables that will be needed ============================================
'''
# for the dropdown menu
correctionMethods = Util.correctionNameConversions.keys()

dropdownText = tkinter.StringVar()
dropdownText.set(Util.defaultCorrection)

'''
>>>>Defining some methods ====================================================================
'''


def onEntry():
    # get all of the inputs that are used to then generate a graph.
    ontologyID       = goOntologyEntry.get()
    clusterName      = clusterNameEntry.get()
    numCluster       = clusterNumEntry.get()
    rangeMinimum     = minRange.get()
    rangeMaximum     = maxRange.get()
    correctionMethod = dropdownText.get()


    numCluster   = int(numCluster)   if numCluster.isnumeric()   else 0
    rangeMinimum = int(rangeMinimum) if rangeMinimum.isnumeric() else 0
    rangeMaximum = int(rangeMaximum) if rangeMaximum.isnumeric() else 0

    Util.log.updateText("WAWAWAWAWA!!!!")

    grapher.generateGraphs(ontologyID, clusterName, numCluster, rangeMinimum, rangeMaximum, correctionMethod)


def viewGraph():
    # get all of the inputs that are used to then generate a graph.
    ontologyID = goOntologyEntry.get()
    clusterName = clusterNameEntry.get()
    numCluster = clusterNumEntry.get()
    rangeMinimum = minRange.get()
    rangeMaximum = maxRange.get()
    correctionMethod = dropdownText.get()

    # TODO: remove this later, replace it with a validate for int inputs.
    numCluster =   int(numCluster)   if numCluster.isnumeric()   else 0
    rangeMinimum = int(rangeMinimum) if rangeMinimum.isnumeric() else 0
    rangeMaximum = int(rangeMaximum) if rangeMaximum.isnumeric() else 0

    Util.log.updateText("WAWAWAWAWA!!!!")

    grapher.graphResult(ontologyID, clusterName, numCluster, rangeMinimum, rangeMaximum, correctionMethod)


'''
>>>>Space to declare new elements to the tkinter widget =======================================
'''
# entries which are all used for generating a graph.
goOntologyEntry = TextInput(window, defaultText="Go Ontology ID")
clusterNameEntry = TextInput(window, defaultText="Cluster Name")
clusterNumEntry = TextInput(window, defaultText="Number of Cluster(s)")
minRange = TextInput(window, defaultText="Range Minimum")
maxRange = TextInput(window, defaultText="Range Maximum")

# the other parts
dropdown = tkinter.OptionMenu(window, dropdownText, *correctionMethods)

submitButton = tkinter.Button(window, text="Submit Graph", height=5, width=20)
viewButton = tkinter.Button(window, text="View Graph", height=5, width=20)

log = tkinter.Text(window, height=23, width=68, wrap=tkinter.WORD)


'''
>>>>Packing / Placing / Binding all defined elements =========================================
'''
goOntologyEntry.packAndPlace(xPos=0, yPos=0)
clusterNameEntry.packAndPlace(xPos=0, yPos=25)
clusterNumEntry.packAndPlace(xPos=0, yPos=50)
minRange.packAndPlace(xPos=0, yPos=75)
maxRange.packAndPlace(xPos=0, yPos=100)

dropdown.pack()
dropdown.place(x=0, y=125)

submitButton.pack()
submitButton.place(x=250, y=0)
submitButton.bind("<Button>", lambda w: onEntry())

viewButton.pack()
viewButton.place(x=250, y=90)
viewButton.bind("<Button>", lambda w: viewGraph())

Util.log.setup(window) # test idk lol
Util.log.msg.pack()
Util.log.msg.place(x=0, y=185)

'''
>>>>Run the window! :) =======================================================================
'''
window.mainloop()
