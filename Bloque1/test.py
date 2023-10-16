from manim import *

class Video(Scene):
    def construct(self):
        
        self.camera.background_color = BLACK
        
        # Table creation
        rowLabels = [Text("Unión"), Text("Intersección"), Text("Intersección con L.3"), Text("Complemento"), Text("Concatenación"), Text("Potencia"), Text("Cierre"), Text("Cierre estricto"), Text("Inverso")]
        columnLabels = [Text("Estructura de frase"), Text("Sensible al contexto"), Text("Contexo libre"), Text("Lineales"), Text("Regular")]
        closureTable = Table(
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
            rowLabels,
            columnLabels,
            include_outer_lines=True)
        closureTable.get_vertical_lines().set_stroke(width=0.7)
        closureTable.get_horizontal_lines().set_stroke(width=0.7)
        closureTable.scale(0.30)
        #Cells containing "No" are highlighted in red
        cellsContainingNo = [(3,4), (3,5), (5,2), (5,4), (5,5), (6,5), (7,5), (8,5), (9,5)]
        highlightedCells = VGroup()
        for cell in cellsContainingNo:
            highlightedCells.add(closureTable.get_highlighted_cell(cell, color=RED, fill_opacity=0.5))
            
        #Store everything in a VGroup so we can move it all together
        highlightedClosureTable = VGroup(closureTable, highlightedCells)
        
        title = Text("2.11 - Cierre de los Tipos de Lenguajes").scale(0.8)
        
        slideTable = VGroup(title.copy(), highlightedClosureTable).arrange(DOWN, buff = 1)
        
        
        
        # Create the rings of the Venn diagram
        ring1 = Annulus(inner_radius=0, outer_radius=1, fill_opacity=0.05, stroke_width=1)
        ring2 = Annulus(inner_radius=1 ,outer_radius=2.5, fill_opacity= 0.1, stroke_width=1)
        ring3 = Annulus(inner_radius=2.5 ,outer_radius=4, fill_opacity= 0.15, stroke_width=1)
        ring4 = Annulus(inner_radius=4 ,outer_radius=5.5, fill_opacity= 0.2, stroke_width=1)
        ring5 = Annulus(inner_radius=5.5 ,outer_radius=7, fill_opacity= 0.25, stroke_width=1)
        # Add them to a VGroup so we can move them all together
        rings = VGroup(ring5, ring4, ring3, ring2, ring1)
        
        # Create the labels for the rings
        label1 = Tex(r"\textbf{L.3}", color=WHITE).move_to(ring1.get_center())
        label2 = Tex(r"\textbf{Lineales}", color=WHITE).move_to((ring1.get_bottom() + ring2.get_bottom())/2/1.1)
        label3 = Tex(r"\textbf{L.2}", color=WHITE).move_to((ring2.get_bottom() + ring3.get_bottom())/2)
        label4 = Tex(r"\textbf{L.1}", color=WHITE).move_to((ring3.get_bottom() + ring4.get_bottom())/2)
        label5 = Tex(r"\textbf{L.0}", color=WHITE).move_to((ring4.get_bottom() + ring5.get_bottom())/2)
        # Add them to a VGroup so we can move them all together
        labels = VGroup(label5, label4, label3, label2, label1)
        
        vennLenguages = VGroup(rings, labels)
        vennLenguages.scale(0.3)
        
        
        # Create arcs to represent the "holes" between the rings for operations
        holes = VGroup()
        holeAngle = PI/24
        for ring in rings:
            holes.add(Arc(
            start_angle=PI/2+holeAngle,
            angle=-2*holeAngle,
            arc_center=ring.get_center(),
            radius=ring.radius*0.3,
            color=BLACK))
        
        textEsCerrado = Tex(r"$A\: es \: cerrado\: para \: \bullet \Leftrightarrow \forall a,b \in A, \: a\bullet b \in A$") 
        
        
            
        naturalSet = Circle(radius=1.5, color=WHITE, fill_opacity=0.1, fill_color=WHITE)
        naturalSet.shift(DOWN*0.8)
        naturalSetLabel = Tex(r"$\mathbb{N}$", color=WHITE).next_to(naturalSet.get_top(), UP)
        
        self.play(Write(title), run_time=0.5)
        self.play(FadeOut(title, shift=UP), run_time=1.5)
        self.play(Write(textEsCerrado), run_time=1.0)
        self.play(textEsCerrado.animate.shift(UP*2.5), run_time=1.0)
        self.play(DrawBorderThenFill(naturalSet), run_time=1.0)
        self.play(Write(naturalSetLabel), run_time=0.5)
        
        pentagon = Polygon(*[naturalSet.point_from_proportion(i/5) for i in range(5)], color=BLUE).scale(0.6)
        
        
        
        
        
        
        
        naturalSetElements = VGroup()
        for i in range(5):
            naturalSetElements.add(Tex(str(i), color=WHITE).move_to(pentagon.get_vertices()[i]))
        
        naturalSetGroup = VGroup(naturalSet, naturalSetLabel, naturalSetElements)
        
        self.play(Write(naturalSetElements), run_time=1.0)
        self.play(naturalSetGroup.animate.shift(LEFT*2.75), run_time=1.0)
        
        boxes = VGroup()
        op_box = Rectangle(height=1.5, width=1.5, color=WHITE, fill_opacity=0.2, fill_color=WHITE)
        classification_box = Rectangle(height=1.5, width=1.5, color=WHITE, fill_opacity=0.2, fill_color=WHITE)
        boxes.add(op_box, classification_box)
        boxes.arrange(DOWN, buff=1)
        boxes.shift(RIGHT*2.75)
        boxes.shift(DOWN*0.8)
        
        self.play(DrawBorderThenFill(op_box), run_time=1.0)
        sumSymbol = Tex(r"$+$", color=WHITE).move_to(op_box.get_center()).scale(1.5)
        moreThanOrEqualToZero = Tex(r"$\geq 0$", color=WHITE).move_to(classification_box.get_center())
        self.play(Write(sumSymbol), run_time=1.0)
        self.play(DrawBorderThenFill(classification_box), run_time=1.0)
        self.play(Write(moreThanOrEqualToZero), run_time=1.0)
        
        number1 = naturalSetElements[1].copy()
        number3 = naturalSetElements[3].copy()
        
        self.play(number1.animate.next_to(op_box, LEFT), run_time=1.0)
        self.play(FadeOut(number1, shift=RIGHT), run_time=1.0)
        self.play(number3.animate.next_to(op_box, LEFT), run_time=1.0)
        self.play(FadeOut(number3, shift=RIGHT), run_time=1.0)
        
        number4 = naturalSetElements[4].copy()
        middlePoint = (op_box.get_center() + classification_box.get_center())/2
        number4.move_to(middlePoint)
        
        self.play(FadeIn(number4, shift=DOWN), run_time=1.0)
        self.play(FadeOut(number4, shift=DOWN), run_time=1.0)
        number4.move_to(classification_box.get_center() + LEFT*1.2)
        number4.color = GREEN
        self.play(FadeIn(number4, shift=LEFT), run_time=1.0)
        
        
        
        self.play(Indicate(number4), run_time=1.0, color=GREEN)
        self.play(number4.animate.move_to(naturalSetElements[4]), run_time=1.0)
        self.wait(2)
        
        number1 = naturalSetElements[1].copy()
        number3 = naturalSetElements[3].copy()
        
        subSymbol = Tex(r"$-$", color=WHITE).move_to(op_box.get_center()).scale(1.5)
        
        self.play(FadeTransform(sumSymbol, subSymbol), run_time=1.0)
        
        self.play(number1.animate.next_to(op_box, LEFT), run_time=1.0)
        self.play(FadeOut(number1, shift=RIGHT), run_time=1.0)
        self.play(number3.animate.next_to(op_box, LEFT), run_time=1.0)
        self.play(FadeOut(number3, shift=RIGHT), run_time=1.0)
        
        numberMinus2 = Tex(r"$-2$", color=WHITE).move_to(middlePoint)
        
        
        
        self.play(FadeIn(numberMinus2, shift=DOWN), run_time=1.0)
        self.play(FadeOut(numberMinus2, shift=DOWN), run_time=1.0)
        numberMinus2.move_to(classification_box.get_center() + LEFT*1.2)
        numberMinus2.color = RED
        self.play(FadeIn(numberMinus2, shift=LEFT), run_time=1.0)
        
        
        
        self.play(Wiggle(numberMinus2), run_time=1.0, color=RED)
        self.play(numberMinus2.animate.next_to(naturalSet, RIGHT), run_time=1.0)
        self.play(Wiggle(numberMinus2), run_time=1.0, color=RED)
        self.wait(2)
        
        scene = VGroup(naturalSetGroup, numberMinus2, subSymbol, textEsCerrado, moreThanOrEqualToZero, number4)
        self.play(FadeOut(scene, shift=UP*5), run_time=1.0)
        self.play(boxes.animate.shift(UP*0.8), run_time=1.0)
        
        
        vennLenguages.shift(LEFT*2.75)
        # Add everything to the scene
        for i in range(5):
            self.play(DrawBorderThenFill(rings[i]), run_time=1.0)
            self.play(Write(labels[i]), run_time=0.5)
       
        
        
        
        
        
        
        #TODO
        
        middlePoint = (op_box.get_center() + classification_box.get_center())/2
        interSymbol = Tex(r"$\bigcap$", color=WHITE).move_to(op_box.get_center()).scale(1.5)
        questionSymbol = Tex(r"$?$", color=WHITE).move_to(classification_box.get_center())
        self.play(Write(interSymbol), run_time=1.0)
        self.play(Write(questionSymbol), run_time=1.0)
        
        lenguage1 = Tex(r"$L_{1}$", color=WHITE).next_to(vennLenguages, RIGHT)
        lenguage2 = Tex(r"$L_{2}$", color=WHITE).next_to(vennLenguages, RIGHT)
        lenguage3 = Tex(r"$L_{3}$", color=WHITE).next_to(vennLenguages, RIGHT)
        
        
        self.play(FadeIn(lenguage1, target_position=vennLenguages.get_center()), run_time=1.0)
        self.play(lenguage1.animate.next_to(op_box, LEFT), run_time=1.0)
        self.play(FadeOut(lenguage1, shift=RIGHT), run_time=1.0)
        
        self.play(FadeIn(lenguage2, target_position=vennLenguages.get_center()), run_time=1.0)
        self.play(lenguage2.animate.next_to(op_box, LEFT), run_time=1.0)
        self.play(FadeOut(lenguage2, shift=RIGHT), run_time=1.0)
        
        middlePoint = (op_box.get_center() + classification_box.get_center())/2
        lenguage3.move_to(middlePoint)
        
        self.play(FadeIn(lenguage3, shift=DOWN), run_time=1.0)
        
        self.play(FadeOut(VGroup(classification_box, questionSymbol), run_time=1.0))
        self.play(lenguage3.animate.next_to(vennLenguages, RIGHT), run_time=1.0)
        lenguage3b = Tex(r"$?$", color=WHITE).next_to(lenguage3, RIGHT)
        self.play(Write(lenguage3b), run_time=1.0)
        
        
        self.play(Indicate(VGroup(lenguage3, lenguage3b)), run_time=2.0, color=YELLOW)
        self.wait(2)
        
        
        
        
        
        
        
        #? REMNANTS
        
        """
        self.play(closureTable.create(line_animation=Write,
                            label_animation=Write,
                            element_animation=Create),
                            run_time=3)
        self.wait(2)
        self.play(Write(highlightedCells), run_time=4.5)
        self.wait(2)
        self.play(Unwrite(title), run_time=1.0)
        self.play(FadeOut(highlightedClosureTable, shift=DOWN), run_time=1.0)
        self.wait(2)
        
        # move diagram to a corner and scale it down so it can serve as a preview
        self.play(vennLenguages.animate.move_to(3*LEFT), run_time=1.0)
        
        self.play(Create(holes), run_time=1.0)
    
        self.wait(5)
        """
        self.wait(10)
        
#with tempconfig({"quality": "high_quality", "preview": True, "save_last_frame": True}):   
#with tempconfig({"quality": "low_quality", "preview": True}):
with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Video()
    scene.render()