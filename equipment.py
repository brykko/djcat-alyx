import datajoint as dj

schema = dj.schema(dj.config['names.%s' % __name__], locals())


@schema
class LabLocation(dj.Manual):
    # <class 'equipment.models.LabLocation'>
    definition = """
    lab_location:		int             # lab location
    ---
    name:                       varchar(255)    # name
    """


@schema
class Supplier(dj.Manual):
    # <class 'equipment.models.Supplier'>
    definition = """
    supplier_name:		int             # supplier name
    ---
    description:		varchar(1024)	# description
    """


@schema
class VirusBatch(dj.Manual):
    # <class 'equipment.models.VirusBatch'>
    definition = """
    -> Supplier
    batch_id:			int             # batch id
    virus_type:			varchar(255)	# virus type
    ---
    description:		varchar(255)	# description
    date_time_made:		datetime	# date time made
    nominal_titer:		float		# nominal titer
    """


@schema
class EquipmentModel(dj.Manual):
    # <class 'equipment.models.EquipmentModel'>
    # TODO: Should model types be a lookup?
    # ... assuming Alyx' separate classes vs field is reasoned.
    definition = """
    -> Supplier
    model_id:			int             # model id
    ---
    model_name:			varchar(255)	# model name
    description:		varchar(255)	# description
    """

    class LightSource(dj.Part):
        # <class 'equipment.models.LightSource'>
        definition = """
        -> EquipmentModel
        """

    class Amplifier(dj.Part):
        # <class 'equipment.models.Amplifier'>
        definition = """
        -> EquipmentModel
        """

    class PipettePuller(dj.Part):
        # <class 'equipment.models.PipettePuller'>
        definition = """
        -> EquipmentModel
        """

    class DAQ(dj.Part):
        # <class 'equipment.models.DAQ'>
        definition = """
        -> EquipmentModel
        """

    class ProbeModel(dj.Part):
        # <class 'electrophysiology.models.ProbeModel'>
        definition = """
        -> EquipmentModel
        """


@schema
class LightSource(dj.Manual):
    # <class 'equipment.models.Appliance'>
    # <class 'equipment.models.LightSource'>
    definition = """
    -> EquipmentModel.LightSource
    -> LabLocation
    light_source_serial:        varchar(255)	# serial no
    ---
    description:		varchar(255)	# description
    descriptive_name:		varchar(255)	# descriptive name
    """


@schema
class Amplifier(dj.Manual):
    # <class 'equipment.models.Appliance'>
    # <class 'equipment.models.Amplifier'>
    definition = """
    -> EquipmentModel.Amplifier
    -> LabLocation
    amplifier_serial_no:        varchar(255)	# serial no
    ---
    description:		varchar(255)	# description
    descriptive_name:		varchar(255)	# descriptive name
    """


@schema
class PipettePuller(dj.Manual):
    # <class 'equipment.models.Appliance'>
    # <class 'equipment.models.PipettePuller'>
    definition = """
    -> EquipmentModel.PipettePuller
    -> LabLocation
    pipette_puller_serial_no:   varchar(255)	# serial no
    ---
    description:		varchar(255)	# description
    descriptive_name:		varchar(255)	# descriptive name
    """


@schema
class DAQ(dj.Manual):
    # <class 'equipment.models.Appliance'>
    # <class 'equipment.models.DAQ'>
    definition = """
    -> EquipmentModel.DAQ
    -> LabLocation
    daq_serial_no:              varchar(255)	# serial no
    ---
    description:		varchar(255)	# description
    descriptive_name:		varchar(255)	# descriptive name
    """


@schema
class ProbeModel(dj.Manual):
    # <class 'equipment.models.Appliance'>
    # <class 'electrophysiology.models.ProbeModel'>
    definition = """
    -> EquipmentModel.ProbeModel
    -> LabLocation
    probe_model_serial_no:      varchar(255)	# serial no
    ---
    description:		varchar(255)	# description
    descriptive_name:		varchar(255)	# descriptive name
    """
