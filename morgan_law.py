from manim import *

class MorganLaw(Scene):
    def construct(self):
        # Título
        title = Text("Morgan's Law", color=WHITE).to_edge(UP)
        self.play(Write(title))
        
        # Universal set
        Universe = Rectangle(width=6, height=6, color=WHITE).shift(UP*1.5)


        # Create circles for sets A y B
        A = Circle(radius=1.5, color=BLUE).shift(LEFT + UP*1.5)
        B = Circle(radius=1.5, color=BLUE).shift(RIGHT + UP*1.5)

         # Set labels
        label_A = Text("A", color=WHITE).next_to(A, UP)
        label_B = Text("B", color=WHITE).next_to(B, UP)

        # Create the sets
        self.play(Create(A), Write(label_A))
        self.play(Create(B), Write(label_B))

        # A U B
        union_AB_title = Text("A U B", color=WHITE).next_to(label_A,UP+LEFT)
        
        self.add(union_AB_title)
        AB_union = Union(A, B, color=ORANGE, fill_opacity=0.5)
        self.wait(1)
        self.play(Create(AB_union))
        self.wait(2)
        self.play(FadeOut(AB_union), FadeOut(union_AB_title))