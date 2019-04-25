# Face recognition based on openCV
Using dlib, face_recognition library and webcam
-----------------------------------------------------------------------

**Reference:** https://github.com/ageitgey/face_recognition

 ## Dependencies (libraries)
  * openCV
  * dlib
  * face_recognition
  * pickle (optional, if you want to load and save image encodings in specific directory.)

 ## Environment
  * Windows 10
  * Anaconda 3
  * Python 3.6
  * GPU accelerating : cuda 10.1 + cudnn v7.5.1
 
 ## My camera
  * Logitech HD Pro Webcam C920
  
 ## Instructions
 1.Download and install Anaconda 3:
 https://www.anaconda.com/distribution/
  
 2.Download and install cuda and cudnn from Nvidia: 
 (Remember to add them into the path in your environment variables)
 https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal
 https://developer.nvidia.com/rdp/cudnn-download
  
 3.Create virtual environment in Anaconda prompt
 conda create -n pytorch python=3.6 (In my case, I create a pytorch environment)
  
 install packages:
        
        conda install pytorch torchvision cudatoolkit=10.0 -c pytorch 
        conda install opencv
        conda install cmake
  
 Test your pytorch + cuda + cudnn in your environment by typing these in python command line :
 
        import torch
        x = torch.rand(5,3)
        print(x)
        torch.cuda.is_available()
  
  4.Install dlib gpu version and face_recognition
  (If you download the .whl file and use pip install dlib to install, you only get dlib cpu version) 
  
  First, you should have some tools installed in your computer.
  cmake: 
  https://cmake.org/download/ 
  visual studio 2017:
  https://docs.microsoft.com/zh-tw/visualstudio/releasenotes/vs2017-relnotes
  git:
  https://git-scm.com/
  
  Next, open command line and enter:
        git clone https://github.com/davisking/dlib.git
  install dlib gpu version: 
        cd dlib
        mkdir build
        cd build
        cmake -G "Visual Studio 15 2017 Win64" -T host=x64 .. -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1
        cmake --build
        cd ..
        python setup.py install
        
  If you have problem in this step, you need to cancel line 23 in dlib/tools/python/CMakeLists:
  
       if (MSVC)
         #include(${CMAKE_CURRENT_LIST_DIR}/../../dlib/cmake_utils/tell_visual_studio_to_use_static_runtime.cmake)
       endif()
        
  Test your dlib gpu version in your environment by typing these in python command line :
 
       import dlib
       print(dlib.DLIB_USE_CUDA)
       
  install face_recognition:
        pip install face_recognition
  
  5.Run 
        python data_encode.py
        python face_recognition_webcam.py
