from flow_core import run_flow
from config_loader import load_config

def main():
    config = load_config('config/config.sample.json')
    run_flow(config)

if __name__ == '__main__':
    main()
