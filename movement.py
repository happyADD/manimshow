from manim import *


class ParametricFunctionScene(Scene):
    def construct(self):
        # 创建坐标轴
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
        )
        self.add(axes)

        # 定义参数函数
        def x_func(self,t):
            return np.sin(t)  # x = sin(t)

        def y_func(self,t):
            return np.cos(t)  # y = cos(t)

        # 创建参数函数图像
        param_graph = ParametricFunction(
            [x_func(0), y_func(0)], t_range=(0, 2 * np.pi, 0.01)
        ).set_color(RED)

        # 显示参数函数图像
        self.play(Create(param_graph), run_time=4)

        # 你可以通过添加一个ValueTracker来动态更新图像
        t_tracker = ValueTracker(0)

        def update_graph(graph, dt):
            t_tracker.increment_value(dt)
            graph.become(ParametricFunction(
                [x_func, y_func], t_range=(0, t_tracker.get_value(), 0.01)
            ))

        param_graph.add_updater(update_graph)
        self.play(t_tracker.animate.set_value(2 * np.pi), run_time=10)
        self.wait(1)
