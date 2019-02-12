__author__ = 'Kyle Vitautas Lopin'

import matplotlib.pyplot as plt
import run_simulations as rs
import tkinter as tk

def MakeSimulationWindow(self):
    """
    make a blank window that will be updated with simulation runs
    initialize the window to run in current clamp mode and make 2 axis' one to view voltage or current protocol
    given to the axon, and one to view the voltage of the simulation
    :return: the figure bed and the axis's that will be updated
    """
    simulation_figure_bed = plt.figure(figsize=(7, 3.7))
    simulation_plot_axis_voltage = simulation_figure_bed.add_subplot(111)
    plt.ylabel("Membrane potential (mV)", fontsize=12)
    plt.xlabel("time (msec)", fontsize=12)
    plt.xlim(self.time_range)
    plt.ylim([-100, 120])
    plt.title("Simulation Window")
    plt.subplots_adjust(bottom=0.14, left=0.16)
    simulation_plot_axis_current = simulation_plot_axis_voltage.twinx()
    simulation_plot_axis_current.set_ylabel("Input current (uA/cm2)")
    simulation_plot_axis_current.set_ylim([-30, 100])
    return simulation_figure_bed, simulation_plot_axis_voltage, simulation_plot_axis_current

def MakeGatesWithTimeWindow(time_range):
    gating_simulation_bed = plt.figure(figsize=(7,3.3))
    gating_simulation_axis = gating_simulation_bed.add_subplot(111)
    plt.ylabel("conductance (mS/cm^2)", fontsize=12)
    plt.xlabel("time (msec)", fontsize=12)
    plt.xlim(time_range)
    plt.ylim([0, 50])
    plt.subplots_adjust(bottom=0.14, left=0.16)

    return gating_simulation_bed, gating_simulation_axis

def MakeGatesWindowOptions(self, _frame):
    tk.Label(_frame, text="View Options").pack(side="top")
    var = tk.StringVar()
    gK_Button = tk.Checkbutton(_frame, text="K conductance", font=("Times",14), variable=var,
                               onvalue="On__gK", offvalue="Off_gK",
                               command=lambda: rs.Draw_gK(self, var.get()))
    gK_Button.pack(side="top")
    gK_Button.select()

def MakeParameterFrame(self, master):
    param_master = tk.Frame(master=master, bd=2)

    left_frame = tk.Frame(param_master, bd=2)
    right_frame = tk.Frame(param_master, bd=2)

    cap_label   = tk.Label(param_master, text="Cm=1 uF/Cm^2")

    gNa_label   = tk.Label(right_frame, text="gNa    = 120 mS/cm^2")
    gK_label    = tk.Label(right_frame, text="gK      = 36   mS/cm^2")
    gleak_label = tk.Label(right_frame, text="gLeak = 0.3  mS/cm^2")

    E_Na_label = tk.Label(left_frame, text="E Na   = 115 mV")
    E_K_label  = tk.Label(left_frame, text="E K     = -12 mV")
    E_leak_label = tk.Label(left_frame, text="E leak = 10.613 mV")

    cap_label.pack(side="top")

    gNa_label.pack(side="top", anchor="w")
    gK_label.pack(side="top", anchor="w")
    gleak_label.pack(side="top", anchor="w")

    E_Na_label.pack(side="top", anchor="w")
    E_K_label.pack(side="top", anchor="w")
    E_leak_label.pack(side="top", anchor="w")

    left_frame.pack(side="left", ipadx=10)
    right_frame.pack(side="right", ipadx=10)
    return param_master

def MakeSimulationOptionWindow(self, _frame):
    applied_stimulus_bar = tk.Scale(_frame, from_=-20, to=50, resolution=0.1, orient='horizontal', sliderlength=20,
                                    length=300)
    applied_stimulus_bar.set(10)


    tk.Button(_frame, text="View n gate rates", command=rs.Make_n_GateRateWindow(self))

    run_button = tk.Button(_frame, text="Run Simulation",
                           command=lambda:rs.UpdateSimulationWindow(self, applied_stimulus_bar.get()))
    run_button.pack(side="bottom")
    applied_stimulus_bar.pack(side="bottom")