from manim import *

class ConsoleExample(Scene):
    def construct(self):
        # Simulate a Python program code
        code_text = Code(
            code="""
                def greet(name):
                return "Hello, " + name + "!"

                print(greet("World"))
                """,
            tab_width=4,
            background="window", # Adds a window-like background to the code
            language="Python",
            insert_line_no=True,
        ).move_to(UP * 2)

        # Create the initial console text (empty)
        console_prompt = Text(
            "C:\\> ",
            font="Courier",
            color=GREEN
        ).scale(0.7)

        # Create the output text, initially invisible
        output_text = Text(
            "Hello, World!",
            font="Courier",
            color=GREEN
        ).scale(0.7).set_opacity(0)

        # Create the cursor symbol, which will blink
        cursor = Text("_", font="Courier", color=GREEN).scale(0.7).next_to(console_prompt, RIGHT)

        # Position the output below the code
        console_prompt.next_to(code_text, DOWN*2)
        output_text.next_to(console_prompt, DOWN*1)

        # Show code and then animate console interaction
        self.play(Create(code_text))
        self.wait(1)

        # Typing animation for the console prompt
        self.play(Write(console_prompt))
        self.wait(0.5)
        # Simulate the typing of the command 'python my_script.py'
        command = "python my_script.py"
        for i, char in enumerate(command):
            self.play(Write(Text(char, font="Courier", color=GREEN).scale(0.7).next_to(console_prompt, RIGHT + i*0.1)))
            self.wait(0.1)  # small delay to simulate typing

        self.wait(0.5)

        # Add blinking cursor animation
        self.play(FadeIn(cursor), rate_func=lambda t: abs(math.sin(t * 10)), run_time=2)

        # Simulate a loading/waiting animation (e.g., '-\\|/' looping)
        loading_symbols = ["-", "\\", "|", "/"]
        loading_animation = [Text(sym, font="Courier", color=GREEN).scale(0.7).next_to(console_prompt, RIGHT * 3) for sym in loading_symbols]

        for sym in loading_animation:
            self.play(ReplacementTransform(cursor, sym), run_time=0.3)
            self.wait(0.3)

        # Fade in the output (as if the program has run)
        self.play(FadeIn(output_text))
        self.wait(2)
