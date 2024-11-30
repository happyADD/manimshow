import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 参数设置
L = 50  # 势阱的长度
N = 1000  # 点的数量
dx = L / N  # 空间步长
dt = 0.01  # 时间步长
c = 1  # 波速

# 初始化波函数
x = np.linspace(0, L, N)
psi = np.sin(np.pi * x / L)  # 初始波形

# 动画函数
def animate(t):
    global psi
    # 波的传播
    psi = np.roll(psi, -int(c * dt / dx))
    # 反射
    psi[:int(c * dt / dx)] = psi[:int(c * dt / dx)] * -1
    psi[-int(c * dt / dx):] = psi[-int(c * dt / dx):] * -1
    plt.cla()
    plt.plot(x, psi)
    plt.ylim(-1.5, 1.5)

# 创建动画
ani = animation.FuncAnimation(plt.gcf(), animate, frames=200, interval=20, blit=True)

# 显示动画
plt.show()