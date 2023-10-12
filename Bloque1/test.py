from manim import *

class VennDiagram(Scene):
    def construct(self):
        # Create 5 circles
        test = 1
        
#with tempconfig({"quality": "low_quality", "preview": True}):
with tempconfig({"quality": "high_quality", "preview": True}):
    scene = VennDiagram()
    scene.render()