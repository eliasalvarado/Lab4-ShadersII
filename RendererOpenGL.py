import pygame as pg
from pygame.locals import *
from OpenGL.GL import GL_TRUE, glReadPixels, GL_RGB, GL_UNSIGNED_BYTE, GL_TRUE
import glm

from gl import Renderer
from Model import Model
from shaders import vertexShader, fragmentShader, pruebaShader

from glm import vec3


width = 960
height = 540

pg.init()

screen = pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF)
clock = pg.time.Clock()

renderer = Renderer(screen)

renderer.setShader(vertexShader, pruebaShader)

renderer.loadModel(filename="model.obj",
                   textureFile="model.bmp",
                   potition=(0,0,-5),
                   rotation=(0,0,0),
                   scale=(3,3,3))


speed = 10
isRunning = True
while isRunning:

    keys = pg.key.get_pressed()
    deltaTime = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                isRunning = False
            elif event.key == pg.K_SPACE:
                size = screen.get_size()
                buffer = glReadPixels(0, 0, *size, GL_RGB, GL_UNSIGNED_BYTE)
                pg.display.flip()
                screen_surf = pg.image.fromstring(buffer, size, "RGB", GL_TRUE)
                pg.image.save(screen_surf, "output.jpg")

    if keys[K_RIGHT]:
        renderer.camPosition.x += deltaTime  * speed
    elif keys[K_LEFT]:
        renderer.camPosition.x -= deltaTime  * speed
    if keys[K_UP]:
        renderer.camPosition.y += deltaTime  * speed
    elif keys[K_DOWN]:
        renderer.camPosition.y -= deltaTime  * speed
    if keys[K_MINUS]:
        renderer.camPosition.z += deltaTime  * speed
    elif keys[K_PERIOD]:
        renderer.camPosition.z -= deltaTime  * speed

    if keys[K_a]:
        renderer.camRotation.y += deltaTime * speed ** 2
    elif keys[K_d]:
        renderer.camRotation.y -= deltaTime * speed ** 2
    if keys[K_w]:
        renderer.camRotation.x += deltaTime * speed ** 2
    elif keys[K_s]:
        renderer.camRotation.x -= deltaTime * speed ** 2
        
    if keys[K_1]:
        renderer.directionalLight = vec3(1,0,0)
    elif keys[K_2]:
        renderer.directionalLight = vec3(-1,0,0)
    elif keys[K_3]:
        renderer.directionalLight = vec3(0,1,0)
    elif keys[K_4]:
        renderer.directionalLight = vec3(0,-1,0)
    elif keys[K_5]:
        renderer.directionalLight = vec3(0,0,1)
    elif keys[K_6]:
        renderer.directionalLight = vec3(0,0,-1)

    renderer.time += deltaTime
        
    renderer.render()
    pg.display.flip()


pg.quit()

