# Copyright (c) 2018 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""
Model portion of the Hodgkin Huxley neuron model
"""

__author__ = "Kyle Vitatus Lopin"

# local files
import initial_parameters as init_params


class HodgkinHuxleyModel:
    def __init__(self, params=None):
        if not params:
            # load the original model parameters
            params = init_params
        for params in params.model_parameters:
            print(params, type(params))
            print(init_params.__dict__)
            setattr(self, params, init_params.params)
        print(self.__dict__)


    def check(self):
        pass


class HodgkinHuxleyOriginalModel:
    def __init__(self):
        # model parameters
        self.V_rest = 0  # mV
        self.Cm = 1  # uF/cm2
        self.gbar_Na = 120  # mS/cm2
        self.gbar_K = 36  # mS/cm2
        self.gbar_l = 0.3  # mS/cm2
        self.E_Na = 115  # mV
        self.E_K = -12  # mV
        self.E_l = 10.613  # mV

        # n gate
        self.alpha_n_max = 0.01
        self.alpha_n_shift = 10.
        self.alpha_n_slope = 10.
        self.beta_n_max = 0.125
        self.beta_n_slope = 80.

        # m gate
        self.alpha_m_max = 0.1
        self.alpha_m_shift = 25.
        self.alpha_m_slope = 10.
        self.beta_m_max = 4.
        self.beta_m_slope = 18.

        # h gate
        self.alpha_h_max = 0.07
        self.alpha_h_slope = 20.
        self.beta_h_max = 1.
        self.beta_h_shift = 30.
        self.beta_h_slope = 10.


if __name__ == "__main__":
    HodgkinHuxleyModel()
