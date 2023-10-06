from manim import *

class ToyExample(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        rowLabels = [Text("Unión"), Text("Intersección"), Text("Intersección con L.3"), Text("Complemento"), Text("Concatenación"), Text("Potencia"), Text("Cierre"), Text("Cierre estricto"), Text("Inverso")]
        columnLabels = [Text("Estructura de frase"), Text("Sensible al contexto"), Text("Contexo libre"), Text("Lineales"), Text("Regular")]
        t2 = Table(
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
        t2.get_vertical_lines().set_stroke(width=0.7)
        t2.get_horizontal_lines().set_stroke(width=0.7)
        t2.scale(0.30)
        title = Text("Cierre de los Tipos de Lenguajes").scale(0.8)
        slide1 = VGroup(title, t2).arrange(DOWN, buff = 1)
        self.play(Write(title), run_time=0.5)
        self.play(t2.create(line_animation=Write,
                            element_animation=Create,
                            label_animation=Write), run_time=3)
        self.wait(2)
        #Cells containing "No" are highlighted in red
        cellsContainingNo = [(3,4), (3,5), (5,2), (5,4), (5,5), (6,5), (7,5), (8,5), (9,5)]
        highlightedCells = VGroup()
        for cell in cellsContainingNo:
            highlightedCells.add(t2.get_highlighted_cell(cell, color=RED, fill_opacity=0.5))
    
        self.play(Write(highlightedCells), run_time=4.5, )
        self.wait(5)
        
#with tempconfig({"quality": "low_quality", "preview": True}):
with tempconfig({"quality": "high_quality", "preview": True}):
    scene = ToyExample()
    scene.render()