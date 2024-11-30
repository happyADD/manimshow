import numpy as np
from manim import *

class Scene(Scene):

    def construct(self):

        """ 序幕，介绍 """
        preface_text = Text("我们将讨论一维无限深势井中的单电子的波函数\n并解释量子纠缠的基本原理。").to_edge(UP).set_color(BLUE)
        self.play(Write(preface_text))
        self.wait(2)
        self.play(FadeOut(preface_text))

        text = Text("这是一维无限深势井的函数：").to_edge(UP).set_color(BLUE)
        equation = Tex(r"|\Psi(x,t)|^2 = e^{-|\frac{x}{2\pi}\left(1-\cos(2\pi f_0 t)\right)|^2}").scale(1.5).next_to(text,DOWN).set_color(YELLOW)

        self.play(Create(text), Create(equation))
        self.wait(1)

        """ 第一幕，从薛定谔方程到氢原子定式解"""

        # 创建文本和方程
        text = Text("Schrodinger Equation:").to_edge(UP).set_color(BLUE)
        equation = Tex(r"$i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r}, t) = \hat{H}\Psi(\mathbf{r}, t)$").scale(1.5).next_to(text,DOWN).set_color(YELLOW)

        text_hydrogen = Text("as to Hydrogen atom:").to_edge(UP).set_color(BLUE)
        hydrogen_equation = Tex(r"$\psi_{100}(r, \theta, \phi) = \frac{1}{\sqrt{\pi a_0^3}} e^{-r/a_0} \cdot Y_{00}(\theta, \phi)$").scale(1.5).next_to(text_hydrogen,DOWN).set_color(YELLOW)
        
        text_that_is = Text("即:").set_color(BLUE).to_edge(LEFT)
        H2_equation = Tex(r"$\Psi_{H_2}(r) = \frac{1}{\sqrt{\pi a_0^3}} e^{-r/a_0} $").set_color(YELLOW).scale(2).center()

        self.play(Create(text), Create(equation))
        self.wait(1)

        
        self.play(Transform(text, text_hydrogen), Transform(equation, hydrogen_equation))
        self.wait(1)

        self.play(Transform(text, text_that_is), Transform(equation, H2_equation))
        self.wait(1)

        self.play(FadeOut(text))

        """第二幕，展示氢原子的波函数"""

        text = Text("我们把r看为一维的运动形式").to_edge(UP).set_color(BLUE)
        equation2 = Tex(r"$\Psi_{H_2}(x) = \frac{1}{\sqrt{\pi a_0^3}} e^{-x/a_0} $").set_color(YELLOW).scale(2).next_to(text,DOWN)

        text_eula = Text("由欧拉公式可化为：").to_corner(UL).set_color(BLUE)
        equation3 = Tex(r"$\Psi_{H_2}(x) = \frac{1}{\sqrt{\pi a_0^3}}(\cos(-\frac{x}{a_0})+i\sin(-\frac{x}{a_0})) $").set_color(YELLOW).scale(1.5).to_edge(LEFT)

        self.play(Create(text))
        self.wait(1)
        self.play(Transform(equation,equation2))
        self.wait(1)
        self.play(Transform(text,text_eula), Transform(equation,equation3))
        self.wait(5)
        



        """第三幕，展示氢原子的波函数的图像"""




        self.wait(1)