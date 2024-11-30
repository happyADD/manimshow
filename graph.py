from manim import *

class InfiniteWell(Scene):
    def construct(self):
        # 设置坐标轴
        axes = NumberPlane()
        self.add(axes)

        # 绘制势能函数
        well_width = 3  # 势井宽度
        well = VGroup(*[Line(LEFT * well_width + y * UP, RIGHT * well_width + y * UP) for y in range(-3, 4, 1)])
        well.set_stroke(BLACK, 2)
        self.add(well)

        # 绘制波函数
        wave_func = ParametricFunction(lambda x: np.sin(PI * x / well_width), x_min=-well_width, x_max=well_width, color=BLUE)
        self.play(ShowCreation(wave_func))
        self.wait()

        # 可以添加更多的波函数，例如第二激发态
        wave_func_2 = ParametricFunction(lambda x: np.sin(2 * PI * x / well_width), x_min=-well_width, x_max=well_width, color=RED)
        self.play(Transform(wave_func, wave_func_2))
        self.wait()