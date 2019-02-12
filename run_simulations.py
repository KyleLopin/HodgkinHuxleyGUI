from __future__ import division

__author__ = 'Kyle Vitautas Lopin'

from numpy import arange, zeros, exp, vectorize
import Gates
import matplotlib.pyplot as plt

def UpdateSimulationWindow(self, stimulus):
    self.I_applied = stimulus

    time, Vm, I, gNa, gK, gleak, m, n, h = RunSimulation(self)
    self.sim.time = time
    self.sim.gNa = gNa
    self.sim.gK = gK
    self.sim.gleak = gleak
    self.sim.m = m
    self.sim.n = n
    self.sim.h = h
    V = arange(-50, 151)
    # plt.figure()
    # plt.plot(V, self.gates.m_gate.alpha(V))
    # plt.show()
    if not hasattr(self, 'line_Vm'):
        # check if a line has been draw before, if not then draw them
        self.line_Vm, = self.simulation_voltage_axis.plot(time, Vm)
        self.line_I,  = self.simulation_current_axis.plot(time, I, 'g')
        self.simulation_canvas.show()

        self.line.gNa, = self.gates_time_graph_axis.plot(time, gNa)
        self.line.gK,  = self.gates_time_graph_axis.plot(time, gK, 'g')
        self.gates_time_graph_axis.set_ylim([0, max(max(gNa), max(gK))*1.1])
        self.gate_simulation_canvas.draw()
    else:
        # if lines are already drawn, update the data
        self.line_Vm.set_ydata(Vm)
        self.line_I.set_ydata(I)
        self.simulation_canvas.draw()

        self.line_gNa.set_ydata(gNa)
        self.line_gK.set_ydata(gK)
        self.gate_simulation_canvas.draw()


def RunSimulation(self):
    dt = 0.025
    time=arange(self.time_range[0], self.time_range[1]+dt, dt)
    Vm = zeros(len(time))
    g_Na_array = zeros(len(time))
    g_K_array  = zeros(len(time))
    g_l_array  = zeros(len(time))
    m_array = zeros(len(time))
    n_array = zeros(len(time))
    h_array = zeros(len(time))
    V_rest = self.model_parameters['V_rest']
    Vm[0] = V_rest
    m = self.gates.m_gate.inf(V_rest)
    h = self.gates.h_gate.inf(V_rest)
    n = self.gates.n_gate.inf(V_rest)

    gbar_Na = self.model_parameters['gbar_Na']
    gbar_K = self.model_parameters['gbar_K']
    gbar_l = self.model_parameters['gbar_l']
    E_Na = self.model_parameters['E_Na']
    E_K = self.model_parameters['E_K']
    E_l = self.model_parameters['E_l']
    Cm = self.model_parameters['Cm']

    ## Stimulus
    I = zeros(len(time))
    for i, t in enumerate(time):
        if 5 <= t <= 30: I[i] = self.I_applied # uA/cm2

    for i in range(1,len(time)):
        g_Na = gbar_Na*(m**3)*h
        g_K  = gbar_K*(n**4)
        g_l  = gbar_l
        # save all parameters in an array to export
        g_Na_array[i] = g_Na
        g_K_array[i] = g_K
        g_l_array[i] = g_l

        m_array[i] = m
        n_array[i] = n
        h_array[i] = h

        m += dt*(self.gates.m_gate.alpha(Vm[i-1])*(1 - m) - self.gates.m_gate.beta(Vm[i-1])*m)
        h += dt*(self.gates.h_gate.alpha(Vm[i-1])*(1 - h) - self.gates.h_gate.beta(Vm[i-1])*h)
        n += dt*(self.gates.n_gate.alpha(Vm[i-1])*(1 - n) - self.gates.n_gate.beta(Vm[i-1])*n)

        Vm[i] = Vm[i-1] + (I[i-1] - g_Na*(Vm[i-1] - E_Na) - g_K*(Vm[i-1] - E_K)
                           - g_l*(Vm[i-1] - E_l)) / Cm * dt
    return time, Vm, I, g_Na_array, g_K_array, g_l_array, m_array, n_array, h_array

def InitializeSimulations(self, parameters):
    gates = GetGatingParameters(self, parameters)


def GetGatingParameters(self, parameters):
    """
    Get new parameters to use in the hodgkin huxley model, this creates a custom class from Gates.py file,
    binds variables to self
    :param parameters: parameters to use to make the alpha and beta rates
    :return:
    """
    self.gates = Gates.Model_Gates(parameters)


def Make_n_GateRateWindow(self):
    pass

def Draw_gK(self, _value):
    print(_value)
    if _value == 0 and hasattr(self.line, 'gK'):
        self.line_gK.remove()
    if _value == 1 and hasattr(self.sim, 'gK'):
        self.line_gK,  = self.gates_time_graph_axis.plot(self.sim.time, self.sim.gK, 'g')


    self.gate_simulation_canvas.draw()
