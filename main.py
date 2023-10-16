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
window.title("／人◕ ‿‿ ◕人＼")  # kyubey
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
    ontologyID = goOntologyEntry.get()
    clusterName = clusterNameEntry.get()
    numCluster = clusterNumEntry.get()
    rangeMinimum = minRange.get()
    rangeMaximum = maxRange.get()
    correctionMethod = dropdownText.get()

    # TODO: remove this later, replace it with a validate for int inputs.
    numCluster = int(numCluster)     if numCluster.isnumeric()   else 0
    rangeMinimum = int(rangeMinimum) if rangeMinimum.isnumeric() else 0
    rangeMaximum = int(rangeMaximum) if rangeMaximum.isnumeric() else 0

    print("Uwaa! >o<", ontologyID, clusterName, numCluster, rangeMinimum, rangeMaximum, correctionMethod)

    #oPlot.parseAndPlot(ontologyID, clusterName, numCluster, rangeMinimum, rangeMaximum, correctionMethod)
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

submitButton = tkinter.Button(window, text="Submit Graph", height=10, width=20)


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


'''
>>>>Run the window! :) =======================================================================
'''
window.mainloop()
