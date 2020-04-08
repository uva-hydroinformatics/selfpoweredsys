# Imports timeseries and harvester modules from environment package
from context import timeseries
from context import turbine
from context import battery

# Imports other required modules for this example
import pandas as pd
import os
import matplotlib.pyplot as plt

try: 
	# Reads the pickle dataframe generated by the example_usgs.py script
	flow_df = pd.read_pickle(os.path.join('./','data_files/ILState03612600.pkl'))
except:
	print("=== Error: File  \"data_files/ILState03612600.pkl \" could not be found!                ===" )
	print("=== Make sure to first run the script  \"example_usgs.py \"  to download required file. ===" )
	exit()

# Creates an one-minute linearly interpolated time series
resampled_flow_df = timeseries.resampledf(flow_df, interp_method='linear', verbose=True)

# Creates power time series based on first version of water lily turbine model 
power_df = turbine.waterlilyv1(resampled_flow_df, verbose=True)

# Plots power output data for first version of water lily turbine model 
power_df.plot()
plt.title("Power Generation for WaterLily Turbine Model (V1)")
plt.xlabel("Timestamp")
plt.ylabel("Generated power in Watts")
plt.legend(loc='upper right')
plt.show()

# Calculates the energy neutral battery requirements based on ideal batteries
[batt_capacity, initial_charge, mean_power, total_energy_kwh, net_energy_kwh] = battery.eneutralreq(power_df,verbose=True)

# Plots power data for first version of water lily turbine model 
net_energy_kwh.plot()
plt.title("Energy storage demand for energy neutral operation")
plt.xlabel("Timestamp")
plt.ylabel("Net energy in kWh")
plt.legend(loc='lower right')
plt.show()