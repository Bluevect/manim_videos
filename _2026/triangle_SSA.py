from manim_imports_ext import *

t2c_map = {
    "AB": BLUE_B,
    "BC": BLUE_B,
    "BH": BLUE_B,
    "CH": BLUE_B,
    "AH": BLUE_B,
    "AC": BLUE_B,
    r"\angle C": BLUE_B,
    r"\angle BHC": BLUE_B,
    r"\angle BHA": BLUE_B,
    r"\triangle BHC": BLUE_B,
    r"\mathrm{Rt}\triangle BHA": BLUE_B,
    r"\triangle ABC": BLUE_B,
    "DE": YELLOW_B,
    "EF": YELLOW_B,
    "EI": YELLOW_B,
    "FI": YELLOW_B,
    "DI": YELLOW_B,
    "DF": YELLOW_B,
    r"\angle F": YELLOW_B,
    r"\angle EIF": YELLOW_B,
    r"\angle EID": YELLOW_B,
    r"\triangle EIF": YELLOW_B,
    r"\mathrm{Rt}\triangle EID": YELLOW_B,
    r"\triangle DEF": YELLOW_B,
    "=": WHITE
}

t2c_map_for_tex_text = {
    "$B$": BLUE_B,
    r"$BH \bot AC$": BLUE_B,
    "$AC$": BLUE_B,
    "$H$": BLUE_B,
    "$E$": YELLOW_B,
    r"$EI \bot DF$": YELLOW_B,
    "$DF$": YELLOW_B,
    "$I$": YELLOW_B
}


class ShowQuestionScene(CustScene):
    def construct(self):
        self.wait()

        # ==== Debug ====
        # Create axes
        axes = Axes(
            x_range=(-7, 7),
            y_range=(-4, 4),
            width=14,
            height=8,

            axis_config={
                "stroke_color": WHITE,
                "stroke_width": 3
            }
        )

        axes.add_coordinate_labels(
            font_size=25,
            text_config={"font": "monospace"}
        )

        # self.play(ShowCreation(axes))
        # self.wait()

        # ==== Debug ends ====

        # ==== Show question ====
        dotx_a = DotX(np.array([-3, 3, 0]), "A", mark_pos=UP)
        dotx_b = DotX(np.array([-4.2, 1, 0]), "B", mark_pos=LEFT)
        dotx_c = DotX(np.array([-2.2, 1, 0]), "C", mark_pos=RIGHT)

        orig_triangle1 = TriangleX(dotx_a, dotx_b, dotx_c).set_color(BLUE_B) \
            .set_color_for_marks(WHITE)
        self.play(ShowCreation(orig_triangle1))
        self.wait()

        dotx_d = DotX(np.array([3, 3, 0]), "D", mark_pos=UP)
        dotx_e = DotX(np.array([1.8, 1, 0]), "E", mark_pos=LEFT)
        dotx_f = DotX(np.array([3.8, 1, 0]), "F", mark_pos=RIGHT)

        orig_triangle2 = TriangleX(dotx_d, dotx_e, dotx_f).set_color(YELLOW_B) \
            .set_color_for_marks(WHITE)
        self.play(ReplacementTransform(orig_triangle1.copy(), orig_triangle2))

        self.write_new_subtitle(Subtitle("这是两个三角形"))
        self.wait()

        self.change_subtitle(Subtitle("其中，"))

        conditions = Tex(
            "AB", "=", "DE", r",\quad ", "BC", "=", "EF",
            r",\quad ", r"\angle C", "=", r"\angle F",
            color=WHITE, tex_to_color_map=t2c_map
        )
        conditions.move_to(ORIGIN + DOWN)

        # AB
        self.line_to_text(dotx_a.dot, dotx_b.dot, conditions[0])
        self.play(Write(conditions[1]), run_time=0.5)
        # DE
        self.line_to_text(dotx_d.dot, dotx_e.dot, conditions[2])
        self.play(Write(conditions[3]), run_time=0.5)
        # BC
        self.line_to_text(dotx_b.dot, dotx_c.dot, conditions[4])
        self.play(Write(conditions[5]), run_time=0.5)
        # EF
        self.line_to_text(dotx_e.dot, dotx_f.dot, conditions[6])
        self.play(Write(conditions[7]), run_time=0.5)
        # \angle C
        angle_c = Arc(
            start_angle=np.pi - np.arctan(2.5),
            angle=np.arctan(2.5),
            arc_center=dotx_c.dot.get_center(),
            radius=0.3,
            color=BLUE_B
        )
        self.play(ShowCreation(angle_c), run_time=0.5)
        self.wait(0.5)
        self.play(ReplacementTransform(angle_c.copy(), conditions[8]), run_time=0.5)
        self.play(Write(conditions[9]), run_time=0.5)
        # \angle F
        angle_f = Arc(
            start_angle=np.pi - np.arctan(2.5),
            angle=np.arctan(2.5),
            arc_center=dotx_f.dot.get_center(),
            radius=0.3,
            color=YELLOW_B
        )
        self.play(ShowCreation(angle_f), run_time=0.5)
        self.wait(0.5)
        self.play(ReplacementTransform(angle_f.copy(), conditions[10]), run_time=0.5)
        self.wait()

        self.change_subtitle(Subtitle("众所周知，"), waiting_time=0.5)
        self.change_subtitle(
            Subtitle("三角形两边及一个邻角分别相等不能判定两个三角形全等"),
            run_time=0.3,
            waiting_time=2
        )
        # self.change_subtitle(Subtitle("我们将其简称为 SSA 命题不成立"), run_time=0.4, waiting_time=2)
        self.change_subtitle(Subtitle("即 SSA 不能判定两个三角形全等"), run_time=0.4, waiting_time=2)
        # self.change_subtitle(Subtitle("但是，SSA 为何不能用来判定全等呢？"), run_time=0.3)
        self.wait(2.5)
        # self.change_subtitle(Subtitle("下面我们尝试证明一下 SSA"), waiting_time=2)
        self.change_subtitle(Subtitle("但，这里有一个 SSA 能够判定全等的证明"), waiting_time=2)
        # Old Text
        # self.change_subtitle(Subtitle("相信大家在学习相关内容时，都曾尝试过证明 SSA"), run_time=0.3)
        # self.change_subtitle(Subtitle("有的证明甚至似乎是正确的"), waiting_time=2)
        # self.change_subtitle(Subtitle("例如下面这个证明"), waiting_time=2)

        self.play(self.current_subtitle.animate.shift(0.5 * UP), run_time=0.5, rate_func=smooth)
        self.play(self.current_subtitle.animate.shift(3 * DOWN), run_time=0.5, rate_func=rush_into)
        self.remove(self.current_subtitle)
        self.play(conditions.animate.shift(5 * DOWN), run_time=0.5, rate_func=rush_into)
        self.remove(conditions)

        dotx_a = DotX(np.array([2.5, 3, 0]), "A", mark_pos=UP)
        dotx_b = DotX(np.array([0.8, 1, 0]), "B", mark_pos=DOWN)
        dotx_c = DotX(np.array([3.2, 1, 0]), "C", mark_pos=DOWN)
        triangle1 = TriangleX(dotx_a, dotx_b, dotx_c).set_color(color=BLUE_B).set_color_for_marks(WHITE)
        dotx_d = DotX(np.array([5.8, 3, 0]), "D", mark_pos=UP)
        dotx_e = DotX(np.array([4.1, 1, 0]), "E", mark_pos=DOWN)
        dotx_f = DotX(np.array([6.5, 1, 0]), "F", mark_pos=DOWN)
        triangle2 = TriangleX(dotx_d, dotx_e, dotx_f).set_color(color=YELLOW_B).set_color_for_marks(WHITE)

        self.play(
            FadeOut(angle_c),
            FadeOut(angle_f)
        )

        self.play(
            ReplacementTransform(orig_triangle1, triangle1),
            ReplacementTransform(orig_triangle2, triangle2)
        )

        y_axis = Line(4 * DOWN, 4 * UP, color=WHITE, stroke_width=3)
        self.play(ShowCreation(y_axis))

        # Add ticks
        self.write_new_subtitle(Subtitle("为方便, 标记相等的线段和角度"))

        tick_ab = get_tick(dotx_a.get_point(), dotx_b.get_point())
        tick_de = get_tick(dotx_d.get_point(), dotx_e.get_point())
        tick_bc = get_double_tick(dotx_b.get_point(), dotx_c.get_point())
        tick_ef = get_double_tick(dotx_e.get_point(), dotx_f.get_point())

        angle_c = Arc(
            start_angle=np.pi - np.arctan(2.8571),  # (y_A - y_C) / (x_C - x_A)
            angle=np.arctan(2.8571),
            arc_center=dotx_c.get_point(),
            radius=0.3,
            color=WHITE
        )
        angle_f = Arc(
            start_angle=np.pi - np.arctan(2.8571),
            angle=np.arctan(2.8571),
            arc_center=dotx_f.get_point(),
            radius=0.3,
            color=WHITE
        )

        self.play(
            ShowCreation(tick_ab),
            ShowCreation(tick_de)
        )
        self.play(
            ShowCreation(tick_bc),
            ShowCreation(tick_ef)
        )
        self.play(
            ShowCreation(angle_c),
            ShowCreation(angle_f)
        )

        self.play(FadeOut(self.current_subtitle))

        proof = VGroup(
            TexText(r"证明：过点 $B$ 作 $BH \bot AC$ 交 $AC$ 于", tex_to_color_map=t2c_map_for_tex_text, color=WHITE),
            TexText(r"点 $H$，过点 $E$ 作 $EI \bot DF$ 交 $DF$ 于", tex_to_color_map=t2c_map_for_tex_text, color=WHITE),
            TexText(r"点 $I$ .", tex_to_color_map=t2c_map_for_tex_text, color=WHITE),
            Tex(r"\because BC = EF, \ \angle C = \angle F,",
                tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\angle BHC", "=", r"\angle EIF", r"= 90^\circ", tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\therefore ", r"\triangle BHC", r"\cong", r"\triangle EIF", r"\ \mathrm{(AAS)}",
                tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\therefore BH = EI, \ CH = FI", tex_to_color_map=t2c_map, color=WHITE),
            Tex(
                r"\because AB = DE, \ ", r"\angle BHA", "=", r"\angle EID", r"= 90^\circ",
                tex_to_color_map=t2c_map,
                color=WHITE
            ).set_color_by_tex_to_color_map(t2c_map),
            Tex(r"\therefore ", r"\mathrm{Rt}\triangle BHA", r"\cong", r"\mathrm{Rt}\triangle EID", r"\ \mathrm{(HL)}",
                tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\therefore AH = DI", tex_to_color_map=t2c_map, color=WHITE),
            # Tex(r"\because AC = AH + CH, \ DF = DI + FI", tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\therefore AC = DF", tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\therefore ", r"\triangle ABC", r"\cong", r"\triangle DEF", r"\ \mathrm{(SSS)} \quad \blacksquare",
                tex_to_color_map=t2c_map, color=WHITE)
        ).arrange(DOWN).scale(0.8)

        for i, tex_text in enumerate(proof):
            if not i == 0:
                tex_text.align_to(proof[i - 1], LEFT)

        proof.to_corner(UL).shift(0.2 * UL)

        # Calculate the equation of AC and BH (Hard coding)
        # Set y_AC = y_BH to solve the position of H
        dotx_h = DotX(np.array([2.9381, 1.7483, 0]), "H", mark_pos=UR, point_config={"color": BLUE_B})
        dotx_i = DotX(np.array([6.2381, 1.7483, 0]), "I", mark_pos=UR, point_config={"color": YELLOW_B})
        bh = DashedLine(dotx_b.dot.get_center(), dotx_h.dot.get_center(), color=BLUE_B)
        # angle: (y_H - y_B) / (x_H - x_B) + PI / 2
        elbow1 = Elbow(angle=0.3499 + PI / 2).move_to(dotx_h.dot)
        elbow1.shift(0.1 * UP + 0.22 * LEFT)
        ei = DashedLine(dotx_e.dot.get_center(), dotx_i.dot.get_center(), color=YELLOW_B)
        elbow2 = Elbow(angle=0.3499 + PI / 2).move_to(dotx_i.dot)
        elbow2.shift(0.1 * UP + 0.22 * LEFT)

        for i, tex_text in enumerate(proof):
            self.play(Write(tex_text))
            if i > 2:
                self.wait(2)
            if i == 2:
                self.play(ShowCreation(bh), ShowCreation(dotx_h))
                self.play(ShowCreation(elbow1))
                self.play(ShowCreation(ei), ShowCreation(dotx_i))
                self.play(ShowCreation(elbow2))
            if i == 5:
                triangle_bhc = Polygon(
                    dotx_b.get_point(),
                    dotx_c.get_point(),
                    dotx_h.get_point(),
                    color=GOLD
                ).set_fill(GOLD, opacity=0.5)
                triangle_eif = Polygon(
                    dotx_e.get_point(),
                    dotx_i.get_point(),
                    dotx_f.get_point(),
                    color=GOLD
                ).set_fill(GOLD, opacity=0.5)

                self.play(
                    ShowCreationThenDestruction(triangle_bhc),
                    ShowCreationThenDestruction(triangle_eif),
                    ShowCreationThenDestructionAround(tex_text),
                    run_time=4
                )

            if i == 8:
                triangle_bha = Polygon(
                    dotx_b.get_point(),
                    dotx_h.get_point(),
                    dotx_a.get_point(),
                    color=GOLD
                ).set_fill(GOLD, opacity=0.5)
                triangle_eid = Polygon(
                    dotx_e.get_point(),
                    dotx_i.get_point(),
                    dotx_d.get_point(),
                    color=GOLD
                ).set_fill(GOLD, opacity=0.5)

                self.wait()
                self.play(
                    ShowCreationThenDestruction(triangle_bha),
                    ShowCreationThenDestruction(triangle_eid),
                    ShowCreationThenDestructionAround(tex_text),
                    run_time=4
                )

            if i == 11:
                triangle_abc = Polygon(
                    dotx_a.get_point(),
                    dotx_b.get_point(),
                    dotx_c.get_point(),
                    color=GOLD
                ).set_fill(GOLD, opacity=0.5)
                triangle_def = Polygon(
                    dotx_d.get_point(),
                    dotx_e.get_point(),
                    dotx_f.get_point(),
                    color=GOLD
                ).set_fill(GOLD, opacity=0.5)

                self.wait()
                self.play(
                    ShowCreationThenDestruction(triangle_abc),
                    ShowCreationThenDestruction(triangle_def),
                    ShowCreationThenDestructionAround(tex_text),
                    run_time=4
                )

        self.current_subtitle = Subtitle(r"通过证明两个小三角形全等，$\triangle ABC \cong \triangle DEF$ 确实成立")
        self.play(Write(self.current_subtitle))
        self.wait()
        self.change_subtitle(Subtitle("那么，SSA 能用来判定全等了，吗？"))
        self.wait(2)

        count = 5
        count_tex = Tex(str(count), color=WHITE).to_corner(DR)
        self.play(Write(count_tex))
        for i in range(count - 1, 0, -1):
            new_count_tex = Tex(str(i), color=WHITE).to_corner(DR)
            # A number countdown takes 2s!
            self.wait()
            self.play(ReplacementTransform(count_tex, new_count_tex))
            count_tex = new_count_tex

        self.wait()
        self.play(Uncreate(count_tex))
        self.wait()
        self.change_subtitle(Subtitle("答案将在下期视频揭晓"), run_time=0.5, waiting_time=2)
        self.play(self.current_subtitle.animate.shift(0.5 * UP), run_time=0.5, rate_func=smooth)
        self.play(self.current_subtitle.animate.shift(3 * DOWN), run_time=0.5, rate_func=rush_into)
        self.remove(self.current_subtitle)

        # Create a screen rectangle covering the screen for texting
        cover = FullScreenRectangle(color="#333333")
        self.play(ShowCreation(cover), run_time=3)
        self.wait()

        # Ending part
        central_text = VGroup(
            TexText("Thanks for Watching!", font_size=95, color=YELLOW_B),
            TexText("Presented by 蓝叉戟"),
            TexText(
                "Powered by ManimGL v1.6.1",
                tex_to_color_map={"ManimGL": BLUE_B, "v1.6.1": GREEN_B}
            )
        )
        central_text.arrange(DOWN)
        central_text.to_edge(TOP)
        central_text.shift(DOWN)

        self.play(FadeIn(central_text[0], RIGHT), run_time=0.5)
        self.play(
            FadeIn(central_text[1], RIGHT),
            FadeIn(central_text[2], RIGHT),
            run_time=0.5
        )

        self.wait(3)

        # ==== Show question part ends ====

        # ==== Cut ====
        self.remove(central_text)
        self.write_new_subtitle(Subtitle("回到之前的证明"))
        self.wait()
        self.play(Uncreate(cover), run_time=2)
        self.change_subtitle(Subtitle("事实上，这个证明在过程上并没有错误"))
        self.wait()
        self.change_subtitle(Subtitle("但这个证明只证了两个三角形同为锐角三角形的情况"))
        self.wait()
        self.change_subtitle(Subtitle("并不能推广到所有三角形"))
        self.wait()
        self.play(FadeOut(self.current_subtitle, DOWN))

        hidden_condition = VGroup(
            TexText(r"前提：$\triangle ABC$ 与 $\triangle DEF$"),
            TexText(r"均为锐角三角形")
        ).arrange(DOWN * 1.5).move_to(ORIGIN + DOWN + RIGHT * 3.5)
        hidden_condition[1].align_to(hidden_condition[0], LEFT)
        self.play(Write(hidden_condition))
        self.wait()
        self.write_new_subtitle(Subtitle("因此该证明并不能说明 SSA 能用来判定全等"))
        self.wait()
        self.play(FadeOut(self.current_subtitle, DOWN))
        self.wait(2)

        # self.write_new_subtitle(Subtitle("虽然对于所有的三角形来说, SSA 全等并不成立"))
        # self.wait()
        # self.change_subtitle(Subtitle("但这个证明仍有其意义"))
        # self.wait()
        # self.change_subtitle(Subtitle("因为该证明指出，若两个三角形同为锐角三角形"))
        # self.wait()
        # self.change_subtitle(Subtitle("则可用 SSA 证明其全等"))
        # self.wait()
        self.write_new_subtitle(Subtitle("值得一提的是"))
        self.wait()
        self.change_subtitle(Subtitle("若两个三角形同为钝角三角形"))
        self.wait(2)
        self.change_subtitle(Subtitle("用类似的证明方法也可得其全等"))
        self.wait(2)

        # Proof for obtuse triangles
        dotx_a_obtuse = DotX(np.array([0.5, 3, 0]), "A", mark_pos=UP)
        dotx_b_obtuse = DotX(np.array([1.5, 1.5, 0]), "B", mark_pos=DOWN)
        dotx_c_obtuse = DotX(np.array([3.5, 1.5, 0]), "C", mark_pos=DOWN)
        triangle1_obtuse = (TriangleX(dotx_a_obtuse, dotx_b_obtuse, dotx_c_obtuse)
                            .set_color(color=BLUE_B).set_color_for_marks(WHITE))
        dotx_d_obtuse = DotX(np.array([3.5, 3, 0]), "D", mark_pos=UP)
        dotx_e_obtuse = DotX(np.array([4.5, 1.5, 0]), "E", mark_pos=DOWN)
        dotx_f_obtuse = DotX(np.array([6.5, 1.5, 0]), "F", mark_pos=DOWN)
        triangle2_obtuse = (TriangleX(dotx_d_obtuse, dotx_e_obtuse, dotx_f_obtuse)
                            .set_color(color=YELLOW_B).set_color_for_marks(WHITE))

        tick_ab_obtuse = get_tick(dotx_a_obtuse.get_point(), dotx_b_obtuse.get_point())
        tick_de_obtuse = get_tick(dotx_d_obtuse.get_point(), dotx_e_obtuse.get_point())
        tick_bc_obtuse = get_double_tick(dotx_b_obtuse.get_point(), dotx_c_obtuse.get_point())
        tick_ef_obtuse = get_double_tick(dotx_e_obtuse.get_point(), dotx_f_obtuse.get_point())

        dotx_h_obtuse = DotX(np.array([1.9, 2.3, 0]), "H", mark_pos=UR, point_config={"color": BLUE_B})
        dotx_i_obtuse = DotX(np.array([4.9, 2.3, 0]), "I", mark_pos=UR, point_config={"color": YELLOW_B})

        bh_obtuse = DashedLine(dotx_h_obtuse.get_point(), dotx_b_obtuse.get_point(), color=BLUE_B)
        ei_obtuse = DashedLine(dotx_e_obtuse.get_point(), dotx_i_obtuse.get_point(), color=YELLOW_B)

        angle_c_obtuse = Arc(
            start_angle=PI - 0.46,
            angle=0.46,
            arc_center=dotx_c_obtuse.get_point(),
            radius=0.5,
            color=WHITE
        )
        angle_f_obtuse = Arc(
            start_angle=PI - 0.46,
            angle=0.46,
            arc_center=dotx_f_obtuse.get_point(),
            radius=0.5,
            color=WHITE
        )

        elbow1_obtuse = Elbow(angle=1.1 + PI).move_to(dotx_h_obtuse.dot)
        elbow1_obtuse.shift(0.24 * DOWN + 0.05 * RIGHT)
        elbow2_obtuse = Elbow(angle=1.1 + PI).move_to(dotx_i_obtuse.dot)
        elbow2_obtuse.shift(0.24 * DOWN + 0.05 * RIGHT)

        hidden_condition_obtuse = VGroup(
            TexText(r"前提：$\triangle ABC$ 与 $\triangle DEF$"),
            TexText(r"均为钝角三角形")
        ).arrange(DOWN).move_to(DOWN * 0.5 + RIGHT * 3.5)
        hidden_condition_obtuse[1].align_to(hidden_condition_obtuse[0], LEFT)

        for i, tex_text in enumerate(proof):
            self.play(FadeOut(tex_text, LEFT), run_time=0.2)
        self.play(FadeOut(hidden_condition, RIGHT), run_time=0.2)

        self.play(
            Uncreate(tick_ab),
            Uncreate(tick_de),
            Uncreate(tick_bc),
            Uncreate(tick_ef),
            Uncreate(angle_c),
            Uncreate(angle_f),
            Uncreate(bh),
            Uncreate(ei),
            Uncreate(elbow1),
            Uncreate(elbow2),
            Uncreate(dotx_h),
            Uncreate(dotx_i)
        )
        self.play(
            ReplacementTransform(triangle1, triangle1_obtuse),
            ReplacementTransform(triangle2, triangle2_obtuse)
        )
        self.play(
            ShowCreation(tick_ab_obtuse),
            ShowCreation(tick_de_obtuse)
        )
        self.play(
            ShowCreation(tick_bc_obtuse),
            ShowCreation(tick_ef_obtuse)
        )
        self.play(
            ShowCreation(angle_c_obtuse),
            ShowCreation(angle_f_obtuse)
        )
        self.play(Write(hidden_condition_obtuse))
        self.play(FadeOut(self.current_subtitle, DOWN))

        # Proof for SSA of obtuse triangles (Unchanged)
        proof_for_ssa_obtuse = VGroup(
            TexText(r"证明：过点 $B$ 作 $BH \bot AC$ 交 $AC$ 于", tex_to_color_map=t2c_map_for_tex_text, color=WHITE),
            TexText(r"点 $H$，过点 $E$ 作 $EI \bot DF$ 交 $DF$ 于", tex_to_color_map=t2c_map_for_tex_text, color=WHITE),
            TexText(r"点 $I$ .", tex_to_color_map=t2c_map_for_tex_text, color=WHITE),
            Tex(r"\because BC = EF, \ \angle C = \angle F,",
                tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\angle BHC", "=", r"\angle EIF", r"= 90^\circ", tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\therefore ", r"\triangle BHC", r"\cong", r"\triangle EIF", r"\ \mathrm{(AAS)}",
                tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\therefore BH = EI, \ CH = FI", tex_to_color_map=t2c_map, color=WHITE),
            Tex(
                r"\because AB = DE, \ ", r"\angle BHA", "=", r"\angle EID", r"= 90^\circ",
                tex_to_color_map=t2c_map,
                color=WHITE
            ).set_color_by_tex_to_color_map(t2c_map),
            Tex(r"\therefore ", r"\mathrm{Rt}\triangle BHA", r"\cong", r"\mathrm{Rt}\triangle EID", r"\ \mathrm{(HL)}",
                tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\therefore AH = DI", tex_to_color_map=t2c_map, color=WHITE),
            # Tex(r"\because AC = AH + CH, \ DF = DI + FI", tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\therefore AC = DF", tex_to_color_map=t2c_map, color=WHITE),
            Tex(r"\therefore ", r"\triangle ABC", r"\cong", r"\triangle DEF", r"\ \mathrm{(SSS)} \quad \blacksquare",
                tex_to_color_map=t2c_map, color=WHITE)
        ).arrange(DOWN).scale(0.8)

        for i, tex_text in enumerate(proof_for_ssa_obtuse):
            if not i == 0:
                tex_text.align_to(proof_for_ssa_obtuse[i - 1], LEFT)

        proof_for_ssa_obtuse.to_corner(UL).shift(0.2 * UL)

        for i, tex_text in enumerate(proof_for_ssa_obtuse):
            self.play(Write(tex_text))

            if i == 2:
                self.play(
                    ShowCreation(dotx_h_obtuse),
                    ShowCreation(bh_obtuse),
                    ShowCreation(dotx_i_obtuse),
                    ShowCreation(ei_obtuse)
                )
                self.play(
                    ShowCreation(elbow1_obtuse),
                    ShowCreation(elbow2_obtuse)
                )

        # self.interact()
        self.wait(2)
        # self.change_subtitle(Subtitle("只要两个三角形的形状一致"))
        # self.wait()
        # self.change_subtitle(Subtitle("SSA 判定全等即可成立"))
        # self.wait(3)
        # self.play(FadeOut(self.current_subtitle, DOWN))

        # Create a screen rectangle covering the screen for texting
        cover = FullScreenRectangle(color="#333333")
        self.play(ShowCreation(cover), run_time=3)
        self.wait()

        self.write_new_subtitle(Subtitle("因此，我们可以拓展一下三角形全等的判定条件"))
        self.wait()

        conclusion = VGroup(
            TexText(r"若两个三角形同为锐角三角形或同为钝角三角形，"),
            TexText(r"且满足两边及一个邻角分别相等，"),
            TexText(r"则这两个三角形全等")
        ).arrange(DOWN).set_color(BLUE_B).move_to(ORIGIN)

        for i, tex_text in enumerate(conclusion):
            if not i == 0:
                tex_text.align_to(conclusion[i - 1], LEFT)

        for i, tex_text in enumerate(conclusion):
            self.play(Write(tex_text))

        self.wait(5)
        self.play(FadeOut(conclusion, LEFT))

        self.change_subtitle(Subtitle("实际上之前对三角形存在性的讨论是不完整的"))
        self.wait(2)
        self.change_subtitle(Subtitle("下面给出完整的讨论"))
        # self.change_subtitle(Subtitle("最后，我们再来回顾确定了两边及一邻角时，三角形的情况"))
        self.wait(2)
        self.play(FadeOut(self.current_subtitle, DOWN))
        self.wait()

        dotx_a_new = DotX(np.array([-3, 0, 0]), "A", mark_pos=LEFT, point_config={"color": BLUE_B})
        dotx_b_new = DotX(np.array([0, 2, 0]), "B", mark_pos=UP, point_config={"color": BLUE_B})
        dotx_d_new = DotX(np.array([5, 0, 0]), "D", mark_pos=DOWN, point_config={"color": BLUE_B})
        line_ab = Line(dotx_a_new.get_point(), dotx_b_new.get_point(), color=BLUE_B)
        line_ad = Line(dotx_a_new.get_point(), dotx_d_new.get_point(), color=BLUE_B)

        midpoint_ab = midpoint(dotx_a_new.get_point(), dotx_b_new.get_point())
        c_tex = Tex("c", color=WHITE).next_to(midpoint_ab, UL)

        angle_bad = Arc(
            start_angle=0,
            angle=np.arctan(2 / 3),
            arc_center=dotx_a_new.get_point(),
            radius=0.5,
            color=BLUE_B
        )

        self.play(
            ShowCreation(dotx_a_new),
            ShowCreation(dotx_b_new)
        )
        self.play(
            ShowCreation(line_ab),
            ShowCreation(line_ad)
        )
        self.play(
            ShowCreation(angle_bad),
            Write(c_tex)
        )
        self.wait(2)
        self.write_new_subtitle(Subtitle(r"当 $0 < a < c \sin A$ 时"))
        self.wait()

        dot_1 = Dot(np.array([1.12, 1, 0]), color=YELLOW_B)
        dotx_c_1 = DotX(
            np.array([0, 0.5, 0]),
            "C",
            mark_pos=RIGHT,
            point_config={"color": BLUE_B},
            mark_config={"color": WHITE}
        )
        line_1_rotate = Line(dot_1.get_center(), dotx_b_new.get_point(), color=YELLOW_B)
        arc_1 = Arc(
            start_angle=3.871,
            angle=1.682,
            arc_center=dotx_b_new.get_point(),
            radius=1.5,
            color=YELLOW_B
        )
        midpoint_bc_1 = midpoint(dotx_b_new.get_point(), dotx_c_1.get_point())
        a_tex_1 = Tex("a", color=WHITE).next_to(midpoint_bc_1, RIGHT)
        line_bc_1 = Line(dotx_b_new.get_point(), dotx_c_1.get_point(), color=BLUE_B)

        self.play(ShowCreation(line_1_rotate))

        line_1_rotate_copied = line_1_rotate.copy()

        self.play(
            Rotating(
                line_1_rotate_copied, 1.682, IN,
                about_point=dotx_b_new.get_point(),
                run_time=1
            ),
            Write(arc_1, rate_func=linear)
        )
        self.play(ShowCreation(dotx_c_1.dot))
        self.play(
            Uncreate(arc_1),
            Uncreate(line_1_rotate_copied),
            Uncreate(line_1_rotate)
        )
        self.play(
            Write(dotx_c_1.mark),
            Write(a_tex_1),
            ShowCreation(line_bc_1)
        )
        self.wait()
        self.change_subtitle(Subtitle(r"$\triangle ABC$ 不存在"), waiting_time=2)
        self.wait()

        self.play(
            Uncreate(line_bc_1),
            Uncreate(dotx_c_1),
            Uncreate(a_tex_1)
        )

        self.change_subtitle(Subtitle(r"当 $a = c \sin A$ 时"), waiting_time=2)

        dot_2 = Dot(np.array([1, 0.27, 0]), color=YELLOW_B)
        dotx_c_2 = DotX(
            np.array([0, 0, 0]),
            "C",
            mark_pos=DOWN,
            point_config={"color": BLUE_B},
            mark_config={"color": WHITE}
        )
        line_2_rotate = Line(dot_2.get_center(), dotx_b_new.get_point(), color=YELLOW_B)
        arc_2 = Arc(
            start_angle=4 * PI / 3,
            angle=PI / 3,
            arc_center=dotx_b_new.get_point(),
            radius=2,
            color=YELLOW_B
        )
        a_tex_2 = Tex("a", color=WHITE).next_to(UP, RIGHT)
        line_bc_2 = Line(dotx_b_new.get_point(), dotx_c_2.get_point(), color=BLUE_B)

        self.play(ShowCreation(line_2_rotate))

        line_2_rotate_copied = line_2_rotate.copy()

        self.play(
            Rotating(
                line_2_rotate_copied, PI / 3, IN,
                about_point=dotx_b_new.get_point(),
                run_time=1
            ),
            Write(arc_2, rate_func=linear)
        )
        self.play(ShowCreation(dotx_c_2.dot))
        self.play(
            Uncreate(arc_2),
            Uncreate(line_2_rotate_copied),
            Uncreate(line_2_rotate)
        )
        self.play(
            Write(dotx_c_2.mark),
            Write(a_tex_2),
            ShowCreation(line_bc_2)
        )
        self.wait()
        self.change_subtitle(Subtitle(r"$\triangle ABC$ 仅有一解"), waiting_time=2)
        self.wait()

        self.play(
            Uncreate(line_bc_2),
            Uncreate(dotx_c_2),
            Uncreate(a_tex_2)
        )

        self.change_subtitle(Subtitle(r"当 $c \sin A < a < c$ 时"), waiting_time=2)

        dot_3 = Dot(np.array([2, 0.5, 0]), color=YELLOW_B)
        dotx_c_3_1 = DotX(
            np.array([-1.5, 0, 0]),
            "C_1",
            mark_pos=DOWN,
            point_config={"color": BLUE_B},
            mark_config={"color": WHITE}
        )
        dotx_c_3_2 = DotX(
            np.array([1.5, 0, 0]),
            "C_2",
            mark_pos=DOWN,
            point_config={"color": BLUE_B},
            mark_config={"color": WHITE}
        )
        line_3_rotate = Line(dot_3.get_center(), dotx_b_new.get_point(), color=YELLOW_B)
        arc_3 = Arc(
            start_angle=3.785,
            angle=1.855,
            arc_center=dotx_b_new.get_point(),
            radius=2.5,
            color=YELLOW_B
        )
        a_tex_3_1 = Tex("a_1", color=WHITE).next_to(UR * 0.8, UR)
        a_tex_3_2 = Tex("a_2", color=WHITE).move_to(UL * 0.6)
        line_bc_3_1 = Line(dotx_b_new.get_point(), dotx_c_3_1.get_point(), color=BLUE_B)
        line_bc_3_2 = Line(dotx_b_new.get_point(), dotx_c_3_2.get_point(), color=BLUE_B)

        self.play(ShowCreation(line_3_rotate))

        line_3_rotate_copied = line_3_rotate.copy()

        self.play(
            Rotating(
                line_3_rotate_copied, 1.855, IN,
                about_point=dotx_b_new.get_point(),
                run_time=1
            ),
            Write(arc_3, rate_func=linear)
        )
        self.play(ShowCreation(dotx_c_3_1.dot))
        self.play(ShowCreation(dotx_c_3_2.dot))
        self.play(
            Uncreate(arc_3),
            Uncreate(line_3_rotate_copied),
            Uncreate(line_3_rotate)
        )
        self.play(
            Write(dotx_c_3_1.mark),
            Write(dotx_c_3_2.mark),
            Write(a_tex_3_1),
            Write(a_tex_3_2),
            ShowCreation(line_bc_3_1),
            ShowCreation(line_bc_3_2)
        )
        self.wait()
        self.change_subtitle(Subtitle(r"$\triangle ABC$ 有两解"), waiting_time=2)
        self.change_subtitle(Subtitle(r"且一解为锐角三角形，一解为钝角三角形"), waiting_time=2)
        self.wait()

        self.play(
            Uncreate(line_bc_3_1),
            Uncreate(line_bc_3_2),
            Uncreate(dotx_c_3_1),
            Uncreate(dotx_c_3_2),
            Uncreate(a_tex_3_1),
            Uncreate(a_tex_3_2)
        )

        self.change_subtitle(Subtitle(r"当 $a \geq c$ 时"), waiting_time=2)

        dot_4 = Dot(np.array([3.8, 0.94, 0]), color=YELLOW_B)
        dotx_c_4 = DotX(
            np.array([3.4, 0, 0]),
            "C",
            mark_pos=DOWN,
            point_config={"color": BLUE_B},
            mark_config={"color": WHITE}
        )
        line_4_rotate = Line(dot_4.get_center(), dotx_b_new.get_point(), color=YELLOW_B)
        arc_4 = Arc(
            start_angle=3.413,
            angle=2.598,
            arc_center=dotx_b_new.get_point(),
            radius=3.94,
            color=YELLOW_B
        )
        a_tex_4 = Tex("a", color=WHITE).move_to(UP * 1.2 + 2 * RIGHT)
        line_bc_4 = Line(dotx_b_new.get_point(), dotx_c_4.get_point(), color=BLUE_B)

        self.play(ShowCreation(line_4_rotate))

        line_4_rotate_copied = line_4_rotate.copy()

        self.play(
            Rotating(
                line_4_rotate_copied, 2.598, IN,
                about_point=dotx_b_new.get_point(),
                run_time=1
            ),
            Write(arc_4, rate_func=linear)
        )
        self.play(ShowCreation(dotx_c_4.dot))
        self.play(
            Uncreate(arc_4),
            Uncreate(line_4_rotate_copied),
            Uncreate(line_4_rotate)
        )
        self.play(
            Write(dotx_c_4.mark),
            Write(a_tex_4),
            ShowCreation(line_bc_4)
        )
        self.wait()
        self.change_subtitle(Subtitle(r"$\triangle ABC$ 仅有一解"))
        self.wait(3)

        # Uncreate Everything
        self.play(FadeOut(self.current_subtitle, DOWN))
        self.play(
            Uncreate(a_tex_4),
            Uncreate(c_tex)
        )
        self.play(
            Uncreate(line_bc_4),
            Uncreate(dotx_c_4),
            Uncreate(dotx_a_new),
            Uncreate(dotx_b_new),
            Uncreate(line_ab),
            Uncreate(line_ad),
            Uncreate(angle_bad)
        )
        # ==== Cut ends ====

        self.wait()

        # Ending part (Repeated)
        central_text = VGroup(
            TexText("Thanks for Watching!", font_size=95, color=YELLOW_B),
            TexText("Presented by 蓝叉戟"),
            TexText(
                "Powered by ManimGL v1.6.1",
                tex_to_color_map={"ManimGL": BLUE_B, "v1.6.1": GREEN_B}
            )
        )
        central_text.arrange(DOWN)
        central_text.to_edge(TOP)
        central_text.shift(DOWN)

        self.play(FadeIn(central_text[0], RIGHT), run_time=0.5)
        self.play(
            FadeIn(central_text[1], RIGHT),
            FadeIn(central_text[2], RIGHT),
            run_time=0.5
        )

        self.wait(3)


class SolutionScene(CustScene):
    def construct(self):
        # ==== Debug ====
        # Create axes
        axes = Axes(
            x_range=(-7, 7),
            y_range=(-4, 4),
            width=14,
            height=8,

            axis_config={
                "stroke_color": WHITE,
                "stroke_width": 3
            }
        )

        axes.add_coordinate_labels(
            font_size=25,
            text_config={"font": "monospace"}
        )

        # self.play(ShowCreation(axes))
        # self.wait()

        # ==== Debug ends ====

        # ==== Prove cosine law ====
        self.write_new_subtitle(Subtitle("为了证明 SSA 不能判定全等"))
        self.wait()
        self.change_subtitle(Subtitle("需要先找到一对满足 SSA 但不全等的一对特例三角形"))
        self.wait()
        self.change_subtitle(Subtitle("但直接画这样的一对特例也许有些棘手"))
        self.wait()
        self.change_subtitle(Subtitle("不妨先从代数的角度研究满足 SSA 的三角形"))
        self.wait()
        self.change_subtitle(Subtitle(
            "这就不得不介绍一下余弦定理",
            tex_to_color_map={
                "余弦定理": BLUE_B
            }
        ))
        self.wait()
        self.play(FadeOut(self.current_subtitle))

        cosine_law_intro = VGroup(
            TexText(
                "余弦定理：三角形中任意一边的平方等于其他两边的平方的和",
                color=WHITE,
                tex_to_color_map={
                    "余弦定理": BLUE_B
                }
            ),
            TexText(
                "减去这两边与它们的夹角的余弦的积的两倍",
                color=WHITE
            ),
            TexText(
                r"分别记两边为 $a$, $b$, 第三边为 $c$, 两边夹角为 $\theta$,",
                color=WHITE,
                tex_to_color_map={
                    "$a$": BLUE_B,
                    "$b$": BLUE_B,
                    "$c$": YELLOW_B,
                    r"$\theta$": BLUE_B
                }
            ),
            Tex(
                "c^2", "=", "a^2", "+", "b^2", "-", r"2ab\cos \theta",
                tex_to_color_map={
                    "c^2": YELLOW_B,
                    "a^2": BLUE_B,
                    "b^2": BLUE_B,
                    r"2ab\cos \theta": BLUE_B,
                    "=": WHITE,
                    "+": WHITE,
                    "-": WHITE
                }
            ),
            Tex(
                "b^2", "=", "a^2", "+", "c^2", "-", r"2ac\cos B",
                tex_to_color_map={
                    "b^2": YELLOW_B,
                    "a^2": BLUE_B,
                    "c^2": BLUE_B,
                    r"2ac\cos B": BLUE_B,
                    "=": WHITE,
                    "+": WHITE,
                    "-": WHITE
                }
            ),
            Tex(
                "a^2", "=", "b^2", "+", "c^2", "-", r"2bc\cos A",
                tex_to_color_map={
                    "a^2": YELLOW_B,
                    "b^2": BLUE_B,
                    "c^2": BLUE_B,
                    r"2bc\cos A": BLUE_B,
                    "=": WHITE,
                    "+": WHITE,
                    "-": WHITE
                }
            )
        ).arrange(DOWN)

        for i, tex_text in enumerate(cosine_law_intro):
            if i > 0:
                tex_text.align_to(cosine_law_intro[i - 1], LEFT)

        cosine_law_intro.to_edge(UL).shift(0.1 * UL)

        dotx_a_acute = DotX(np.array([4.8, 1, 0]), "A", mark_pos=UP)
        dotx_b_acute = DotX(np.array([3.1, -1, 0]), "B", mark_pos=DOWN)
        dotx_c_acute = DotX(np.array([5.5, -1, 0]), "C", mark_pos=DOWN)
        triangle_acute = TriangleX(dotx_a_acute, dotx_b_acute, dotx_c_acute) \
            .set_color(color=BLUE_B).set_color_for_marks(WHITE)
        angle_theta = Arc(
            start_angle=np.pi - np.arctan(2.8571),
            angle=np.arctan(2.8571),
            arc_center=dotx_c_acute.get_point(),
            radius=0.3,
            color=WHITE
        )
        midpoint_bc = midpoint(dotx_b_acute.get_point(), dotx_c_acute.get_point())
        midpoint_ac = midpoint(dotx_a_acute.get_point(), dotx_c_acute.get_point())
        midpoint_ab = midpoint(dotx_a_acute.get_point(), dotx_b_acute.get_point())

        a_tex = Tex("a", color=WHITE).next_to(midpoint_bc, DOWN)
        b_tex = Tex("b", color=WHITE).next_to(
            midpoint_ac, get_unit_vector_on_direction(midpoint_ac - dotx_b_acute.get_point()))
        c_tex = Tex("c", color=WHITE).next_to(
            midpoint_ab, get_unit_vector_on_direction(midpoint_ab - dotx_c_acute.get_point()))
        theta_tex = Tex(r"\theta", color=WHITE).next_to(angle_theta, 0.2 * UP + 0.5 * LEFT)

        for i, tex_text in enumerate(cosine_law_intro):
            if i < 3:
                self.play(Write(tex_text))
                if i != 0:
                    self.wait(2)

            if i == 2:
                self.play(ShowCreation(triangle_acute))
                self.play(ShowCreation(angle_theta))
                self.play(Write(theta_tex))
                self.play(
                    Write(a_tex),
                    Write(b_tex),
                    Write(c_tex)
                )

            elif i == 3:
                self.line_to_text(dotx_a_acute.dot, dotx_b_acute.dot, tex_text[0])
                self.play(Write(tex_text[1]))
                self.line_to_text(dotx_b_acute.dot, dotx_c_acute.dot, tex_text[2])
                self.play(Write(tex_text[3]))
                self.line_to_text(dotx_a_acute.dot, dotx_c_acute.dot, tex_text[4])
                self.play(Write(tex_text[5]))
                self.play(ReplacementTransform(angle_theta.copy(), tex_text[6]))

        self.write_new_subtitle(Subtitle("其余两个角也有对应关系"))
        self.wait()

        self.play(
            TransformMatchingTex(cosine_law_intro[3].copy(), cosine_law_intro[4]),
            key_map={
                r"2ab\cos \theta": r"2ac\cos \angle ABC",
            }
        )
        self.play(
            TransformMatchingTex(cosine_law_intro[3].copy(), cosine_law_intro[5]),
            key_map={
                r"2ab\cos \theta": r"2bc\cos \angle BAC",
            }
        )
        self.wait()

        self.play(FadeOut(self.current_subtitle))

        for i, tex_text in enumerate(cosine_law_intro):
            if i < 3:
                self.play(FadeOut(tex_text, RIGHT), run_time=0.4 - 0.1 * i)
            elif i > 3:
                self.play(FadeOut(cosine_law_intro[i], RIGHT), run_time=0.2)

        cosine_law = cosine_law_intro[3].copy().to_corner(UR)
        self.play(ReplacementTransform(cosine_law_intro[3], cosine_law), run_time=2)

        self.write_new_subtitle(Subtitle("高中课本里对余弦定理的证明使用了向量"))
        self.wait()
        self.change_subtitle(Subtitle("为了照顾初中生，接下来介绍一种更朴素的证明方法"))
        self.wait()
        self.change_subtitle(Subtitle("先来看看锐角三角形的情况"))
        self.wait()
        self.play(FadeOut(self.current_subtitle))

        t2c_map_for_tex_text_2 = {
            "$A$": BLUE_B,
            r"$AH \bot BC$": BLUE_B,
            "$BC$": BLUE_B,
            "$H$": BLUE_B,
            "勾股定理": BLUE_B
        }

        proof_for_acute_triangles = VGroup(
            TexText(r"过点 $A$ 作 $AH \bot BC$ 交 $BC$ 于点 $H$", color=WHITE, tex_to_color_map=t2c_map_for_tex_text_2),
            TexText(r"设 $HC = x$, 则 $BH = a - x$", color=WHITE, tex_to_color_map=t2c_map_for_tex_text_2),
            TexText("根据勾股定理得", color=WHITE, tex_to_color_map=t2c_map_for_tex_text_2),
            Tex("c^2", "-", "(a - x)^2", "=", "b^2", "-", "x^2", color=WHITE),
            Tex("c^2", "-", "a^2", "+", "2ax", "-", "x^2", "=", "b^2", "-", "x^2", color=WHITE),
            Tex("c^2", "-", "a^2", "-", "b^2", "+", "2ax", "=", "0", color=WHITE),
            Tex("2ax", "=", "a^2", "+", "b^2", "-", "c^2", color=WHITE),
            Tex("x", "=", r"\frac {a^2 + b^2 - c^2}{2a}", color=WHITE),
            Tex(r"\cos \theta", "=", r"\frac xb", "=", r"\frac {a^2 + b^2 - c^2}{2ab}", color=WHITE),
            Tex("2ab", r"\cos \theta", "=", "a^2", "+", "b^2", "-", "c^2", color=WHITE),
            Tex("c^2", "=", "a^2", "+", "b^2", "-2ab", r"\cos \theta", r"\quad", r"\blacksquare", color=WHITE)
        ).arrange(DOWN * 1.5).scale(0.8)

        for i, tex_text in enumerate(proof_for_acute_triangles):
            if 0 < i <= 3:
                tex_text.align_to(proof_for_acute_triangles[i - 1], LEFT)
            else:
                tex_text.align_to(proof_for_acute_triangles[2], LEFT)

        proof_for_acute_triangles.to_edge(UL).shift(0.1 * UL)

        y_axis = Line(4 * DOWN, 4 * UP, color=WHITE, stroke_width=3)
        self.play(ShowCreation(y_axis))

        # Assign mobjects
        dotx_h_acute = DotX(np.array([4.8, -1, 0]), "H", mark_pos=DOWN, point_config={"color": BLUE_B})
        ah = DashedLine(dotx_a_acute.dot.get_center(), dotx_h_acute.dot.get_center(), color=BLUE_B)

        hc = Line(dotx_h_acute.get_point(), dotx_c_acute.get_point())
        brace_hc = Brace(hc, DOWN).shift(0.7 * DOWN)
        brace_tex_hc = Tex("x").next_to(brace_hc, DOWN)

        bh = Line(dotx_b_acute.get_point(), dotx_h_acute.get_point())
        brace_bh = Brace(bh, DOWN).shift(0.7 * DOWN)
        brace_tex_bh = Tex("a - x").next_to(brace_bh, DOWN)

        # Animate tex texts
        for i, tex_text in enumerate(proof_for_acute_triangles):
            if i <= 3:
                self.play(Write(tex_text))
                self.wait(2)
            elif i <= 7:
                self.play(TransformMatchingTex(proof_for_acute_triangles[i - 1].copy(), tex_text))
                self.wait(2)
            elif i > 7:
                tex_text.next_to(proof_for_acute_triangles[i - 1], 1.5 * DOWN)
                tex_text.align_to(proof_for_acute_triangles[i - 1], LEFT)
                self.play(TransformMatchingTex(proof_for_acute_triangles[i - 1].copy(), tex_text))
                self.wait(2)

            if i == 0:
                self.play(
                    ShowCreation(dotx_h_acute),
                    ShowCreation(ah)
                )
            elif i == 1:
                self.play(
                    ShowCreation(brace_hc),
                    ShowCreation(brace_tex_hc)
                )

                self.play(
                    ShowCreation(brace_bh),
                    ShowCreation(brace_tex_bh)
                )
            elif i == 7:
                for j in range(3, 7):
                    self.play(FadeOut(proof_for_acute_triangles[j], LEFT), run_time=0.4 - 0.1 * (j - 3))

                self.play(tex_text.animate.shift(2.75 * UP))

        # Fade Out and Uncreate
        self.wait(5)
        for i in range(0, 11):
            if 0 <= i <= 2 or 7 <= i <= 11:
                self.play(FadeOut(proof_for_acute_triangles[i], LEFT), run_time=0.2)

        self.play(
            Uncreate(brace_bh),
            Uncreate(brace_hc),
            Uncreate(brace_tex_bh),
            Uncreate(brace_tex_hc),
            run_time=0.5
        )
        self.play(
            Uncreate(a_tex),
            Uncreate(b_tex),
            Uncreate(c_tex),
            Uncreate(angle_theta),
            Uncreate(theta_tex),
            run_time=0.5
        )
        self.play(
            Uncreate(ah),
            Uncreate(dotx_h_acute),
            run_time=0.5
        )

        self.write_new_subtitle(Subtitle("下面讨论钝角三角形的情况"))
        self.wait()
        self.play(FadeOut(self.current_subtitle))

        dotx_a_obtuse = DotX(np.array([5.8, 1.5, 0]), "A", mark_pos=UP)
        dotx_b_obtuse = DotX(np.array([3, -0.5, 0]), "B", mark_pos=DOWN)
        dotx_c_obtuse = DotX(np.array([5, -0.5, 0]), "C", mark_pos=DOWN)
        triangle_obtuse = TriangleX(dotx_a_obtuse, dotx_b_obtuse, dotx_c_obtuse) \
            .set_color(color=BLUE_B).set_color_for_marks(WHITE)
        angle_theta = Arc(
            # Calculate the tangent value:
            # \tan start_angle = (y_A - y_C) / (x_A - x_C)
            start_angle=np.arctan(2.5),
            angle=np.pi - np.arctan(2.5),
            arc_center=dotx_c_obtuse.get_point(),
            radius=0.3,
            color=WHITE
        )
        midpoint_bc = midpoint(dotx_b_obtuse.get_point(), dotx_c_obtuse.get_point())
        midpoint_ac = midpoint(dotx_a_obtuse.get_point(), dotx_c_obtuse.get_point())
        midpoint_ab = midpoint(dotx_a_obtuse.get_point(), dotx_b_obtuse.get_point())

        a_tex = Tex("a", color=WHITE).next_to(midpoint_bc, DOWN)
        b_tex = Tex("b", color=WHITE).next_to(
            midpoint_ac, get_unit_vector_on_direction(dotx_b_obtuse.get_point() - midpoint_ac) + 0.35 * UP)
        c_tex = Tex("c", color=WHITE).next_to(
            midpoint_ab, get_unit_vector_on_direction(midpoint_ab - dotx_c_obtuse.get_point()))
        theta_tex = Tex(r"\theta", color=WHITE).next_to(angle_theta, 0.25 * UP + 0.4 * LEFT)

        self.wait()
        self.play(
            ReplacementTransform(triangle_acute, triangle_obtuse),
            y_axis.animate.shift(RIGHT * 0.6)
        )
        self.play(ShowCreation(angle_theta))
        self.play(Write(theta_tex))
        self.play(
            Write(a_tex),
            Write(b_tex),
            Write(c_tex)
        )

        proof_for_obtuse_triangles = VGroup(
            TexText(r"过点 $A$ 作 $AH \bot BC$ 交射线 $BC$ 于点 $H$", color=WHITE,
                    tex_to_color_map=t2c_map_for_tex_text_2),
            TexText(r"设 $HC = x$, 则 $BH = a + x$", color=WHITE, tex_to_color_map=t2c_map_for_tex_text_2),
            TexText("根据勾股定理得", color=WHITE, tex_to_color_map=t2c_map_for_tex_text_2),
            Tex("c^2", "-", "(a + x)^2", "=", "b^2", "-", "x^2", color=WHITE),
            Tex("c^2", "-", "a^2", "-", "2ax", "-", "x^2", "=", "b^2", "-", "x^2", color=WHITE),
            Tex("c^2", "-", "a^2", "-", "b^2", "-", "2ax", "=", "0", color=WHITE),
            Tex("2ax", "=", "c^2", "-", "a^2", "-", "b^2", color=WHITE),
            Tex("x", "=", r"\frac {c^2 - a^2 - b^2}{2a}", color=WHITE),
            Tex(r"\cos (\pi - \theta)", "=", r"\frac xb", "=", r"\frac {c^2 - a^2 - b^2}{2ab}", color=WHITE),
            Tex("2ab", r"\cos (\pi - \theta)", "=", "c^2", "-", "a^2", "-", "b^2", color=WHITE),
            Tex("c^2", "=", "a^2", "+", "b^2", "+", "2ab", r"\cos (\pi - \theta)", color=WHITE),
            Tex("c^2", "=", "a^2", "+", "b^2", "-", "2ab", r"\cos \theta", r"\quad", r"\blacksquare", color=WHITE),
        ).arrange(DOWN * 1.5).scale(0.8)

        for i, tex_text in enumerate(proof_for_obtuse_triangles):
            if 0 < i <= 3:
                tex_text.align_to(proof_for_obtuse_triangles[i - 1], LEFT)
            else:
                tex_text.align_to(proof_for_obtuse_triangles[2], LEFT)

        proof_for_obtuse_triangles.to_edge(UL).shift(0.1 * UL)

        # Assign mobjects
        dotx_h_obtuse = DotX(np.array([5.8, -0.5, 0]), "H", mark_pos=DOWN, point_config={"color": BLUE_B})
        ah = DashedLine(dotx_a_obtuse.dot.get_center(), dotx_h_obtuse.dot.get_center(), color=BLUE_B)

        hc = DashedLine(dotx_h_obtuse.get_point(), dotx_c_obtuse.get_point(), color=BLUE_B)
        brace_hc = Brace(hc, DOWN).shift(0.7 * DOWN)
        brace_tex_hc = Tex("x").next_to(brace_hc, DOWN)

        bc = Line(dotx_b_obtuse.get_point(), dotx_c_obtuse.get_point())
        brace_bc = Brace(bc, DOWN).shift(0.7 * DOWN)
        brace_tex_bc = Tex("a").next_to(brace_bc, DOWN)

        induction_formula = Tex(
            r"\cos", "(", r"\pi", "-", r"\theta", ")", "=", "-", r"\cos", r"\theta",
            color=BLUE_B,
            tex_to_color_map={
                "=": WHITE
            }
        ).to_corner(DR)

        # Animate tex texts
        for i, tex_text in enumerate(proof_for_obtuse_triangles):
            if i <= 3:
                self.play(Write(tex_text))
                self.wait(2)
            elif i <= 7:
                self.play(TransformMatchingTex(proof_for_obtuse_triangles[i - 1].copy(), tex_text))
                self.wait(2)
            elif i > 7:
                tex_text.next_to(proof_for_obtuse_triangles[i - 1], 1.5 * DOWN)
                tex_text.align_to(proof_for_obtuse_triangles[i - 1], LEFT)
                self.play(TransformMatchingTex(proof_for_obtuse_triangles[i - 1].copy(), tex_text))
                self.wait(2)
            elif i > 10:
                tex_text.next_to(proof_for_obtuse_triangles[i - 1], 1.5 * DOWN)
                tex_text.align_to(proof_for_obtuse_triangles[i - 1], LEFT)
                self.play(TransformMatchingTex(proof_for_obtuse_triangles[i - 1].copy(), tex_text))
                self.wait(2)

            if i == 0:
                self.play(
                    ShowCreation(dotx_h_obtuse),
                    ShowCreation(ah),
                    ShowCreation(hc)
                )
            elif i == 1:
                self.play(
                    ShowCreation(brace_hc),
                    ShowCreation(brace_tex_hc)
                )

                self.play(
                    ShowCreation(brace_bc),
                    ShowCreation(brace_tex_bc)
                )
            elif i == 7:
                for j in range(3, 7):
                    self.play(FadeOut(proof_for_obtuse_triangles[j], LEFT), run_time=0.4 - 0.1 * (j - 3))

                self.play(tex_text.animate.shift(2.75 * UP))
            elif i == 8:
                self.write_new_subtitle(Subtitle(r"这里 $\pi$ 即 $180^\circ$", tex_to_color_map={
                    r"$\pi$": BLUE_B,
                    r"$180^\circ$": BLUE_B
                }))
                self.wait(2)
            elif i == 10:
                self.play(FadeOut(proof_for_obtuse_triangles[2], LEFT), run_time=0.4)
                for j in range(7, 10):
                    self.play(FadeOut(proof_for_obtuse_triangles[j], LEFT), run_time=0.4 - 0.1 * (j - 7))

                self.play(tex_text.animate.shift(3.85 * UP))

                self.play(FadeOut(self.current_subtitle))
                self.write_new_subtitle(Subtitle("由诱导公式"))
                self.play(Write(induction_formula))
                self.wait(2)
                self.play(ShowCreationThenDestructionAround(induction_formula))
                self.play(FadeOut(self.current_subtitle))

        # Fade Out and Uncreate
        self.wait(5)
        for i in range(0, 12):
            if 0 <= i <= 1 or 10 <= i <= 11:
                self.play(FadeOut(proof_for_obtuse_triangles[i], LEFT), run_time=0.2)

        self.play(
            Uncreate(brace_bc),
            Uncreate(brace_hc),
            Uncreate(brace_tex_bc),
            Uncreate(brace_tex_hc),
            run_time=0.5
        )
        self.play(
            Uncreate(a_tex),
            Uncreate(b_tex),
            Uncreate(c_tex),
            Uncreate(angle_theta),
            Uncreate(theta_tex),
            run_time=0.5
        )
        self.play(
            Uncreate(ah),
            Uncreate(dotx_h_obtuse),
            Uncreate(hc),
            FadeOut(induction_formula, DOWN),
            run_time=0.5
        )

        self.write_new_subtitle(Subtitle("直角三角形的情况"))
        self.wait()

        dotx_a_rt = DotX(np.array([5, 1.5, 0]), "A", mark_pos=UP)
        dotx_b_rt = DotX(np.array([3, -0.5, 0]), "B", mark_pos=DOWN)
        dotx_c_rt = DotX(np.array([5, -0.5, 0]), "C", mark_pos=DOWN)
        triangle_rt = TriangleX(dotx_a_rt, dotx_b_rt, dotx_c_rt) \
            .set_color(color=BLUE_B).set_color_for_marks(WHITE)

        elbow_theta = Elbow(angle=PI / 2).move_to(dotx_c_rt.dot).shift(0.12 * UL)
        midpoint_bc = midpoint(dotx_b_rt.get_point(), dotx_c_rt.get_point())
        midpoint_ac = midpoint(dotx_a_rt.get_point(), dotx_c_rt.get_point())
        midpoint_ab = midpoint(dotx_a_rt.get_point(), dotx_b_rt.get_point())

        a_tex = Tex("a", color=WHITE).next_to(midpoint_bc, DOWN)
        b_tex = Tex("b", color=WHITE).next_to(
            midpoint_ac, get_unit_vector_on_direction(midpoint_ac - dotx_b_rt.get_point()))
        c_tex = Tex("c", color=WHITE).next_to(
            midpoint_ab, get_unit_vector_on_direction(midpoint_ab - dotx_c_rt.get_point()))
        theta_tex = Tex(r"\theta", color=WHITE).next_to(elbow_theta, 0.25 * UP + 0.4 * LEFT)

        self.wait()
        self.play(
            ReplacementTransform(triangle_obtuse, triangle_rt),
            y_axis.animate.shift(LEFT * 0.6)
        )
        self.play(ShowCreation(elbow_theta))
        self.play(Write(theta_tex))
        self.play(
            Write(a_tex),
            Write(b_tex),
            Write(c_tex)
        )

        proof_for_rt_triangles = VGroup(
            TexText("由于此时", color=WHITE),
            Tex(
                r"\cos \theta", "=", r"\cos \frac \pi 2", "=", "0", color=WHITE,
                tex_to_color_map={
                    r"\cos \theta": BLUE_B,
                    r"\cos \frac \pi 2": BLUE_B
                }
            ),
            TexText("则有", color=WHITE),
            cosine_law.copy()
        ).arrange(DOWN * 1.5)

        for i, tex_text in enumerate(proof_for_rt_triangles):
            if i > 0:
                tex_text.align_to(proof_for_rt_triangles[i - 1], LEFT)

        proof_for_rt_triangles.to_edge(UL).shift(0.1 * UL)

        simplified_cosine_law = Tex(
            "c^2", "=", "a^2", "+", "b^2",
            tex_to_color_map={
                "c^2": YELLOW_B,
                "a^2": BLUE_B,
                "b^2": BLUE_B,
                "=": WHITE,
                "+": WHITE,
                "-": WHITE
            }
        ).move_to(proof_for_rt_triangles[3]).align_to(proof_for_rt_triangles[3], LEFT)

        for i, tex_text in enumerate(proof_for_rt_triangles):
            if 0 <= i <= 2:
                self.play(Write(tex_text))
                if i > 0:
                    self.wait()
            elif i == 3:
                self.play(ReplacementTransform(cosine_law.copy(), tex_text))
                self.wait()
                self.play(ReplacementTransform(tex_text, simplified_cosine_law))
                self.change_subtitle(Subtitle("可见，此时勾股定理即为余弦定理的一个特殊情况"))
                self.wait(2)

        self.change_subtitle(Subtitle("余弦定理证毕"))
        # ==== Prove cosine law ends ====

        # Switching everything
        self.wait(5)
        self.play(FadeOut(self.current_subtitle))
        for i in range(0, 3):
            self.play(FadeOut(proof_for_rt_triangles[i], LEFT), run_time=0.2)
        self.play(FadeOut(simplified_cosine_law, LEFT), run_time=0.2)
        self.play(
            Uncreate(elbow_theta),
            Uncreate(theta_tex),
            Uncreate(a_tex),
            Uncreate(b_tex),
            Uncreate(c_tex)
        )

        # Re-assign mobjects
        dotx_a_acute = DotX(np.array([3, 1.25, 0]), "A", mark_pos=UP)
        dotx_b_acute = DotX(np.array([2.1, -1, 0]), "B", mark_pos=DOWN)
        dotx_c_acute = DotX(np.array([5.5, -1, 0]), "C", mark_pos=DOWN)
        angle_value = get_angle_of_3_points(
            dotx_a_acute.get_point(),
            dotx_c_acute.get_point(),
            dotx_b_acute.get_point()
        )
        triangle_acute = TriangleX(dotx_a_acute, dotx_b_acute, dotx_c_acute) \
            .set_color(color=BLUE_B).set_color_for_marks(WHITE)
        angle_theta = Arc(
            start_angle=np.pi - angle_value,
            angle=angle_value,
            arc_center=dotx_c_acute.get_point(),
            radius=0.3,
            color=WHITE
        )
        midpoint_bc = midpoint(dotx_b_acute.get_point(), dotx_c_acute.get_point())
        midpoint_ac = midpoint(dotx_a_acute.get_point(), dotx_c_acute.get_point())
        midpoint_ab = midpoint(dotx_a_acute.get_point(), dotx_b_acute.get_point())

        a_tex = Tex("a", color=WHITE).next_to(midpoint_bc, DOWN)
        x_tex = Tex("x", color=WHITE).next_to(
            midpoint_ac, get_unit_vector_on_direction(midpoint_ac - dotx_b_acute.get_point()))
        c_tex = Tex("c", color=WHITE).next_to(
            midpoint_ab, get_unit_vector_on_direction(midpoint_ab - dotx_c_acute.get_point()))
        theta_tex = Tex(r"\theta", color=WHITE).next_to(angle_theta, 0.4 * RIGHT + 0.2 * UP)

        self.play(ReplacementTransform(triangle_rt, triangle_acute))

        self.play(ShowCreation(angle_theta))
        self.play(Write(theta_tex))
        self.play(
            Write(a_tex),
            Write(c_tex)
        )

        self.write_new_subtitle(Subtitle("若 SSA 能够用于判定全等"))
        self.wait()
        self.change_subtitle(Subtitle("则已知两条边和一个邻角，三角形只能有一种情况"))
        self.change_subtitle(Subtitle("第三条边也只能有一种情况"))
        self.change_subtitle(Subtitle(r"这里 $a$, $c$, $\theta$ 均为已知量"), waiting_time=2)
        self.change_subtitle(Subtitle("设第三边为 $x$"), waiting_time=2)
        self.play(Write(x_tex))
        self.change_subtitle(Subtitle("若 SSA 成立，则 $x$ 有唯一确定的值"))
        self.change_subtitle(Subtitle("根据余弦定理"))
        self.play(ShowCreationThenDestructionAround(cosine_law))

        exploration_1 = VGroup(
            Tex("c^2", "=", "a^2", "+", "x^2", "-", r"2ax \cos \theta", color=WHITE),
            Tex(r"x^2", "-", r"2ax \cos \theta", "+", "a^2", "-", "c^2", "=", "0", color=WHITE),
            Tex(
                r"\Delta", "=", "4", "a^2", r"\cos^2 \theta", "-", "4", "(", "a^2", "-", "c^2", ")",
                color=WHITE
            ),
            Tex(
                r"\Delta", "=", "4", "a^2", r"\cos^2 \theta", "-", "4", "a^2", "+", "4", "c^2",
                color=WHITE
            ),
            Tex(
                r"\Delta", "=", "4", "a^2", "(", r"\cos^2 \theta", "-", "1", ")", "+", "4", "c^2",
                color=WHITE
            ),
            Tex(
                "4", "a^2", "(", r"\cos^2 \theta", "-", "1", ")", "+", "4", "c^2", r"\geq", "0",
                color=WHITE
            ),
            Tex(
                "4", "c^2", r"\geq", "4", "a^2", "(", "1", "-", r"\cos^2 \theta", ")",
                color=WHITE
            ),
            Tex(
                "c^2", r"\geq", " ", "a^2", r"\sin^2 \theta",
                color=WHITE
            ),
            Tex(
                "c", r"\geq", " ", "a", r"\sin", r"\theta",
                color=WHITE
            )
        ).arrange(DOWN * 1.5).scale(0.8)

        for i, tex_text in enumerate(exploration_1):
            if i > 0:
                tex_text.align_to(exploration_1[i - 1], LEFT)

        exploration_1.to_edge(UL).shift(0.1 * UL)

        for i, tex_text in enumerate(exploration_1):
            if i == 0:
                self.play(Write(tex_text))
                continue

            self.play(TransformMatchingTex(exploration_1[i - 1].copy(), tex_text))

            if i == 1:
                self.wait(2)
                self.change_subtitle(Subtitle("若该方程有两解，则可找出满足 SSA 但不全等的特例三角形"))
                self.wait(2)
                self.change_subtitle(Subtitle(r"令 $\Delta \geq 0$"))
                self.wait()

            if i == 7:
                self.wait()
                self.change_subtitle(Subtitle(r"此处 $c$, $a$, $\sin \theta$ 均大于 $0$"))
                self.wait()

        self.wait()
        self.play(FadeOut(self.current_subtitle))

        exploration_2 = VGroup(
            Tex("c", r"\geq", " ", "a", r"\sin", r"\theta", color=WHITE),
            TexText(r"当 $c = a \sin \theta$ 时:", color=BLUE_B),
            TexText("方程仅有一根，", color=WHITE),
            TexText("即三角形只有一种情况", color=WHITE),
            TexText(r"当 $c > a \sin \theta$ 时:", color=BLUE_B),
            TexText(r"方程有两根，", color=WHITE),
            TexText(r"三角形有两种情况", color=WHITE),
            TexText(r"当 $c < a \sin \theta$ 时:", color=BLUE_B),
            TexText(r"方程无根，", color=WHITE),
            TexText(r"此时 $\triangle ABC$ 不存在", color=WHITE),
        ).arrange(DOWN * 1.5).scale(0.8)

        for i, tex_text in enumerate(exploration_2):
            if i > 0:
                tex_text.align_to(exploration_2[i - 1], LEFT)

        exploration_2.to_edge(UL).shift(0.1 * UL)

        for i, tex_text in enumerate(exploration_1):
            if i <= 7:
                self.play(FadeOut(tex_text, LEFT), run_time=0.2)

        self.play(ReplacementTransform(exploration_1[8], exploration_2[0]))

        angle_value = get_angle_of_3_points(
            dotx_a_acute.get_point(),
            dotx_b_acute.get_point(),
            dotx_c_acute.get_point()
        )

        dotx_a_temp = DotX(get_vertical_point(
            dotx_a_acute.get_point(), dotx_c_acute.get_point(), dotx_b_acute.get_point()),
            "A'", color=BLUE_B, mark_pos=UP)
        triangle_temp = TriangleX(
            dotx_a_temp, dotx_b_acute, dotx_c_acute,
        ).set_color(color=BLUE_B).set_color_for_marks(WHITE)
        midpoint_ba_temp = midpoint(dotx_b_acute.get_point(), dotx_a_temp.get_point())
        midpoint_ca_temp = midpoint(dotx_a_temp.get_point(), dotx_c_acute.get_point())
        c_tex_temp = Tex("c", color=WHITE).next_to(
            midpoint_ba_temp, get_unit_vector_on_direction(midpoint_ba_temp - dotx_c_acute.get_point()))
        x_tex_temp = Tex("x", color=WHITE).next_to(
            midpoint_ca_temp, get_unit_vector_on_direction(midpoint_ca_temp - dotx_b_acute.get_point()))

        line_ba = Line(dotx_a_acute.get_point(), dotx_b_acute.get_point(), color=BLUE_B)
        line_ba_temp = Line(dotx_a_temp.get_point(), dotx_b_acute.get_point(), color=BLUE_B)

        dotx_a_2 = DotX(np.array([4.24, 0.13, 0]), "A'", mark_pos=UP, point_config={"color": BLUE_B})
        arc_1 = Arc(radius=2.42, angle=angle_value, arc_center=dotx_b_acute.get_point(), color=YELLOW_B)
        line_ba_2 = Line(dotx_a_2.dot, dotx_b_acute.dot, color=BLUE_B)

        ca_1 = Line(dotx_c_acute.get_point(), dotx_a_acute.get_point())
        ca_2 = Line(dotx_c_acute.get_point(), dotx_a_2.get_point())
        vec = get_unit_vector_on_direction(dotx_a_temp.get_point() - dotx_b_acute.get_point())

        brace_ca_1 = Brace(ca_1, vec).shift(vec * 0.5)
        brace_tex_ca_1 = Tex("x_1").next_to(brace_ca_1, vec).shift(-vec * 1.5)
        brace_ca_2 = Brace(ca_2, vec).shift(vec * 0.5)
        brace_tex_ca_2 = Tex("x_2").next_to(brace_ca_2, vec).shift(-vec * 0.8)

        dot_g = Dot(np.array([2.74, 0.6, 0]), color=BLUE_B)
        line_bg = Line(dotx_b_acute.get_point(), dot_g.get_center(), color=YELLOW_B)
        arc_2 = Arc(
            radius=1.72,
            arc_center=dotx_b_acute.get_point(),
            start_angle=PI / 12,
            angle=angle_value - PI / 12,
            color=YELLOW_B
        )
        line_bg_copied = line_bg.copy()

        elbow_tri = Elbow(angle=0.84 + PI).move_to(dotx_a_temp.get_point())
        elbow_tri.shift(0.25 * DOWN)

        for i, tex_text in enumerate(exploration_2):
            if i == 0:
                self.wait()
                self.write_new_subtitle(Subtitle("围绕该临界条件进行粗略讨论"))
                self.wait(2)
                self.play(FadeOut(self.current_subtitle))
                continue
            self.play(Write(tex_text))

            if i == 2:
                self.play(ReplacementTransform(line_ba, line_ba_temp))
                self.play(ShowCreation(elbow_tri))
                self.wait()
                self.play(
                    ReplacementTransform(triangle_acute, triangle_temp),
                    ReplacementTransform(c_tex, c_tex_temp),
                    ReplacementTransform(x_tex, x_tex_temp),
                )
            if i == 3:
                triangle_to_fade = Polygon(
                    dotx_b_acute.get_point(),
                    dotx_a_temp.get_point(),
                    dotx_c_acute.get_point(),
                    color=GOLD
                ).set_fill(GOLD, opacity=0.5)

                # Reassign transformed mobjects
                dotx_a_acute = DotX(np.array([3, 1.25, 0]), "A", mark_pos=UP)
                dotx_b_acute = DotX(np.array([2.1, -1, 0]), "B", mark_pos=DOWN)
                dotx_c_acute = DotX(np.array([5.5, -1, 0]), "C", mark_pos=DOWN)
                triangle_acute = TriangleX(dotx_a_acute, dotx_b_acute, dotx_c_acute) \
                    .set_color(color=BLUE_B).set_color_for_marks(WHITE)
                c_tex = Tex("c", color=WHITE).next_to(
                    midpoint_ab, get_unit_vector_on_direction(midpoint_ab - dotx_c_acute.get_point()))
                x_tex = Tex("x", color=WHITE).next_to(
                    midpoint_ac, get_unit_vector_on_direction(midpoint_ac - dotx_b_acute.get_point()))

                self.play(ShowCreation(triangle_to_fade))
                self.play(Uncreate(triangle_to_fade))
                self.play(
                    ReplacementTransform(triangle_temp, triangle_acute),
                    ReplacementTransform(c_tex_temp, c_tex),
                    ReplacementTransform(x_tex_temp, x_tex)
                )
                self.wait()
            if i == 4:
                line_ba_yellow = Line(dotx_a_acute.get_point(), dotx_b_acute.get_point(), color=YELLOW_B)

                self.wait()
                self.play(ShowCreation(line_ba_yellow))
                line_ba_yellow_copied = line_ba_yellow.copy()
                self.play(
                    Rotating(
                        line_ba_yellow_copied, angle_value, IN,
                        about_point=dotx_b_acute.get_point(),
                        run_time=1
                    ),
                    Write(arc_1, rate_func=linear)
                )
                self.play(ShowCreation(dotx_a_2))
                self.wait(2)
                self.play(
                    Uncreate(arc_1),
                    Uncreate(line_ba_yellow),
                    Uncreate(line_ba_yellow_copied)
                )
                self.wait()
                self.play(ShowCreation(line_ba_2))
                self.play(Uncreate(x_tex))
                self.wait()
            if i == 5:
                self.play(ShowCreation(brace_ca_1), ShowCreation(brace_tex_ca_1))
                self.wait()
                self.play(
                    ReplacementTransform(brace_ca_1, brace_ca_2),
                    ReplacementTransform(brace_tex_ca_1, brace_tex_ca_2)
                )
                self.wait()
                self.play(
                    Uncreate(brace_tex_ca_2),
                    Uncreate(brace_ca_2)
                )
            if i == 6:
                self.wait()

                triangle_to_fade_1 = Polygon(
                    dotx_b_acute.get_point(),
                    dotx_a_temp.get_point(),
                    dotx_c_acute.get_point(),
                    color=GOLD
                ).set_fill(GOLD, opacity=0.5)

                triangle_to_fade_2 = Polygon(
                    dotx_b_acute.get_point(),
                    dotx_a_2.get_point(),
                    dotx_c_acute.get_point(),
                    color=GOLD
                ).set_fill(GOLD, opacity=0.5)

                self.play(ShowCreation(triangle_to_fade_1))
                self.play(Uncreate(triangle_to_fade_1))
                self.wait()
                self.play(ShowCreation(triangle_to_fade_2))
                self.play(Uncreate(triangle_to_fade_2))

            if i == 7:
                self.wait()
                self.play(
                    Uncreate(line_ba_2),
                    Uncreate(dotx_a_2),
                    Uncreate(line_ba_temp),
                    Uncreate(elbow_tri)
                )
                self.wait()
                self.play(
                    ShowCreation(dot_g),
                    ShowCreation(line_bg)
                )
                self.wait()
                self.play(
                    Rotating(
                        line_bg_copied, angle_value - PI / 12, IN,
                        about_point=dotx_b_acute.get_point(),
                        run_time=1
                    ),
                    Write(arc_2, rate_func=linear)
                )
                self.wait()
            if i == 9:
                self.wait()
                self.play(
                    Uncreate(line_bg),
                    Uncreate(line_bg_copied),
                    Uncreate(arc_2),
                    Uncreate(dot_g)
                )
                self.wait(2)

        self.wait()

        # Create a screen rectangle covering the screen for coherence
        cover = FullScreenRectangle(color="#333333")
        self.play(ShowCreation(cover), run_time=3)

        # Re-assign mobjects
        dotx_a_acute_1 = DotX(np.array([3, 1.25, 0]), "A", mark_pos=UP)
        dotx_b_acute_1 = DotX(np.array([2.1, -1, 0]), "B", mark_pos=DOWN)
        dotx_c_acute_1 = DotX(np.array([5.5, -1, 0]), "C", mark_pos=DOWN)

        midpoint_bc_1 = midpoint(dotx_b_acute_1.get_point(), dotx_c_acute_1.get_point())
        midpoint_ac_1 = midpoint(dotx_a_acute_1.get_point(), dotx_c_acute_1.get_point())
        midpoint_ab_1 = midpoint(dotx_a_acute_1.get_point(), dotx_b_acute_1.get_point())

        a_tex_1 = Tex("a", color=WHITE).next_to(midpoint_bc_1, DOWN)
        c_tex_1 = Tex("c", color=WHITE).next_to(
            midpoint_ab_1, get_unit_vector_on_direction(midpoint_ab_1 - dotx_c_acute_1.get_point()))
        angle_value_acb = get_angle_of_3_points(
            dotx_a_acute_1.get_point(),
            dotx_c_acute_1.get_point(),
            dotx_b_acute_1.get_point()
        )
        angle_theta_1 = Arc(
            start_angle=np.pi - angle_value_acb,
            angle=angle_value_acb,
            arc_center=dotx_c_acute_1.get_point(),
            radius=0.3,
            color=WHITE
        )

        theta_tex_1 = Tex(r"\theta", color=WHITE).next_to(angle_theta_1, 0.4 * RIGHT + 0.2 * UP)

        triangle_acute_1 = TriangleX(dotx_a_acute_1, dotx_b_acute_1, dotx_c_acute_1) \
            .set_color(color=BLUE_B).set_color_for_marks(WHITE)

        # Recreate the arc and dotx_a_2
        # Re-assign mobjects for re-using
        angle_value_abc = get_angle_of_3_points(
            dotx_a_acute.get_point(),
            dotx_b_acute.get_point(),
            dotx_c_acute.get_point()
        )
        line_ba_yellow = Line(dotx_a_acute_1.get_point(), dotx_b_acute_1.get_point(), color=YELLOW_B)
        arc_1 = Arc(radius=2.42, angle=angle_value_abc, arc_center=dotx_b_acute_1.get_point(), color=YELLOW_B)
        dotx_a_2 = DotX(np.array([4.24, 0.13, 0]), "A'", mark_pos=UP, point_config={"color": BLUE_B})
        line_ba_2 = Line(dotx_a_2.dot, dotx_b_acute_1.dot, color=BLUE_B)

        self.play(ShowCreation(triangle_acute_1))
        self.play(
            ShowCreation(a_tex_1),
            ShowCreation(c_tex_1)
        )
        self.play(ShowCreation(angle_theta_1))
        self.play(ShowCreation(theta_tex_1))
        self.wait()
        self.play(ShowCreation(line_ba_yellow))
        line_ba_yellow_copied = line_ba_yellow.copy()
        self.play(
            Rotating(
                line_ba_yellow_copied, angle_value_abc, IN,
                about_point=dotx_b_acute_1.get_point(),
                run_time=1
            ),
            Write(arc_1, rate_func=linear)
        )
        self.play(ShowCreation(dotx_a_2))
        self.play(
            Uncreate(arc_1),
            Uncreate(line_ba_yellow),
            Uncreate(line_ba_yellow_copied)
        )
        self.play(ShowCreation(line_ba_2))

        triangle_to_fade_2 = Polygon(
            dotx_b_acute_1.get_point(),
            dotx_a_2.get_point(),
            dotx_c_acute_1.get_point(),
            color=GOLD
        ).set_fill(GOLD, opacity=0.5)

        dotx_a_2_temp = DotX(np.array([-1.96, 0.13, 0]), "A'", mark_pos=UP, point_config={"color": BLUE_B})
        dotx_b_2 = DotX(np.array([-4.1, -1, 0]), "B", mark_pos=DOWN, point_config={"color": BLUE_B})
        dotx_c_2 = DotX(np.array([-0.7, -1, 0]), "C", mark_pos=DOWN, point_config={"color": BLUE_B})

        angle_value_acb_2 = get_angle_of_3_points(
            dotx_a_2_temp.get_point(),
            dotx_c_2.get_point(),
            dotx_b_2.get_point()
        )

        angle_theta_2 = Arc(
            start_angle=np.pi - angle_value_acb_2,
            angle=angle_value_acb_2,
            arc_center=dotx_c_2.get_point(),
            radius=0.3,
            color=WHITE
        )

        triangle_obtuse_2 = TriangleX(
            dotx_b_2,
            dotx_a_2_temp,
            dotx_c_2,
            triangle_config={"color": BLUE_B}
        )

        midpoint_ab_2 = midpoint(dotx_a_2_temp.get_point(), dotx_b_2.get_point())
        midpoint_bc_2 = midpoint(dotx_b_2.get_point(), dotx_c_2.get_point())

        a_tex_2 = Tex("a", color=WHITE).next_to(midpoint_bc_2, DOWN)
        c_tex_2 = Tex("c", color=WHITE).next_to(
            midpoint_ab_2, get_unit_vector_on_direction(midpoint_ab_2 - dotx_c_2.get_point()))
        theta_tex_2 = Tex(r"\theta", color=WHITE).next_to(angle_theta_2, 0.2 * UP + 0.5 * RIGHT)

        self.wait()
        self.play(ShowCreation(triangle_to_fade_2))
        self.play(
            ReplacementTransform(triangle_to_fade_2, triangle_obtuse_2.tri)
        )
        self.play(
            ShowCreation(dotx_a_2_temp),
            ShowCreation(dotx_b_2),
            ShowCreation(dotx_c_2),
            ShowCreation(angle_theta_2)
        )
        self.play(
            Write(a_tex_2),
            Write(c_tex_2),
            Write(theta_tex_2)
        )
        self.play(
            Uncreate(line_ba_2),
            Uncreate(dotx_a_2)
        )

        # Add Ticks
        tick_c1 = get_tick(dotx_b_2.get_point(), dotx_a_2_temp.get_point())
        tick_c2 = get_tick(dotx_b_acute_1.get_point(), dotx_a_acute_1.get_point())
        tick_a1 = get_double_tick(dotx_b_2.get_point(), dotx_c_2.get_point())
        tick_a2 = get_double_tick(dotx_b_acute_1.get_point(), dotx_c_acute_1.get_point())

        self.play(
            ShowCreation(tick_c1),
            ShowCreation(tick_c2)
        )
        self.play(
            ShowCreation(tick_a1),
            ShowCreation(tick_a2)
        )

        self.write_new_subtitle(Subtitle("可见，这一对三角形即为满足 SSA 但不全等的特例"))
        self.wait(2)
        self.change_subtitle(Subtitle("由此可得 SSA 不能判定两个三角形全等"))
        self.wait(3)

        self.play(
            FadeOut(self.current_subtitle, DOWN),
            FadeOut(cosine_law, UP)
        )

        self.play(
            Uncreate(tick_c1),
            Uncreate(tick_c2)
        )
        self.play(
            Uncreate(tick_a1),
            Uncreate(tick_a2)
        )
        self.play(
            Uncreate(a_tex_2),
            Uncreate(a_tex_1),
            Uncreate(c_tex_2),
            Uncreate(c_tex_1),
            Uncreate(angle_theta_2),
            Uncreate(angle_theta_1),
            Uncreate(theta_tex_2),
            Uncreate(theta_tex_1)
        )

        self.write_new_subtitle(Subtitle("虽然对于一般的情况而言，SSA 不能判定全等"))
        self.wait()
        self.change_subtitle(Subtitle("但从刚才的讨论可以看出"))
        self.change_subtitle(Subtitle("在某些特殊的条件下，SSA 可以判定两个三角形全等"))

        self.wait()

        self.play(
            FadeOut(triangle_obtuse_2, LEFT),
            FadeOut(triangle_acute_1, RIGHT)
        )

        self.change_subtitle(Subtitle("回到之前的讨论"))

        self.play(Uncreate(cover), run_time=3)

        """
        # Recreate the arc and dotx_a_2
        # Re-assign mobjects for re-using... again
        angle_value = get_angle_of_3_points(
            dotx_a_acute.get_point(),
            dotx_b_acute.get_point(),
            dotx_c_acute.get_point()
        )

        line_ba_yellow = Line(dotx_a_acute.get_point(), dotx_b_acute.get_point(), color=YELLOW_B)
        arc_1 = Arc(radius=2.42, angle=angle_value, arc_center=dotx_b_acute.get_point(), color=YELLOW_B)
        dotx_a_2 = DotX(np.array([4.24, 0.13, 0]), "A'", mark_pos=UP, point_config={"color": BLUE_B})
        line_ba_2 = Line(dotx_a_2.dot, dotx_b_acute.dot, color=BLUE_B)

        self.wait()
        self.play(ShowCreation(line_ba_yellow))
        line_ba_yellow_copied = line_ba_yellow.copy()
        self.play(
            Rotating(
                line_ba_yellow_copied, angle_value, IN,
                about_point=dotx_b_acute.get_point(),
                run_time=1
            ),
            Write(arc_1, rate_func=linear)
        )
        self.play(ShowCreation(dotx_a_2))
        self.play(
            Uncreate(arc_1),
            Uncreate(line_ba_yellow),
            Uncreate(line_ba_yellow_copied)
        )
        self.play(ShowCreation(line_ba_2))
        """

        self.change_subtitle(Subtitle("三角形有两种情况时"))
        self.play(ShowCreationThenDestructionAround(exploration_2[6]))

        self.play(
            FadeOut(exploration_2, LEFT),
            Uncreate(y_axis)
        )

        # Re-assign mobjects
        dotx_a_acute_moved = DotX(np.array([0, 2.5, 0]), "A", mark_pos=UP)
        dotx_b_acute_moved = DotX(np.array([-0.9, 0.25, 0]), "B", mark_pos=DOWN)
        dotx_c_acute_moved = DotX(np.array([2.5, 0.25, 0]), "C", mark_pos=DOWN)
        midpoint_ab_moved = midpoint(dotx_b_acute_moved.get_point(), dotx_a_acute_moved.get_point())
        midpoint_bc_moved = midpoint(dotx_b_acute_moved.get_point(), dotx_c_acute_moved.get_point())
        a_tex_moved = Tex("a", color=WHITE).next_to(midpoint_bc_moved, DOWN)
        c_tex_moved = Tex("c", color=WHITE).next_to(
            midpoint_ab_moved, get_unit_vector_on_direction(midpoint_ab_moved - dotx_c_acute_moved.get_point()))
        angle_value_moved = get_angle_of_3_points(
            dotx_a_acute_moved.get_point(),
            dotx_c_acute_moved.get_point(),
            dotx_b_acute_moved.get_point()
        )
        angle_theta_moved = Arc(
            start_angle=np.pi - angle_value_moved,
            angle=angle_value_moved,
            arc_center=dotx_c_acute_moved.get_point(),
            radius=0.3,
            color=WHITE
        )
        theta_tex_moved = Tex(r"\theta", color=WHITE).next_to(angle_theta_moved, 0.4 * RIGHT + 0.2 * UP)
        triangle_acute_moved = TriangleX(dotx_a_acute_moved, dotx_b_acute_moved, dotx_c_acute_moved) \
            .set_color(color=BLUE_B).set_color_for_marks(WHITE)

        self.play(
            ReplacementTransform(triangle_acute, triangle_acute_moved),
            ReplacementTransform(a_tex, a_tex_moved),
            ReplacementTransform(c_tex, c_tex_moved),
            ReplacementTransform(theta_tex, theta_tex_moved),
            ReplacementTransform(angle_theta, angle_theta_moved)
        )

        extended_pos = np.array([-5, 7, 0])
        line_extended = Line(extended_pos, dotx_a_acute_moved.get_point(), color=BLUE_B)
        line_bc = Line(dotx_b_acute_moved.get_point(), dotx_c_acute_moved.get_point(), color=BLUE_B)
        line_ac = Line(dotx_c_acute_moved.get_point(), dotx_a_acute_moved.get_point(), color=BLUE_B)

        lines_group = VGroup(line_ac, line_bc)

        self.add(lines_group)
        self.play(
            Uncreate(c_tex_moved),
            Uncreate(dotx_a_acute_moved),
            Uncreate(triangle_acute_moved.tri),
            ShowCreation(line_extended)
        )
        self.wait()

        dot_h = Dot(get_vertical_point(
            dotx_a_acute_moved.get_point(), dotx_c_acute_moved.get_point(), dotx_b_acute_moved.get_point()
        ) - np.array([0.03, 0.03, 0]), color=BLUE_B)

        line_bh = Line(dot_h.get_center(), dotx_b_acute_moved.dot, color=BLUE_B)

        self.play(ShowCreation(dot_h))
        self.play(ShowCreation(line_bh))

        circle_1 = Circle(
            radius=get_norm(dot_h.get_center() - dotx_b_acute_moved.get_point()),
            color=YELLOW_B
        ).move_to(dotx_b_acute_moved.get_point())

        self.play(ShowCreation(circle_1))
        self.wait()

        dot_intersection_1 = Dot(np.array([-0.333, 2.8, 0]), color=BLUE_B)
        dot_intersection_2 = Dot(np.array([1.576, 1.081, 0]), color=BLUE_B)
        line_tri_1 = Line(dot_intersection_1.get_center(), dotx_b_acute_moved.get_point(), color=BLUE_B)
        line_tri_2 = Line(dot_intersection_2.get_center(), dotx_b_acute_moved.get_point(), color=BLUE_B)

        circle_2 = Circle(
            radius=get_norm(dot_intersection_1.get_center() - dotx_b_acute_moved.get_point()),
            color=YELLOW_B
        ).move_to(dotx_b_acute_moved.get_point())

        self.play(
            ReplacementTransform(circle_1, circle_2),
            ReplacementTransform(dot_h.copy(), dot_intersection_1),
            ReplacementTransform(dot_h, dot_intersection_2),
            ReplacementTransform(line_bh.copy(), line_tri_1),
            ReplacementTransform(line_bh, line_tri_2),
            run_time=2
        )

        self.change_subtitle(Subtitle("必为一个锐角三角形，一个钝角三角形"))

        dot_intersection_3 = Dot(np.array([0, 2.5, 0]), color=BLUE_B)
        dot_intersection_4 = Dot(np.array([1.243, 1.381, 0]), color=BLUE_B)
        line_tri_3 = Line(dot_intersection_3.get_center(), dotx_b_acute_moved.get_point(), color=BLUE_B)
        line_tri_4 = Line(dot_intersection_4.get_center(), dotx_b_acute_moved.get_point(), color=BLUE_B)

        circle_3 = Circle(
            radius=get_norm(dot_intersection_3.get_center() - dotx_b_acute_moved.get_point()),
            color=YELLOW_B
        ).move_to(dotx_b_acute_moved.get_point())

        self.play(
            ReplacementTransform(circle_2, circle_3),
            ReplacementTransform(dot_intersection_1, dot_intersection_3),
            ReplacementTransform(dot_intersection_2, dot_intersection_4),
            ReplacementTransform(line_tri_1, line_tri_3),
            ReplacementTransform(line_tri_2, line_tri_4),
            run_time=2
        )

        self.wait()

        dot_intersection_5 = Dot(np.array([-0.778, 3.2, 0]), color=BLUE_B)
        dot_intersection_6 = Dot(np.array([2.02, 0.681, 0]), color=BLUE_B)
        line_tri_5 = Line(dot_intersection_5.get_center(), dotx_b_acute_moved.get_point(), color=BLUE_B)
        line_tri_6 = Line(dot_intersection_6.get_center(), dotx_b_acute_moved.get_point(), color=BLUE_B)

        circle_4 = Circle(
            radius=get_norm(dot_intersection_5.get_center() - dotx_b_acute_moved.get_point()),
            color=YELLOW_B
        ).move_to(dotx_b_acute_moved.get_point())

        self.play(
            ReplacementTransform(circle_3, circle_4),
            ReplacementTransform(dot_intersection_3, dot_intersection_5),
            ReplacementTransform(dot_intersection_4, dot_intersection_6),
            ReplacementTransform(line_tri_3, line_tri_5),
            ReplacementTransform(line_tri_4, line_tri_6),
            run_time=2
        )

        self.wait()

        dot_intersection_7 = Dot(np.array([0, 2.5, 0]), color=BLUE_B)
        dot_intersection_8 = Dot(np.array([1.243, 1.381, 0]), color=BLUE_B)
        line_tri_7 = Line(dot_intersection_7.get_center(), dotx_b_acute_moved.get_point(), color=BLUE_B)
        line_tri_8 = Line(dot_intersection_8.get_center(), dotx_b_acute_moved.get_point(), color=BLUE_B)

        circle_5 = Circle(
            radius=get_norm(dot_intersection_7.get_center() - dotx_b_acute_moved.get_point()),
            color=YELLOW_B
        ).move_to(dotx_b_acute_moved.get_point())

        self.play(
            ReplacementTransform(circle_4, circle_5),
            ReplacementTransform(dot_intersection_5, dot_intersection_7),
            ReplacementTransform(dot_intersection_6, dot_intersection_8),
            ReplacementTransform(line_tri_5, line_tri_7),
            ReplacementTransform(line_tri_6, line_tri_8),
            run_time=2
        )

        triangle_to_fade_1 = Polygon(
            dotx_b_acute_moved.get_point(),
            dotx_c_acute_moved.get_point(),
            dot_intersection_7.get_center(),
            color=GOLD
        ).set_fill(GOLD, opacity=0.5)

        triangle_to_fade_2 = Polygon(
            dotx_b_acute_moved.get_point(),
            dotx_c_acute_moved.get_point(),
            dot_intersection_8.get_center(),
            color=GOLD
        ).set_fill(GOLD, opacity=0.5)

        self.play(ShowCreation(triangle_to_fade_1))
        self.play(Uncreate(triangle_to_fade_1))
        self.wait()
        self.play(ShowCreation(triangle_to_fade_2))
        self.play(Uncreate(triangle_to_fade_2))

        self.wait()
        self.change_subtitle(Subtitle("因此若两个三角形同为锐角三角形，或同为钝角三角形"))
        self.wait()
        self.change_subtitle(Subtitle("且这两个三角形满足 SSA"))
        self.wait()
        self.change_subtitle(Subtitle("则这两个三角形全等"))
        self.wait(2)

        # Fade out everything
        self.play(Uncreate(circle_5))
        self.play(
            Uncreate(a_tex_moved),
            Uncreate(theta_tex_moved),
            Uncreate(angle_theta_moved)
        )
        self.play(
            Uncreate(line_extended),
            Uncreate(line_tri_7),
            Uncreate(line_tri_8),
            Uncreate(dot_intersection_8),
            Uncreate(dot_intersection_7)
        )
        self.play(
            Uncreate(dotx_b_acute_moved),
            Uncreate(dotx_c_acute_moved),
            Uncreate(lines_group),
            FadeOut(self.current_subtitle, DOWN),
        )

        # Create a screen rectangle covering the screen for coherence
        cover = FullScreenRectangle(color="#333333")
        self.play(ShowCreation(cover), run_time=3)

        """
        self.play(
            Uncreate(tick_c1),
            Uncreate(tick_c2)
        )
        self.play(
            Uncreate(tick_a1),
            Uncreate(tick_a2)
        )
        """

        """
        # self.change_subtitle(Subtitle("而这样的特例一定为一个锐角三角形和一个钝角三角形"))
        # self.wait(2)
        # self.change_subtitle(Subtitle("因此若两个三角形同为锐角三角形，或同为钝角三角形"))
        self.wait()

        triangle_obtuse_copied = triangle_obtuse_2.copy().shift(6 * RIGHT)
        a_tex_2_copied = a_tex_2.copy().shift(6 * RIGHT)
        c_tex_2_copied = c_tex_2.copy().shift(6 * RIGHT)
        theta_tex_2_copied = theta_tex_2.copy().shift(6 * RIGHT)
        angle_theta_2_copied = angle_theta_2.copy().shift(6 * RIGHT)
        self.play(
            ReplacementTransform(triangle_acute, triangle_obtuse_copied),
            ReplacementTransform(a_tex, a_tex_2_copied),
            ReplacementTransform(c_tex, c_tex_2_copied),
            ReplacementTransform(theta_tex, theta_tex_2_copied),
            ReplacementTransform(angle_theta, angle_theta_2_copied)
        )

        # self.change_subtitle(Subtitle("且这两个三角形满足 SSA"))
        # self.wait(2)
        # self.change_subtitle(Subtitle("则可推断这两个三角形全等"))
        # self.wait(2)
        """

        """
        # Fade out everything
        self.play(
            Uncreate(a_tex_2),
            Uncreate(a_tex),
            Uncreate(c_tex_2),
            Uncreate(c_tex),
            Uncreate(angle_theta_2),
            Uncreate(angle_theta),
            Uncreate(theta_tex_2),
            Uncreate(theta_tex)
        )
        self.play(
            FadeOut(triangle_obtuse_2, LEFT),
            FadeOut(triangle_acute, RIGHT)
        )
        self.play(
            FadeOut(self.current_subtitle, DOWN),
            FadeOut(cosine_law, UP)
        )

        # Create a screen rectangle covering the screen for coherence
        # cover = FullScreenRectangle(color="#333333")
        # self.play(ShowCreation(cover), run_time=3)
        """

