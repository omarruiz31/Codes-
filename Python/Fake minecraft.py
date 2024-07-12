from ursina import *

app = Ursina()

# Configurar la ventana
window.title = 'Minecraft Sencillo'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False

# Configurar la cámara
camera.fov = 90
camera.position = (0, 30, -35)
camera.rotation_x = 45

# Clase Voxel para los bloques
class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.white,
            highlight_color=color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
            elif key == 'right mouse down':
                destroy(self)

# Crear bloques en un patrón básico
for x in range(-8, 9):
    for z in range(-8, 9):
        voxel = Voxel(position=(x, 0, z))

# Controlador de primera persona para el jugador
app.run()
