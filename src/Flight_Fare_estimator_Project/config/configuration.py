from src.Flight_Fare_estimator_Project.constants import *
from src.Flight_Fare_estimator_Project.utils.common import read_yaml, create_directories
from src.Flight_Fare_estimator_Project.entity.config_entity import DataIngestionConfig
from src.Flight_Fare_estimator_Project.entity.config_entity import DatapreprocessConfig
from src.Flight_Fare_estimator_Project.entity.config_entity import DataTransformationConfig
from src.Flight_Fare_estimator_Project.entity.config_entity import DataModellingConfig




class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
        

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    

    def get_datapreprocessing_config(self) -> DatapreprocessConfig:
        config = self.config.data_preprocessing

        create_directories([config.root_dir])

        datapreprocess_config = DatapreprocessConfig(
            root_dir=config.root_dir,
            datapath=config.datapath
        )

        return datapreprocess_config
    

    def get_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        datatransformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            datapath=config.datapath
        )

        return datatransformation_config
    

    def get_modelling_config(self) -> DataModellingConfig:
        config = self.config.data_modelling
        params= self.params.xgboost_params

        create_directories([config.root_dir])

        datamodelling_config = DataModellingConfig(
            root_dir=config.root_dir,
            x_datapath=config.x_datapath,
            y_datapath=config.y_datapath,
            max_depth=params.max_depth,
            max_features=params.max_features,
            min_samples_leaf=params.min_samples_leaf,
            min_samples_split=params.min_samples_split,
            n_estimators=params.n_estimators
        )

        return datamodelling_config
