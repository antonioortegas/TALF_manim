from manim import *

class Video(Scene):
    def construct(self):
        
        self.camera.background_color = BLACK
        
        
        
#with tempconfig({"quality": "high_quality", "preview": True, "save_last_frame": True}):   
#with tempconfig({"quality": "low_quality", "preview": True}):
with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Video()
    scene.render()