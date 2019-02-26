# Copyright (c) 2018 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""
Model classes to simulate a Hodgkin and Huxley neuron model.
"""

__author__ = "Kyle Vitatus Lopin"

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


class ModelGates(object):
    """
    take in parameter dictionary and make the vectors of alpha and betas in a voltage look up table
    """
    def __init__(self, parameters):

        self.n_gate = Object()  # Probably a better way to do this
        self.n_gate.alpha, self.n_gate.beta, self.n_gate.inf = \
            Model_Gates.set_gate_kinetics_activation(self, parameters['alpha_n_max'],
                                                     parameters['alpha_n_shift'],
                                                     parameters['alpha_n_slope'],
                                                     parameters['beta_n_max'],
                                                     parameters['beta_n_slope'])
        self.m_gate = Object()
        self.m_gate.alpha, self.m_gate.beta, self.m_gate.inf = Model_Gates.set_gate_kinetics_activation(self,
                                                                                                        parameters['alpha_m_max'],
                                                                                                        parameters['alpha_m_shift'], parameters['alpha_m_slope'],
                                                                                                        parameters['beta_m_max'], parameters['beta_m_slope'])
        self.h_gate = Object()
        self.h_gate.alpha, self.h_gate.beta, self.h_gate.inf = Model_Gates.set_gate_kinetics_inactivation(self,
                                                                                                          parameters['alpha_h_max'],
                                                                                                          parameters['alpha_h_slope'], parameters['beta_h_max'],
                                                                                                          parameters['beta_h_shift'], parameters['beta_h_slope'])

    def set_gate_kinetics_activation(self, alpha_max, alpha_shift, alpha_slope, beta_max, beta_slope):
        alpha = lambda v: alpha_max*(-v + alpha_shift)/(exp((-v + alpha_shift)/alpha_slope) - 1)
        hold = (alpha(alpha_shift-1) + alpha(alpha_shift+1))/2.
        # not the best way, FIX THIS AT SOME POINT
        alpha = vectorize(lambda v: alpha_max*(-v + alpha_shift)
                                    /(exp((-v + alpha_shift)/alpha_slope) - 1) if v != alpha_shift else hold)

        beta = lambda v: beta_max*exp(-v/beta_slope)
        gate_inf = lambda v: alpha(v)/(alpha(v) + beta(v))
        return (alpha, beta, gate_inf)

    def set_gate_kinetics_inactivation(self, alpha_max, alpha_slope, beta_max, beta_shift, beta_slope):
        alpha = lambda v: alpha_max*exp(-v/alpha_slope)
        beta  = lambda v: beta_max/(exp((-v + beta_shift)/beta_slope) + 1)
        gate_inf   = lambda v: alpha(v)/(alpha(v) + beta(v))
        return alpha, beta, gate_inf
