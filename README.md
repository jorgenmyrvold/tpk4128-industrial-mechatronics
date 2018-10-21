# TPK4128 Industrial Mechatronics

Introduction to Python programming for the course TPK4128 Industrial Mechatronics at the Department of Mechanical and Industrial Engineering, NTNU, Norwegian University of Science and Technology

## Basics

- Start the Python interpreter
- Arithmetic operators
- Variables and assignment
- Integers and floats
- Booleans, comparison operators, and logical operators
- String
- Type and type conversion
- String methods and formatting
- Data structures
    - Lists
    - Tuples
    - Set
    - Dictionaries and identity operators
    - Compound data structures

## Control flow

- If, elif, and else
- Indentation, white space, and best practices
- Complex boolean expressions
- For loops (definite iteration)
- While loops (indefinite iterations)
- Break and continue
- Zip and enumerate
- List comprehension

## Functions

- Function definition, body, arguments, and return value(s)
- Variable scope (local and global)
- Documentation
- Lambda expressions
- Iterators and generators (lazy evaluation)

## Classes

- Object oriented programming
- Objects and methods
- Constructors
- Inheritance
- Composition

## Exercise: Building a webcam server using OpenCV and Python

The task is to build a Python module that implements a socket server that fetches images from a webcam and sends it over a TCP/IP or UDP socket when it gets a request from a client.

1) Install Ubuntu in a virtual machine, e.g., VirtualBox.
2) Mount the the integrated webcam into the Ubuntu VM.
    1) Make sure the virtual machine is not running and your webcam is not being used.
    2) Bring up the main VBox window and in the details tab for your virtual machine click USB.
    3) Make sure "Enable USB Controller" is selected. Also make sure that "Enable USB 2.0 (EHCI) Controller" is selected too.
    4) Click the "Add filter from device" button (the cable with the '+' icon).
    5) Select your device from the list.
    6) Now click OK and start your VM.
3) Open a terminal and execute the command `ls /dev`. You should now see `video0` in the output. Note that you might need to add the camera manually from the top menu: Devices > Webcams > NameOfYourCamera
4) Install opencv: `pip install opencv-python`
5) Implement the `Camera` class in the file `camera_opencv.py`. See https://docs.opencv.org/3.4/dd/d43/tutorial_py_video_display.html for a tutorial on how to open a video stream from a webcam.
6) Implement the `run_client_opencv.py` script, that sends a message over `localhost` to a server implemented in the `run_server_opencv.py` script.
7) Open a new terminal and execute the `run_server_opencv.py` script.
8) Open a new terminal and execute the `run_client_opencv.py` script. You should now see a live stream from your webcam.
9) If time permits, work together in pairs and try to get the above system to work between two remote machines.

Tip: For an interactive introduction to python, follow the exercises on http://learnpython.org/
