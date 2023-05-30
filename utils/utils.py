import configparser


def get_config(config_name):
    config = configparser.ConfigParser()
    config.read("config.ini")

    conf = config['chatgpt'][f'{config_name}']
    return conf
