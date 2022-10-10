import yaml
import argparse


def read_params(config_path):
    with open(config_path, 'r') as stream:
        try:
            # config = yaml.load(stream)
            config = yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)
    return config


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml",
                      help="Directory params.yaml")
    parsed_args = args.parse_args()
    config = read_params(config_path=parsed_args.config)
