# Copyright (c) 2018 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""

"""

__author__ = "Kyle Vitatus Lopin"

from numpy import arange, vectorize, exp, zeros
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib import rcParams

import tkinter as tk
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavToolbar

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

font_gate_legend = FontProperties()
font_gate_legend.set_size('medium')

AXIS_LABEL_SIZE = 11


class HHGateFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # simulation_figure = plt.figure(figsize=(7, 7))
        # membrane_axis = simulation_figure.add_subplot(311)
        figure, (self.membrane_axis, self.conductance_axis, self.gate_axis) = \
        plt.subplots(3, 1, gridspec_kw={'height_ratios': [3, 2, 2]}, figsize=(7, 11))

        self.membrane_axis.set_ylabel("Membrane potential (mV)", fontsize=AXIS_LABEL_SIZE)
        self.membrane_axis.set_ylim([-30, 120])
        self.current_axis = self.membrane_axis.twinx()
        self.current_axis.set_ylabel("Input current (uA/cm2)")
        self.current_axis.set_ylim([-20, 100])

        # conductance_axis = simulation_figure.add_subplot(312)
        self.conductance_axis.set_ylabel("Conductance (mS/cm\u00b2)", fontsize=AXIS_LABEL_SIZE)

        # gate_axis = simulation_figure.add_subplot(313)
        self.gate_axis.set_ylabel("fraction of channels", fontsize=AXIS_LABEL_SIZE)
        self.gate_axis.legend(("m gate", "h gate", "n gate"),
                              loc="lower right", prop=font_gate_legend,
                              frameon=False, borderpad=0, handletextpad=0,
                              labelspacing=0)

        self.canvas = FigureCanvasTkAgg(figure, master=self)
        print(figure)
        print(self)
        toolbar = NavToolbar(self.canvas, self)
        toolbar.pack(side=tk.BOTTOM)

        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        figure.tight_layout()
        self.plot_first = False
        self.lines = [None, None, None, None, None, None, None, None]

    def update_graph(self, time, Vm, I, gNa, gK, gleak, m, h, n):
        if not self.plot_first:
            self.lines[0] = self.membrane_axis.plot(time, Vm)[0]
            self.lines[1], = self.current_axis.plot(time, I, 'g')

            self.lines[2], self.lines[3], self.lines[4], = \
                self.conductance_axis.plot(time, gNa, time, gK, time, gleak)
            self.conductance_axis.set_ylim([0, max(gNa)*1.1])

            self.lines[5], self.lines[6], self.lines[7], = \
                self.gate_axis.plot(time, m, 'b', time, h, 'b-.', time, n, 'orange')
            self.plot_first = True
        else:
            for i, data in enumerate([Vm, I, gNa, gK, gleak, m, h, n]):
                self.lines[i].set_ydata(data)

        self.membrane_axis.legend(('Membrane Voltage',),
                              loc="upper left", prop=font_gate_legend,
                              frameon=False, borderpad=0, handletextpad=0,
                              labelspacing=0)
        self.current_axis.legend(("Current Injection",),
                                 loc="upper right", prop=font_gate_legend,
                              frameon=False, borderpad=0, handletextpad=0,
                              labelspacing=0)

        self.conductance_axis.legend(("Na conductance", "K conductance", "leak conductance"),
                                     loc="upper right", prop=font_gate_legend,
                                     frameon=False, borderpad=0, handletextpad=0,
                                     labelspacing=0
                                     )

        self.gate_axis.legend(("m gate", "h gate", "n gate"),
                              loc="upper right", prop=font_gate_legend,
                              frameon=False, borderpad=0, handletextpad=0,
                              labelspacing=0)

        self.canvas.draw()

