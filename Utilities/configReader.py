from configparser import ConfigParser

from Consts.consts import Consts

config = ConfigParser()
#config.read("../ConfigurationData/conf.ini")
config.read(Consts.DATA_CONFIG_DIR)


def readConfig(section, key):
    return config.get(section, key)


def writeConfig(sesction,key,newvalue):
    config.set(sesction, key, newvalue)
    with open(Consts.PROJECT_ROOT+'/ConfigurationData/conf.ini', 'w') as configfile:
        config.write(configfile)


#a = readConfig("config","is_create_test_run")
#print (a)
