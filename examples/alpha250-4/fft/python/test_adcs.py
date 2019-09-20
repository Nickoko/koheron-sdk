#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Measure the noise floor of the ADC and ADC + DAC
'''

import numpy as np
import os
import time
import matplotlib.pyplot as plt

from fft import FFT
from koheron import connect

host = os.getenv('HOST', '192.168.1.50')
client = connect(host, 'fft', restart=False)
driver = FFT(client)

print(driver.get_fs())

driver.set_fft_window(1)
driver.set_input_channel(1)

freqs = np.arange(driver.n_pts / 2) * 250. / driver.n_pts
plt.loglog(freqs, driver.read_psd_raw(0))
plt.loglog(freqs, driver.read_psd_raw(1))
plt.show()
