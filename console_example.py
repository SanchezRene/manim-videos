from manim import *

class ConsoleExample(Scene):
    def construct(self):
        # Simulate a Python program code
        self.display_code()
        self.display_console()

    def display_code(self):
        """Display the code snippet with a window-like background."""
        code_text = Code(
            code="""
                def greet(name):
                    return "Hello, " + name + "!"

                print(greet("World"))
                """,
            tab_width=4,
            background="window",  # Adds a window-like background to the code
            language="Python",
            insert_line_no=True,
        ).to_edge(UP)
        
        self.play(Create(code_text))

    def display_console(self):
        """Display the simulated terminal with output text."""
        # Create a console background and label
        console_background = Rectangle(
            color="#0000AA", fill_opacity=0.85, width=8, height=1.5
        ).next_to(ORIGIN, DOWN*0.5)

        console_label = Text("Terminal:", color=WHITE).to_edge(LEFT).shift(UP * 0.5).scale(0.8)
        
        # Terminal output simulation
        output_1 = Text("C:\$ python my_script.py", font="Courier", color=WHITE).scale(0.7).next_to(console_label, DOWN*2, aligned_edge=LEFT)
        output_2 = Text("Hello, World!", font="Courier", color=WHITE).scale(0.7).next_to(output_1, DOWN, aligned_edge=LEFT)

        # Add console elements to the scene
        self.wait(1)
        self.add(console_label)
        self.add(console_background)
        self.play(Create(output_1))
        self.wait(0.5)
        self.play(Create(output_2))
        self.wait(2)
