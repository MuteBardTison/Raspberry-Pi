#!/usr/bin/env python
cpu_temp_file = open("../../../sys/class/thermal/thermal_zone0/temp")
print("CPU temperature: {:.3f}".format(float(cpu_temp_file.readline()) / 1000) + "\u00b0" + "C")
cpu_temp_file.close()
