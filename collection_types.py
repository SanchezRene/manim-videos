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
        self.wait(2)

        # Remove the linear group
        self.play(FadeOut(linear_group), FadeOut(linear_label), FadeOut(linear_lines))



        ## HierarchicalGroup
        nodes = VGroup(
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4),  # D1
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4),  # D2
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4),  # D3
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4),  # D4
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4),  # D5
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4)   # D6
        )

        # Arrage nodes in a hierarchical way
        nodes[0].move_to(UP * 2)         # D1
        nodes[1].move_to(LEFT * 1.8)     # D2
        nodes[2].move_to(RIGHT * 1.8)    # D3 (center)
        nodes[3].move_to(DOWN * 2 + RIGHT * 0.6)  # D4
        nodes[4].move_to(DOWN * 2 + RIGHT* 1.8)   # D5
        nodes[5].move_to(DOWN * 2 + RIGHT * 3)    # D6

        # Lines between nodes
        lines = VGroup(
            Line(nodes[0].get_bottom(), nodes[1].get_top(), color=WHITE),  # D1 -> D2
            Line(nodes[0].get_bottom(), nodes[2].get_top(), color=WHITE),  # D1 -> D3
            Line(nodes[2].get_bottom(), nodes[3].get_top(), color=WHITE),  # D3 -> D4
            Line(nodes[2].get_bottom(), nodes[4].get_top(), color=WHITE),  # D3 -> D5
            Line(nodes[2].get_bottom(), nodes[5].get_top(), color=WHITE)   # D3 -> D6
        )
        hierarchical_label = Text("Hierarchical", color=WHITE).shift(UP * 3.5)

        self.add(nodes)
        self.add(lines)
        self.play(Write(hierarchical_label))
        self.wait(2)

        # Remove the hierarchical group
        self.play(FadeOut(nodes), FadeOut(lines), FadeOut(hierarchical_label))



        ## Graph
        graph_label = Text("Graph", color=WHITE).shift(UP * 3.5)

        # Create new nodes
        nodes_v2 = VGroup(
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4),  # D1
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4),  # D2
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4),  # D3
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4),  # D4
            Circle(fill_opacity=0.2, fill_color=YELLOW, color=WHITE).scale(0.4),  # D5
        )

        # Arrage nodes in a graph way
        nodes_v2[0].move_to(UP*2 + LEFT*2)     # D1
        nodes_v2[1].move_to(UP*2 + RIGHT*2)  # D2
        nodes_v2[2].move_to(ORIGIN)     # D3 (center)
        nodes_v2[3].move_to(DOWN*2 + LEFT*2)   # D4
        nodes_v2[4].move_to(DOWN*2 + RIGHT*2)   # D5

        # Lines between nodes
        lines_v2 = VGroup(
        # D1 -> D2
        Line(nodes_v2[0].get_right(), nodes_v2[1].get_left(), color=WHITE),
        # D1 -> D3 (use a diagonal position calculation)
        Line((nodes_v2[0].get_bottom() + nodes_v2[0].get_right()) / 2.1,
         (nodes_v2[2].get_top() + nodes_v2[2].get_left()) / 1.5, color=WHITE),
        # D1 -> D4
        Line(nodes_v2[0].get_bottom(), nodes_v2[3].get_top(), color=WHITE),
        # D2 -> D3 (use a diagonal position calculation)
        Line((nodes_v2[1].get_bottom() + nodes_v2[1].get_left()) / 2.1,
         (nodes_v2[2].get_top() + nodes_v2[2].get_right()) / 1.5, color=WHITE),
        # D3 -> D4
        Line((nodes_v2[2].get_bottom() + nodes_v2[2].get_left()) / 1.5,
         (nodes_v2[3].get_top() + nodes_v2[3].get_right()) / 2.1, color=WHITE),
        # D3 -> D5
            Line((nodes_v2[2].get_bottom() + nodes_v2[2].get_right()) / 1.5,
         (nodes_v2[4].get_top() + nodes_v2[4].get_left()) / 2.1, color=WHITE)
        )

        self.add(nodes_v2)
        self.add(lines_v2)
        self.play(Write(graph_label))
        self.wait(2)

        # Remove the graph group
        self.play(FadeOut(nodes_v2), FadeOut(lines_v2), FadeOut(graph_label))
