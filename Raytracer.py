from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 500
height = 500

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)

mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)

blueMirror = Material(diffuse = (0.2, 0.2, 0.9), spec = 64, matType = REFLECTIVE)
yellowMirror = Material(diffuse = (0.9, 0.9, 0.2), spec = 64, matType = REFLECTIVE)

rtx = Raytracer(width, height)

rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))
#rtx.lights.append( PointLight(point = (0,0,0)))

rtx.scene.append( Sphere(V3(0,0,-10), 1, glass)  )

# rtx.scene.append( Sphere(V3(3,0,-10), 1, brick)  )
# rtx.scene.append( Sphere(V3(0,3,-10), 1, stone)  )

# rtx.scene.append( Sphere(V3(-3,0,-10),1, blueMirror)  )
# rtx.scene.append( Sphere(V3(0,-3,-10), 1, yellowMirror)  )


rtx.glRender()

rtx.glFinish("output.bmp")