import svgwrite
import math

def step_fractal_tree(dvg, iterations, x1, y1, angle, length):
    x2 = x1+length*math.sin(math.radians(angle))
    y2 = y1+length*math.cos(math.radians(180-angle))
    print(x1," ",y1,":",x2," ",y2)
    if iterations>1:
        step_fractal_tree(dvg, iterations-1, x2, y2, angle-30, 0.7*length)
        step_fractal_tree(dvg, iterations-1, x2, y2, angle+30, 0.7*length)
    dvg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(150, 10, 16, '%')))

def make_fractal(step, iterations):
    dwg = svgwrite.Drawing('fractal.svg', profile='tiny')
    step(dwg, iterations,0,0,0,100)
    dwg.save()

make_fractal(step_fractal_tree,12)