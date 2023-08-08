from matplotlib import pyplot as yae    # i love me some bad naming :)
import pandas
import numpy as np
import time
import tkinter
from Modules.TextInput import TextInput

# yeah i still can't believe it, when i was coding ~4 years ago
# i used to name my variables weird stuff like 'butts'
# 'poop', 'pee' and all the likeness. weiiiiiiiird.
# i also had my code organized in the most odd ways out there
# like entire functions in one line sorta odd.
# nowadays the worse i do is just giving them character names, a good bit different


'''
>>>>Setting up a tkinter widget ==============================================================
'''
window = tkinter.Tk()
window.geometry("500x500")
window.title("／人◕ ‿‿ ◕人＼") # kyubey
window.tk_setPalette("#fffafa")


'''
>>>>Setting up some variables that will be needed ============================================
'''
# for the dropdown menu
correctionMethods = {
    "Uncorrected",
    "Fdr-bh",
    "Holm",
    "Sidak",
    "Holm-Sidak",
    "Bonferroni",
    "Simes-Hochberg",
    "Hommel",
    "Fdr-by",
    "Fdr-tsbh",
    "Fdr-gbs",
    "Fdr-tsbky"

}
dropdownText = tkinter.StringVar()
dropdownText.set("Select a correction method")

# for graphing
graphEnabled = False


'''
>>>>Defining some methods ====================================================================
'''
def testPlot(plotName):
    # *sigh* this again.
    global graphEnabled

    xPoint = [i/10 for i in range(10+1)]
    yPoint = [1/2 * np.cos(i) + .5 for i in range(10+1)]

    #print(xPoint)
    #print(yPoint)

    # set up some things
    if not graphEnabled:
        yae.title("P Value graph for an Ontology")
        yae.xlabel("Motif")
        yae.ylabel("P Value")
        yae.ylim([0,1])
        yae.ticklabel_format(style='sci')
        graphEnabled = True

        yae.plot(xPoint,yPoint, label = plotName)
        yae.draw()
    else:
        yae.plot(yPoint,xPoint, label = plotName)
        yae.draw()
    
    yae.legend()
    yae.show()
    print("======")
    if graphEnabled:
        graphEnabled = False
    # switch it once the graph is closed!
    # also do it once :)

def onEntry():
    # get all of the inputs that are used to then generate a graph.
    ontologyID = goOntologyEntry.get()
    clusterName = clusterNameEntry.get()
    numCluster = clusterNumEntry.get()
    rangeMinimum = minRange.get()
    rangeMaximum = maxRange.get()
    correctionMethod = dropdownText.get()

    print("Uwaa! >o<", ontologyID, clusterName, numCluster, rangeMinimum, rangeMaximum, correctionMethod)

    testPlot( numCluster + clusterName + rangeMinimum + "-" + rangeMaximum )

def textFocusIn(input: tkinter.Entry):
    # clear all of the text within this input
    input.delete(0, tkinter.END)
    input.config(fg='black')

def textFocusOut(input: tkinter.Entry):
    input.config(fg='grey')
    

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
dropdown.place(x=0,y=125)

submitButton.pack()
submitButton.place(x=250, y=0)
submitButton.bind("<Button>", lambda w: onEntry())


'''
>>>>Run the window! :) =======================================================================
'''
window.mainloop()
