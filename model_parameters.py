# Copyright (c) 2018 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""
File to include initial values for
"""

__author__ = "Kyle Vitatus Lopin"

from numpy import arange, zeros, exp, vectorize


# if not params:
#     # if a set of parameters has not been loaded from a
#     # previous version, load the original HnH parameters
#     import initial_parameters as params

import initial_parameters as params


class Gates:
    def __init__(self, gate: str):
        if gate == 'n':
            self.alpha_max = params.alpha_n_max
            self.alpha_shift = params.alpha_n_shift
            self.alpha_slope = params.alpha_n_slope
            self.beta_max = params.beta_n_max
            self.beta_slope = params.beta_n_slope
        elif gate == 'm':
            self.alpha_max = params.alpha_m_max
            self.alpha_shift = params.alpha_m_shift
            self.alpha_slope = params.alpha_m_slope
            self.beta_max = params.beta_m_max
            self.beta_slope = params.beta_m_slope
        elif gate == 'h':
            self.alpha_max = params.alpha_m_max
            self.alpha_shift = params.alpha_m_shift
            self.alpha_slope = params.alpha_m_slope
            self.beta_max = params.beta_m_max
            self.beta_slope = params.beta_m_slope

    def alpha(self, voltage):
        if voltage != self.alpha_shift:
            return self.calc_alpha(voltage)
        else:
            return (self.calc_alpha(voltage-1) +
                    self.calc_alpha(voltage+1))/2

    def calc_alpha(self, voltage):
        return self.alpha_max * (self.alpha_shift-voltage) / (
               exp((self.alpha_shift-voltage) / self.alpha_slope)-1)

    def beta(self, voltage):
        return self.beta_max * exp(-voltage / self.beta_slope)
