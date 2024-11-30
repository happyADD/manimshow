from manim import *


class SineWave(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_time = 0  # 初始化last_time为实例属性


    def atom_wave(self, x, dt, A=1.0, k=1.0, omega=1.0):
        if dt is not 0:
            self.last_time = self.last_time + dt
        return A * (np.cos(k * x - omega * self.last_time) + 1j * np.sin(k * x - omega * self.last_time))

    def wave_function(self, x, dt=0):
        # 如果提供了t_last，则更新last_time
        if dt is not 0:
            self.last_time = self.last_time + dt
        # 定义波形函数，使用self.last_time
        return np.sin(10 * (self.last_time - x / 2) + np.pi / 2)

    def construct(self):
        def update_wave(mob, dt):
            mob.become(axes.plot(lambda x: self.atom_wave(x, dt)))

        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
        )

        # 绘制初始波形
        graph = axes.plot(lambda x: self.atom_wave(x, 0), color=RED)

        graph.add_updater(lambda mob, dt: update_wave(mob, dt))

        self.add(axes, graph)

        self.wait(3)

        graph.remove(graph)
        graph.add_updater(lambda mob, dt: update_wave(mob, dt))
        self.wait(3)
