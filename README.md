# PyVista Reality

*PyVista plotter variants for Virtual and eXtended Reality (VR and XR)*

This is currently a work in progress and the code will be released soon - watch this repository for updates.

## Windows VTK Wheels

You can download and install VTK with OpenVR (OpenXR coming soon) from the this shared file on Dropbox: https://www.dropbox.com/s/5vsmq6pp30vtaau/vtk-9.1.20220227.dev0-cp39-cp39-win_amd64.whl?dl=0

Ping [@banesullivan](https://github.com/banesullivan) if you have any issues with the wheel

### Building the Wheel

This is what I used to build locally on my machine after downloading the OpenVR modules from: https://github.com/ValveSoftware/openvr/releases

```
cmake -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DVTK_BUILD_TESTING=OFF \
  -DVTK_BUILD_DOCUMENTATION=OFF \
  -DVTK_BUILD_EXAMPLES=OFF \
  -DVTK_DATA_EXCLUDE_FROM_ALL:BOOL=ON \
  -DVTK_MODULE_ENABLE_VTK_PythonInterpreter:STRING=NO \
  -DVTK_WHEEL_BUILD=ON \
  -DVTK_PYTHON_VERSION=3 \
  -DVTK_WRAP_PYTHON=ON \
  -DVTK_MODULE_ENABLE_VTK_RenderingOpenVR=YES \
  -DOpenVR_INCLUDE_DIR="C:\Users\banes\source\repos\openvr\headers" \
  -DOpenVR_LIBRARY="C:\Users\banes\source\repos\openvr\lib\win64\openvr_api.lib" \
  ../../../
```
