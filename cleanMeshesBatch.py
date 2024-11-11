# This function runs the Clean function from the SurfaceToolbox on all meshes in a scene that contain a specific phrase specified by the variable targetNameContains.
# Models are overwritten with the cleaned versions
# Eva C. Herbst, 2024 

import SurfaceToolbox

def clean(targetNameContains):

    # Initialize SurfaceToolbox logic
    logic = SurfaceToolbox.SurfaceToolboxLogic()

    slicer.app.setRenderPaused(True)  # Disable real-time rendering until finished

    # Get the number of model nodes
    number_of_model_nodes = slicer.mrmlScene.GetNumberOfNodesByClass('vtkMRMLModelNode')

    # Process each model node
    for i in range(number_of_model_nodes):
        # Get the model node
        model = slicer.mrmlScene.GetNthNodeByClass(i, 'vtkMRMLModelNode')
        # Skip if "Scapula" is not in the model node name
        if targetNameContains not in model.GetName():
            continue


        # Get the model node
        model = slicer.mrmlScene.GetNthNodeByClass(i, 'vtkMRMLModelNode')
        logic.clean(
            inputModel=model,
            outputModel=model
        )

# specify what you want the target names to contain - otherwise will also get red, green, yellow slice nodes
targetNameContains = "_Glenoid"   
clean(targetNameContains)