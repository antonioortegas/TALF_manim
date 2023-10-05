from manim import *

class ToyExample(Scene):
    def construct(self):
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
        t2.get_vertical_lines().set_stroke(width=0.5)
        t2.get_horizontal_lines().set_stroke(width=0.5)
        t2.scale(0.25)
        self.add(t2)
        self.play(t2.create(line_animation=Write,
                            element_animation=Create,
                            label_animation=Write), run_time=3)
        self.wait(10)
        

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = ToyExample()
    scene.render()