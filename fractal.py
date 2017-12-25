import svgwrite
import math

def step_fractal_tree(img, iterations, x1, y1, angle, length):
    """
    Recursive procedure creating a line and than calls itself twice for
    making two separate branches.
    """
    x2 = x1+length*math.sin(math.radians(angle))
    y2 = y1+length*math.cos(math.radians(180-angle))
    img.add(img.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(150, 10, 16, '%')))
    if iterations > 1:
        step_fractal_tree(img, iterations - 1, x2, y2, angle - 30, 0.7 * length)
        step_fractal_tree(img, iterations - 1, x2, y2, angle + 30, 0.7 * length)

def fractal_tree(img, iterations, size):
    """
    Initial step for making a fractal tree.
    """
    step_fractal_tree(img, iterations, 0, 0, 0, size)

def step_fractal_triangle(img, iterations, triangle_coordinates):
    """
    Makes one iteration of splitting the triangle into four equal triangles.
    Than it recursively continues by splitting three triangles in the corners.
    """

    new = []
    old = triangle_coordinates

    #Finds coordinates for splitting the triangle.
    for i in ([0, 1], [1, 2], [2, 0]):
        new.append([(old[i[0]][0] + old[i[1]][0])/2,
                    (old[i[0]][1] + old[i[1]][1])/2])

    #Makes three lines splitting old triangle into four equal triangles.
    for i in ([0, 1], [1, 2], [2, 0]):
        img.add(img.line(new[i[0]], new[i[1]], stroke=svgwrite.rgb(150, 10, 16, '%')))

    #Starts recursion on new triangles made in the corners of the old triangle.
    if iterations>1:
        step_fractal_triangle(img, iterations - 1, [old[0], new[0], new[2]])
        step_fractal_triangle(img, iterations - 1, [new[0], old[1], new[1]])
        step_fractal_triangle(img, iterations - 1, [new[2], new[1], old[2]])

def fractal_triangle(img, iterations, size):
    """
    Initial step of making Sierpinski triangle. Than it activates the
    recursive procedure of splitting the triangle.
    """
    a = math.radians(60)
    new = [(0, 0), (size*math.cos(a),-size*math.sin(a)), (size, 0)]

    for i in ([0, 1], [1, 2], [2, 0]):
        img.add(img.line(new[i[0]], new[i[1]], stroke=svgwrite.rgb(150, 10, 16, '%')))

    step_fractal_triangle(img, iterations-1, new)

def make_fractal(fname, function, iterations):
    """
    General function for creating fractal based on the given function.
    """
    img = svgwrite.Drawing(fname, profile='full')
    function(img, iterations, 500)
    img.save()

make_fractal("ftree.svg", fractal_tree, 12)
make_fractal("ftriangle.svg", fractal_triangle, 7)