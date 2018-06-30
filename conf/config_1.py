
import configparser

cf=configparser.ConfigParser()
cf.read('db.conf')
config=cf.get('DATABASE','config')
print(config)