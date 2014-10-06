from __future__ import division

__author__ = 'Kyle Vitautas Lopin'

"""
Custom class to create vectors of the alpha and betas of the n,m, and h gates of a hodgkin huxley model
"""

from numpy import arange, zeros, exp, vectorize

class Object(object):
    pass

class Model_Gates(object):
    """
    take in parameter dictionary and make the vectors of alpha and betas in a voltage look up table
    """
    def __init__(self, parameters):

        self.n_gate = Object()  # Probably a better way to do this
        self.n_gate.alpha, self.n_gate.beta, self.n_gate.inf = Model_Gates.SetGateKinetics_activation(self,
                                                             parameters['alpha_n_max'],
                                                             parameters['alpha_n_shift'], parameters['alpha_n_slope'],
                                                             parameters['beta_n_max'], parameters['beta_n_slope'])
        self.m_gate = Object()
        self.m_gate.alpha, self.m_gate.beta, self.m_gate.inf = Model_Gates.SetGateKinetics_activation(self,
                                                             parameters['alpha_m_max'],
                                                             parameters['alpha_m_shift'], parameters['alpha_m_slope'],
                                                             parameters['beta_m_max'], parameters['beta_m_slope'])
        self.h_gate = Object()
        self.h_gate.alpha, self.h_gate.beta, self.h_gate.inf = Model_Gates.SetGateKinetics_inactivation(self,
                                                              parameters['alpha_h_max'],
                                                              parameters['alpha_h_slope'], parameters['beta_h_max'],
                                                              parameters['beta_h_shift'], parameters['beta_h_slope'])


    def SetGateKinetics_activation(self, alpha_max, alpha_shift, alpha_slope, beta_max, beta_slope):
        alpha = lambda v: alpha_max*(-v + alpha_shift)/(exp((-v + alpha_shift)/alpha_slope)- 1)
        hold = (alpha(alpha_shift-1) + alpha(alpha_shift+1))/2.
        # not the best way, FIX THIS AT SOME POINT
        alpha = vectorize(lambda v: alpha_max*(-v + alpha_shift)
                                    /(exp((-v + alpha_shift)/alpha_slope) - 1) if v != alpha_shift else hold)


        beta = lambda v: beta_max*exp(-v/beta_slope)
        gate_inf = lambda v: alpha(v)/(alpha(v) + beta(v))
        return (alpha, beta, gate_inf)

    def SetGateKinetics_inactivation(self, alpha_max, alpha_slope, beta_max, beta_shift, beta_slope):
        alpha = lambda v: alpha_max*exp(-v/alpha_slope)
        beta  = lambda v: beta_max/(exp((-v + beta_shift)/beta_slope) + 1)
        gate_inf   = lambda v: alpha(v)/(alpha(v) + beta(v))
        return alpha, beta, gate_inf