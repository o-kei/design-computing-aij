import bpy
import random

random.seed(0)
n = 7
a = 4.0
for i in range(n):
    for j in range(n):
        for k in range(n):
            b = 1.5*a * (i+j+k)/(3*n)
            loc = (a*i, a*j, a*k)
            translate_v = (random.random()*b, random.random()*b, random.random()*b)
            bpy.ops.mesh.primitive_cube_add(location=loc)
            bpy.ops.transform.translate(value=translate_v)
            