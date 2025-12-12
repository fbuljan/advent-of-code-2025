from pathlib import Path

def main():
    p = Path("input.txt")
    points = []
    
    with p.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                x, y = (int(part) for part in line.split(','))
            except ValueError:
                continue
            points.append((x, y))

    vertical_edges = []
    horizontal_edges = []
    
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        
        if x1 == x2:
            y_min, y_max = min(y1, y2), max(y1, y2)
            vertical_edges.append((x1, y_min, y_max))
        else:
            x_min, x_max = min(x1, x2), max(x1, x2)
            horizontal_edges.append((y1, x_min, x_max))

    def is_on_border(x, y):
        for ex, ey_min, ey_max in vertical_edges:
            if x == ex and ey_min <= y <= ey_max:
                return True
        for ey, ex_min, ex_max in horizontal_edges:
            if y == ey and ex_min <= x <= ex_max:
                return True
        return False

    def is_point_inside(x, y):
        crossings = 0
        for ex, ey_min, ey_max in vertical_edges:
            if ex > x and ey_min < y < ey_max:
                crossings += 1
        return crossings % 2 == 1

    def is_valid_point(x, y):
        return is_on_border(x, y) or is_point_inside(x, y)

    def is_rectangle_valid(x1, y1, x2, y2):
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        
        for y in [min_y, max_y]:
            crossings = [min_x, max_x]
            for ex, ey_min, ey_max in vertical_edges:
                if min_x <= ex <= max_x and ey_min <= y <= ey_max:
                    crossings.append(ex)
            crossings = sorted(set(crossings))
            
            for k in range(len(crossings) - 1):
                mid_x = (crossings[k] + crossings[k+1]) / 2
                if not is_valid_point(mid_x, y):
                    return False
        
        for x in [min_x, max_x]:
            crossings = [min_y, max_y]
            for ey, ex_min, ex_max in horizontal_edges:
                if min_y <= ey <= max_y and ex_min <= x <= ex_max:
                    crossings.append(ey)
            crossings = sorted(set(crossings))
            
            for k in range(len(crossings) - 1):
                mid_y = (crossings[k] + crossings[k+1]) / 2
                if not is_valid_point(x, mid_y):
                    return False
        
        return True
    
    largest_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            
            if area > largest_area and is_rectangle_valid(x1, y1, x2, y2):
                largest_area = area

    print(largest_area)

if __name__ == "__main__":
    main()
