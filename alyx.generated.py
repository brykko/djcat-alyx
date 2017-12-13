
# initial auto-translated alyx schema

# traversal complete. processing.
# nmods: 64
# nrels: 199
# nselr: 195

@schema
class Species(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    binomial:    varchar(255) # binomial
    display_name:    varchar(255) # display name
    """

@schema
class Strain(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    descriptive_name:    varchar(255) # descriptive name
    description:    varchar(255) # description
    """

@schema
class Line(dj.Manual):
    definition="""
    -> Strain
    -> Species
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    description:    varchar(255) # description
    target_phenotype:    varchar(255) # target phenotype
    auto_name:    varchar(255) # auto name
    subject_autoname_index:    integer # subject autoname index
    breeding_pair_autoname_index:    integer # breeding pair autoname index
    litter_autoname_index:    integer # litter autoname index
    is_active:    boolean # is active
    sequences:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # sequences
    """

@schema
class BreedingPair(dj.Manual):
    definition="""
    -> Line
    -> Subject
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    start_date:    date # start date
    end_date:    date # end date
    description:    varchar(255) # description
    """

@schema
class Litter(dj.Manual):
    definition="""
    -> Line
    -> BreedingPair
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    descriptive_name:    varchar(255) # descriptive name
    description:    varchar(255) # description
    birth_date:    date # birth date
    """

@schema
class Source(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    description:    varchar(255) # description
    """

@schema
class OrderedUser(dj.Manual):
    definition="""
    id:    type_unknown <class 'django.db.models.fields.AutoField'> # ID
    ---
    password:    varchar(255) # password
    last_login:    datetime # last login
    is_superuser:    boolean # superuser status
    username:    varchar(255) # username
    first_name:    varchar(255) # first name
    last_name:    varchar(255) # last name
    email:    varchar(255) # email address
    is_staff:    boolean # staff status
    is_active:    boolean # active
    date_joined:    datetime # date joined
    groups:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # groups
    user_permissions:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # user permissions
    """

@schema
class SubjectRequest(dj.Manual):
    definition="""
    -> OrderedUser
    -> Line
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    count:    integer # count
    date_time:    date # date time
    due_date:    date # due date
    description:    varchar(255) # description
    """

@schema
class Subject(dj.Manual):
    definition="""
    -> Species
    -> Litter
    -> Strain
    -> Source
    -> Line
    -> OrderedUser
    -> SubjectRequest
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    nickname:    varchar(255) # nickname
    sex:    varchar(255) # sex
    birth_date:    date # birth date
    death_date:    date # death date
    wean_date:    date # wean date
    genotype_date:    date # genotype date
    lamis_cage:    integer # lamis cage
    implant_weight:    float # implant weight
    ear_mark:    varchar(255) # ear mark
    protocol_number:    varchar(255) # protocol number
    description:    varchar(255) # description
    cull_method:    varchar(255) # cull method
    adverse_effects:    varchar(255) # adverse effects
    actual_severity:    integer # actual severity
    to_be_genotyped:    boolean # to be genotyped
    to_be_culled:    boolean # to be culled
    reduced:    boolean # reduced
    reduced_date:    date # reduced date
    genotype:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # genotype
    genotype_test:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # genotype test
    """

@schema
class User(dj.Manual):
    definition="""
    id:    type_unknown <class 'django.db.models.fields.AutoField'> # ID
    ---
    password:    varchar(255) # password
    last_login:    datetime # last login
    is_superuser:    boolean # superuser status
    username:    varchar(255) # username
    first_name:    varchar(255) # first name
    last_name:    varchar(255) # last name
    email:    varchar(255) # email address
    is_staff:    boolean # staff status
    is_active:    boolean # active
    date_joined:    datetime # date joined
    groups:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # groups
    user_permissions:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # user permissions
    """

@schema
class Allele(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    standard_name:    varchar(255) # standard name
    informal_name:    varchar(255) # informal name
    """

@schema
class Zygosity(dj.Manual):
    definition="""
    -> Subject
    -> Allele
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    zygosity:    integer # zygosity
    """

@schema
class Sequence(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    base_pairs:    varchar(255) # base pairs
    description:    varchar(255) # description
    informal_name:    varchar(255) # informal name
    """

@schema
class GenotypeTest(dj.Manual):
    definition="""
    -> Subject
    -> Sequence
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    test_result:    integer # test result
    """

@schema
class LabLocation(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    """

@schema
class ContentType(dj.Manual):
    definition="""
    id:    type_unknown <class 'django.db.models.fields.AutoField'> # ID
    ---
    app_label:    varchar(255) # app label
    model:    varchar(255) # python model class name
    """

@schema
class EquipmentModel(dj.Manual):
    definition="""
    -> Supplier
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    model_name:    varchar(255) # model name
    description:    varchar(255) # description
    """

@schema
class VirusBatch(dj.Manual):
    definition="""
    -> Supplier
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    virus_type:    varchar(255) # virus type
    description:    varchar(255) # description
    date_time_made:    datetime # date time made
    nominal_titer:    float # nominal titer
    """

@schema
class Appliance(dj.Manual):
    definition="""
    -> ContentType
    -> LabLocation
    -> EquipmentModel
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    serial:    varchar(255) # serial
    description:    varchar(255) # description
    descriptive_name:    varchar(255) # descriptive name
    """

@schema
class WeighingScale(dj.Manual):
    definition="""
    -> ContentType
    -> LabLocation
    -> EquipmentModel
    -> Appliance
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    serial:    varchar(255) # serial
    description:    varchar(255) # description
    descriptive_name:    varchar(255) # descriptive name
    """

@schema
class LightSource(dj.Manual):
    definition="""
    -> ContentType
    -> LabLocation
    -> EquipmentModel
    -> Appliance
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    serial:    varchar(255) # serial
    description:    varchar(255) # description
    descriptive_name:    varchar(255) # descriptive name
    """

@schema
class Amplifier(dj.Manual):
    definition="""
    -> ContentType
    -> LabLocation
    -> EquipmentModel
    -> Appliance
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    serial:    varchar(255) # serial
    description:    varchar(255) # description
    descriptive_name:    varchar(255) # descriptive name
    """

@schema
class PipettePuller(dj.Manual):
    definition="""
    -> ContentType
    -> LabLocation
    -> EquipmentModel
    -> Appliance
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    serial:    varchar(255) # serial
    description:    varchar(255) # description
    descriptive_name:    varchar(255) # descriptive name
    """

@schema
class DAQ(dj.Manual):
    definition="""
    -> ContentType
    -> LabLocation
    -> EquipmentModel
    -> Appliance
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    serial:    varchar(255) # serial
    description:    varchar(255) # description
    descriptive_name:    varchar(255) # descriptive name
    """

@schema
class ProcedureType(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    description:    varchar(255) # description
    """

@schema
class Weighing(dj.Manual):
    definition="""
    -> OrderedUser
    -> Subject
    -> WeighingScale
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    date_time:    datetime # date time
    weight:    float # weight
    """

@schema
class WaterAdministration(dj.Manual):
    definition="""
    -> OrderedUser
    -> Subject
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    date_time:    datetime # date time
    water_administered:    float # water administered
    hydrogel:    boolean=NULL # hydrogel
    """

@schema
class VirusInjection(dj.Manual):
    definition="""
    -> Subject
    -> LabLocation
    -> VirusBatch
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    narrative:    varchar(255) # narrative
    start_time:    datetime # start time
    end_time:    datetime # end time
    injection_volume:    float # injection volume
    rate_of_injection:    float # rate of injection
    injection_type:    varchar(255) # injection type
    users:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # users
    procedures:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # procedures
    """

@schema
class BrainLocation(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    stereotaxic_coordinates:    longblob # stereotaxic coordinates
    description:    varchar(255) # description
    allen_location_ontology:    varchar(255) # allen location ontology
    """

@schema
class Surgery(dj.Manual):
    definition="""
    -> Subject
    -> BrainLocation
    -> LabLocation
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    narrative:    varchar(255) # narrative
    start_time:    datetime # start time
    end_time:    datetime # end time
    outcome_type:    varchar(255) # outcome type
    users:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # users
    procedures:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # procedures
    """

@schema
class Session(dj.Manual):
    definition="""
    -> Subject
    -> LabLocation
    -> Session
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    narrative:    varchar(255) # narrative
    start_time:    datetime # start time
    end_time:    datetime # end time
    type:    varchar(255) # type
    number:    integer # number
    users:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # users
    procedures:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # procedures
    """

@schema
class WaterRestriction(dj.Manual):
    definition="""
    -> Subject
    -> LabLocation
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    narrative:    varchar(255) # narrative
    start_time:    datetime # start time
    end_time:    datetime # end time
    users:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # users
    procedures:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # procedures
    """

@schema
class OtherAction(dj.Manual):
    definition="""
    -> Subject
    -> LabLocation
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    narrative:    varchar(255) # narrative
    start_time:    datetime # start time
    end_time:    datetime # end time
    users:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # users
    procedures:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # procedures
    """

@schema
class DataRepositoryType(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    """

@schema
class DataRepository(dj.Manual):
    definition="""
    -> DataRepositoryType
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    path:    varchar(255) # path
    """

@schema
class DatasetType(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    """

@schema
class Dataset(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> DatasetType
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    name:    varchar(255) # name
    md5:    char(32) # md5
    """

@schema
class FileRecord(dj.Manual):
    definition="""
    -> Dataset
    -> DataRepository
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    relative_path:    varchar(255) # relative path
    """

@schema
class DataCollection(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    name:    varchar(255) # name
    data:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # data
    """

@schema
class Timescale(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    nominal_start:    datetime # nominal start
    nominal_time_unit:    float # nominal time unit
    final:    boolean # final
    info:    varchar(255) # info
    """

@schema
class TimeSeries(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> DataCollection
    -> Timescale
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    name:    varchar(255) # name
    data:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # data
    """

@schema
class EventSeries(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> DataCollection
    -> Timescale
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    name:    varchar(255) # name
    data:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # data
    """

@schema
class IntervalSeries(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> Timescale
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    """

@schema
class Note(dj.Manual):
    definition="""
    -> OrderedUser
    -> ContentType
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    date_time:    datetime # date time
    text:    varchar(255) # text
    object_id:    char(32) # object id
    """

@schema
class CoordinateTransformation(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    description:    varchar(255) # description
    allen_location_ontology:    varchar(255) # allen location ontology
    origin:    longblob # origin
    transformation_matrix:    longblob # transformation matrix
    """

@schema
class PupilTracking(dj.Manual):
    definition="""
    -> Session
    -> User
    -> TimeSeries
    -> Dataset
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    eye:    varchar(255) # eye
    description:    varchar(255) # description
    generating_software:    varchar(255) # generating software
    """

@schema
class HeadTracking(dj.Manual):
    definition="""
    -> Session
    -> User
    -> TimeSeries
    -> Dataset
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    description:    varchar(255) # description
    generating_software:    varchar(255) # generating software
    """

@schema
class EventSeries(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    description:    varchar(255) # description
    generating_software:    varchar(255) # generating software
    """

@schema
class IntervalSeries(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    description:    varchar(255) # description
    generating_software:    varchar(255) # generating software
    """

@schema
class OptogeneticStimulus(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> Appliance
    -> BrainLocation
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    light_delivery:    varchar(255) # light delivery
    description:    varchar(255) # description
    wavelength:    float # wavelength
    power_calculation_method:    varchar(255) # power calculation method
    """

@schema
class Pharmacology(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    drug:    varchar(255) # drug
    administration_route:    varchar(255) # administration route
    start_time:    float # start time
    end_time:    float # end time
    concentration:    varchar(255) # concentration
    volume:    varchar(255) # volume
    """

@schema
class ExtracellularRecording(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> DataCollection
    -> Timescale
    -> TimeSeries
    -> Amplifier
    -> DAQ
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    name:    varchar(255) # name
    data:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # data
    filter_info:    varchar(255) # filter info
    recording_type:    varchar(255) # recording type
    ground_electrode:    varchar(255) # ground electrode
    reference_electrode:    varchar(255) # reference electrode
    """

@schema
class ProbeModel(dj.Manual):
    definition="""
    -> Supplier
    -> Dataset
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    probe_model:    varchar(255) # probe model
    description:    varchar(255) # description
    """

@schema
class ProbeInsertion(dj.Manual):
    definition="""
    -> ExtracellularRecording
    -> ProbeModel
    -> Dataset
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    entry_point_rl:    float # entry point rl
    entry_point_ap:    float # entry point ap
    vertical_angle:    float # vertical angle
    horizontal_angle:    float # horizontal angle
    axial_angle:    float # axial angle
    distance_advanced:    float # distance advanced
    """

@schema
class BaseBrainLocation(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    ccf_ap:    float # ccf ap
    ccf_dv:    float # ccf dv
    ccf_lr:    float # ccf lr
    allen_ontology:    varchar(255) # allen ontology
    """

@schema
class RecordingSite(dj.Manual):
    definition="""
    -> BaseBrainLocation
    -> ProbeInsertion
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    ccf_ap:    float # ccf ap
    ccf_dv:    float # ccf dv
    ccf_lr:    float # ccf lr
    allen_ontology:    varchar(255) # allen ontology
    site_no:    integer # site no
    """

@schema
class SpikeSorting(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> DataCollection
    -> Timescale
    -> EventSeries
    -> ExtracellularRecording
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    name:    varchar(255) # name
    data:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # data
    """

@schema
class SpikeSortedUnit(dj.Manual):
    definition="""
    -> BaseBrainLocation
    -> SpikeSorting
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    ccf_ap:    float # ccf ap
    ccf_dv:    float # ccf dv
    ccf_lr:    float # ccf lr
    allen_ontology:    varchar(255) # allen ontology
    cluster_number:    integer # cluster number
    channel_group:    integer # channel group
    trough_to_peak_width:    float # trough to peak width
    half_width:    float # half width
    trough_to_peak_amplitude:    float # trough to peak amplitude
    refractory_violation_rate:    float # refractory violation rate
    isolation_distance:    float # isolation distance
    l_ratio:    float # l ratio
    mean_firing_rate:    float # mean firing rate
    cluster_group:    varchar(255) # cluster group
    spike_width_class:    varchar(255) # spike width class
    optogenetic_response:    varchar(255) # optogenetic response
    putative_cell_type:    varchar(255) # putative cell type
    """

@schema
class IntracellularRecording(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> BrainLocation
    -> PipettePuller
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    electrode_type:    varchar(255) # electrode type
    inner_diameter:    float # inner diameter
    outer_diameter:    float # outer diameter
    electrode_solution:    varchar(255) # electrode solution
    cp_fast:    float # cp fast
    cp_slow:    float # cp slow
    whole_cell_cap_comp:    float # whole cell cap comp
    whole_cell_series_resistance:    float # whole cell series resistance
    series_resistance_compensation_bandwidth:    float # series resistance compensation bandwidth
    series_resistance_compensation_correction:    float # series resistance compensation correction
    series_resistance_compensation_prediction:    float # series resistance compensation prediction
    pipette_cap_comp:    float # pipette cap comp
    bridge_balance:    float # bridge balance
    gain:    float # gain
    """

@schema
class SVDCompressedMovie(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> TimeSeries
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    """

@schema
class WidefieldImaging(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> TimeSeries
    -> SVDCompressedMovie
    -> CoordinateTransformation
    -> LightSource
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    nominal_start_time:    datetime # nominal start time
    nominal_end_time:    datetime # nominal end time
    imaging_indicator:    varchar(255) # imaging indicator
    preprocessing:    varchar(255) # preprocessing
    description:    varchar(255) # description
    excitation_nominal_wavelength:    float # excitation nominal wavelength
    recording_nominal_wavelength:    float # recording nominal wavelength
    recording_device:    varchar(255) # recording device
    """

@schema
class TwoPhotonImaging(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> TimeSeries
    -> SVDCompressedMovie
    -> CoordinateTransformation
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    description:    varchar(255) # description
    excitation_wavelength:    float # excitation wavelength
    recording_wavelength:    float # recording wavelength
    """

@schema
class ROIDetection(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> TimeSeries
    -> TwoPhotonImaging
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    preprocessing:    varchar(255) # preprocessing
    """

@schema
class ROI(dj.Manual):
    definition="""
    -> Session
    -> User
    -> Dataset
    -> ROIDetection
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    created_datetime:    datetime # created datetime
    generating_software:    varchar(255) # generating software
    roi_type:    varchar(255) # roi type
    optogenetic_response:    varchar(255) # optogenetic response
    putative_cell_type:    varchar(255) # putative cell type
    estimated_layer:    varchar(255) # estimated layer
    """


'''
external models (e.g library Models):
   <class 'django.contrib.auth.models.User'>
   <class 'django.contrib.contenttypes.models.ContentType'>
stack objs (not django Fields):
   <class 'subjects.models.StockManager'>
   <class 'equipment.models.Supplier'>
'''
