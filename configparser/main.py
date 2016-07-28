from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')
print(cfg.sections())
print(cfg.get('installation', 'library'))
print(cfg.getboolean('debug','log_errors'))
print(cfg.getint('server','port'))
cfg.set('server','port','9002')
with open("config2.ini", "w") as f:
    cfg.write(f)
