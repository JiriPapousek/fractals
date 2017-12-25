import svgwrite
import math

golden_ratio = 0.618

def step_fractal_tree(img, iterations, color, x1, y1, angle, length):
    """
    Recursive procedure creating a line and than calls itself twice for
    making two separate branches.
    """
    x2 = x1+length*math.sin(math.radians(angle))
    y2 = y1+length*math.cos(math.radians(180-angle))
    img.add(img.line((x1, y1), (x2, y2), stroke=color))
    if iterations > 1:
        step_fractal_tree(img, iterations - 1, color, x2, y2, angle - 30, 0.7 * length)
        step_fractal_tree(img, iterations - 1, color, x2, y2, angle + 30, 0.7 * length)

def fractal_tree(img, iterations, size, color):
    """
    Initial step for making a fractal tree.
    """
    step_fractal_tree(img, iterations, color, 0, 0, 0, size)

def step_fractal_triangle(img, iterations, color, triangle_coordinates):
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
        img.add(img.line(new[i[0]], new[i[1]], stroke=color))

    #Starts recursion on new triangles made in the corners of the old triangle.
    if iterations>1:
        step_fractal_triangle(img, iterations - 1, color, [old[0], new[0], new[2]])
        step_fractal_triangle(img, iterations - 1, color, [new[0], old[1], new[1]])
        step_fractal_triangle(img, iterations - 1, color, [new[2], new[1], old[2]])

def fractal_triangle(img, iterations, size, color):
    """
    Initial step of making Sierpinski triangle. Than it activates the
    recursive procedure of splitting the triangle.
    """
    a = math.radians(60)
    new = [(0, 0), (size*math.cos(a),-size*math.sin(a)), (size, 0)]

    for i in ([0, 1], [1, 2], [2, 0]):
        img.add(img.line(new[i[0]], new[i[1]], stroke=color))

    step_fractal_triangle(img, iterations-1, color, new)

def golden_fractal_step(img, iterations, color, center, start, dir, mode):
    p = img.path('m' + str(start[0]) + ',' + str(start[1]),fill = 'none', stroke = color)
    r = (center[1]-start[1],-center[0]+start[0])

    if dir==mode:
        target = (center[0] + r[0], center[1] + r[1])
    else:
        target = (center[0] - r[0], center[1] - r[1])

    next1 = (target[0] + r[0]*golden_ratio, target[1] + r[1]*golden_ratio)
    next2 = (target[0] - r[0]*golden_ratio, target[1] - r[1]*golden_ratio)

    p.push_arc(target, r=math.fabs(r[0]+r[1]), rotation=0,large_arc=False, absolute=True, angle_dir=dir)
    img.add(p)

    if iterations>1:
        golden_fractal_step(img, iterations - 1, color, next1, target, '-', mode)
        golden_fractal_step(img, iterations - 1, color, next2, target, '+', mode)

def golden_fractal_imp(img, iterations, size, color):
    golden_fractal_step(img, iterations - 1, color, (-size,0), (0, 0), '-', '-')
    golden_fractal_step(img, iterations - 1, color, (size,0), (0, 0), '+', '-',)

def golden_fractal_exp(img, iterations, size, color):
    golden_fractal_step(img, iterations - 1, color, (-size,0), (0, 0), '-', '+')
    golden_fractal_step(img, iterations - 1, color, (size,0), (0, 0), '+', '+')


def make_fractal(fname, function, iterations, base_size, color):
    """
    General function for creating fractal based on the given function.
    """
    img = svgwrite.Drawing(fname, profile='full')
    function(img, iterations, base_size, color)
    img.save()

color = 'blue'
make_fractal("ftree.svg", fractal_tree, 12, 300, color)
make_fractal("ftriangle.svg", fractal_triangle, 7, 300, color)
make_fractal('goldenf1.svg', golden_fractal_imp, 10, 300, color)
make_fractal('goldenf2.svg', golden_fractal_exp, 10, 300, color)