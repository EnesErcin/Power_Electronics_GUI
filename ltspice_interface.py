import ltspy3
import os 
import numpy as np


def extract_var(component):

    if component == "THYRISTOR":
        lt_spice_raw = ltspy3.SimData(os.path.dirname(__file__)+'\\Ltspice'+'\\THYRISTOR.raw')
        data_len = int(np.shape(lt_spice_raw.values[0])[0]) 
        time_ref = np.linspace(0,data_len,data_len)
        v_s = lt_spice_raw.values[1]
        v_o = lt_spice_raw.values[2]

        ## Delay Angle Calculation

        # Adjust this parameter accordingly to your design
        # For example -- > tdif = 6ms , source frequancy = 50Hz
        tdif   = 6*10**-3       
        source_freq = 50
        source_period = 1/source_freq 
        if tdif>source_period:
            tdif = tdif%source_period
        delay_angle = tdif*360*source_freq

        return time_ref,v_s,v_o,delay_angle


    elif component == "BJT":
        lt_spice= os.path.dirname(__file__)+'\\Ltspice'+'\\BJT.'          
        lt_spice_raw =  lt_spice+"raw"
        lt_spice_raw =  ltspy3.SimData(lt_spice_raw)
        data_len = int(np.shape(lt_spice_raw.values[0])[1])
        time_ref = np.linspace(0,data_len,data_len)
        print(lt_spice_raw.variables)
        vce     =   lt_spice_raw.values[1]
        vbe     =   lt_spice_raw.values[3]
        ic      =   lt_spice_raw.values[4]
        return time_ref,vce,vbe,ic

    elif component == "DIODE":
        lt_spice_raw = ltspy3.SimData(os.path.dirname(__file__)+'\\Ltspice'+'\\DIODE.raw')
        data_len = int(np.shape(lt_spice_raw.values[0])[0]) 
        time_ref = np.linspace(0,data_len,data_len)
        vs = lt_spice_raw.values[1]
        vo = lt_spice_raw.values[2]
        return time_ref,vs,vo


    elif component == "MOSFET":
        lt_spice= os.path.dirname(__file__)+'\\Ltspice'+'\\MOSFET.'          
        lt_spice_raw =  lt_spice+"raw"
        lt_spice_raw =  ltspy3.SimData(lt_spice_raw)
        data_len = int(np.shape(lt_spice_raw.values[0])[1])
        time_ref = np.linspace(0,data_len,data_len)
        vds         = lt_spice_raw.values[0]
        vgs         = lt_spice_raw.values[2]
        id_current  = lt_spice_raw.values[5]
        return time_ref,vds,vgs,id_current



