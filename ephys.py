import datajoint as dj

import acquisition
import reference
import equipment


schema = dj.schema(dj.config['names.%s' % __name__], locals())


@schema
class ExtracellularRecording(dj.Manual):
    # <class 'electrophysiology.models.ExtracellularRecording'>
    # <class 'electrophysiology.models.ProbeInsertion'>
    # <class 'electrophysiology.models.ProbeModel'>
    definition = """
    -> acquisition.Session
    extracellular_rec_start:    datetime        # start time
    ---
    extracellular_rec_end:      datetime        # end time
    -> equipment.Amplifier
    -> equipment.DAQ
    ground_electrode:		varchar(255)    # ground electrode
    reference_electrode:	varchar(255)    # reference electrode
    filter_info:		varchar(255)    # filter information
    recorded_potential:         longblob        # low-pass filtered
    impedance:                  longblob        # impedance
    gains:                      longblob        # gain
    """

    class Probe(dj.Part):
        # XXX: TODO: split by electrode x/y/z; tie to other data
        definition = """
        -> ephys.ExtracellularRecording
        probe_id                int
        ---
        -> reference.BrainLocation
        -> equipment.ProbeModel
        site_positions:         blob            # probe site positions
        channel_mapping:        blob            # channel mapping
        """


@schema
class SortedUnitGroup(dj.Computed):
    # <class 'electrophysiology.models.SpikeSorting'>
    definition = """
    -> ExtracellularRecording
    ---
    """

    class Unit(dj.Part):
        # <class 'electrophysiology.models.SpikeSortedUnit'>
        # TODO: CLUSTER_GROUPS
        # TODO: WIDTH_CLASSES
        definition = """
        -> SortedUnitGroup
        cluster_number:         integer         # cluster number
        ---
        -> reference.BrainLocation
        channel_group:          integer         # channel group
        width:                  float		# trough to peak width
        half_width:             float		# half width
        amplitude:              float		# trough to peak amplitude
        rvr:                    float		# refractory violation rate
        isolation_distance:     float		# isolation distance
        l_ratio:                float		# l ratio
        mean_firing_rate:	float		# mean firing rate
        cluster_group:          varchar(255)	# cluster group
        spike_width_class:	varchar(255)	# spike width class
        optogenetic_response:   varchar(255)	# optogenetic response
        putative_cell_type:	varchar(255)	# putative cell type
        """


@schema
class IntracellularRecording(dj.Manual):
    # <class 'electrophysiology.models.IntracellularRecording'>
    definition = """
    -> acquisition.Session
    -> reference.BrainLocation
    intracelllular_rec_start:   datetime        # start time
    ---
    intracelllular_rec_end:     datetime        # end time
    recorded_current:           longblob        # recorded current
    current_command:            longblob        # current command
    recorded_voltage:           longblob        # recorded voltage
    voltage_command:            longblob        # voltage command
    electrode_type:             enum("W", "S")  # electrode type
    -> equipment.PipettePuller          	# pipette puller
    inner_diameter:		float		# inner diameter
    outer_diameter:		float		# outer diameter
    electrode_solution:		varchar(255)	# electrode solution
    cp_fast:			float		# cp fast
    cp_slow:			float		# cp slow
    cell_cap_comp:		float		# whole cell cap comp
    cell_series_resistance:	float		# whole cell series resistance
    src_bandwidth:		float		# src bandwidth
    src_correction:		float		# src correction
    src_prediction:		float		# src prediction
    pipette_cap_comp:		float		# pipette cap comp
    bridge_balance:		float		# bridge balance
    gain:			float		# gain
    """
