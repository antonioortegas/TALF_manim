from manim import *

class ToyExample(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        
#with tempconfig({"quality": "low_quality", "preview": True}):
with tempconfig({"quality": "high_quality", "preview": True}):
    scene = ToyExample()
    scene.render()