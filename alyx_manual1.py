# alyx.manual1.py:
# manually converted Alyx schema -
# preserves Alyx' object inheritance model & uuid aspects;
# some bugs exist w/r/t primary keys - intended mainly as a reference.

import datajoint as dj

schema = dj.schema(dj.config['names.%s' % __name__], locals())

# #####################################################################
# reference.py ########################################################
# #####################################################################


@schema
class User(dj.Manual):
    # <class 'misc.models.OrderedUser'>
    # <class 'django.contrib.auth.models.User'>
    definition = """
    username:		varchar(255)	# username
    ---
    password:		varchar(255)	# password
    email:		varchar(255)	# email address
    last_login:		datetime	# last login
    first_name:		varchar(255)	# first name
    last_name:		varchar(255)	# last name
    date_joined:	datetime	# date joined
    is_active:		boolean		# active
    is_staff:		boolean		# staff status
    is_superuser:	boolean		# superuser status
    """


@schema
class UserGroup(dj.Manual):
    TODO = True
    definition = """
    groupname:		varchar(255)	# groupname
    """

    class UserGroupMembership(dj.Part):

        definition = """
        -> UserGroup
        -> User
        """


@schema
class PermissionType(dj.Lookup):

    definition = """
    permission: varchar(30)
    """
    contents = zip(['p1', 'p2', 'p3'])


@schema
class UserPermission(dj.Lookup):

    definition = """
    -> User
    -> PermissionType
    """


@schema
class BrainLocation(dj.Manual):
    # <class 'misc.models.BrainLocation'>
    definition = """
    brain_location_id:		char(32)	# brain location id
    ---
    name:			varchar(255)	# name
    stereotaxic_coordinates:	longblob	# stereotaxic coordinates
    description:		varchar(255)	# description
    allen_location_ontology:    varchar(255)	# allen location ontology
    json:			varchar(255)	# json
    """


@schema
class Severity(dj.Lookup):
    definition = """
    severity:			tinyint			# severity
    ---
    severity_desc:		varchar(32)		# severity desc
    """
    contents = (
        (0, ''),
        (1, 'Sub-threshold'),
        (2, 'Mild'),
        (3, 'Moderate'),
        (4, 'Severe'),
        (5, 'Non-recovery'),
    )


@schema
class CoordinateTransformation(dj.Manual):
    # <class 'misc.models.CoordinateTransformation'>
    definition = """
    transform_id:		char(32)	# id
    ---
    json:			varchar(255)	# json
    name:    			varchar(255)	# name
    description:		varchar(255)	# description
    allen_location_ontology:	varchar(255)	# allen location ontology
    origin:			longblob	# origin
    transformation_matrix:    	longblob	# transformation matrix
    """


@schema
class Note(dj.Manual):
    # <class 'misc.models.Note'>
    # FIXME: allows tagging objects via django's ContentType and UUIDs
    definition = """
    -> User
    note_id:		char(32)		# id
    ---
    date_time:		datetime		# date time
    text:		varchar(255)		# text
    object_id:		char(32)		# object id
    json:		varchar(255)		# json
    """

# #####################################################################
# subject.py ##########################################################
# #####################################################################


@schema
class Species(dj.Manual):
    # <class 'subjects.models.Species'>
    definition = """
    species_id:				char(32)	# species id
    ---
    json:				varchar(255)	# json
    binomial:				varchar(255)	# binomial
    display_name:			varchar(255)	# display name
    """


@schema
class Strain(dj.Manual):
    # <class 'subjects.models.Strain'>
    definition = """
    strain_id:				char(32)	# strain id
    ---
    json:				varchar(255)	# json
    descriptive_name:			varchar(255)	# descriptive name
    description:    			varchar(255)	# description
    """


@schema
class Sequence(dj.Manual):
    # <class 'subjects.models.Sequence'>
    definition = """
    sequence_id:			char(32)	# sequence id
    ---
    base_pairs:				varchar(255)	# base pairs
    description:			varchar(255)	# description
    informal_name:			varchar(255)	# informal name
    json:				varchar(255)	# json
    """


@schema
class Allele(dj.Manual):
    # <class 'subjects.models.Allele'>
    definition = """
    allele_id:				char(32)	# allele id
    ---
    standard_name:			varchar(255)	# standard name
    informal_name:			varchar(255)	# informal name
    json:				varchar(255)	# json
    """


@schema
class Line(dj.Manual):
    # <class 'subjects.models.Line'>
    # XXX: autoname index: basically autogenerates a unique sequence
    definition = """
    -> Species
    -> Strain
    -> Sequence
    line_id:				char(32) 	# line id
    ---
    name:				varchar(255)	# name
    description:			varchar(255)	# description
    target_phenotype:			varchar(255)	# target phenotype
    auto_name:				varchar(255)	# auto name
    is_active:				boolean		# is active
    subject_autoname_index:		integer		# subject autoname index
    breeding_pair_autoname_index:	integer		# breeding pair autoname index
    litter_autoname_index:		integer		# litter autoname index
    json:				varchar(255)	# json
    """


@schema
class Source(dj.Manual):
    # <class 'subjects.models.Source'>
    definition = """
    source_id:				char(32)	# source id
    ---
    json:				varchar(255)	# json
    name:				varchar(255)	# name
    description:			varchar(255)	# description
    """


@schema
class SubjectRequest(dj.Manual):
    # <class 'subjects.models.SubjectRequest'>
    definition = """
    -> User
    -> Line
    subject_request_id:			char(32)	# subject request id
    ---
    json:				varchar(255)	# json
    count:				integer		# count
    date_time:				date		# date time
    due_date:				date		# due date
    description:			varchar(255)	# description
    """


@schema
class Subject(dj.Manual):
    # <class 'subjects.models.Subject'>
    # todo:
    # - where did responsible_user go? RETEST ADDED
    # - -> SubjectRequest or track subjects as part table of subject request?
    #      RETEST ADDED

    definition = """
    subject_id:			char(32)		# subject id
    ---
    -> Line
    nickname:			varchar(255)		# nickname
    json:			varchar(255)		# json
    sex:			enum("M", "F", "U")	# sex
    sex:			varchar(255)		# sex
    birth_date:			date			# birth date
    death_date:			date			# death date
    wean_date:			date			# wean date
    genotype_date:		date			# genotype date
    (responsible_user)          -> User
    (request)                   -> SubjectRequest
    lamis_cage:			integer			# lamis cage
    implant_weight:		float			# implant weight
    ear_mark:			varchar(255)		# ear mark
    protocol_number:		varchar(255)		# protocol number
    description:		varchar(255)		# description
    cull_method:		varchar(255)		# cull method
    adverse_effects:		varchar(255)		# adverse effects
    (actual_severity)		-> Severity		# actual severity
    to_be_genotyped:		boolean			# to be genotyped
    to_be_culled:		boolean			# to be culled
    reduced:			boolean			# reduced
    reduced_date:		date			# reduced date
    """

    class Genotype(dj.Part):
        # <class 'subjects.models.Zygosity'>
        # genotype = models.ManyToManyField('Allele', through='Zygosity')
        definition = """
        -> Subject
        -> Allele
        ---
        zygosity:			integer		# zygosity
        """


@schema
class BreedingPair(dj.Manual):
    # <class 'subjects.models.BreedingPair'>
    definition = """
    breeding_pair_id:		char(32)		# breeding pair id
    ---
    name:			varchar(255)		# name
    description:		varchar(255)		# description
    start_date:			date			# start date
    end_date:			date			# end date
    (father)			-> Subject		# father
    (mother1) 			-> Subject		# mother1
    (mother2)			-> [nullable] Subject	# mother2
    json:			varchar(255)		# json
    """

    class Litter(dj.Part):
        # <class 'subjects.models.Litter'>
        definition = """
        -> BreedingPair
        litter_id:			char(32)	# litter id
        ---
        descriptive_name:		varchar(255)	# descriptive name
        description:			varchar(255)	# description
        birth_date:			date		# birth date
        json:				varchar(255)	# json
        """

    class Offspring(dj.Part):
        definition = """
        -> BreedingPair
        -> BreedingPair.Litter
        -> Subject
        """


@schema
class GenotypeTest(dj.Manual):
    # <class 'subjects.models.GenotypeTest'>
    definition = """
    -> Subject
    -> Sequence
    genotype_test_id:			char(32)	# genotype test id
    ---
    json:				varchar(255)	# json
    test_result:			integer		# test result
    """


# #####################################################################
# equipment.py ########################################################
# #####################################################################

@schema
class LabLocation(dj.Manual):
    # <class 'equipment.models.LabLocation'>
    definition = """
    lab_location:		char(32)	# lab location
    ---
    json:			varchar(255)	# json
    """


@schema
class Supplier(dj.Manual):
    # <class 'equipment.models.Supplier'>
    definition = """
    supplier_name:		char(32)	# supplier name
    ---
    description:		varchar(1024)	# description
    """


@schema
class VirusBatch(dj.Manual):
    # <class 'equipment.models.VirusBatch'>
    definition = """
    -> Supplier
    batch_id:			char(32)	# id
    ---
    description:		varchar(255)	# description
    virus_type:			varchar(255)	# virus type
    date_time_made:		datetime	# date time made
    nominal_titer:		float		# nominal titer
    json:			varchar(255)	# json
    """


@schema
class EquipmentModel(dj.Manual):
    # <class 'equipment.models.EquipmentModel'>
    definition = """
    -> Supplier
    model_id:			char(32)	# id
    ---
    model_name:			varchar(255)	# model name
    description:		varchar(255)	# description
    json:			varchar(255)	# json
    """


@schema
class Appliance(dj.Manual):
    # <class 'equipment.models.Appliance'>
    # TODO: -> ContentType
    # TODO: Should appliance types just be a lookup?
    #   currently assuming Alyx use of separate classes vs field is reasoned.
    definition = """
    -> LabLocation
    -> EquipmentModel
    appliance_id:		char(32)	# id
    ---
    serial:			varchar(255)	# serial
    description:		varchar(255)	# description
    descriptive_name:		varchar(255)	# descriptive name
    json:			varchar(255)	# json
    """

    class WeighingScale(dj.Part):
        # <class 'equipment.models.WeighingScale'>
        definition = """
        -> Appliance
        """

    class LightSource(dj.Part):
        # <class 'equipment.models.LightSource'>
        definition = """
        -> Appliance
        """

    class Amplifier(dj.Part):
        # <class 'equipment.models.Amplifier'>
        definition = """
        -> Appliance
        """

    class PipettePuller(dj.Part):
        # <class 'equipment.models.PipettePuller'>
        definition = """
        -> Appliance
        """

    class DAQ(dj.Part):
        # <class 'equipment.models.DAQ'>
        definition = """
        -> Appliance
        """

# #####################################################################
# actions.py ##########################################################
# #####################################################################


@schema
class ProcedureType(dj.Manual):
    # <class 'actions.models.ProcedureType'>
    definition = """
    procedure_id:		char(32)		# procedure id
    ---
    json:			varchar(255)		# json
    name:			varchar(255)		# name
    description:		varchar(255)		# description
    """


@schema
class Weighing(dj.Manual):
    # <class 'actions.models.Weighing'>
    # XXX: is date_time name consistent with other uses?
    definition = """
    -> Subject
    -> Appliance.WeighingScale
    weighing_id:    		char(32)		# weighing id
    ---
    -> User
    date_time:			datetime		# date time
    weight:			float			# weight
    json:			varchar(255)		# json
    """


@schema
class WaterAdministration(dj.Manual):
    # <class 'actions.models.WaterAdministration'>
    # TODO: hydrogel=NULL default, nullable boolean
    definition = """
    -> User
    -> Subject
    water_administration_id:	char(32)		# water admin. id
    ---
    date_time:			datetime		# date time
    water_administered:		float			# water administered
    hydrogel:			boolean			# hydrogel
    json:			varchar(255)		# json
    """


@schema
class BaseAction(dj.Manual):
    # <class 'actions.models.BaseAction'>
    definition = """
    -> Subject
    -> LabLocation
    action_id:			char(32)	# action id
    ---
    narrative:			varchar(255)	# narrative
    start_time:			datetime	# start time
    end_time:			datetime	# end time
    json:			varchar(255)	# json
    """

    class ActionUser(dj.Part):
        definition = """
        -> BaseAction
        -> User
        """

    class ActionProcedure(dj.Part):
        definition = """
        -> BaseAction
        -> ProcedureType
        """


@schema
class VirusInjection(dj.Manual):
    # <class 'actions.models.VirusInjection'>
    definition = """
    -> BaseAction
    ---
    -> VirusBatch
    injection_volume:		float		# injection volume
    rate_of_injection:		float		# rate of injection
    injection_type:		varchar(255)	# injection type
    """


@schema
class Surgery(dj.Manual):
    # <class 'actions.models.Surgery'>
    # XXX: isa BaseAction
    definition = """
    -> BaseAction
    -> BrainLocation
    ---
    outcome_type:		varchar(255)	# outcome type
    json:			varchar(255)	# json
    """


@schema
class Session(dj.Manual):
    # <class 'actions.models.Session'>
    # XXX: isa BaseAction
    definition = """
    -> BaseAction
    ---
    type:			varchar(255)	# type
    number:			integer		# number
    """


@schema
class WaterRestriction(dj.Manual):
    # <class 'actions.models.WaterRestriction'>
    # XXX: isa BaseAction
    definition = """
    -> BaseAction
    """

@schema
class OtherAction(dj.Manual):
    # <class 'actions.models.OtherAction'>
    # XXX: isa BaseAction
    definition = """
    -> BaseAction
    """


# #####################################################################
# acquisition.py ######################################################
# #####################################################################
'''
class deps/inheretance notes from Alyx.data.models
- BaseExperimenalData
  - Dataset
  - DataCollection
    - TimeSeries (DataCollection + timescale & timestamps)
    - EventSeries (DataCollection + timescale & timestamp id)
  - IntervalSeries (DataCollection + timescale & timestamp id)
# examples of subclasses from other Alyx modules:
  - OptogeneticStimulus -> Dataset
  - ExtracellularRecording -> {DataCollection, Timescale, TimeSeries}

Method (for now): modeling DataCollection, etc directly -
and client tables will refer here - not a very natively dj construction,
but somewhat preserves upstream notions of provenance, etc.
and preserves notion that reference.Note should apply to objects,
even if it doesn't apply to datajoint direcly.

TODO: Narrowing of relations to make keys fit?
 ... or alternate approach overall..
'''


@schema
class DataRepositoryType(dj.Lookup):
    # <class 'data.models.DataRepositoryType'>
    # TODO: Some default values please?
    # XXX: repository_type is referred elsewhere - attribute name ok?
    definition = """
    repository_type:		varchar(255)		# name
    ---
    json:			varchar(255)		# json
    """


@schema
class DataRepository(dj.Manual):
    # <class 'data.models.DataRepository'>
    definition = """
    -> DataRepositoryType
    data_repository_name:	varchar(255)		# data repository name
    ---
    path:			varchar(255)		# path
    json:			varchar(255)		# json
    """


@schema
class DatasetType(dj.Lookup):
    # <class 'data.models.DatasetType'>
    definition = """
    dataset_type_name:		varchar(255)		# name
    ---
    json:			varchar(255)		# json
    """


@schema
class DataDescription(dj.Manual):
    # <class 'data.models.BaseExperimentalData> # Abstract
    definition = """
    -> Session
    -> User
    datadescription_id:		char(32)		# data id
    created:			datetime		# created
    generating_software:	varchar(255)		# generating software
    provenance_directory:	varchar(255)		# provenance directory
    """


@schema
class Dataset(dj.Manual):
    # <class 'data.models.Dataset'>
    definition = """
    -> DataDescription
    ---
    -> DatasetType
    name:			varchar(255)		# name
    md5:			char(32)		# md5
    json:			varchar(255)		# json
    """

    class FileRecord(dj.Part):
        # <class 'data.models.FileRecord'>
        # ''' "Normally specified by a path within an archive" '''
        definition = """
        -> Dataset
        file_record_id:		char(32)		# dataset id
        ---
        -> DataRepository
        relative_path:		varchar(255)		# relative path
        json:			varchar(255)		# json
        """


@schema
class DataCollection(dj.Manual):
    # <class 'data.models.DataCollection'>
    definition = """
    -> DataDescription
    """

    class DataMember(dj.Part):
        definition = """
        -> DataCollection
        -> Dataset
        """


@schema
class Timescale(dj.Manual):
    # <class 'data.models.Timescale'>
    # original spec makes session mandatory and series/experiment optional
    definition = """
    timescale_id:		char(32)		# id
    ---
    timescale_name:		varchar(255)		# name
    nominal_start:		datetime		# nominal start
    nominal_time_unit:		float			# nominal time unit
    final:			boolean			# final
    info:			varchar(255)		# info
    json:			varchar(255)		# json
    """


@schema
class TimeSeries(dj.Manual):
    # <class 'data.models.TimeSeries'>
    definition = """
    -> DataDescription
    -> Timescale
    -> Dataset						# timestamps
    """


@schema
class EventSeries(dj.Manual):
    # <class 'data.models.EventSeries'>
    definition = """
    -> DataDescription
    -> Timescale
    -> Dataset						# event times
    """


@schema
class IntervalSeries(dj.Manual):
    # <class 'data.models.IntervalSeries'>
    definition = """
    -> DataDescription
    -> Timescale
    -> Dataset						# intervals
    """


# #####################################################################
# behavior.py #########################################################
# #####################################################################

# Note:
# skipped:
#   <class 'behavior.models.EventSeries'>
#   <class 'behavior.models.IntervalSeries'>
# since these appear to be duplicatedd w.r.t data.models.* copy.


@schema
class PupilTracking(dj.Manual):
    # <class 'behavior.models.PupilTracking'>
    definition = """
    -> DataDescription
    pupil_tracking_id:		char(32)		# id
    ---
    (x_y_d)			-> TimeSeries		# x y data
    (movie)			-> TimeSeries		# movie
    eye:			varchar(255)		# eye
    description:		varchar(255)		# description
    json:			varchar(255)		# json
    """


@schema
class HeadTracking(dj.Manual):
    # <class 'behavior.models.HeadTracking'>
    definition = """
    -> DataDescription
    head_tracking_id:		char(32)		# id
    ---
    (x_y_theta)			-> TimeSeries		# x y theta
    (movie)			-> TimeSeries		# movie
    description:		varchar(255)		# description
    json:			varchar(255)		# json
    """


@schema
class OptogeneticStimulus(dj.Manual):
    # <class 'behavior.models.OptogeneticStimulus'>
    definition = """
    -> DataDescription
    -> BrainLocation
    ---
    description:		varchar(255)	# description
    -> Appliance
    light_delivery:		varchar(255)	# light delivery
    wavelength:    		float		# wavelength
    power_calculation_method:	varchar(255)	# power calculation method
    json:			varchar(255)	# json
    """

    class Time(dj.Part):
        definition = """
        -> OptogeneticStimulus
        -> Dataset				# times
        """

    class Position(dj.Part):
        definition = """
        -> OptogeneticStimulus
        -> Dataset				# positions
        """

    class Power(dj.Part):
        definition = """
        -> OptogeneticStimulus
        -> Dataset				# stimulus power
        """


@schema
class Pharmacology(dj.Manual):
    # <class 'behavior.models.Pharmacology'>
    definition = """
    -> DataDescription
    pharmacology_id:		char(32)	# pharmacology id
    ---
    drug:			varchar(255)	# drug
    administration_route:	varchar(255)	# administration route
    start_time:			float		# start time
    end_time:			float		# end time
    concentration:		varchar(255)	# concentration
    volume:			varchar(255)	# volume
    json:			varchar(255)	# json
    """


# #####################################################################
# ephys.py ############################################################
# #####################################################################

@schema
class ExtracellularRecording(dj.Manual):
    # <class 'electrophysiology.models.ExtracellularRecording'>
    # isa timeseries
    # todo: RECORDING_TYPES
    definition = """
    -> TimeSeries
    ---
    filter_info:		varchar(255)		# filter information
    ground_electrode:		varchar(255)		# ground electrode
    reference_electrode:	varchar(255)		# reference electrode
    -> Appliance.Amplifier
    -> Appliance.DAQ
    json:			varchar(255)		# json
    """

    class LFP(dj.Part):
        definition = """
        -> ExtracellularRecording
        -> TimeSeries
        """

    class Impedances(dj.Part):
        definition = """
        -> ExtracellularRecording
        -> TimeSeries
        """

    class Gains(dj.Part):
        definition = """
        -> ExtracellularRecording
        -> TimeSeries
        """


@schema
class ProbeModel(dj.Manual):
    # <class 'electrophysiology.models.ProbeModel'>
    definition = """
    -> Supplier
    ---
    probe_model:		varchar(255)		# probe model
    description:		varchar(255)		# description
    json:			varchar(255)		# json
    """

    class SitePositions(dj.Part):
        definition = """
        -> ProbeModel
        ---
        -> Dataset
        """


@schema
class ProbeInsertion(dj.Manual):
    # <class 'electrophysiology.models.ProbeInsertion'>
    definition = """
    -> ExtracellularRecording
    -> ProbeModel
    ---
    entry_point_rl:		float			# entry point rl
    entry_point_ap:		float			# entry point ap
    vertical_angle:		float			# vertical angle
    horizontal_angle:		float			# horizontal angle
    distance_advanced:		float			# distance advanced
    axial_angle:		float			# axial angle
    json:			varchar(255)		# json
    """

    class ChannelMapping(dj.Part):
        definition = """
        -> ProbeInsertion
        ---
        -> Dataset
        """


@schema
class BaseBrainLocation(dj.Manual):
    # <class 'electrophysiology.models.BaseBrainLocation'>
    definition = """
    ccf_ap:			float			# ccf ap
    ccf_dv:			float			# ccf dv
    ccf_lr:			float			# ccf lr
    ---
    allen_ontology:		varchar(255)		# allen ontology
    json:			varchar(255)		# json
    """


@schema
class RecordingSite(dj.Manual):
    # <class 'electrophysiology.models.RecordingSite'>
    definition = """
    -> BaseBrainLocation
    -> ProbeInsertion
    ---
    allen_ontology:		varchar(255)		# allen ontology
    site_no:			integer			# site no
    json:			varchar(255)		# json
    """


@schema
class SpikeSorting(dj.Manual):
    # <class 'electrophysiology.models.SpikeSorting'>
    # isa: EventSeries
    definition = """
    -> EventSeries
    ---
    json:    varchar(255) # json
    """

    class Recording(dj.Part):
        definition = """
        -> SpikeSorting
        ---
        -> ExtracellularRecording
        """

    class Probe(dj.Part):
        definition = """
        -> SpikeSorting
        ---
        -> ExtracellularRecording
        """


@schema
class SpikeSortedUnit(dj.Manual):
    # <class 'electrophysiology.models.SpikeSortedUnit'>
    # TODO: CLUSTER_GROUPS
    # TODO: WIDTH_CLASSES
    definition = """
    -> BaseBrainLocation
    -> SpikeSorting
    cluster_number:		integer		# cluster number
    ---
    channel_group:		integer		# channel group
    trough_to_peak_width:	float		# trough to peak width
    half_width:			float		# half width
    trough_to_peak_amplitude:	float		# trough to peak amplitude
    refractory_violation_rate:	float		# refractory violation rate
    isolation_distance:		float		# isolation distance
    l_ratio:			float		# l ratio
    mean_firing_rate:		float		# mean firing rate
    cluster_group:		varchar(255)	# cluster group
    spike_width_class:		varchar(255)	# spike width class
    optogenetic_response:	varchar(255)	# optogenetic response
    putative_cell_type:		varchar(255)	# putative cell type
    """


@schema
class IntracellularRecording(dj.Manual):
    # <class 'electrophysiology.models.IntracellularRecording'>
    # TODO: ELECTRODE_TYPES
    definition = """
    -> DataDescription
    -> BrainLocation
    -> Dataset
    ---
    electrode_type:		varchar(255)	# electrode type
    -> Appliance.PipettePuller			# pipette puller
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
    json:			varchar(255)	# json
    """

    class Current(dj.Part):
        definition = """
        -> IntracellularRecording
        ---
        -> Dataset
        """

    class Voltage(dj.Part):
        definition = """
        -> IntracellularRecording
        ---
        -> Dataset
        """


# #####################################################################
# imaging.py ##########################################################
# #####################################################################

@schema
class SVDCompressedMovie(dj.Manual):
    # <class 'imaging.models.SVDCompressedMovie'>
    definition = """
    -> DataDescription
    ---
    json:			varchar(255)	# json
    """

    class DataU(dj.Part):
        definition = """
        -> SVDCompressedMovie
        ---
        -> Dataset
        """

    class DataV(dj.Part):
        definition = """
        -> SVDCompressedMovie
        ---
        -> TimeSeries
        """


@schema
class WidefieldImaging(dj.Manual):
    # <class 'imaging.models.WidefieldImaging'>
    definition = """
    -> DataDescription
    ---
    start_time:			datetime	# nominal start time
    end_time:			datetime	# nominal end time
    imaging_indicator:		varchar(255)	# imaging indicator
    preprocessing:		varchar(255)	# preprocessing
    description:		varchar(255)	# description
    excitation_wavelength:	float		# excitation nominal wavelength
    recording_wavelength:	float		# recording nominal wavelength
    recording_device:		varchar(255)	# recording device
    json:			varchar(255)	# json
    """

    class Raw(dj.Part):
        definition = """
        -> WidefieldImaging
        ---
        -> TimeSeries
        """

    class Compressed(dj.Part):
        definition = """
        -> WidefieldImaging
        ---
        -> SVDCompressedMovie
        """


@schema
class TwoPhotonImaging(dj.Manual):
    # <class 'imaging.models.TwoPhotonImaging'>
    definition = """
    -> DataDescription
    ---
    description:                varchar(255)    # description
    json:			varchar(255)	# json
    (image_position)                            -> CoordinateTransformation
    excitation_wavelength:      float           # excitation wavelength
    recording_wavelength:       float           # recording wavelength
    """

    class Raw(dj.Part):
        definition = """
        -> TwoPhotonImaging
        ---
        -> TimeSeries
        """

    class Compressed(dj.Part):
        definition = """
        -> TwoPhotonImaging
        ---
        -> SVDCompressedMovie
        """


@schema
class ROIDetection(dj.Manual):
    # <class 'imaging.models.ROIDetection'>
    definition = """
    -> DataDescription
    ---
    preprocessing:              varchar(255)            # preprocessing
    json:                       varchar(255)            # json
    """

    class TwoPhoton(dj.Part):
        definition = """
        -> ROIDetection
        ---
        -> TwoPhotonImaging
        """

    class RawFluorescence(dj.Part):
        definition = """
        -> ROIDetection
        ---
        -> TimeSeries
        """

    class RestingFluorescencea(dj.Part):
        definition = """
        -> ROIDetection
        ---
        -> TimeSeries
        """

    class Masks(dj.Part):
        definition = """
        -> ROIDetection
        ---
        -> Dataset
        """

    class Plane(dj.Part):
        definition = """
        -> ROIDetection
        ---
        -> Dataset
        """


@schema
class ROI(dj.Manual):
    # <class 'imaging.models.ROI'>
    definition = """
    -> DataDescription
    ---
    roi_type:			varchar(255)    # roi type
    optogenetic_response:       varchar(255)    # optogenetic response
    putative_cell_type:         varchar(255)    # putative cell type
    estimated_layer:            varchar(255)    # estimated layer
    -> ROIDetection
    json:                       varchar(255)    # json
    """
