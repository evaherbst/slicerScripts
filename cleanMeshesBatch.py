# This function runs the Clean function from the SurfaceToolbox on all meshes in a scene that contain a specific phrase specified by the variable targetNameContains.
# Models are overwritten with the cleaned versions
# Eva C. Herbst, 2024 

import SurfaceToolbox

def clean(targetNameContains):

    # Initialize SurfaceToolbox logic
    logic = SurfaceToolbox.SurfaceToolboxLogic()

    # Get the number of model nodes
    number_of_model_nodes = slicer.mrmlScene.GetNumberOfNodesByClass('vtkMRMLModelNode')

    # Process each model node
    for i in range(number_of_model_nodes):
        # Get the model node
        model = slicer.mrmlScene.GetNthNodeByClass(i, 'vtkMRMLModelNode')
        # Skip if "Scapula" is not in the model node name
        if targetNameContains not in model.GetName():
            continue
        if targetNameCannotContain in model.GetName():
            continue

        print ("found model called " + model.GetName())
        
        #TODO note that the clean function from surface toolbox does not get rid of certain non manifold parts of the mesh
        # in future will try to implement more thorough cleaning for FE meshes similar to that done in the 3D Print Add On in Blender
        logic.clean(
            inputModel=model,
            outputModel=model
        )
        if updateNormals == "True":
        # update normals
        logic.computeNormals(
            inputModel=model, 
            outputModel=model, 
            autoOrient=True, 
            flip=False, 
            split=False, 
            splitAngle=30.0)
        
        slicer.app.processEvents()  # Process pending UI updates

# specify what you want the target names to contain - otherwise will also get red, green, yellow slice nodes
targetNameContains = "Glenoid"   # add and does not contain CC 
targetNameCannotContain = "CC"
updateNormals = "False" # set update normals to false as default, since it can cause issues with curvecut generated outputs
clean(targetNameContains,updateNormals)

