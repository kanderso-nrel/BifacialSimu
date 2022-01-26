# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 16:36:57 2022

@author: Olli
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import pvlib as pvlib
from pvlib import solarposition, irradiance

pvlib.irradiance.dirint(ghi, solar_zenith, times, pressure=101325.0, use_delta_kt_prime=True, temp_dew=None, min_cos_zenith=0.065, max_zenith=87)