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


class HHGateFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        simulation_figure = plt.figure(figsize=(7, 7))
        membrane_axis = simulation_figure.add_subplot(311)
        membrane_axis.set_ylabel("Membrane potential (mV)", fontsize=12)

        self.canvas = FigureCanvasTkAgg(simulation_figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
