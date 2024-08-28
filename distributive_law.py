from manim import *

class DistributiveLaw(Scene):
    def construct(self):
        # Estandar position for titles
        def place_title(text, shift_amount=6 * UP):
            return Text(text, color=WHITE).move_to(shift_amount)

        # Create the title
        title = place_title("Distributive Law")
        self.play(Write(title))

        # Create circles for sets A, B, and C
        A = Circle(radius=2, color=BLUE).shift(LEFT)
        B = Circle(radius=2, color=BLUE).shift(RIGHT + UP)
        C = Circle(radius=2, color=BLUE).shift(RIGHT + DOWN)

        # Set labels
        label_A = Text("A", color=WHITE).next_to(A, UP)
        label_B = Text("B", color=WHITE).next_to(B, UP)
        label_C = Text("C", color=WHITE).next_to(C, DOWN)

        # Create the sets
        self.play(Create(A), Write(label_A))
        self.play(Create(B), Write(label_B))
        self.play(Create(C), Write(label_C))

        self.play(FadeOut(title))  # Fade out the title

        # A ∪ B
        union_AB_title = place_title("A ∪ B")
        self.add(union_AB_title)
        AB_union = Union(A, B, color=ORANGE, fill_opacity=0.5)
        self.play(Create(AB_union))
        self.wait(2)
        self.play(FadeOut(AB_union), FadeOut(union_AB_title))

        # A ∪ C
        union_AC_title = place_title("A ∪ C")
        self.add(union_AC_title)
        AC_union = Union(A, C, color=ORANGE, fill_opacity=0.5)
        self.play(Create(AC_union))
        self.wait(2)
        self.play(FadeOut(AC_union), FadeOut(union_AC_title))

        # intersection (A ∪ B) ∩ (A ∪ C)
        intersection_title = place_title("(A ∪ B) ∩ (A ∪ C)")
        self.add(intersection_title)
        AB_AC_intersection = Intersection(AB_union, AC_union, color=ORANGE, fill_opacity=0.5)
        self.play(Create(AB_AC_intersection))
        self.wait(2)
        self.play(FadeOut(AB_AC_intersection), FadeOut(intersection_title))

        # intersection B ∩ C
        intersection_title = place_title("B ∩ C")
        BC_intersection = Intersection(B, C, color=YELLOW, fill_opacity=0.5)
        self.add(intersection_title)
        self.play(Create(BC_intersection)) 
        self.wait(1)
        self.play(FadeOut(BC_intersection), FadeOut(intersection_title))

        # union A ∪ (B ∩ C)
        union_title = place_title("A ∪ (B ∩ C)")
        self.add(union_title)
        left_side = Union(A, BC_intersection, color=YELLOW, fill_opacity=0.5)
        self.play(Create(left_side))
        self.wait(2)
        self.play(FadeOut(left_side), FadeOut(union_title))

        # union (A ∪ B) ∩ (A ∪ C) = A ∪ (B ∩ C)
        union_intersection_title = place_title("(A ∪ B) ∩ (A ∪ C) = A ∪ (B ∩ C)")
        union_intersection_title.scale(0.6)  # 60% scale
        self.add(union_intersection_title)
        left_side = Union(A, BC_intersection, color=YELLOW, fill_opacity=0.6)
        self.play(Create(left_side))
        self.wait(2)
        self.play(FadeOut(left_side), FadeOut(union_intersection_title))





