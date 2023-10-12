from manim import *

class ToyExample(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        rowLabels = [Text("Unión"), Text("Intersección"), Text("Intersección con L.3"), Text("Complemento"), Text("Concatenación"), Text("Potencia"), Text("Cierre"), Text("Cierre estricto"), Text("Inverso")]
        columnLabels = [Text("Estructura de frase"), Text("Sensible al contexto"), Text("Contexo libre"), Text("Lineales"), Text("Regular")]
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
            rowLabels,
            columnLabels,
            include_outer_lines=True)
        closure_table.get_vertical_lines().set_stroke(width=0.7)
        closure_table.get_horizontal_lines().set_stroke(width=0.7)
        closure_table.scale(0.30)
        title = Text("Cierre de los Tipos de Lenguajes").scale(0.8)
        slide1 = VGroup(title, closure_table).arrange(DOWN, buff = 1)
        #Cells containing "No" are highlighted in red
        cellsContainingNo = [(3,4), (3,5), (5,2), (5,4), (5,5), (6,5), (7,5), (8,5), (9,5)]
        highlightedCells = VGroup()
        for cell in cellsContainingNo:
            highlightedCells.add(closure_table.get_highlighted_cell(cell, color=RED, fill_opacity=0.5))
            
        #Store everything in a VGroup so we can move it all together
        table = VGroup(closure_table, highlightedCells)
    
        self.play(Write(title), run_time=0.5)
        self.play(closure_table.create(line_animation=Write,
                            label_animation=Write,
                            element_animation=Create),
                            run_time=3)
        self.wait(2)
        self.play(Write(highlightedCells), run_time=4.5)
        self.wait(2)
        
        self.play(Unwrite(title), run_time=1.0)
        self.play(FadeOut(table, shift=DOWN), run_time=1.0)
        self.wait(2)
        
        #* VENN DIAGRAM 
        
        ring1 = Annulus(inner_radius=0, outer_radius=1, fill_opacity=0.05, stroke_width=1)
        ring2 = Annulus(inner_radius=1 ,outer_radius=2.5, fill_opacity= 0.1, stroke_width=1)
        ring3 = Annulus(inner_radius=2.5 ,outer_radius=4, fill_opacity= 0.15, stroke_width=1)
        ring4 = Annulus(inner_radius=4 ,outer_radius=5.5, fill_opacity= 0.2, stroke_width=1)
        ring5 = Annulus(inner_radius=5.5 ,outer_radius=7, fill_opacity= 0.25, stroke_width=1)
        
        
        
        # Add them to a VGroup so we can move them all together
        rings = VGroup(ring5, ring4, ring3, ring2, ring1)
        
        # Position the circles
        #circle1.move_to(LEFT)
        #circle2.move_to(RIGHT)
        
        # Create labels for the 5 circles
        # Position the label right below the upper edge of the circle
        
        
        label1 = Tex(r"\textbf{L.3}", color=WHITE).move_to(ring1.get_center())
        label2 = Tex(r"\textbf{Lineales}", color=WHITE).move_to((ring1.get_bottom() + ring2.get_bottom())/2/1.1)
        label3 = Tex(r"\textbf{L.2}", color=WHITE).move_to((ring2.get_bottom() + ring3.get_bottom())/2)
        label4 = Tex(r"\textbf{L.1}", color=WHITE).move_to((ring3.get_bottom() + ring4.get_bottom())/2)
        label5 = Tex(r"\textbf{L.0}", color=WHITE).move_to((ring4.get_bottom() + ring5.get_bottom())/2)
        
        labels = VGroup(label5, label4, label3, label2, label1)
        
        diagram = VGroup(rings, labels)
        diagram.scale(0.3)
        
        # Create intersection region
        #intersection = circle1.copy()
        #intersection.set_fill(opacity=0.5)
        #intersection.set_color(PURPLE)
        #intersection.set_stroke(width=0)
        #intersection.move_to(circle1.get_center() + circle2.get_center())
        #intersection.scale(0.6)
        
        # Add everything to the scene
        for i in range(5):
            self.play(DrawBorderThenFill(rings[i]), run_time=1.0)
            self.play(Write(labels[i]), run_time=0.5)
        
        # move diagram to a corner and scale it down so it can serve as a preview
        self.play(diagram.animate.move_to(3*LEFT), run_time=1.0)
        
        holes = VGroup()
        holeAngle = PI/24
        for ring in rings:
            
            holes.add(Arc(
            start_angle=PI/2+holeAngle,
            angle=-2*holeAngle,
            arc_center=ring.get_center(),
            radius=ring.radius*0.3,
            color=BLACK))
        
        self.play(Create(holes), run_time=1.0)
        
        
        
        self.wait(5)
        
#with tempconfig({"quality": "low_quality", "preview": True}):
with tempconfig({"quality": "high_quality", "preview": True}):
    scene = ToyExample()
    scene.render()