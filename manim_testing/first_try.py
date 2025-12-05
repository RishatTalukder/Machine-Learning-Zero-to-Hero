from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class Square_with_text(Scene):
    def construct(self):
        #create a square and a text and group them
        square = Square()
        text = Text("Hello world")
        #text size smaller
        text.scale(0.5)
        group = VGroup(square, text)
        self.add(group)

        #wait 5 seconds
        self.wait(5)
        #now move the group to the far left of the screen
        self.play(group.animate.shift(LEFT * 5))

        #now make another box on the same position of the first box
        square2 = square.copy()
        text2 = text.copy()
        group2 = VGroup(square2, text2)
        self.add(group2)
        #while shifting there should be an arrow attached to the group
        self.play(group.animate.shift(RIGHT * 5), Create(Arrow(group.get_center(), group2.get_center())))



def create_textbox(color, string):
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=2, width=3, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result


class TextBox(Scene):  
    def construct(self):

        # create text box
        textbox = create_textbox(color=BLUE, string="Hello world")
        self.add(textbox)

        # move text box around
        self.play(textbox.animate.shift(2*RIGHT), run_time=3)
        self.play(textbox.animate.shift(2*UP), run_time=3)
        self.wait()
