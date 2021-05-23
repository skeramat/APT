# This is python script for Metashape Pro. 
# To execute this script Go to Tools - run script
# This script is used to add coordinates to images that do not have 
# coordinates or to update the exact coordinates of images. 

# Programming by Saeed Keramat
# en.point@yahoo.com

import Metashape
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

# Checking compatibility
# compatible_major_version = "1.7"
# found_major_version = ".".join(Metashape.app.version.split('.')[:2])
# if found_major_version != compatible_major_version:
#     raise Exception("Incompatible Metashape version: {} != {}".format(found_major_version, compatible_major_version))

##############################################################
def xy():
        
    Tk().withdraw() 
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)

    X = []
    Y = []
    
    with open(filename) as f:
     xy = list(f)
    
    for line in xy:
        x, y = line.split()
        X.append(float(x))
        Y.append(float(y))

    return  X, Y
####################################################

def add_altitude():
    """
    Adds user-defined altitude for camera instances in the Reference pane
    Script adds user defined altitude to Source values in the Reference pane.
    """
   
    doc = Metashape.app.document
    if not len(doc.chunks):
        raise Exception("No chunks!")

    alt = Metashape.app.getFloat("Please specify the height to be added:", 100)

    print("Script started...")
    chunk = doc.chunk

    for camera in chunk.cameras:
        if camera.reference.location:
            coord = camera.reference.location
            camera.reference.location = Metashape.Vector([coord.x, coord.y, coord.z + alt])

    print("Script finished!")

def camera_center():
    """
    Adds Point file (XY coordinate) for camera instances in the Reference pane
    """

    doc = Metashape.app.document
    if not len(doc.chunks):
        raise Exception("No chunks!")

    print("Script started...")
    chunk = doc.chunk

    coord = xy()    #   Call Func XY
    coord_x = coord[0]
    coord_y = coord[1]
    
    i = 0
    for camera in chunk.cameras:
               
            camera.reference.location = Metashape.Vector([coord_x[i], coord_y[i], 0])
            
            i = i + 1

    print("Script finished!")
  
    

label = "Keramat/Add reference altitude"
label2 = "Keramat/Add reference XY"

Metashape.app.addMenuItem(label, add_altitude)
Metashape.app.addMenuItem(label2, camera_center)

