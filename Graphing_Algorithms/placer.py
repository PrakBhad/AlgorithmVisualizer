import math
def choose_component(component, current_component):
    if component == 1:
        current_component[0] = "Node"
    elif component == 2:
        current_component[0] = "Line"


def near_circle(pos, circles):
    for circle in circles:
        distance = ((pos[0]-circle[0])**2 + (pos[1]-circle[1])**2)**0.5
        if distance <= 15:
            return circle
    return None


def point_to_line_distance(point, line_start, line_end):
    # Vector from line_start to line_end
    line_vec = (line_end[0] - line_start[0], line_end[1] - line_start[1])
    # Vector from line_start to point
    point_vec = (point[0] - line_start[0], point[1] - line_start[1])

    # Dot product of line_vec and point_vec
    line_len_sq = line_vec[0]**2 + line_vec[1]**2
    if line_len_sq == 0:  # Degenerate case: the line segment has zero length
        return math.hypot(point[0] - line_start[0], point[1] - line_start[1])

    dot = (point_vec[0] * line_vec[0] +
           point_vec[1] * line_vec[1]) / line_len_sq

    # Project the point onto the line, clamping the projection to the line segment
    closest_point = (
        line_start[0] + dot * line_vec[0],
        line_start[1] + dot * line_vec[1]
    )

    # Calculate the distance from the point to the closest point on the line segment
    return math.hypot(point[0] - closest_point[0], point[1] - closest_point[1])


def near_line(mouse_pos, lines, threshold=5):
    for line in lines:
        start, end, _ = line
        if point_near_line(mouse_pos, start, end, threshold):
            return line
    return None


def point_near_line(p, a, b, threshold):
    """Check if point p is within `threshold` pixels of line segment ab."""
    ax, ay = a
    bx, by = b
    px, py = p

    # Compute distance from p to line segment ab
    line_len_sq = (bx - ax)**2 + (by - ay)**2
    if line_len_sq == 0:
        return math.hypot(px - ax, py - ay) < threshold

    t = max(0, min(1, ((px - ax) * (bx - ax) + (py - ay) * (by - ay)) / line_len_sq))
    proj_x = ax + t * (bx - ax)
    proj_y = ay + t * (by - ay)

    return math.hypot(px - proj_x, py - proj_y) < threshold



def remove_components(circles: list, Lines: list):
    circles.clear()
    Lines.clear()
