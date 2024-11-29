from manim import *
import numpy as np

def wave_function(x, t, A=1.0, k=1.0, omega=1.0):
    return A * (np.cos(k * x - omega * t) + 1j * np.sin(k * x - omega * t))

class WaveFunctionScene(Scene):
    def construct(self):
        t_tracker = ValueTracker(0)

        axes = Axes(x_range=[-5, 5], y_range=[-1.5, 1.5])  # 创建带有指定范围的轴对象
        self.add(axes)

        def get_wave_graph_real(t):
            def wave_real(x):
                return wave_function(x, t).real
            return axes.plot(wave_real, color=BLUE)  # 使用 axes.plot 而不是 FunctionGraph

        def get_wave_graph_imag(t):
            def wave_imag(x):
                return wave_function(x, t).imag
            return axes.plot(wave_imag, color=RED)

        def get_probability_graph(t):
            def probability(x):
                psi = wave_function(x, t)
                return np.abs(psi)**2
            return axes.plot(probability, color=GREEN)

        real_graph = get_wave_graph_real(t_tracker.get_value())
        imag_graph = get_wave_graph_imag(t_tracker.get_value())
        prob_graph = get_probability_graph(t_tracker.get_value())

        real_label = Tex("Real").next_to(real_graph, UP)
        imag_label = Tex("Img").next_to(imag_graph, UP)
        prob_label = Tex("P").next_to(prob_graph, UP)

        self.add(real_graph, imag_graph, prob_graph, real_label, imag_label, prob_label)

        t_tracker.add_updater(lambda t, dt: t.increment_value(0.05))

        real_graph.add_updater(lambda g: g.become(get_wave_graph_real(t_tracker.get_value())))
        imag_graph.add_updater(lambda g: g.become(get_wave_graph_imag(t_tracker.get_value())))
        prob_graph.add_updater(lambda g: g.become(get_probability_graph(t_tracker.get_value())))

        self.wait(10)