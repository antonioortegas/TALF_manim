from manim import *

class Video(Scene):
    def construct(self):
        
        #Camera background color to black
        self.camera.background_color = BLACK
        
        #Try to add audio to the scene if the file exists
        try:
            audio_path = "Bloque1/audio.wav"
            self.add_sound(audio_path, time_offset=1.0)
        except:
            print("There is no audio file in that path") 
        self.wait(1)
        
        video_title = Text("2.11 - Cierre de los Tipos de Lenguajes").scale(0.8)
        self.play(Write(video_title), run_time=1)
        self.wait(24)
        self.play(FadeOut(video_title, shift=UP), run_time=2)
        
        #28
        # Text - Closure definition
        texto_ser_cerrado = Tex(r"$A\: es \: cerrado\: para \: \bullet \Leftrightarrow \forall a,b \in A, \: a\bullet b \in A$") 
        self.play(Write(texto_ser_cerrado), run_time=3)
        self.wait(7)
        self.play(texto_ser_cerrado.animate.shift(UP*2.5), run_time=1.0)
        
        #39
        # Create a figure of the natural set and its elements
        naturalSet = Circle(radius=1.5, color=WHITE, fill_opacity=0.1, fill_color=WHITE)
        naturalSet.shift(DOWN*0.8)
        naturalSetLabel = Tex(r"$\mathbb{N}$", color=WHITE).next_to(naturalSet.get_top(), UP)
        pentagon = Polygon(*[naturalSet.point_from_proportion(i/5) for i in range(5)], color=BLUE).scale(0.6)
        naturalSetElements = VGroup()
        for i in range(5):
            naturalSetElements.add(Tex(str(i), color=WHITE).move_to(pentagon.get_vertices()[i]))
        naturalSetGroup = VGroup(naturalSet, naturalSetLabel, naturalSetElements)
        self.play(DrawBorderThenFill(naturalSet), run_time=1.0)
        self.play(Write(naturalSetLabel), run_time=1)
        self.play(Write(naturalSetElements), run_time=1.0)
        self.wait(2)
        self.play(naturalSetGroup.animate.shift(LEFT*2.75), run_time=1.0)
        
        #45
        # Create the boxes for the operations and the classification
        operation_box = Rectangle(height=1.5, width=1.5, color=WHITE, fill_opacity=0.2, fill_color=WHITE)
        classification_box = Rectangle(height=1.5, width=1.5, color=WHITE, fill_opacity=0.2, fill_color=WHITE)
        boxes = VGroup(operation_box, classification_box)
        boxes.arrange(DOWN, buff=1)
        boxes.shift(RIGHT*2.75)
        boxes.shift(DOWN*0.8)
        text_sum_symbol = Tex(r"$+$", color=WHITE).move_to(operation_box.get_center()).scale(1.5)
        text_classification_symbol = Tex(r"$\mathbb{N}?$", color=WHITE).move_to(classification_box.get_center())
        self.play(DrawBorderThenFill(operation_box), run_time=1.0)
        self.play(Write(text_sum_symbol), run_time=1.0)
        self.wait(4)
        
        #51
        # Copy the elements of the natural set to operate with them
        number1 = naturalSetElements[1].copy()
        number3 = naturalSetElements[3].copy()
        self.play(number1.animate.next_to(operation_box, LEFT), run_time=0.5)
        self.play(FadeOut(number1, shift=RIGHT), run_time=0.5)
        self.play(number3.animate.next_to(operation_box, LEFT), run_time=0.5)
        self.play(FadeOut(number3, shift=RIGHT), run_time=0.5)
        
        #53
        # Create the number 4
        number4 = naturalSetElements[4].copy()
        middlePoint = (operation_box.get_center() + classification_box.get_center())/2
        number4.move_to(middlePoint)
        self.play(FadeIn(number4, shift=DOWN), run_time=1.0)
        self.wait(2)
        
        #56
        # Animate the classification box
        self.play(DrawBorderThenFill(classification_box), run_time=1.0)
        self.play(Write(text_classification_symbol), run_time=1.0)
        
        #58
        # Classify the number 4
        self.play(FadeOut(number4, shift=DOWN), run_time=1.0)
        
        #59
        # Number 4 is a natural number
        number4.move_to(classification_box.get_center() + LEFT*1.2)
        number4.color = GREEN
        self.play(FadeIn(number4, shift=LEFT), run_time=1.0)
        self.play(Indicate(number4), run_time=1.0, color=GREEN)
        self.play(number4.animate.move_to(naturalSetElements[4]), run_time=1.0)
        self.wait(3)
        # Indicate pairs of numbers that are in the natural set
        self.play(Indicate(VGroup(naturalSetElements[2], naturalSetElements[1])), run_time=1.0, color=YELLOW)
        self.play(Indicate(VGroup(naturalSetElements[0], naturalSetElements[3])), run_time=1.0, color=YELLOW)
        self.play(Indicate(VGroup(naturalSetElements[1], naturalSetElements[0])), run_time=1.0, color=YELLOW)
        self.wait(5)
        
        #1:13
        # Change the operation symbol to a subtraction symbol
        text_substraction_symbol = Tex(r"$-$", color=WHITE).move_to(operation_box.get_center()).scale(1.5)
        self.play(FadeTransform(text_sum_symbol, text_substraction_symbol), run_time=1.0)
        self.wait(1)
        
        #1:15
        # Operate with the number 1 and the number 3
        number1 = naturalSetElements[1].copy()
        number3 = naturalSetElements[3].copy()
        self.play(number1.animate.next_to(operation_box, LEFT), run_time=0.5)
        self.play(FadeOut(number1, shift=RIGHT), run_time=0.5)
        self.play(number3.animate.next_to(operation_box, LEFT), run_time=0.5)
        self.play(FadeOut(number3, shift=RIGHT), run_time=0.5)
        
        #1:17
        # Create the number -2
        numberMinus2 = Tex(r"$-2$", color=WHITE).move_to(middlePoint)
        self.play(FadeIn(numberMinus2, shift=DOWN), run_time=1.0)
        self.wait(1)
        self.play(FadeOut(numberMinus2, shift=DOWN), run_time=1.0)
        
        #1:20
        # Classify the number -2
        numberMinus2.move_to(classification_box.get_center() + LEFT*1.2)
        numberMinus2.color = RED
        self.play(FadeIn(numberMinus2, shift=LEFT), run_time=1.0)
        
        #1:21
        # Number -2 is not a natural number
        self.play(Wiggle(numberMinus2), run_time=1.0, color=RED)
        self.play(numberMinus2.animate.next_to(naturalSet, RIGHT), run_time=1.0)
        self.play(Wiggle(numberMinus2), run_time=1.0, color=RED)
        self.wait(10)
        
        #1:34
        # Leave only the empty boxes and move them up
        scene = VGroup(naturalSetGroup, numberMinus2, text_substraction_symbol, texto_ser_cerrado, text_classification_symbol, number4)
        self.play(FadeOut(scene, shift=UP*5), run_time=1.0)
        self.play(boxes.animate.shift(UP*0.8), run_time=1.0)
        self.wait(2)
        
        #1:38
        # Create the rings of the Venn diagram
        chomsky_ring_1 = Annulus(inner_radius=0, outer_radius=1, fill_opacity=0.05, stroke_width=1)
        chomsky_ring_2 = Annulus(inner_radius=1 ,outer_radius=2.5, fill_opacity= 0.1, stroke_width=1)
        chomsky_ring_3 = Annulus(inner_radius=2.5 ,outer_radius=4, fill_opacity= 0.15, stroke_width=1)
        chomsky_ring_4 = Annulus(inner_radius=4 ,outer_radius=5.5, fill_opacity= 0.2, stroke_width=1)
        chomsky_ring_5 = Annulus(inner_radius=5.5 ,outer_radius=7, fill_opacity= 0.25, stroke_width=1)
        # Add them to a VGroup so we can move them all together
        chomsky_rings = VGroup(chomsky_ring_5, chomsky_ring_4, chomsky_ring_3, chomsky_ring_2, chomsky_ring_1)
        
        # Create the labels for the rings
        label_ring1 = Tex(r"\textbf{L.3}", color=WHITE).move_to(chomsky_ring_1.get_center())
        label_ring2 = Tex(r"\textbf{Lineales}", color=WHITE).move_to((chomsky_ring_1.get_bottom() + chomsky_ring_2.get_bottom())/2/1.1)
        label_ring3 = Tex(r"\textbf{L.2}", color=WHITE).move_to((chomsky_ring_2.get_bottom() + chomsky_ring_3.get_bottom())/2)
        label_ring4 = Tex(r"\textbf{L.1}", color=WHITE).move_to((chomsky_ring_3.get_bottom() + chomsky_ring_4.get_bottom())/2)
        label_ring5 = Tex(r"\textbf{L.0}", color=WHITE).move_to((chomsky_ring_4.get_bottom() + chomsky_ring_5.get_bottom())/2)
        # Add them to a VGroup so we can move them all together
        labels = VGroup(label_ring5, label_ring4, label_ring3, label_ring2, label_ring1)
        
        # Group the rings and the labels together to form the diagram
        chomsky_diagram = VGroup(chomsky_rings, labels)
        chomsky_diagram.scale(0.3)
        
        chomsky_diagram.shift(LEFT*2.75)
        # Add everything to the scene
        for i in range(5):
            self.play(DrawBorderThenFill(chomsky_rings[i]), run_time=1.5)
            self.play(Write(labels[i]), run_time=0.5)
       
        #1:48
        # Indicate the rings separately
        self.play(Indicate(chomsky_rings[0]), run_time=2.0, color=BLUE, scale_factor=1)
        self.play(Indicate(chomsky_rings[1]), run_time=2.0, color=BLUE, scale_factor=1)
        self.play(Indicate(chomsky_rings[2]), run_time=2.0, color=BLUE, scale_factor=1)
        self.play(Indicate(chomsky_rings[3]), run_time=2.0, color=BLUE, scale_factor=1)
        self.play(Indicate(chomsky_rings[4]), run_time=2.0, color=BLUE, scale_factor=1)
        self.wait(15)
        
        #2:13
        # Indicate the boxes
        self.play(Indicate(operation_box), run_time=1.0, color=BLUE)
        self.play(Indicate(classification_box), run_time=1.0, color=BLUE)
        self.wait(3)
        
        #2:18
        # Create the intersection symbol and the question symbol and place them in the middle of the boxes
        middlePoint = (operation_box.get_center() + classification_box.get_center())/2
        interSymbol = Tex(r"$\bigcap$", color=WHITE).move_to(operation_box.get_center()).scale(1.5)
        questionSymbol = Tex(r"$?$", color=WHITE).move_to(classification_box.get_center())
        self.play(Write(interSymbol), run_time=1.5)
        self.play(Write(questionSymbol), run_time=1.5)
        
        
        #2:21
        # Get 2 elements from the diagram and move them to the operation box
        lenguage1 = Tex(r"$L_{1}$", color=WHITE).next_to(chomsky_diagram, RIGHT)
        lenguage2 = Tex(r"$L_{2}$", color=WHITE).next_to(chomsky_diagram, RIGHT)
        lenguage3 = Tex(r"$L_{3}$", color=WHITE).next_to(chomsky_diagram, RIGHT)
        self.play(Indicate(chomsky_rings[3]), run_time=1, color=BLUE, scale_factor=1)
        
        self.play(FadeIn(lenguage1, target_position=chomsky_diagram.get_center()), run_time=1.0)
        self.play(lenguage1.animate.next_to(operation_box, LEFT), run_time=1.0)
        self.play(FadeOut(lenguage1, shift=RIGHT), run_time=0.5)
        
        self.play(FadeIn(lenguage2, target_position=chomsky_diagram.get_center()), run_time=1.0)
        self.play(lenguage2.animate.next_to(operation_box, LEFT), run_time=1.0)
        self.play(FadeOut(lenguage2, shift=RIGHT), run_time=0.5)
        
        
        #2:27
        # Create the result
        lenguage3.move_to(middlePoint)
        self.play(FadeIn(lenguage3, shift=DOWN), run_time=1.0)
        # Fade out the classification box and the question symbol
        self.play(VGroup(classification_box, questionSymbol).animate.set_opacity(0.2), run_time=1.0)
        # Move the result next to the diagram
        self.play(lenguage3.animate.next_to(chomsky_diagram, RIGHT), run_time=1.0)
        # Create a question symbol next to it
        lenguage3b = Tex(r"$?$", color=WHITE).next_to(lenguage3, RIGHT)
        self.play(Write(lenguage3b), run_time=1.0)
        
        #2:31
        # Indicate the result and the question symbol a few times
        for i in range(12):
            self.play(Indicate(VGroup(lenguage3, lenguage3b)), run_time=2.0, color=YELLOW)
        self.wait(5)
        
        
        #3:00
        # Fade out the elements of the scene keeping the classification box and the question symbol
        mobjects = self.mobjects
        copyOfIntBox = VGroup(classification_box, questionSymbol).copy()
        self.add(copyOfIntBox)
        self.play(AnimationGroup(*[
            obj.animate(lag_ratio=0, run_time=1.5).set_opacity(0)
            for obj in mobjects
        ]))
        # Move the classification box and the question symbol to the center of the screen and scale them to give a zoom effect
        self.play(copyOfIntBox.animate(lag_ratio=0, run_time=1.5).move_to(ORIGIN))
        self.play(copyOfIntBox[1].animate(lag_ratio=0, run_time=1.5).set_opacity(0))
        self.play(copyOfIntBox.animate(lag_ratio=0, run_time=1.5).scale(15))
        self.play(copyOfIntBox.animate(lag_ratio=0, run_time=1).set_opacity(0))
        self.wait(2)
        
        #3:09
        # Table creation
        row_labels = [Text("Unión"), Text("Intersección"), Text("Intersección con L.3"), Text("Complemento"), Text("Concatenación"), Text("Potencia"), Text("Cierre"), Text("Cierre estricto"), Text("Inverso")]
        column_labels = [Text("Estructura de frase"), Text("Sensible al contexto"), Text("Contexo libre"), Text("Lineales"), Text("Regular")]
        closure_table = Table(
            [
                ["Sí", "Sí", "Sí", "Sí", "Sí"],
                ["Sí", "Sí", "No", "No", "Sí"],
                ["Sí", "Sí", "Sí", "Sí", "Sí"],
                ["No", "Sí", "No", "No", "Sí"],
                ["Sí", "Sí", "Sí", "No", "Sí"],
                ["Sí", "Sí", "Sí", "No", "Sí"],
                ["Sí", "Sí", "Sí", "No", "Sí"],
                ["Sí", "Sí", "Sí", "No", "Sí"],
                ["Sí", "Sí", "Sí", "Sí", "Sí"],
            ],
            row_labels,
            column_labels,
            include_outer_lines=True)
        closure_table.get_vertical_lines().set_stroke(width=0.7)
        closure_table.get_horizontal_lines().set_stroke(width=0.7)
        closure_table.scale(0.30)
        self.play(closure_table.create(line_animation=Write,
                            label_animation=Write,
                            element_animation=Create),
                            run_time=4)
        self.wait(2)
        
        #3:15
        # Indicate the rows , then the columns and finally the entries
        self.play(Indicate(closure_table.get_rows()[0]), color=YELLOW, run_time=1.0, scale_factor = 1.05)
        self.play(Indicate(closure_table.get_columns()[0]), color=YELLOW, run_time=1.0, scale_factor = 1.05)
        self.wait(2)
        self.play(Indicate(closure_table.get_entries_without_labels()), color=YELLOW, run_time=1.0, scale_factor = 1.05)
        self.wait(5)
        
        #3:25
        # Indicate some entries
        self.play(Indicate(closure_table.get_entries((6,4))), run_time=1.0)
        self.wait(2)
        self.play(Indicate(closure_table.get_entries((3,4))), run_time=1.0)
        self.wait(4)
        
        #3:33
        # Indicate some entries
        self.play(Indicate(closure_table.get_entries((6,4)), color=BLUE), run_time=2.0)
        self.wait(2)
        self.play(Indicate(closure_table.get_entries((3,4)), color=BLUE), run_time=2.0)
        self.wait(6)
        
        #3:45
        self.wait(17)
        
        #4:02
        # Indicate some cells
        # Cells are of the form (row, column)
        cellsL0 = [(5,2)]
        cellsL1 = [(2,3), (3,3), (4,3), (5,3), (6,3), (7,3), (8,3), (9,3), (10,3)]
        cellsL2 = [(3,4), (5,4)]
        cellsL  = [(3,5), (5,5), (6,5), (7,5), (8,5), (9,5)]
        cellsL3 = [(2,6), (3,6), (4,6), (5,6), (6,6), (7,6), (8,6), (9,6), (10,6)]
        
        highlightedCellsL0= VGroup()
        for cell in cellsL0:
            highlightedCellsL0.add(closure_table.get_highlighted_cell(cell, color=RED, fill_opacity=0.5))
            
        highlightedCellsL1= VGroup()
        for cell in cellsL1:
            highlightedCellsL1.add(closure_table.get_highlighted_cell(cell, color=GREEN, fill_opacity=0.5))
        
        highlightedCellsL2 = VGroup()
        for cell in cellsL2:
            highlightedCellsL2.add(closure_table.get_highlighted_cell(cell, color=RED, fill_opacity=0.5))
            
        highlightedCellsL= VGroup()
        for cell in cellsL:
            highlightedCellsL.add(closure_table.get_highlighted_cell(cell, color=RED, fill_opacity=0.5)) 
            
        highlightedCellsL3 = VGroup()
        for cell in cellsL3:
            highlightedCellsL3.add(closure_table.get_highlighted_cell(cell, color=GREEN, fill_opacity=0.5))
        
        self.play(Write(highlightedCellsL3), run_time=2.0)
        self.play(Write(highlightedCellsL1), run_time=2.0)
        self.play(Unwrite(highlightedCellsL3), run_time=2.0)
        self.play(Unwrite(highlightedCellsL1), run_time=2.0)
        
        #4:10
        # Some more indications
        self.play(Write(highlightedCellsL, run_time=10.0))
        self.wait(3)
        self.play(Write(highlightedCellsL2, run_time=2.0))
        self.wait(3)
        self.play(Write(highlightedCellsL0, run_time=1.0))
        self.play(Unwrite(VGroup(highlightedCellsL, highlightedCellsL2, highlightedCellsL0), run_time=1.0))
        
        
        #4:30
        # Fade out the table
        self.play(FadeOut(closure_table, shift=UP*5), run_time=2.0)
        
        # Create the rings of the Venn diagram again
        chomsky_ring_0 = Annulus(inner_radius=0, outer_radius=0.3, fill_opacity=0.05, stroke_width=1).scale(0.3)
        chomsky_ring_1 = Annulus(inner_radius=0, outer_radius=1, fill_opacity=0.1, stroke_width=1)
        chomsky_ring_2 = Annulus(inner_radius=1 ,outer_radius=2.5, fill_opacity= 0.15, stroke_width=1)
        chomsky_ring_3 = Annulus(inner_radius=2.5 ,outer_radius=4, fill_opacity= 0.2, stroke_width=1)
        chomsky_ring_4 = Annulus(inner_radius=4 ,outer_radius=5.5, fill_opacity= 0.25, stroke_width=1)
        chomsky_ring_5 = Annulus(inner_radius=5.5 ,outer_radius=7, fill_opacity= 0.3, stroke_width=1)
        chomsky_ring_6 = Annulus(inner_radius=7 ,outer_radius=8.5, fill_opacity= 0.35, stroke_width=1).scale(0.3)
        chomsky_ring_7 = Annulus(inner_radius=8.5 ,outer_radius=25, fill_opacity= 0.2, stroke_width=1).scale(0.3)
        
        # Add them to a VGroup so we can move them all together
        chomsky_rings = VGroup(chomsky_ring_5, chomsky_ring_4, chomsky_ring_3, chomsky_ring_2, chomsky_ring_1)
        extra_rings = VGroup(chomsky_ring_7, chomsky_ring_6, chomsky_ring_0)
        
        # Create the labels for the rings
        label_ring1 = Tex(r"L.3", color=WHITE).move_to((chomsky_ring_0.get_bottom() + chomsky_ring_1.get_bottom())/2)
        label_ring2 = Tex(r"Lineales", color=WHITE).move_to((chomsky_ring_1.get_bottom() + chomsky_ring_2.get_bottom())/2/1.1)
        label_ring3 = Tex(r"L.2", color=WHITE).move_to((chomsky_ring_2.get_bottom() + chomsky_ring_3.get_bottom())/2)
        label_ring4 = Tex(r"L.1", color=WHITE).move_to((chomsky_ring_3.get_bottom() + chomsky_ring_4.get_bottom())/2)
        label_ring5 = Tex(r"L.0", color=WHITE).move_to((chomsky_ring_4.get_bottom() + chomsky_ring_5.get_bottom())/2)
        # Add them to a VGroup so we can move them all together
        labels = VGroup(label_ring5, label_ring4, label_ring3, label_ring2, label_ring1)
        
        chomsky_diagram = VGroup(chomsky_rings, labels)
        chomsky_diagram.scale(0.3)
    
        chomsky_diagram.move_to(ORIGIN+DOWN)
        extra_rings.move_to(ORIGIN+DOWN)
        
        # Add everything to the scene
        self.play(FadeIn(VGroup(chomsky_rings, labels)), run_time=1.0)
        
        # Create some lenguaje complements exmaples and place them next to the diagram
        complement_1 = Tex(r"$\overline{L_{1}}$", color=WHITE).next_to(chomsky_diagram, RIGHT)
        complement_2 = Tex(r"$\overline{L_{2}}$", color=WHITE).next_to(complement_1, DOWN)
        complement_3 = Tex(r"$\overline{L_{3}}$", color=WHITE).next_to(chomsky_diagram, LEFT)
        complement_4 = Tex(r"$\overline{L_{4}}$", color=WHITE).next_to(complement_3, LEFT)
        complement_5 = Tex(r"$\overline{L_{5}}$", color=WHITE).next_to(complement_3, UP)
        complements = VGroup(complement_1, complement_2, complement_3, complement_4, complement_5)
        for i in range(5):
            self.play(Write(complements[i]), run_time=0.8)
        for i in range(5):
            self.play(Unwrite(complements[i]), run_time=0.8)
        self.wait(5)
        
        #4:47
        # Inclusions
        # FULL TEXT: L.finitos\subset L.3\subset L.Lineales\subset L.2\subset L.1\subset L.0\subset L.REP\subset 2^{\Sigma^{*}}
        inclusion0 = Tex(r"$L.finitos$", color=WHITE)
        inclusion1 = Tex(r"$\subset L.3$", color=WHITE).next_to(inclusion0, RIGHT)
        inclusion2 = Tex(r"$\subset L.Lineales$", color=WHITE).next_to(inclusion1, RIGHT)
        inclusion3 = Tex(r"$\subset L.2$", color=WHITE).next_to(inclusion2, RIGHT)
        inclusion4 = Tex(r"$\subset L.1$", color=WHITE).next_to(inclusion3, RIGHT)
        inclusion5 = Tex(r"$\subset L.0$", color=WHITE).next_to(inclusion4, RIGHT)
        inclusion6 = Tex(r"$\subset L.REP$", color=WHITE).next_to(inclusion5, RIGHT)
        inclusions = VGroup(inclusion0, inclusion1, inclusion2, inclusion3, inclusion4, inclusion5, inclusion6)
        inclusions.next_to(chomsky_diagram, UP*2)
        self.play(Indicate(chomsky_ring_0), color=GREEN, run_time=1.0, scale_factor = 1)
        self.play(Write(inclusions[0]), run_time=1)
        
        for i in range(5):
            self.play(Indicate(chomsky_rings[4-i]), color=GREEN, run_time=1.0, scale_factor = 1)
            self.play(Write(inclusions[i+1]), run_time=1.5)
            
        self.wait(3)
        self.play(Indicate(chomsky_ring_6), color=GREEN, run_time=1.0, scale_factor = 1)
        self.play(Write(inclusions[6]), run_time=1)
        self.wait(2)
        self.play(Indicate(chomsky_ring_7), color=GREEN, run_time=1.0, scale_factor = 1)
        self.wait(22)
        self.play(Indicate(inclusions), color=YELLOW, run_time=1.0, scale_factor = 1.1)
        self.wait(2)
        
#with tempconfig({"quality": "low_quality", "preview": True}):
with tempconfig({"quality": "high_quality", "preview": True}):   
#with tempconfig({"quality": "fourk_quality", "preview": True}):
    scene = Video()
    scene.render()