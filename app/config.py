import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    HOST = "localhost"
    PORT = "5000"
    DEBUG = True
    SECRET_KEY = "039e3cea804ae6c10a53ab3a4b7ae4c9"
    CACHE_HOST = "localhost"
    CACHE_PORT = "6379"

    ENABLE_AUTH = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"


class StageConfig(BaseConfig):
    CONFIG_NAME = "stage"
    HOST = "0.0.0.0"
    PORT = "5005"

    CACHE_HOST = "crm_user_info_cache"
    CACHE_PORT = "6300"


class ProdConfig(BaseConfig):
    CONFIG_NAME = 'prod'
    HOST = "0.0.0.0"
    PORT = "5005"

    CACHE_HOST = "crm_user_info_cache"
    CACHE_PORT = "6300"

    CRM_REDIS_HOST = "185.14.186.77"
    CRM_REDIS_PORT = "6399"
    CRM_REDIS_PASSWORD = "FsQ6#9uwcawSBCqA8w$DN@+=$7hAF?RF9GHL#tLJBcYhwbd!P$MR?&h8V%qgAFWLdPRFPfRNBhW9DPcErjjz-" \
                         "xSz@NRcMV&HsedzU-rv=A$pcm&A66*F?_x#68Sz*fFH4SBYb?tNa6MwB4fDsSJWDre29N5@?cGM967c!Ve3YQp" \
                         "rxQjwvZ2%kmQ6qywJT*3-!PL2*k*WbPbJ8dHxV9C%NB#4r4&ENkRvJr3bcv9baf3#nRBMkC_K_u7ZRkwZ^KSu"

    ENABLE_AUTH = True


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    ProdConfig,
    StageConfig,
    DevelopmentConfig

]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
