# Visualizer README

This project is a sorting algorithm visualizer built using Python and Pygame. It allows you to visualize various sorting algorithms in real-time, with customizable settings such as FPS and sorting modes.

## Step 1: Setting Up Environment
Create a Conda Environment
To create a new Conda environment for this project, use the following command:

```sh
conda create -n "visualizer" python=3.11
```
To activate conda environment
```bash
conda activate visualizer
```

## Step 2: Installing Libraries
To install libraries
```bash
pip install -r requirements.txt
```
To make sure there is no update
```bash
pip freeze
```

## Step 3:Starting App
To start app run
```bash
python app.py
```
## **Graphing Mode Controls**
- **Left Click**: Place a node or a line  
- **Right Click**: Remove a line or a node  

## **Colour Coding**
### **Sorting:**
- 🟩 **Green**: Normal colour of the bar  
- 🔴 **Red**: Elements that are being compared  

### **Graphing:**
- 🟣 **Purple**: Goal node  
- 🟩 **Green**: Start node  
- 🔴 **Red**: Final path from goal to start  
- 🟡 **Yellow**: Explored area  

## **Licence**
[MIT Licence](LICENSE)
