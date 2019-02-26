# Copyright (c) 2018 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""
tkinter frame that impliments the original hodgkin and huxley model
"""

__author__ = "Kyle Vitatus Lopin"

# standard libraries
import tkinter as tk
# local files
import hh_graphs
import parameter_frame as control_frame


class HodgkinHuxleyOriginal(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.view = hh_graphs.HHGateFrame(self)
        self.view.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        self.control = control_frame.ParameterFrame(self)
        self.control.pack(side="top", fill="x")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hodgkin and Huxley Simulator")
    root.geometry("1050x800")
    HodgkinHuxleyOriginal(root)
    root.mainloop()
