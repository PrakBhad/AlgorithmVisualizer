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

### Keybinds:

*   **r:** Randomize the array
*   **b:** Bubble sort
*   **i:** Insertion sort
*   **s:** Selection sort
*   **d:** Toggle between ascending and descending order (Default is ascending)
*   **c:** Comparison mode (Special mode, where FPS is lowered, and the elements currently being evaluated by the sorting algorithm are highlighted in red in real-time. Default is False).

### FPS Adjustment:

To change the FPS in comparison mode, modify the values within the `elif event.key == pygame.K_c:` block and also within the `def main` function in `app.py`.

## **Licence**
[MIT Licence](LICENSE)
