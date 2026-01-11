from manimlib import Scene
from manimlib import ReplacementTransform
from manimlib import Write, ShowCreation
from manimlib import Line
from manimlib.constants import *


# Custom Scene Class
class CustScene(Scene):
    current_subtitle = None

    def change_subtitle(self, new_subtitle, run_time=0.5, waiting_time=1.5) -> None:
        # if not self.current_subtitle:
        #     self.current_subtitle = new_subtitle
        #     self.play(Write(self.current_subtitle))
        #     return None

        self.play(
            ReplacementTransform(self.current_subtitle, new_subtitle),
            run_time=run_time
        )
        self.current_subtitle = new_subtitle

        if waiting_time > 0:
            self.wait(waiting_time)
        elif waiting_time != 0:
            print(f"Warning: Illegal waiting time: {waiting_time}!")

    # def fade_out_subtitle(self, run_time=1.0):
    #     if not self.current_subtitle:
    #         self.play(FadeOut(self.current_subtitle), run_time=run_time)
    #         self.current_subtitle = None

    def write_new_subtitle(self, new_subtitle, run_time=1.0):
        self.current_subtitle = new_subtitle
        self.play(Write(self.current_subtitle), run_time=run_time)

    def line_to_text(self, dot_a, dot_b, text, lining_time=0.5, run_time=0.5) -> None:
        point_a = dot_a.get_center()
        point_b = dot_b.get_center()
        vector_ab = point_b - point_a
        vector_ba = point_a - point_b
        line = Line(dot_a.get_edge_center(vector_ab), dot_b.get_edge_center(vector_ba), color=GOLD, stroke_width=8)
        self.play(
            ShowCreation(line),
            run_time=lining_time
        )

        self.play(
            ReplacementTransform(line, text),
            run_time=run_time
        )
