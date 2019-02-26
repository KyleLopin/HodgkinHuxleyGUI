# Copyright (c) 2018 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""
Parameters to use to model the n, m, and h gates of a Hodgkin Huxley model
"""

__author__ = "Kyle Vitatus Lopin"

# model parameters
V_rest  = 0      # mV
Cm      = 1      # uF/cm2
gbar_Na = 120    # mS/cm2
gbar_K  = 36     # mS/cm2
gbar_l  = 0.3    # mS/cm2
E_Na    = 115    # mV
E_K     = -12    # mV
E_l     = 10.613 # mV

# n gate
alpha_n_max   = 0.01
alpha_n_shift = 10.
alpha_n_slope = 10.
beta_n_max    = 0.125
beta_n_slope  = 80.

# m gate
alpha_m_max   = 0.1
alpha_m_shift = 25.
alpha_m_slope = 10.
beta_m_max    = 4.
beta_m_slope  = 18.

# h gate
alpha_h_max   = 0.07
alpha_h_slope = 20.
beta_h_max    = 1.
beta_h_shift  = 30.
beta_h_slope  = 10.

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
