from manim import *


class PlotParametricFunction(Scene):
    def func(self, t):
        return np.sin(2 * t), np.sin(3 * t), 0

    def construct(self):
        func = ParametricFunction(self.func, t_range=(0, TAU), fill_opacity=0).set_color(RED)
        self.add(func.scale(3))
        self.add_updater(func)
