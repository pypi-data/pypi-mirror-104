import astropy.units as u
from ruamel.yaml import YAML
from collections import namedtuple
import numpy as np
from sklearn.base import is_classifier, is_regressor
import logging

from sklearn import ensemble
from sklearn import linear_model
from sklearn import neighbors
from sklearn import svm
from sklearn import tree
from sklearn import naive_bayes

from .features import find_used_source_features


sklearn_modules = {
    "ensemble": ensemble,
    "linear_model": linear_model,
    "neighbors": neighbors,
    "svm": svm,
    "tree": tree,
    "naive_bayes": naive_bayes,
}


log = logging.getLogger(__name__)
yaml = YAML(typ="safe")


_feature_gen_config = namedtuple(
    "FeatureGenerationConfig",
    ["needed_columns", "features"],
)


class FeatureGenerationConfig(_feature_gen_config):
    """
    Stores the needed features and the expressions for the
    feature generation
    """

    def __new__(cls, needed_columns, features):
        if features is None:
            log.warning("Feature generation config present but no features defined.")
            features = {}
        return super().__new__(cls, needed_columns, features)


def print_models(filter_func=is_classifier):
    for name, module in sklearn_modules.items():
        for cls_name in dir(module):
            cls = getattr(module, cls_name)
            if filter_func(cls):
                logging.info(name + "." + cls.__name__)


def print_supported_classifiers():
    logging.info("Supported Classifiers:")
    print_models(is_classifier)


def print_supported_regressors():
    logging.info("Supported Regressors:")
    print_models(is_regressor)


def load_regressor(config):
    try:
        return eval(config, {}, sklearn_modules)
    except (NameError, AttributeError):
        log.error('Unsupported Regressor: "' + config + '"')
        print_supported_regressors()
        raise


def load_classifier(config):
    try:
        return eval(config, {}, sklearn_modules)
    except (NameError, AttributeError):
        log.error('Unsupported Regressor: "' + config + '"')
        print_supported_classifiers()
        raise


class AICTConfig:
    __slots__ = (
        "seed",
        "events_key",
        "disp",
        "dxdy",
        "energy",
        "separator",
        "data_format",
        "datamodel_version",
        "telescopes",
        "energy_unit",
        "true_energy_column",
        "size_column",
        "n_cross_validations",
        "coordinate_transformation",
        "source_az_column",
        "source_az_unit",
        "source_zd_column",
        "source_zd_unit",
        "source_alt_column",
        "source_alt_unit",
        "pointing_az_column",
        "pointing_az_unit",
        "pointing_zd_column",
        "pointing_zd_unit",
        "pointing_alt_column",
        "pointing_alt_unit",
        "focal_length_column",
        "focal_length_unit",
        "cog_x_column",
        "cog_y_column",
        "delta_column",
        "delta_unit",
        "data_format",
    )

    @classmethod
    def from_yaml(cls, configuration_path):
        with open(configuration_path) as f:
            return cls(yaml.load(f))

    def __init__(self, config):
        self.data_format = config.get("data_format", "simple")
        self.datamodel_version = config.get("datamodel_version", "v1.1.0")
        self.seed = config.get("seed", 0)
        self.n_cross_validations = config.get("n_cross_validations", 5)
        np.random.seed(self.seed)

        if self.data_format == "CTA":
            self.parse_cta(config)
        elif self.data_format == "simple":
            self.parse_simple(config)
        else:
            raise NotImplementedError(
                'Unsupported data format! Supported: "CTA", "simple"'
            )

        self.disp = self.energy = self.separator = None
        if "disp" in config:
            self.disp = DispConfig(config["disp"], self)

        if "dxdy" in config:
            self.dxdy = DxdyConfig(config["dxdy"], self)

        if "energy" in config:
            self.energy = EnergyConfig(config["energy"], self)

        if "separator" in config:
            self.separator = SeparatorConfig(config["separator"], self)

    def parse_cta(self, config):
        SIMPLE_OPTIONS = {
            "size_column",
            "energy_unit",
            "events_key",
            "true_energy_column",
            "coordinate_transformation",
            "source_az_column",
            "source_alt_column",
            "pointing_az_column",
            "pointing_alt_column",
            "source_az_unit",
            "source_alt_unit",
            "pointing_az_unit",
            "pointing_alt_unit",
            "focal_length_column",
            "focal_length_unit",
            "cog_x_column",
            "cog_y_column",
            "delta_column",
            "delta_unit",
            "focal_length_column",
            "focal_length_unit",
        }
        if SIMPLE_OPTIONS.intersection(config.keys()):
            raise TypeError(
                "You are trying to use configuration keys for the simple "
                'data format while setting the data_format to "CTA". '
                "There should be no reason to do this as the DL1-format is fixed"
            )

        self.coordinate_transformation = "CTA"
        self.source_az_column = "true_az"
        self.source_alt_column = "true_alt"
        self.source_zd_column = None
        self.pointing_az_column = "azimuth"
        self.pointing_alt_column = "altitude"
        self.pointing_zd_column = None
        self.focal_length_column = "equivalent_focal_length"
        # This is still speculation
        if config["datamodel_version"] > "1.1.0":
            self.cog_x_column = "hillas_fov_lon"
            self.cog_y_column = "hillas_fov_lat"
        else:
            self.cog_x_column = "hillas_x"
            self.cog_y_column = "hillas_y"
        self.delta_column = "hillas_psi"

        for coord in ("alt", "az", "zd"):
            col = f"source_{coord}_unit"
            setattr(self, col, u.deg)
            col = f"pointing_{coord}_unit"
            setattr(self, col, None)

        self.delta_unit = u.deg
        self.focal_length_unit = u.m
        self.telescopes = config.get("telescopes", None)
        self.true_energy_column = "true_energy"
        self.energy_unit = u.TeV
        self.size_column = "hillas_intensity"

    def parse_simple(self, config):
        if "telescopes" in config.keys():
            raise TypeError("Telescope selection is only possible for CTA data. ")
        self.size_column = config.get("size")
        self.energy_unit = u.Unit(config.get("energy_unit", "GeV"))
        self.true_energy_column = config.get("true_energy_column")
        self.events_key = config.get("events_key", "events")
        self.coordinate_transformation = config.get(
            "coordinate_transformation", "FACT"
        )
        self.source_az_column = config.get(
            "source_az_column", "source_position_az"
        )
        self.source_zd_column = config.get("source_zd_column")
        self.source_alt_column = config.get("source_alt_column")
        self.pointing_az_column = config.get(
            "pointing_az_column", "pointing_position_az"
        )
        self.pointing_zd_column = config.get("pointing_zd_column")
        self.pointing_alt_column = config.get("pointing_alt_column")
        self.focal_length_column = config.get(
            "focal_length_column", "focal_length"
        )
        self.focal_length_unit = u.Unit(config.get("focal_length", "m"))
        self.cog_x_column = config.get("cog_x_column", "cog_x")
        self.cog_y_column = config.get("cog_y_column", "cog_y")
        self.delta_column = config.get("delta_column", "delta")
        self.delta_unit = u.Unit(config.get("delta_unit", "rad"))
        for name in ("source", "pointing"):
            for coord in ("alt", "az", "zd"):
                col = f"{name}_{coord}_unit"
                setattr(self, col, u.Unit(config.get(col, "deg")))


def get_optional_training_columns(aict_config):
    cols = []
    for col in ("true_energy_column", "size_column"):
        value = getattr(aict_config, col, None)
        if value is not None:
            cols.append(value)
    return cols


def check_coordinate_columns_set(aict_config):
    if (aict_config.pointing_zd_column is None) is (aict_config.pointing_alt_column is None):
        raise ValueError(
            "Need to specify exactly one of"
            "pointing_zd_column or pointing_alt_column."
            "pointing_zd_column: {}, pointing_alt_column: {}".format(
                aict_config.pointing_zd_column, aict_config.pointing_alt_column
            )
        )
    if (aict_config.source_zd_column is None) is (aict_config.source_alt_column is None):
        raise ValueError(
            "Need to specify exactly one of "
            "'source_zd_column' or 'source_alt_column'. "
            "source_zd_column: {}, source_alt_column: {}".format(
                aict_config.source_zd_column, aict_config.source_alt_column
            )
        )


class DispConfig:
    __slots__ = [
        "disp_regressor",
        "sign_classifier",
        "n_cross_validations",
        "n_signal",
        "features",
        "feature_generation",
        "columns_to_read_apply",
        "columns_to_read_train",
        "log_target",
        "project_disp",
        "output_name",
    ]

    def __init__(self, model_config, aict_config):
        check_coordinate_columns_set(aict_config)

        self.output_name = model_config.get("output_name", "disp_predictions")
        self.disp_regressor = load_regressor(model_config["disp_regressor"])
        self.sign_classifier = load_classifier(model_config["sign_classifier"])
        self.project_disp = model_config.get("project_disp", False)
        self.log_target = model_config.get("log_target", False)

        self.n_signal = model_config.get("n_signal", None)
        k = "n_cross_validations"
        setattr(self, k, model_config.get(k, aict_config.n_cross_validations))

        self.features = model_config["features"].copy()

        gen_config = model_config.get("feature_generation")
        source_features = find_used_source_features(self.features, gen_config)
        if len(source_features):
            raise ValueError(
                "Source dependent features used: {}".format(source_features)
            )
        if gen_config:
            self.feature_generation = FeatureGenerationConfig(**gen_config)
            self.features.extend(self.feature_generation.features.keys())
        else:
            self.feature_generation = None
        self.features.sort()

        # Only used as group name for CTA Data
        if aict_config.data_format == "CTA":
            self.parse_cta(model_config, aict_config)
        elif aict_config.data_format == "simple":
            self.parse_simple(model_config, aict_config)
        else:
            raise NotImplementedError(
                'Unsupported data format! Supported: "CTA", "simple"'
            )

    def parse_cta(self, model_config, aict_config):

        cols = {
            aict_config.cog_x_column,
            aict_config.cog_y_column,
            aict_config.delta_column,
        }

        cols.update(model_config['features'])
        if self.feature_generation:
            cols.update(self.feature_generation.needed_columns)
        # Add id's because we generate new tables instead of adding columns
        # and want these to be included
        # focal_length is necessary for coordinate transformations
        cols.update(["tel_id", "event_id", "obs_id", "equivalent_focal_length"])
        self.columns_to_read_apply = list(cols)
        cols.update(
            {
                aict_config.pointing_az_column,
                aict_config.pointing_alt_column,
                aict_config.source_az_column,
                aict_config.source_alt_column,
            }
        )

        cols.update(get_optional_training_columns(aict_config))
        self.columns_to_read_train = list(cols)

    def parse_simple(self, model_config, aict_config):
        if "output_name" in model_config.keys():
            raise TypeError(
                "output_name in the disp config is exclusively used to name the "
                "prediction tables in CTA files. Is has no use using the "
                "simple data format"
            )
        cols = {
            aict_config.cog_x_column,
            aict_config.cog_y_column,
            aict_config.delta_column,
        }

        cols.update(model_config['features'])
        if self.feature_generation:
            cols.update(self.feature_generation.needed_columns)

        self.columns_to_read_apply = list(cols)
        cols.update(
            {
                aict_config.pointing_az_column,
                aict_config.pointing_zd_column,
                aict_config.pointing_alt_column,
                aict_config.source_az_column,
                aict_config.source_zd_column,
                aict_config.source_alt_column,
            }
        )
        cols.discard(None)
        if aict_config.coordinate_transformation == 'CTA':
            cols.add(aict_config.focal_length_column)
        cols.update(get_optional_training_columns(aict_config))
        self.columns_to_read_train = list(cols)


class DxdyConfig:
    __slots__ = [
        'dxdy_regressor',
        'n_cross_validations',
        'n_signal',
        'features',
        'feature_generation',
        'columns_to_read_apply',
        'columns_to_read_train',
        'output_name',
    ]

    def __init__(self, model_config, aict_config):
        check_coordinate_columns_set(aict_config)

        self.dxdy_regressor = load_regressor(model_config['dxdy_regressor'])

        self.n_signal = model_config.get("n_signal", None)
        k = "n_cross_validations"
        setattr(self, k, model_config.get(k, aict_config.n_cross_validations))

        self.features = model_config["features"].copy()

        gen_config = model_config.get("feature_generation")
        source_features = find_used_source_features(self.features, gen_config)
        if len(source_features):
            raise ValueError('Source dependent features used: {}'.format(source_features))
        if gen_config:
            self.feature_generation = FeatureGenerationConfig(**gen_config)
            self.features.extend(self.feature_generation.features.keys())
        else:
            self.feature_generation = None
        self.features.sort()

        # Only used as group name for CTA Data
        if aict_config.data_format == 'CTA':
            self.parse_cta(model_config, aict_config)
        elif aict_config.data_format == 'simple':
            self.parse_simple(model_config, aict_config)

    def parse_cta(self, model_config, aict_config):
        self.output_name = model_config.get('output_name', 'dxdy_prediction')

        cols = {
            aict_config.cog_x_column,
            aict_config.cog_y_column,
        }

        cols.update(model_config['features'])
        if self.feature_generation:
            cols.update(self.feature_generation.needed_columns)
        # Add id's because we generate new tables instead of adding columns
        # and want these to be included
        # focal_length is necessary for coordinate transformations
        cols.update(['tel_id', 'event_id', 'obs_id', 'equivalent_focal_length'])
        self.columns_to_read_apply = list(cols)
        cols.update({
            aict_config.pointing_az_column,
            aict_config.pointing_alt_column,
            aict_config.source_az_column,
            aict_config.source_alt_column,
        })

        cols.update(get_optional_training_columns(aict_config))
        self.columns_to_read_train = list(cols)

    def parse_simple(self, model_config, aict_config):
        if 'output_name' in model_config.keys():
            raise TypeError(
                'output_name in the disp config is exclusively used to name the '
                'prediction tables in CTA files. Is has no use using the '
                'simple data format'
            )
        cols = {
            aict_config.cog_x_column,
            aict_config.cog_y_column,
            aict_config.delta_column,
        }

        cols.update(model_config["features"])
        if self.feature_generation:
            cols.update(self.feature_generation.needed_columns)
        self.columns_to_read_apply = list(cols)
        cols.update({
            aict_config.pointing_az_column,
            aict_config.pointing_zd_column,
            aict_config.pointing_alt_column,
            aict_config.source_az_column,
            aict_config.source_zd_column,
            aict_config.source_alt_column,
        })
        cols.discard(None)
        if aict_config.coordinate_transformation == 'CTA':
            cols.add(aict_config.focal_length_column)

        cols.update(get_optional_training_columns(aict_config))
        self.columns_to_read_train = list(cols)


class EnergyConfig:
    __slots__ = [
        "model",
        "n_cross_validations",
        "n_signal",
        "features",
        "feature_generation",
        "columns_to_read_train",
        "columns_to_read_apply",
        "target_column",
        "output_name",
        "log_target",
    ]

    def __init__(self, model_config, aict_config):
        self.model = load_regressor(model_config["regressor"])
        self.features = model_config["features"].copy()

        self.n_signal = model_config.get("n_signal", None)
        k = "n_cross_validations"
        setattr(self, k, model_config.get(k, aict_config.n_cross_validations))

        if aict_config.data_format == "CTA":
            self.parse_cta(model_config, aict_config)
        elif aict_config.data_format == "simple":
            self.parse_simple(model_config, aict_config)
        else:
            raise NotImplementedError(
                'Unsupported data format! Supported: "CTA", "simple"'
            )

    def parse_cta(self, model_config, aict_config):
        if "target_column" in model_config.keys():
            raise TypeError("target_column is fixed for CTA dl1 files")

        self.target_column = "true_energy"
        self.output_name = model_config.get("output_name", "estimated_energy")
        self.log_target = model_config.get("log_target", True)

        gen_config = model_config.get("feature_generation")
        source_features = find_used_source_features(self.features, gen_config)
        if len(source_features):
            raise ValueError(
                "Source dependent features used: {}".format(source_features)
            )
        if gen_config:
            self.feature_generation = FeatureGenerationConfig(**gen_config)
            self.features.extend(self.feature_generation.features.keys())
        else:
            self.feature_generation = None
        self.features.sort()

        cols = set(model_config["features"])
        if self.feature_generation:
            cols.update(self.feature_generation.needed_columns)

        # Add id's because we generate new tables instead of adding columns
        # and want these to be included
        cols.update(["tel_id", "event_id", "obs_id"])
        self.columns_to_read_apply = list(cols)

        cols.update(get_optional_training_columns(aict_config))
        cols.add(self.target_column)
        self.columns_to_read_train = list(cols)

    def parse_simple(self, model_config, aict_config):
        self.target_column = model_config.get(
            "target_column", "corsika_event_header_total_energy"
        )
        self.output_name = model_config.get("output_name", "gamma_energy_prediction")
        self.log_target = model_config.get("log_target", True)

        gen_config = model_config.get("feature_generation")
        source_features = find_used_source_features(self.features, gen_config)
        if len(source_features):
            raise ValueError(
                "Source dependent features used: {}".format(source_features)
            )
        if gen_config:
            self.feature_generation = FeatureGenerationConfig(**gen_config)
            self.features.extend(self.feature_generation.features.keys())
        else:
            self.feature_generation = None
        self.features.sort()

        cols = set(model_config["features"])
        if self.feature_generation:
            cols.update(self.feature_generation.needed_columns)

        self.columns_to_read_apply = list(cols)

        cols.update(get_optional_training_columns(aict_config))
        cols.add(self.target_column)
        self.columns_to_read_train = list(cols)


class SeparatorConfig:
    __slots__ = [
        "model",
        "n_cross_validations",
        "n_signal",
        "n_background",
        "features",
        "feature_generation",
        "columns_to_read_train",
        "columns_to_read_apply",
        "calibrate_classifier",
        "output_name",
    ]

    def __init__(self, model_config, aict_config):
        self.model = load_classifier(model_config["classifier"])
        self.features = model_config["features"].copy()

        self.n_signal = model_config.get("n_signal", None)
        self.n_background = model_config.get("n_background", None)
        k = "n_cross_validations"
        setattr(self, k, model_config.get(k, aict_config.n_cross_validations))
        self.calibrate_classifier = model_config.get("calibrate_classifier", False)
        self.output_name = model_config.get("output_name", "gamma_prediction")

        gen_config = model_config.get("feature_generation")
        source_features = find_used_source_features(self.features, gen_config)
        if len(source_features):
            raise ValueError(
                "Source dependent features used: {}".format(source_features)
            )
        if gen_config:
            self.feature_generation = FeatureGenerationConfig(**gen_config)
            self.features.extend(self.feature_generation.features.keys())
        else:
            self.feature_generation = None
        self.features.sort()

        cols = set(model_config["features"])
        if self.feature_generation:
            cols.update(self.feature_generation.needed_columns)

        # Add id's because we generate new tables instead of adding columns
        # and want these to be included
        if aict_config.data_format == "CTA":
            cols.update(["tel_id", "event_id", "obs_id"])

        self.columns_to_read_apply = list(cols)
        cols.update(get_optional_training_columns(aict_config))
        self.columns_to_read_train = list(cols)
