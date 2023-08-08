from matplotlib import pyplot as yae # i love me some bad naming :)
import pandas                        # yeah i still can't believe it, when i was coding ~4 years ago
import numpy as np                   # i used to name my variables weird stuff like 'butts'
import time                          # 'poop', 'pee' and all the likeness. weiiiiiiiird.
import tkinter                       # i also had my code organized in the most odd ways out there
import multiprocessing               # like entire functions in one line sorta odd.


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
goOntologyEntry = tkinter.Entry(window, fg='grey')
goOntologyEntry.insert(0, 'GO Ontology ID')

clusterNameEntry = tkinter.Entry(window, fg='grey')
clusterNameEntry.insert(0, 'Cluster name')

clusterNumEntry = tkinter.Entry(window, fg='grey')
clusterNumEntry.insert(0, 'Num of cluster(s)')

minRange = tkinter.Entry(window, fg='grey')
minRange.insert(0, 'Range minimum')

maxRange = tkinter.Entry(window, fg='grey')
maxRange.insert(0, 'Range maximum')

# the other parts
dropdown = tkinter.OptionMenu(window, dropdownText, *correctionMethods)

submitButton = tkinter.Button(window, text="Submit Graph", height=10, width=20)


'''
>>>>Packing / Placing / Binding all defined elements =========================================
'''
goOntologyEntry.pack()
goOntologyEntry.place(x=0,y=0)
goOntologyEntry.bind("<FocusIn>", lambda x: textFocusIn(goOntologyEntry))
goOntologyEntry.bind("<FocusOut>", lambda x: textFocusOut(goOntologyEntry))

clusterNameEntry.pack()
clusterNameEntry.place(x=0, y=25)
clusterNameEntry.bind("<FocusIn>", lambda x: textFocusIn(clusterNameEntry))
clusterNameEntry.bind("<FocusOut>", lambda x: textFocusOut(clusterNameEntry))

clusterNumEntry.pack()
clusterNumEntry.place(x=0, y=50)
clusterNumEntry.bind("<FocusIn>", lambda x: textFocusIn(clusterNumEntry))
clusterNumEntry.bind("<FocusOut>", lambda x: textFocusOut(clusterNumEntry))

minRange.pack()
minRange.place(x=0, y=75)
minRange.bind("<FocusIn>", lambda x: textFocusIn(minRange))
minRange.bind("<FocusOut>", lambda x: textFocusOut(minRange))

maxRange.pack()
maxRange.place(x=0, y=100)
maxRange.bind("<FocusIn>", lambda x: textFocusIn(maxRange))
maxRange.bind("<FocusOut>", lambda x: textFocusOut(maxRange))

dropdown.pack()
dropdown.place(x=0,y=125)

submitButton.pack()
submitButton.place(x=250, y=0)
submitButton.bind("<Button>", lambda w: onEntry())


'''
>>>>Run the window! :) =======================================================================
'''
window.mainloop()
