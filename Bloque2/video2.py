from manim import *

class Video(Scene):
    def construct(self):
        
        #Camera background color to black
        self.camera.background_color = BLACK
        
        #Try to add audio to the scene if the file exists
        try:
            audio_path = "Bloque2/audio.wav"
            self.add_sound(audio_path, time_offset=1.0)
        except:
            print("There is no audio file in that path") 
        self.wait(1)
        
        video_title = Text("4.3 - Autómata Finito Determinista Mínimo").scale(0.8)
        self.play(Write(video_title), run_time=1)
        self.wait(3)
        self.play(FadeOut(video_title, shift=UP), run_time=2)
        
        simple_DFA = ImageMobject("Bloque2/simpleDFA.png").shift(LEFT*3)
        simple_NFA = ImageMobject("Bloque2/simpleNFA.png").shift(RIGHT*3)
        
        self.play(FadeIn(simple_DFA, shift=LEFT), run_time=2)
        self.wait(2)
        self.play(FadeIn(simple_NFA, shift=RIGHT), run_time=2)
        self.wait(5) 
        # double arrow implication
        double_arrow = DoubleArrow(simple_DFA.get_edge_center(RIGHT), simple_NFA.get_edge_center(LEFT), color=WHITE)
        self.play(GrowArrow(double_arrow))
        self.wait(3)
        
        lr_arrow = Arrow(simple_DFA.get_edge_center(RIGHT), simple_NFA.get_edge_center(LEFT), color=WHITE)
        rl_arrow = Arrow(simple_NFA.get_edge_center(LEFT), simple_DFA.get_edge_center(RIGHT), color=WHITE)
        self.play(Transform(double_arrow, lr_arrow))
        self.play(Indicate(double_arrow))
        self.wait(7)
        self.play(Transform(double_arrow, rl_arrow))
        self.play(Indicate(double_arrow))
        
        #Animations to FadeOut the images
        self.play(FadeOut(simple_DFA, shift=LEFT), run_time=1)
        self.play(FadeOut(simple_NFA, shift=RIGHT), run_time=1)
        self.wait(1)
        
        power_set_construction_Text = Text("Powerset Construction").scale(0.4)
        #place it under the double arrow
        power_set_construction_Text.next_to(double_arrow, DOWN)
        self.play(Write(power_set_construction_Text))
        
        #create a new NDA
        complex_NFA = ImageMobject("Bloque2/complexNFA.png").shift(RIGHT*3)
        self.play(FadeIn(complex_NFA, shift=LEFT), run_time=2)
        self.wait(2)
        complex_DFA = ImageMobject("Bloque2/complexDFA.png").shift(LEFT*4).scale(0.7)
        self.play(FadeIn(complex_DFA, shift=RIGHT), run_time=2)
        self.wait(5)
        
        #write "n" below the NFA and 2^n below the DFA
        n_text = Text("n").scale(0.5).next_to(complex_NFA, DOWN)
        self.play(Write(n_text))
        self.wait(2)
        two_n_text = Tex(r"$2^{n}$").scale(0.5).next_to(complex_DFA, DOWN)
        self.play(Write(two_n_text))
        self.wait(4)
        
        #FadeOut everything
        self.play(Unwrite(n_text), run_time=1)
        self.play(Unwrite(two_n_text), run_time=1)
        self.play(FadeOut(complex_NFA, shift=LEFT), run_time=1)
        self.play(FadeOut(complex_DFA, shift=RIGHT), run_time=1)
        self.play(FadeOut(power_set_construction_Text), run_time=1)
        self.play(FadeOut(double_arrow), run_time=1)
        self.wait(1)
        
        #Create a big question mark symbol and place it in the center of the screen
        question_mark = Text("?").scale(5)
        self.play(Write(question_mark))
        self.wait(5)
        
        #FadeOut the question mark
        self.play(FadeOut(question_mark), run_time=1)
        
        # Create a text
        #\forall{M}AFD
        proposicion_p1 = Tex(r"$\forall{M}\;AFD$").scale(0.8)
        #\exists{M}'\;AFDM
        proposicion_p2 = Tex(r"$\exists{M}'\;AFDM$").scale(0.8)
        #\mid M\equiv {M}'
        proposicion_p3 = Tex(r"$\mid M\equiv {M}'$").scale(0.8)
        #place one next to the other to make a sentence
        proposicion = VGroup(proposicion_p1, proposicion_p2, proposicion_p3).arrange_submobjects(RIGHT)
        #place it in the center of the screen
        proposicion.move_to(ORIGIN)
        self.play(Write(proposicion), run_time=2)
        self.wait(5)
        
        #Shift the text up
        self.play(proposicion.animate.shift(UP*2), run_time=1)
        
        def_img = ImageMobject("Bloque2/def.png").scale(1.0)
        #Show the img
        self.play(FadeIn(def_img, shift=UP), run_time=2)
        self.wait(39)
        
        #FadeOut everything
        self.play(FadeOut(def_img, shift=DOWN), run_time=1)
        self.play(FadeOut(proposicion, shift=DOWN), run_time=1)
        
        #Create a new text "Algoritmo de Hopcroft"
        hopcroft_text = Text("Algoritmo de Hopcroft").scale(0.8)
        #place it in the center of the screen, but shifted up
        hopcroft_text.move_to(UP*2)
        self.play(Write(hopcroft_text), run_time=1)
        self.wait(1)
        
        hopcroft_img = ImageMobject("Bloque2/hopcroft.png").scale(2)
        #Show the img
        hopcroft_img.next_to(hopcroft_text, DOWN)
        self.play(FadeIn(hopcroft_img, shift=UP), run_time=2)
        self.wait(2)

        #FadeOut everything
        self.play(FadeOut(hopcroft_img, shift=DOWN), run_time=1)
        self.play(FadeOut(hopcroft_text, shift=DOWN), run_time=1)
        self.wait(1)
        
        #show the proposition again
        proposicion.scale(2).move_to(ORIGIN)
        self.play(Write(proposicion), run_time=2)
        
        
        
        
        
        
        
        
        
#with tempconfig({"quality": "low_quality", "preview": True}):
#with tempconfig({"quality": "high_quality", "preview": True}):   
with tempconfig({"quality": "fourk_quality", "preview": True}):
    scene = Video()
    scene.render()