import svgwrite
import math

def step_fractal_tree(dwg, iterations, x1, y1, angle, length):
    x2 = x1+length*math.sin(math.radians(angle))
    y2 = y1+length*math.cos(math.radians(180-angle))
    if iterations>1:
        step_fractal_tree(dwg, iterations-1, x2, y2, angle-30, 0.7*length)
        step_fractal_tree(dwg, iterations-1, x2, y2, angle+30, 0.7*length)
    dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(150, 10, 16, '%')))

def fractal_tree(dwg, iterations, size):
    step_fractal_tree(dwg, iterations, 0, 0, 0, size)

def step_fractal_triangle(dwg, iterations, triangle_coordinates):
    lines_coordinates = []
    for p in (0,1,2):
        new_coor = []
        for c in (0,1):
            if p == 2:
                new_coor.append((triangle_coordinates[2][c] + triangle_coordinates[0][c])/2)
            else:
                new_coor.append((triangle_coordinates[p][c] + triangle_coordinates[p+1][c])/2)
        lines_coordinates.append(new_coor)

    dwg.add(dwg.line(lines_coordinates[0], lines_coordinates[1], stroke=svgwrite.rgb(150, 10, 16, '%')))
    dwg.add(dwg.line(lines_coordinates[1], lines_coordinates[2], stroke=svgwrite.rgb(150, 10, 16, '%')))
    dwg.add(dwg.line(lines_coordinates[2], lines_coordinates[0], stroke=svgwrite.rgb(150, 10, 16, '%')))

    if iterations>1:
        step_fractal_triangle(dwg, iterations - 1, [triangle_coordinates[0], lines_coordinates[0], lines_coordinates[2]])
        step_fractal_triangle(dwg, iterations - 1, [lines_coordinates[0], triangle_coordinates[1], lines_coordinates[1]])
        step_fractal_triangle(dwg, iterations - 1, [lines_coordinates[2], lines_coordinates[1], triangle_coordinates[2]])

def fractal_triangle(dwg, iterations, size):
    lines_coordinates = [(0, 0),
                         (size*math.cos(math.radians(60)),-size*math.sin(math.radians(60))),
                         (size, 0)]
    dwg.add(dwg.line(lines_coordinates[0], lines_coordinates[1], stroke=svgwrite.rgb(150, 10, 16, '%')))
    dwg.add(dwg.line(lines_coordinates[1], lines_coordinates[2], stroke=svgwrite.rgb(150, 10, 16, '%')))
    dwg.add(dwg.line(lines_coordinates[2], lines_coordinates[0], stroke=svgwrite.rgb(150, 10, 16, '%')))
    step_fractal_triangle(dwg, iterations-1, lines_coordinates)

def make_fractal(fname, function, iterations):
    dwg = svgwrite.Drawing(fname, profile='tiny')
    function(dwg, iterations, 500)
    dwg.save()

make_fractal("ftree.svg", fractal_tree, 12)
make_fractal("ftriangle.svg", fractal_triangle, 7)