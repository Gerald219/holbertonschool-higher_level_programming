# python-serialization

## goal
save data to a file and loading it back (called serialization and deserialization).

---

## task 0 - basic serialization
- take a python dictionary  
- save it into a json file  
- read that json file back into python  
- tool used: `json` module  

---

## task 1 - pickle
- save a custom object into a file and open it again later  
- class: `CustomObject` with name, age, is_student  
- used the `pickle` tool that freezes an object and restores it exactly the same  

---

## task 2 - csv to json
- read data from a csv file  
- turn each row into a dictionary  
- save all rows into a `data.json` file  
- tool used: `csv` and `json` modules  

---

## task 3 - xml
- convert a dictionary into xml text and back into a dictionary  
- saved and read using `ElementTree` (python’s built-in xml tool)  
- keeps all values as text for simplicity  

---

## task 4 - network serialization
- made a simple server and client that share data  
- client sends a dictionary as json text  
- server receives it, turns it back into a dictionary, and prints it  
- tools used: `socket` and `json`  
