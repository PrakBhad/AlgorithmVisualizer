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

## Additional Info
Do not resize Window During sorting or graph visualization, as that will stop it!

### Keybinds:

*   **r:** Randomize the array
*   **b:** Bubble sort
*   **i:** Insertion sort
*   **s:** Selection sort
*   **m:** Merge sort
*   **d:** Toggle between ascending and descending order (Default is ascending, which is set to True)
*   **c:** Comparison mode (Special mode, where FPS is lowered, elements are highlighted red)
*   **f** Full Screen Mode for immersion

### FPS Adjustment:

To change the FPS values in each mode, change the return values in `fps_toggler`.
Current Values:
Compare mode: 15
Sorting mode: 600

## **Licence**
[MIT Licence](LICENSE)
