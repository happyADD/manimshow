import numpy as np
from manim import *

class Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_time = 0  # 初始化last_time为实例属性

    def Re_psi(self,x,dt=0,L=0.05,n=1,E=1,h_bar=0.1):
        if dt is not 0:
            self.last_time = self.last_time + dt
        return np.sin(n*np.pi*x/L)*np.cos(E*self.last_time/h_bar)


    def Im_psi(self,x,dt=0,L=0.05,n=1,E=1,h_bar=0.1):
        if dt is not 0:
            self.last_time = self.last_time + dt
        return np.sin(n*np.pi*x/L)*np.sin(E*self.last_time/h_bar)
    

    def construct(self):
        
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        latex_text = Text("Made with LaTex and Manim").scale(1).set_color(logo_black).next_to(logo, DOWN)
        self.play(FadeIn(logo,latex_text))
        self.wait(2)
        self.play(FadeOut(logo,latex_text))
        self.clear()
        self.camera.background_color = BLACK

        axes = Axes(
            x_range=[-0.1, 1.1, 0.01],
            y_range=[-1, 2],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(-1, 1.1, 1)},
            y_axis_config={"numbers_to_include": np.arange(-1, 1.1, 1)},
        )

        """ 序幕，介绍 """
        preface_text = Text("我们将讨论一维无限深势井中的单电子的波函数\n并解释量子纠缠的基本原理。").to_edge(UP).set_color(BLUE)
        self.play(Write(preface_text))
        self.wait(2)
        self.play(FadeOut(preface_text))

        text = Text("这是一维无限深势井的函数：").to_edge(UP).set_color(BLUE)
        math_tex = MathTex(r"V(x) = \begin{cases} 0, & 0 \leq x \leq a \\ \infty, & \text{otherwise} \end{cases}")
        equation = math_tex.scale(1.5).next_to(text,DOWN).set_color(YELLOW)

        self.play(Create(text), Create(equation))
        self.wait(1)

        def V(x):
            if 0 <= x <= 1:
                return 0
            else:
                return 1

        text_2 = Text("大概长这个样子：").to_edge(UP).scale(1).set_color(BLUE)
        graph_V = axes.plot(
            lambda x: V(x)

        )
        self.add(axes)
        self.play(Transform(equation,equation.copy().scale(0.5).next_to(text_2,DOWN)))
        self.play(Transform(text,text_2), Create(graph_V))
        self.wait(3)

        self.clear()

        """ 第一幕，从薛定谔方程到一维电子的波函数"""

        # 创建文本和方程
        text = Text("时间依赖的薛定谔方程为：").to_edge(UP).set_color(BLUE)
        equation = Tex(r"$i\hbar \frac{\partial \Psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi(x,t)}{\partial x^2} + V(x)\Psi(x,t)$").scale(1.5).next_to(text,DOWN).set_color(YELLOW)

        self.play(Create(text), Create(equation))
        self.wait(2)

        text_V_Schrodinger = Text("在一维无限深势井中，可以化简为：").to_edge(UP).set_color(BLUE)
        equation_V_Schrodinger = Tex(r"$i\hbar \frac{\partial \Psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi(x,t)}{\partial x^2}$").scale(1.5).next_to(text_V_Schrodinger,DOWN).set_color(YELLOW)

        self.play(Uncreate(text))
        self.play(Create(text_V_Schrodinger), Transform(equation, equation_V_Schrodinger))
        self.wait(2)

        text_3 = Text("我们可以把波函数看做时间和空间函数的乘积：").to_edge(LEFT).set_color(BLUE).next_to(equation_V_Schrodinger,DOWN)
        equation_3 = Tex(r"$\Psi(x,t) = \psi(x) T(t)$").scale(1.5).next_to(text_3,DOWN).set_color(YELLOW)

        self.play(Create(text_3), Create(equation_3))
        self.wait(2)

        text_4 = Text("两边等一个常数，即能量").next_to(equation_3,UP).set_color(BLUE)
        equation_4 = Tex(r"$i\hbar \frac{1}{T(t)} \frac{dT(t)}{dt} = -\frac{\hbar^2}{2m} \frac{1}{\psi(x)} \frac{d^2 \psi(x)}{dx^2} $").scale(1.5).next_to(text_3,DOWN).set_color(YELLOW)
        equation_4_pro = Tex(r"$i\hbar \frac{1}{T(t)} \frac{dT(t)}{dt} = E = -\frac{\hbar^2}{2m} \frac{1}{\psi(x)} \frac{d^2 \psi(x)}{dx^2} $").scale(1.5).next_to(text_4,DOWN).set_color(YELLOW)

        self.play(Transform(equation_3,equation),FadeOut(text_V_Schrodinger))
        self.remove(equation)
        self.play(Transform(equation_3,equation_4))
        self.wait(1)
        self.play(Transform(text_3,text_4))
        self.play(Transform(equation_3,equation_4_pro))
        self.wait(1)
        text_long_wait = Text("经过一长串的推导").set_color(BLUE)
        self.play(FadeOut(text_3),FadeOut(equation_3),FadeIn(text_long_wait))
        self.play(Transform(text_long_wait,text_long_wait.copy().scale(1.5)),ApplyMethod(text_long_wait.shift,UP))
        self.play(Create(Dot([0,0,0]).set_color(LIGHT_BROWN)))
        self.play(ApplyMethod(Dot([0,0,0]).set_color(LIGHT_BROWN).shift,LEFT))
        self.play(ApplyMethod(Dot([0,0,0]).set_color(LIGHT_BROWN).shift,RIGHT))

        self.play(FadeOut(text_long_wait))
        self.clear()

        text_final = Text("我们最终得到：").to_edge(UP).set_color(BLUE)
        equation_final_1 = Tex(r"$T(t) = e^{\frac{-iEt}{\hbar}}$").next_to(text_final,DOWN).set_color(YELLOW)
        equation_final_2 = Tex(r"$\psi(x) = \sqrt{\frac{2}{L}}sin(\frac{n\pi x}{L})$").next_to(equation_final_1,DOWN).set_color(YELLOW)
        self.play(Create(text_final), Create(equation_final_1),Create(equation_final_2))
        self.wait(2)

        equation_final_pro = Tex(r"$\Psi_n(x,t) = \psi(x)T(t) = \sqrt{\frac{2}{L}}sin(\frac{n\pi x}{L})e^{\frac{-iEt}{\hbar}} $").set_color(YELLOW).scale(1).next_to(equation_final_2,DOWN)

        self.play(Create(equation_final_pro))
        self.play(Transform(equation_final_1,equation_final_pro))
        self.play(Transform(equation_final_2,equation_final_pro))
        self.remove(equation_final_1,equation_final_2)
        self.play(ApplyMethod(equation_final_pro.scale,1.5))

        self.play(ApplyMethod(equation_final_pro.shift,UP*2),FadeOut(text_final))
        self.wait(2)
        self.clear()
        """第二幕，展示电子的波函数的图像"""
        
        def update_Re_psi(mob, dt):
            mob.become(axes.plot(lambda x: self.Re_psi(x, dt),x_range=[0,1,0.001]).set_color(RED))

        def update_Im_psi(mob, dt):
            mob.become(axes.plot(lambda x: self.Im_psi(x, dt),x_range=[0,1,0.001]).set_color(YELLOW))



        Re_graph = axes.plot(lambda x: self.Re_psi(x, 0),x_range=[0,1,0.001], color=RED)
        Re_graph.add_updater(lambda mob, dt: update_Re_psi(mob, dt))
        
        Im_graph = axes.plot(lambda x: self.Im_psi(x, 0),x_range=[0,1,0.001], color=YELLOW)
        Im_graph.add_updater(lambda mob, dt: update_Im_psi(mob, dt))
        Re_graph.add_updater(lambda mob, dt: update_Re_psi(mob, dt*0.1))
        Im_graph.add_updater(lambda mob, dt: update_Im_psi(mob, dt*0.1))
        self.play(FadeIn(axes))
        self.play(FadeIn(Re_graph.set_color(RED)), FadeIn(Im_graph.set_color(YELLOW)))
        self.add(Text("-Re").to_corner(UR).set_color(RED))
        self.add(Text("-Img").to_corner(UR).shift(DOWN).set_color(YELLOW))
        self.wait(2)
       

        

        self.wait(15) 

        # self.remove_updater(update_Re_psi, update_Im_psi)

        self.clear()

        
        """谢幕"""

        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        latex_text = Text("Made with LaTex and Manim").scale(1).set_color(logo_black).next_to(logo, DOWN)
        self.play(FadeIn(logo,latex_text))
        self.play(ApplyMethod(logo.scale,0.5),ApplyMethod(latex_text.scale,0.5))
        self.play(ApplyMethod(logo.shift,UP*2),ApplyMethod(latex_text.shift,UP*3))
        self.play(Create(Text("项目已经在github上开源，欢迎star！").next_to(latex_text,DOWN).scale(0.5).set_color(BLACK)))
        self.play(Create(Text("https://github.com/happyADD/manimshow.git").next_to(latex_text,DOWN*3).scale(0.5).set_color(BLACK)))
        self.wait(2)
        self.play(FadeOut(logo,latex_text))
        self.clear()
        self.camera.background_color = BLACK
