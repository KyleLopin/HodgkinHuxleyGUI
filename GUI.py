from __future__ import division

__author__ = 'Kyle Vitautas Lopin'

from numpy import arange, vectorize, exp, zeros
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib import rcParams

import tkinter as tk
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

font_gate_legend = FontProperties()
font_gate_legend.set_size('medium')

import hh_graphs
import parameter_frame as param_frame

# rcParams.update({'figure.autolayout': True})

FIGUREBACKGROUND = "#F0F0F0"
time_range = [0, 45]

V_rest  = 0      # mV
Cm      = 1      # uF/cm2
gbar_Na = 120    # mS/cm2
gbar_K  = 36     # mS/cm2
gbar_l  = 0.3    # mS/cm2
E_Na    = 115    # mV
E_K     = -12    # mV
E_l     = 10.613 # mV

alpha_n = vectorize(lambda v: 0.01*(-v + 10)/(exp((-v + 10)/10) - 1) if v != 10 else 0.1)
beta_n = lambda v: 0.125*exp(-v/80)
n_inf = lambda v: alpha_n(v)/(alpha_n(v) + beta_n(v))

# Na channel (activating)
alpha_m = vectorize(lambda v: 0.1*(-v + 25)/(exp((-v + 25)/10) - 1) if v != 25 else 1)
beta_m = lambda v: 4*exp(-v/18)
m_inf = lambda v: alpha_m(v)/(alpha_m(v) + beta_m(v))

# Na channel (inactivating)
alpha_h = lambda v: 0.07*exp(-v/20)
beta_h  = lambda v: 1/(exp((-v + 30)/10) + 1)
h_inf   = lambda v: alpha_h(v)/(alpha_h(v) + beta_h(v))

def MakeSimulationWindow():
    simulation_figure_bed = plt.figure(figsize=(7, 3.7))
    # simulation_figure_bed.set_facecolor(FIGUREBACKGROUND)
    simulation_plot_axis_voltage = simulation_figure_bed.add_subplot(111)
    plt.ylabel("Membrane potential (mV)", fontsize=12)
    plt.xlabel("time (msec)", fontsize=12)
    plt.xlim(time_range)
    plt.ylim([-100, 120])
    plt.title("Simulation Window")
    plt.subplots_adjust(bottom=0.14, left=0.16)
    simulation_plot_axis_current = simulation_plot_axis_voltage.twinx()
    simulation_plot_axis_current.set_ylabel("Input current (uA/cm2)")
    simulation_plot_axis_current.set_ylim([-30, 100])
    return simulation_figure_bed, simulation_plot_axis_voltage, simulation_plot_axis_current

def MakeGatesWithTimeWindow():
    gating_simulation_bed = plt.figure(figsize=(7,3.3))
    gating_simulation_axis = gating_simulation_bed.add_subplot(111)
    plt.ylabel("conductance (mS/cm^2)", fontsize=12)
    plt.xlabel("time (msec)", fontsize=12)
    plt.xlim(time_range)
    plt.ylim([0, 50])

    return gating_simulation_bed, gating_simulation_axis


def MakeGatingGraph():
    gates_bed = plt.figure(figsize=(4.5, 2.8))
    gates_plot_area = gates_bed.add_subplot(111)
    plt.ylabel("fraction of channels", fontsize=12)
    plt.xlabel("Membrane potential (mV)", fontsize=12)
    plt.xlim([-50, 150])
    plt.ylim([0, 1])
    plt.title("Gating steady state values", fontsize=12, y=1)
    plt.subplots_adjust(left=0.16, bottom=0.1)
    voltage = arange(-50, 151)  # mV
    gates_plot_area.plot(voltage, m_inf(voltage), voltage, h_inf(voltage),
                         voltage, n_inf(voltage))
    gates_plot_area.legend(("m gate", "h gate", "n gate"),
                                        loc="lower right", prop=font_gate_legend,
                                        frameon=False, borderpad=0, handletextpad=0,
                                        labelspacing=0)
    return gates_bed

def MakeGatingParameters():
    gating_param_frame = tk.Frame()

def RunSimulation(current):
    print("Run simulation", current)
    dt = 0.025
    time=arange(time_range[0], time_range[1]+dt, dt)
    Vm = zeros(len(time))
    g_Na_array = zeros(len(time))
    g_K_array  = zeros(len(time))
    g_l_array  = zeros(len(time))
    m_array = zeros(len(time))
    h_array = zeros(len(time))
    n_array = zeros(len(time))
    Vm[0] = V_rest
    m = m_inf(V_rest)
    h = h_inf(V_rest)
    n = n_inf(V_rest)

    ## Stimulus
    I = zeros(len(time))
    for i, t in enumerate(time):
        if 5 <= t <= 30: I[i] = current  # uA/cm2

    for i in range(1,len(time)):
        g_Na = gbar_Na*(m**3)*h
        g_K  = gbar_K*(n**4)
        g_l  = gbar_l

        g_Na_array[i] = g_Na
        g_K_array[i] = g_K
        g_l_array[i] = g_l

        m += dt*(alpha_m(Vm[i-1])*(1 - m) - beta_m(Vm[i-1])*m)
        h += dt*(alpha_h(Vm[i-1])*(1 - h) - beta_h(Vm[i-1])*h)
        n += dt*(alpha_n(Vm[i-1])*(1 - n) - beta_n(Vm[i-1])*n)

        m_array[i] = m
        h_array[i] = h
        n_array[i] = n

        Vm[i] = Vm[i-1] + (I[i-1] - g_Na*(Vm[i-1] - E_Na) - g_K*(Vm[i-1] - E_K)
                           - g_l*(Vm[i-1] - E_l)) / Cm * dt
    return time, Vm, I, g_Na_array, g_K_array, g_l_array, m_array, h_array, n_array

def UpdateSimulationWindow(current):
    time, Vm, I, gNa, gK, gleak, m, h, n = RunSimulation(current)

    simulation_graphs.update_graph(time, Vm, I, gNa, gK, gleak, m, h, n)

    # root.simulation_voltage_axis.plot(time, Vm)
    # root.simulation_current_axis.plot(time, I, 'g')
    # root.simulation_canvas.draw()

    # root.gates_time_graph_axis.plot(time, gNa, time, gK)
    # root.gates_time_graph_axis.set_ylim([0, max(gNa)*1.1])
    # root.gate_simulation_canvas.draw()

def init_menu():
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Close Program", command=root.quit)

    # config_menu = tk.Menu(menubar, tearoff=0)
    # menubar.add_cascade(label="Configure Simulation", menu=config_menu)
    # config_menu.add_command(label="Set")

    root.config(menu=menubar)


root = tk.Tk()
root.title("Hodgkin and Huxley Simulator")
root.geometry("1050x800")

simulation_figure_bed, root.simulation_voltage_axis, root.simulation_current_axis = MakeSimulationWindow()

# parameter_frame = MakeParameterFrame()
parameter_frame = param_frame.ParameterFrame(root)

gating_bed = MakeGatingGraph()

root.gates_time_graph_bed, root.gates_time_graph_axis = MakeGatesWithTimeWindow()

# UpdateSimulationWindow(simulation_plot)
init_menu()


simulation_graphs = hh_graphs.HHGateFrame(root)
simulation_graphs.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

parameter_frame.pack(side="top", fill="x")
applied_stimulus_bar = tk.Scale(root, from_=-10, to=40, resolution=0.1, orient='horizontal', sliderlength=20,
                                length=300)
applied_stimulus_bar.set(10)
run_button = tk.Button(root, text="Run Simulation", command=lambda: UpdateSimulationWindow(applied_stimulus_bar.get()))

run_button.pack(side=tk.BOTTOM, pady=10)
applied_stimulus_bar.pack(side=tk.BOTTOM)

# plt.subplots_adjust(bottom=0.15)
# plt.subplots_adjust(left=0.15)

tk.mainloop()