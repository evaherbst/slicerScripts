# slicerScripts
Scripts and snippets for use in 3D Slicer


## Note if working with curve and plane cuts:
- the original vertices will NOT be deleted (AFAIK this decision was made in Slicer to maintain node IDs)
- this causes issues when fitting spheres etc (old vertices will still be counted in the fitting)
- the solution is using the SurfaceToolbox cleaning function. Here is a method to batch run it based on node names.
