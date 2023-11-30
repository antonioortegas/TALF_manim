from manim import *

class Video(Scene):
    def construct(self):
        
        #Camera background color to black
        self.camera.background_color = BLACK
        #Try to add audio to the scene if the file exists
        try:
            audio_path = "Bloque3/audio.wav"
            self.add_sound(audio_path, time_offset=1.0)
        except:
            print("There is no audio file in that path") 
        self.wait(1)
        
        
        video_title = Text("8.5 - Algunas Consideraciones sobre las MT").scale(0.8)
        self.play(Write(video_title), run_time=1)
        self.wait(4)
        self.play(FadeOut(video_title, shift=UP), run_time=2)
        self.wait(3)
        
        
        # Graphic representation of a Turing Machine
        # It is composed of
        #   a "tape" (an infinite sequence of cells on which symbols can be written)
        #   a "head" (the current cell)
        #   a rectangle that represents the machine itself
        
        # Tape (a series of squares arranged horizontally , each one with a symbol inside)
        number_of_cells = 25
        tape = VGroup()
        for i in range(0, number_of_cells):
            square = Rectangle(height=1, width=1, color=WHITE, fill_opacity=0.1, fill_color=WHITE)
            tape.add(square)
        tape.arrange(RIGHT, buff=0)
        tape.move_to(UP*2)
        self.play(Write(tape), run_time=3)
        
        # Head (a square that moves along the tape)
        # Highlight the central square
        head = Rectangle(height=1.1, width=1.1, color=YELLOW, fill_opacity=0.0, fill_color=WHITE).shift(UP*2)
        head.stroke_width = 5
        self.play(FadeIn(head, shift=UP), run_time=1)
        #Create upwards arrow pointing to the head
        arrow = Arrow(start=ORIGIN, end=UP, color=WHITE).scale(4.0)
        arrow.next_to(head, DOWN)
        self.play(Write(arrow), run_time=1)
        self.wait(2)
        
        # Machine (a rectangle containing the word "MT")
        machine = Rectangle(height=2, width=5, color=WHITE, fill_opacity=0.0, fill_color=WHITE).shift(DOWN*2)
        machine.stroke_width = 5
        machine_text = Text("MT").scale(1.5)
        machine_text.move_to(machine.get_center())
        self.play(FadeIn(machine, shift=UP), Write(machine_text), run_time=1)
        self.wait(7)
        
        # Number each cell of the tape with a number. The head is in cell 0, the next cell is 1, etc.
        cell_numbers = VGroup()
        for i in range(0, number_of_cells):
            cell_number = Text(str(i-(number_of_cells//2 - 2))).scale(0.5)
            cell_number.next_to(tape[i], UP)
            cell_numbers.add(cell_number)
        self.play(Write(cell_numbers), run_time=3)
        self.wait(3)
        
        # Move head, arrow and machine to the left twice
        # Put head, arrow, machine and machine_text in the same group
        MT = VGroup(head, arrow, machine, machine_text)
        self.play(MT.animate.shift(LEFT), run_time=1)
        self.play(MT.animate.shift(LEFT), run_time=1)
        # Return head, arrow, machine and machine_text to their original position
        self.wait(2)
        self.play(MT.animate.shift(RIGHT), run_time=1)
        self.play(MT.animate.shift(RIGHT), run_time=1)
        self.wait(1)
        
        # Move the numbers twice, so that number 0 is in the middle of the tape
        self.play(cell_numbers.animate.shift(RIGHT), run_time=1)
        self.play(cell_numbers.animate.shift(RIGHT), run_time=1)
        self.wait(13)
        
        
        # Put a symbol in each cell of the tape
        symbols = VGroup()
        for i in range(0, number_of_cells):
            symbol = Text("|").scale(0.7)
            if(i % 4 == 0):
                symbol = Text("*").scale(0.7)
            symbol.move_to(tape[i].get_center())
            symbols.add(symbol)
        self.play(Write(symbols), run_time=1)
        
        self.wait(3)

        # Replace the "|" symbol with a "@" symbol
        self.play(FadeOut(symbols), run_time=1)
        symbols2 = VGroup()
        for i in range(0, number_of_cells):
            symbol = Text("@").scale(0.7)
            if(i % 4 == 0):
                symbol = Text("*").scale(0.7)
            symbol.move_to(tape[i].get_center())
            symbols2.add(symbol)
        self.play(Write(symbols2), run_time=1)
        
        self.wait(3)
        self.play(FadeOut(symbols2), run_time=1)
        self.play(FadeIn(symbols), run_time=1)
        
        # Translation table
        text1 = Text("|||").scale(0.8).shift(RIGHT*4)
        text2 = Text("2").scale(0.8).next_to(text1, RIGHT).shift(RIGHT*0.5)
        text3 = Text("|||||").scale(0.8).next_to(text1, DOWN)
        text4 = Text("4").scale(0.8).next_to(text3, RIGHT).shift(RIGHT*0.5)
        # Create arrows between texts 1 and 2, and between texts 3 and 4
        arrow1 = Arrow(start=text1.get_right(), end=text2.get_left(), color=WHITE)
        arrow2 = Arrow(start=text3.get_right(), end=text4.get_left(), color=WHITE)
        # VGroup containing all the elements of the translation table
        translation_table = VGroup(text1, text2, text3, text4, arrow1, arrow2)
        self.wait(10)
        self.play(Write(translation_table), run_time=1)
        self.wait(7)
        
        self.play(FadeOut(text2), FadeOut(text4), run_time=1)
        text2 = Text("&").scale(0.8).next_to(text1, RIGHT).shift(RIGHT*0.5)
        text4 = Text("=").scale(0.8).next_to(text3, RIGHT).shift(RIGHT*0.5)
        self.play(Write(text2), Write(text4), run_time=1)
        translation_table = VGroup(text1, text2, text3, text4, arrow1, arrow2)
        self.wait(15)
        
        # Fade everything out
        self.play(FadeOut(tape),FadeOut(head), FadeOut(arrow), FadeOut(machine), FadeOut(machine_text), FadeOut(cell_numbers), FadeOut(translation_table), FadeOut(symbols), run_time=1)
        
        # Create new symbols, of the form "*|*||*|||*||||*|||||*||||||*"
        periodic = Text(". . . * * * | * | | * | | | * | | | | * | | | | | * | | | | | | * . . .").scale(0.7)
        self.play(Write(periodic), run_time=1)
        
        self.wait(27)
        
        self.play(FadeOut(periodic), run_time=1)
        self.wait(15)
        
        mt_diagram = ImageMobject("Bloque3/complex-TM.png").scale(1)
        self.play(FadeIn(mt_diagram, shift=DOWN), run_time=1)
        
        self.wait(15)
        
        self.play(FadeOut(mt_diagram), run_time=1)
        
        self.wait(5)
        
        tape.shift(LEFT*8)
        complete_MT = VGroup(MT, tape).scale(0.6).shift(LEFT*2)
        self.play(FadeIn(complete_MT), run_time=1) 
        
        # Paint two vertical lines separating the screen into three parts
        line1 = Line(start=UP*3, end=DOWN*3, color=WHITE).shift(LEFT*2.5)
        line2 = Line(start=UP*3, end=DOWN*3, color=WHITE).shift(RIGHT*2.5)
        self.play(Write(line1), Write(line2), run_time=1)
        
        # Write 2 ? symbols 
        question_mark1 = Text("?")
        question_mark2 = Text("?").shift(RIGHT*5)
        
        self.wait(2)
        self.play(Write(question_mark1), Write(question_mark2), run_time=1)
        
        self.wait(2)
        
        # Fade everything out
        self.play(FadeOut(complete_MT), FadeOut(line1), FadeOut(line2), FadeOut(question_mark1), FadeOut(question_mark2), run_time=1)
        
        self.wait(1)
        
        
        
        
        
        
#with tempconfig({"quality": "low_quality", "preview": True}):
#with tempconfig({"quality": "high_quality", "preview": True}):   
with tempconfig({"quality": "fourk_quality", "preview": True}):
    scene = Video()
    scene.render()