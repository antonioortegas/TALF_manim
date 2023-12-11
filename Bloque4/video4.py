from manim import *

class Video(Scene):
    def construct(self):
        
        #Camera background color to black
        self.camera.background_color = BLACK
        
        #Try to add audio to the scene if the file exists
        try:
            audio_path = "Bloque4/audio.wav"
            self.add_sound(audio_path, time_offset=1.0)
        except:
            print("There is no audio file in that path") 
        self.wait(1)
        
        video_title = Text("11.2 - Recursiva => WHILE-Computable").scale(0.8)
        self.play(Write(video_title), run_time=1)
        self.wait(3)
        self.play(FadeOut(video_title, shift=UP), run_time=2)
        
        img_route = "Bloque4/img/"
        # load every img in Bloque4/img folder
        rec_equal_while = ImageMobject(img_route + "rec_equal_while.png")
        while_in_rec = ImageMobject(img_route + "while_in_rec.png").shift(LEFT*3)
        rec_in_while = ImageMobject(img_route + "rec_in_while.png").shift(RIGHT*3)
        
        ini_in_while = ImageMobject(img_route + "ini_in_while.png")

        f_cero = ImageMobject(img_route + "f_cero.png")
        f_succesor = ImageMobject(img_route + "f_succesor.png")
        f_proyection = ImageMobject(img_route + "f_proyection.png").scale(1.2)
        
        ini_in_while2 = ImageMobject(img_route + "ini_in_while2.png").scale(1.5)
        
        composition_def = ImageMobject(img_route + "composition_def.png").shift(LEFT*3)
        composition_proof = ImageMobject(img_route + "composition_proof.png").shift(RIGHT*3)
        primitiverec_def = ImageMobject(img_route + "primitiverec_def.png").shift(LEFT*3)
        primitiverec_proof = ImageMobject(img_route + "primitiverec_proof.png").shift(RIGHT*3)
        minimization_def = ImageMobject(img_route + "minimization_def.png").shift(LEFT*3)
        minimization_proof = ImageMobject(img_route + "minimization_proof.png").shift(RIGHT*3)
        
        self.play(FadeIn(rec_equal_while, shift=UP*5), run_time=2)
        self.wait(12)
        self.play(FadeOut(rec_equal_while, shift=UP*5), run_time=2)
        
        self.play(FadeIn(while_in_rec, shift=UP*5), run_time=2)
        self.play(FadeIn(rec_in_while, shift=UP*5), run_time=2)
        self.wait(8)
        
        self.play(FadeOut(while_in_rec, shift=UP*5), run_time=2)
        self.wait(26)
        self.play(FadeOut(rec_in_while, shift=UP*5), run_time=2)
        self.wait(2)
        
        self.play(FadeIn(ini_in_while, shift=UP*5), run_time=2)
        self.wait(5)
        self.play(FadeOut(ini_in_while, shift=UP*5), run_time=2)
        
        self.play(FadeIn(f_cero, shift=UP*5), run_time=2)
        self.wait(18)
        self.play(FadeOut(f_cero, shift=UP*5), run_time=2)
        
        self.play(FadeIn(f_succesor, shift=UP*5), run_time=2)
        self.wait(20)
        self.play(FadeOut(f_succesor, shift=UP*5), run_time=2)
        
        self.play(FadeIn(f_proyection, shift=UP*5), run_time=2)
        self.wait(17)
        self.play(FadeOut(f_proyection, shift=UP*5), run_time=2)
        
        self.play(FadeIn(ini_in_while2, shift=UP*5), run_time=2)
        self.wait(2)
        self.play(FadeOut(ini_in_while2, shift=UP*5), run_time=2)
        
        self.play(FadeIn(composition_def, shift=UP*5), run_time=2)
        self.play(FadeIn(composition_proof, shift=UP*5), run_time=2)
        self.wait(38)
        
        self.play(FadeOut(composition_def, shift=UP*5), run_time=2)
        self.play(FadeOut(composition_proof, shift=UP*5), run_time=2)
        
        self.play(FadeIn(primitiverec_def, shift=UP*5), run_time=2)
        self.play(FadeIn(primitiverec_proof, shift=UP*5), run_time=2)
        self.wait(37)
        
        self.play(FadeOut(primitiverec_def, shift=UP*5), run_time=2)
        self.play(FadeOut(primitiverec_proof, shift=UP*5), run_time=2)
        
        self.play(FadeIn(minimization_def, shift=UP*5), run_time=2)
        self.play(FadeIn(minimization_proof, shift=UP*5), run_time=2)
        self.wait(53)
        
        self.play(FadeOut(minimization_def, shift=UP*5), run_time=2)
        self.play(FadeOut(minimization_proof, shift=UP*5), run_time=2)
        
        rec_in_while.move_to(ORIGIN)
        rec_equal_while.shift(RIGHT*3)
        rec_in_while.shift(LEFT*3)
        
        self.play(FadeIn(rec_in_while, shift=UP*5), run_time=2)
        self.wait(7)
        self.play(FadeIn(rec_equal_while, shift=UP*5), run_time=2)
        self.wait(5)
        self.play(FadeOut(rec_in_while, shift=UP*5), run_time=2)
        self.play(rec_equal_while.animate.shift(LEFT*3), run_time=2)
        self.wait(2)
        self.play(FadeOut(rec_equal_while, shift=UP*5), run_time=2)
        
#with tempconfig({"quality": "low_quality", "preview": True}):
with tempconfig({"quality": "high_quality", "preview": True}):   
#with tempconfig({"quality": "fourk_quality", "preview": True}):
    scene = Video()
    scene.render()