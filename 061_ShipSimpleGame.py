import ppb
from ppb.features import default_sprites


class Ship(default_sprites.TargetSprite):
    speed = 5

    def on_mouse_motion(self, event: ppb.events.MouseMotion, signal):
        self.target = event.position
        self.facing = event.position - self.position


ppb.run(lambda scene: scene.add(Ship()))
