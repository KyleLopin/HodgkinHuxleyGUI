__author__ = 'Kyle Vitautas Lopin'

"""
User Interface that simulates Hodgkin and Huxley equations for the gaint axon of a squid
"""

import tkinter as tk

import hh_graphs
import init_widgets as iw
import pack_widgets as pw
import run_simulations as rs
import Gates

model_parameters = {
    'V_rest'  : 0,      # mV
    'Cm'      : 1,      # uF/cm2
    'gbar_Na' : 120,    # mS/cm2
    'gbar_K'  : 36,     # mS/cm2
    'gbar_l'  : 0.3,    # mS/cm2
    'E_Na'    : 115,    # mV
    'E_K'     : -12,    # mV
    'E_l'     : 10.613 # mV
}

gate_parameters = {
    'alpha_n_max'   : 0.01,
    'alpha_n_shift' : 10.,
    'alpha_n_slope' : 10.,
    'beta_n_max'    : 0.125,
    'beta_n_slope'  : 80.,
    'alpha_m_max'   : 0.1,
    'alpha_m_shift' : 25.,
    'alpha_m_slope' : 10.,
    'beta_m_max'    : 4.,
    'beta_m_slope'  : 18.,
    'alpha_h_max'   : 0.07,
    'alpha_h_slope' : 20.,
    'beta_h_max'    : 1.,
    'beta_h_shift'  : 30.,
    'beta_h_slope'  : 10.
}


class Hodgkin_Huxley_GUInew(tk.Frame, object):
    """
    Class to create a graphical user interface for people to explore the properties of the
    Hodgkin Huxley model of a gaint axon of a squid
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)



class Hodgkin_Huxley_GUI(tk.Frame, object):
    """
    Class to create a graphical user interface for people to explore the properties of the
    Hodgkin Huxley model of a gaint axon of a squid
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.sim = Gates.Object()
        self.line = Gates.Object()  # find a better way to do this
        self.I_applied = 20
        self.time_range = [0, 55]
        self.model_parameters = model_parameters
        simulation_figure_bed, self.simulation_voltage_axis, \
        self.simulation_current_axis = iw.MakeSimulationWindow(self)

        simulation_master_frame = tk.Frame()
        information_frame = tk.Frame()
        options_frame = tk.Frame()
        view_options_frame = tk.Frame(options_frame)
        simulation_options_frame = tk.Frame(options_frame)

        gates_time_graph_bed, self.gates_time_graph_axis = iw.MakeGatesWithTimeWindow(self.time_range)
        self.parameter_frame = iw.MakeParameterFrame(self, information_frame)
        iw.MakeSimulationOptionWindow(self, simulation_options_frame)
        iw.MakeGatesWindowOptions(self, view_options_frame)

        rs.InitializeSimulations(self, gate_parameters)

        self.simulation_canvas = pw.pack_canvas(self, simulation_figure_bed,
                                                simulation_master_frame, anchor_option="nw")
        self.gate_simulation_canvas = pw.pack_canvas(self, gates_time_graph_bed, simulation_master_frame,
                                                     anchor_option='sw')
        simulation_master_frame.pack(side='left')

        self.parameter_frame.pack(side="top", fill="both", padx=15)
        information_frame.pack()

        view_options_frame.pack(side="left", fill='y')
        simulation_options_frame.pack(side="left")

        options_frame.pack(side="bottom")


def main():
    """
    call the custom class the Hodgkin and Huxley GUI is in
    :return:
    """
    root=tk.Tk()
    root.title("Hodgkin and Huxley Simulator")
    root.geometry("950x600")
    Hodgkin_Huxley_GUI(root)
    root.mainloop()

if __name__ == '__main__':
    """
    run the main loop if this program is called directly, or else the class Hodgkin_Huxley_GUI
    can be called by another program
    """
    main()