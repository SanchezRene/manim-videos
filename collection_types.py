from manim import *

class CollectionTypes(Scene):
    def construct(self):
        # Title
        title = Text("Collection Types", color=WHITE).shift(6 * UP)
        self.play(Write(title))

        # Single Circle
        circle = Circle(fill_opacity=0.2,fill_color=YELLOW,color=WHITE).scale(0.4)

        ## LinearGroup
        linear_group = VGroup(*[circle.copy() for _ in range(5)])
        # Arrage the circles in a row
        linear_group.arrange(RIGHT, buff=0.5)
        # Label
        linear_label = Text("Linear", color=WHITE).next_to(circle, UP*2)
        # Lines between circles
        linear_lines = VGroup(*[Line(linear_group[i].get_right(), linear_group[i+1].get_left(), color=WHITE) for i in range(4)])

        self.add(linear_group)
        self.add(linear_lines)
        self.play(Write(linear_label))
        self.wait(3)

        # Remove the linear group
        self.play(FadeOut(linear_group), FadeOut(linear_label), FadeOut(linear_lines))
