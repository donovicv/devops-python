import configparser
import os


def read_config():
    config = configparser.ConfigParser()

    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, '..', 'config.ini')
    config.read(config_path)

    try:
        debug_mode = config.getboolean('General', 'debug')
        print(debug_mode)
        log_level = config.get('General', 'log_level')
        db_name = config.get('Database', 'db_name')
        db_host = config.get('Database', 'db_host')
        db_port = config.getint('Database', 'db_port')
        db_user = config.get('Database', 'db_user')
        db_password = config.get('Database', 'db_password')

        config_values = {
            'debug_mode': debug_mode,
            'log_level': log_level,
            'db_name': db_name,
            'db_host': db_host,
            'db_port': db_port,
            'db_user': db_user,
            'db_password': db_password
        }
        return config_values

    except configparser.NoSectionError as e:
        print(f"Configuration error: {e}")
    except configparser.NoOptionError as e:
        print(f"Configuration error: {e}")

    return {}
