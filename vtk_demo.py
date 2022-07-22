"""Basic VTK OpenVR Demo."""
import vtk

from vtkmodules.vtkRenderingOpenVR import (
    vtkOpenVRCamera,
    vtkOpenVRRenderer,
    vtkOpenVRRenderWindow,
    vtkOpenVRRenderWindowInteractor,
)


renderer = vtk.vtkOpenVRRenderer()
renderWindow =vtk.vtkOpenVRRenderWindow()
iren = vtk.vtkOpenVRRenderWindowInteractor()
cam = vtk.vtkOpenVRCamera()
renderer.SetShowFloor(True)
renderer.SetBackground(0.2, 0.3, 0.4);
renderWindow.AddRenderer(renderer);
iren.SetRenderWindow(renderWindow);
renderer.SetActiveCamera(cam);

light = vtk.vtkLight()
light.SetLightTypeToSceneLight();
light.SetPosition(1.0, 1.0, 1.0);
renderer.AddLight(light);

#crazy frame rate requirement
#need to look into that at some point
renderWindow.SetDesiredUpdateRate(350.0);
iren.SetDesiredUpdateRate(350.0);
iren.SetStillUpdateRate(350.0);

renderer.RemoveCuller(renderer.GetCullers().GetLastItem());

# renderer.UseShadowsOn();

source = vtk.vtkSphereSource()

actor = vtk.vtkActor()
renderer.AddActor(actor);

# mapper = vtk.vtkOpenGLPolyDataMapper()
mapper = vtk.vtkDataSetMapper()
mapper.SetInputConnection(source.GetOutputPort());
# mapper.SetVBOShiftScaleMethod(vtk.vtkOpenGLVertexBufferObject.AUTO_SHIFT_SCALE);
actor.SetMapper(mapper);
actor.GetProperty().SetAmbientColor(0.2, 0.2, 1.0);
actor.GetProperty().SetDiffuseColor(1.0, 0.65, 0.7);
actor.GetProperty().SetSpecular(0.5);
actor.GetProperty().SetDiffuse(0.7);
actor.GetProperty().SetAmbient(0.5);
actor.GetProperty().SetSpecularPower(20.0);
actor.GetProperty().SetOpacity(1.0);
# actor.GetProperty().SetRepresentationToWireframe();

#actor.SetCoordinateSystemToPhysical();
#actor.SetCoordinateSystemRenderer(renderer);
#actor.UseBoundsOff();

# the HMD may not be turned on/etc
renderWindow.Initialize();
# if renderWindow.GetHMD():

renderer.ResetCamera();
renderWindow.Render();

iren.Start()
