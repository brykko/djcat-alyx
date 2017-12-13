import datajoint as dj

import reference
import equipment
import acquisition

schema = dj.schema(dj.config['names.%s' % __name__], locals())


@schema
class SVDCompressedMovie(dj.Manual):
    '''
    Note:
    eigenframes: (nSVs*nY*nX)
    timecourses: (nSamples*nSVs)
    '''
    definition = """
    -> acquisition.Session
    svd_movie_id:               int             # svd movie id
    ---
    svd_create_date:            datetime        # create date
    eigenframes:                longblob        # svd eigenframes
    timecourses:                longblob        # svd timecourses
    """


@schema
class WidefieldImaging(dj.Manual):
    # <class 'imaging.models.WidefieldImaging'>
    # TODO: Reference Stack
    # TODO: rename imported fkeys; awaiting dj #300
    # TODO: nullable CoordinateTransformation
    # TODO: nullable SVDCompressedMovie
    # TODO: nullable LightSource
    definition = """
    -> acquisition.Session
    ---
    widefield_create_date:      datetime        # create date
    widefield_start_time:       datetime	# nominal start time
    widefield_end_time:         datetime	# nominal end time
    imaging_indicator:		varchar(255)	# imaging indicator
    preprocessing:		varchar(255)	# preprocessing
    description:		varchar(255)	# description
    excitation_wavelength:	float		# excitation nominal wavelength
    recording_wavelength:	float		# recording nominal wavelength
    recording_device:		varchar(255)	# recording device
    raw_frames:                 longblob        # n*w*h*c video
    -> reference.CoordinateTransformation
    -> SVDCompressedMovie
    -> equipment.LightSource
    """


@schema
class TwoPhotonImaging(dj.Manual):
    # <class 'imaging.models.TwoPhotonImaging'>
    # TODO: Reference Stack
    # TODO: rename imported fkeys; awaiting dj #300
    # TODO: nullable CoordinateTransformation
    # TODO: nullable SVDCompressedMovie
    definition = """
    -> acquisition.Session
    ---
    twop_create_date:           datetime        # create date
    twop_start_time:            datetime	# nominal start time
    twop_end_time:              datetime	# nominal end time
    description:		varchar(255)	# description
    excitation_wavelength:	float		# excitation nominal wavelength
    recording_wavelength:	float		# recording nominal wavelength
    raw_frames=NULL:            longblob        # n*w*h*c video
    -> reference.CoordinateTransformation
    -> SVDCompressedMovie
    """


@schema
class ROIDetection(dj.Computed):
    # <class 'imaging.models.TwoPhotonImaging'>
    definition = """
    -> acquisition.Session
    ---
    roi_create_date:            datetime        # create date
    roi_start_time:             datetime	# nominal start time
    roi_end_time:               datetime	# nominal end time
    preprocessing:		varchar(255)	# preprocessing
    """

    class ROI(dj.Part):
        # <class 'imaging.models.ROI'>
        definition = """
        -> ROIDetection
        roi_id:                 int             # ROI ID
        ---
        roi_type:               varchar(255)    # roi type
        optogenetic_response:   varchar(255)    # optogenetic response
        putative_cell_type:     varchar(255)    # putative cell type
        estimated_layer:        varchar(255)    # estimated layer
        -> TwoPhotonImaging
        raw_fluorescence:       longblob        # nTxNROI
        resting_fluorescence:   longblob        # nTxNROI
        masks:                  longblob        # (nYxnX) masks
        plane:                  integer         # discovery plane
        """
