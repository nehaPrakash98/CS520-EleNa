# Simplified Elevation Navigation

## Demo and Code Walkthrough
The demo and code walkthrough of the project can be found here - https://drive.google.com/drive/folders/1Sjm5z_v_EfVoUKlxqfe60roCwewTEJ-A?usp=sharing

## Clone the project
Navigate to the folder where your project needs to be stored and run the following commands:

```
$ git clone https://github.com/Divya-Maiya/EleNa.git
$ cd EleNa
```

## Requirements - Download and Install Dependencies 
To download the required requirements for this project, run the following
```
$ pip install -r requirements.txt
```

## How to run the Project
**Backend**
1. Start by bringing up the backend server by executing the following commmands: 

```
$ pwd
```
Use the path obtained to populate and run the below command
```
$ export PYTHONPATH="${PYTHONPATH}:ABSOLUTE_PATH_TO_PROJECT_DIRECTORY"
```

Eg: export PYTHONPATH="${PYTHONPATH}:/Users/divyamaiya/IdeaProjects/cs520/elena/EleNa"

```
$ cd src/backend
$ python server.py
```
Upon successful execution of the above command, a Flask backend server should be running.

**Frontend**

2. To open the UI for the project, run the following in the root directory in a separate terminal: 

```
$ pwd
```
Use the path obtained to populate and run the below command
```
$ export PYTHONPATH="${PYTHONPATH}:ABSOLUTE_PATH_TO_PROJECT_DIRECTORY"
```

Eg: export PYTHONPATH="${PYTHONPATH}:/Users/divyamaiya/IdeaProjects/cs520/elena/EleNa"
```
$ cd src/frontend
```
For windows:
```
$ start selena.html
```

For Mac:
```
$ open selena.html
```

3. You should be able to see a browser window open the UI and the displayed screen should look like the one mentioned in the Output/Screenshots section of this ReadME. 

Note: While entering addresses in the UI, please use street addresses with zip code. This is essential for the application to run successfully. 
Examples of addresses that have been tested: 
1. Rolling Green Drive, Amherst, MA 01002, USA
2. Brandywine, Amherst, MA 01002, USA
3. Northeastern University, Huntington Avenue, Boston, MA 02115, USA
4. Boston University, Boston, MA 02215, USA

## How to test the Project
For testing, **Mockito**, **unittest** and **pytest** frameworks are used.

To run all unit tests, run the following commands from the root directory

If running in a new terminal, please run the follwoing commands first:
```
$ pwd
```
Use the path obtained to populate and run the below command
```
$ export PYTHONPATH="${PYTHONPATH}:ABSOLUTE_PATH_TO_PROJECT_DIRECTORY"
```

Eg: export PYTHONPATH="${PYTHONPATH}:/Users/divyamaiya/IdeaProjects/cs520/elena/EleNa"


```
$ cd test
$ python -m unittest
$ cd ..
```

## Best Programming Practices followed 
1. **Client-Server Architecture**: Interaction between JavaScript frontend and Python backend follows a Client-Server Architecture pattern.
2. **Model-View-Controller Architecture**: The Python backend follows an Model-View-Controller Architecture Pattern.
3. **Design Pattern**: A **template design pattern** is used by the algorithms (A*, Dijkstra's and BFS) implemented.
4. **Modularity / Code Organization**: The code has a package structure that shows modularity.
5. **Encapsulation**: Encapsulation has been achieved as the code is organized into classes
6. **Reusability**: Since the code is modular, it allows for reusability. 
7. **Test Suite**: A detailed test-suite has been included with a code-coverage of ~85%
8. **Type Safety / Exception Handling**: Exception handling has been included using try/except/raise blocks. 
9. **Version Control**: From the beginning of the project, **Git** has been used as a version control system.
10. **Debuggability**: Logging statements have been added to ensure debuggability.
11. **UI Usability**: The User interface was tested using manual testing and feedback was taken from various users


## Results  

### Frontend Screenshots
#### Initial UI screen to take user input: 
![image](https://user-images.githubusercontent.com/91640174/144970011-59f6c8d2-98e4-463f-886f-13b7dc54234e.png)


#### UI display of Elevation Path Statistics
![image](https://user-images.githubusercontent.com/91640174/144970028-6a8edc32-fdf0-41e0-9203-1f6d6c9286d3.png)


#### The final output map with the trace of the path: 
![image](https://user-images.githubusercontent.com/91640174/144970048-152b0d3a-8ab0-4790-9a2d-d1f611fa7da6.png)


### Algorithm performance 
The following table summarizes the time taken by all the algorithms - 
| Algorithm     | A*    | Dijkstra's    |     BFS       |
| ------------- | ------------- | ------------- | ------------- |
| Shortest Path  | 1.00  | 1.20  | 1.3627  |


### Code Coverage 

![image](https://user-images.githubusercontent.com/91640174/144973057-a9dabe8a-b697-4c5a-8731-10d8e36f6c60.png)


### Usability Survey
Form - https://forms.gle/wEAsN9YZ6NdXAHNX6

### System Architecture 
![image](https://user-images.githubusercontent.com/91640174/145915132-52f8aa36-34dd-4ad1-b56e-eb6360a02ead.png)



