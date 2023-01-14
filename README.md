# PyVista Reality

*PyVista plotter variants for Virtual and eXtended Reality (VR and XR)*

This is currently a work in progress and the code will be released soon - watch this repository for updates.

## Windows VTK Wheels

You can download and install VTK with OpenVR (OpenXR coming soon) from the this shared file on Dropbox: 

- https://www.dropbox.com/s/5vsmq6pp30vtaau/vtk-9.1.20220227.dev0-cp39-cp39-win_amd64.whl?dl=0

Ping [@banesullivan](https://github.com/banesullivan) if you have any issues with the wheel

### Building the Wheel

After downloading the OpenVR modules from: https://github.com/ValveSoftware/openvr/releases

Use the CMake configurations from https://github.com/banesullivan/vtk-cmake

Specifically, the `openvr.cmake` configuraion and be sure to modify the hardcoded paths in those files.

```
cmake -GNinja -C openvr.cmake ..
ninja
python setup.py bdist_wheel
```
