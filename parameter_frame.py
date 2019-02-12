# Copyright (c) 2018 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""
Make tkinter frame to put in Hodgkin Huxley model that has all the parameters the user can change
and the user interface to change them
"""

__author__ = "Kyle Vitatus Lopin"

import tkinter as tk


class ParameterFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bd=2)

        left_frame = tk.Frame(self, bd=2)
        right_frame = tk.Frame(self, bd=2)

        cap_label = tk.Label(self, text="Cm=1 \u03BcF/cm\u00b2")
        # cap_label = tk.Text(param_master, width=15, height=2, borderwidth=0,
        #                     background=param_master.cget("background"),
        #                     font='helvetica 12')
        # cap_label.tag_configure("subscript", offset=-4)
        # cap_label.insert("insert", "C", "", "m", "subscript", "=1 \u03BcF/C", "", "m", "subscript", "\u00b2")
        # cap_label.configure(state="disabled")
        # cap_label.pack(side="top")

        gNa_label = tk.Label(right_frame, text="g(Na)    = 120 mS/cm\u00b2")
        gK_label = tk.Label(right_frame, text="g(K)      = 36   mS/cm\u00b2")
        gleak_label = tk.Label(right_frame, text="g(Leak) = 0.3  mS/cm^\u00b2")

        E_Na_label = tk.Label(left_frame, text="E(Na)   = 115 mV")
        E_K_label = tk.Label(left_frame, text="E(K)     = -12 mV")
        E_leak_label = tk.Label(left_frame, text="E(leak) = 10.613 mV")

        cap_label.pack(side="top")

        gNa_label.pack(side="top", anchor="w")
        gK_label.pack(side="top", anchor="w")
        gleak_label.pack(side="top", anchor="w")

        E_Na_label.pack(side="top", anchor="w")
        E_K_label.pack(side="top", anchor="w")
        E_leak_label.pack(side="top", anchor="w")

        left_frame.pack(side="left", ipadx=4, fill=tk.X)
        right_frame.pack(side="right", ipadx=4, fill=tk.X)
