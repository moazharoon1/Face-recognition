# Face-recognition
Enrollment &amp; Recognition: Webcam-based scripts using OpenCV, dlib, &amp; face_recognition for face enrollment and real-time recognition.

# Installation

## Dependencies
Python 3.x
OpenCV
dlib
face_recognition

Versions of these libraries may depend on the version of Python you are using. I used Python 3.10 and used opencv 4.9.0.80, dlib 19.22.99 and face_recognition 1.3.0.

### Installing dlib
- Install CMake: Ensure CMake is installed on your system and added to PATH. It can be found in the link https://cmake.org/download/.

- Install C/C++ Build Tools: Install the necessary build tools for C/C++ compilation. The Visual Studio can be downloaded at the link https://visualstudio.microsoft.com/visual-cpp-build-tools/.

- Install dlib: Download and install dlib from source or using pre-built binaries.
  - Normal way:
    - First of all, you need to install CMake library.
      ```
      pip install cmake
      ```
    - Now install dlib.
      ```
      pip install dlib
      ```
  - Another Approach:
    - Refer to this GitHub repository: https://github.com/z-mahmud22/Dlib_Windows_Python3.x
    - Download the pre-built dlib WHL file
    - save it in the desired directory
    - run the command from the above-mentioned GitHub repository
    - dlib should be ready to use.

### Install face_recognition and opencv
Use the commands below to install opencv and face_recognition libraries:
```
pip install opencv-python
```
```
pip install face_recognition
```

Run the files 
Press q to capture images
You can improve the performance of this program by tweaking the value of tolerance

Peace :)

