import os
import argparse


def create_microservice(service_name: str, project_name: str = "eduscheduler_backend"):
    base_dirs = [
        f'{project_name}/{service_name}/app/api/v1/endpoints',
        f'{project_name}/{service_name}/app/core',
        f'{project_name}/{service_name}/app/db',
        f'{project_name}/{service_name}/tests',
    ]

    base_files = [
        f'{project_name}/{service_name}/app/api/v1/dependencies.py',
        f'{project_name}/{service_name}/app/api/v1/endpoints/__ini__.py',
        f'{project_name}/{service_name}/app/api/v1/__init__.py',
        f'{project_name}/{service_name}/app/api/__init__.py',
        f'{project_name}/{service_name}/app/core/config.py',
        f'{project_name}/{service_name}/app/core/__init__.py',
        f'{project_name}/{service_name}/app/db/models.py',
        f'{project_name}/{service_name}/app/db/__init__.py',
        f'{project_name}/{service_name}/app/main.py',
        f'{project_name}/{service_name}/app/__init__.py',
        f'{project_name}/{service_name}/tests/test_main.py',
        f'{project_name}/{service_name}/Dockerfile',
        f'{project_name}/{service_name}/requirements.txt',
        f'{project_name}/{service_name}/README.md',
        f'{project_name}/{service_name}/__init__.py',
    ]

    for directory in base_dirs:
        os.makedirs(directory, exist_ok=True)

    for file in base_files:
        open(file, 'a').close()


def main():
    parser = argparse.ArgumentParser(description='Microservice generator script.')
    parser.add_argument('service_name', type=str, help='The name of the microservice to generate.')

    args = parser.parse_args()

    create_microservice(args.service_name)


if __name__ == '__main__':
    main()
