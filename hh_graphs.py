# Copyright (c) 2018 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""

"""

__author__ = "Kyle Vitatus Lopin"

from numpy import arange, vectorize, exp, zeros
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib import rcParams

import tkinter as tk
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
        figure, (membrane_axis, conductance_axis, gate_axis) = \
        plt.subplots(3, 1, gridspec_kw={'height_ratios': [3, 2, 2]}, figsize=(7, 11))

        membrane_axis.set_ylabel("Membrane potential (mV)", fontsize=AXIS_LABEL_SIZE)

        # conductance_axis = simulation_figure.add_subplot(312)
        conductance_axis.set_ylabel("Conductance (mS/cm\u00b2)", fontsize=AXIS_LABEL_SIZE)

        # gate_axis = simulation_figure.add_subplot(313)
        gate_axis.set_ylabel("fraction of channels", fontsize=AXIS_LABEL_SIZE)

        self.canvas = FigureCanvasTkAgg(figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        figure.tight_layout()
