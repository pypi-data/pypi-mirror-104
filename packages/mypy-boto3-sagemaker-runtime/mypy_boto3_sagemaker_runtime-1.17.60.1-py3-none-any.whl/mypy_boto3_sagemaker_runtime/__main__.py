import sys


def print_info() -> None:
    print(
        "Type annotations for boto3.SageMakerRuntime 1.17.60\n"
        "Version:         1.17.60.1\n"
        "Builder version: 4.7.0\n"
        "Docs:            https://pypi.org/project/mypy-boto3-sagemaker-runtime/\n"
        "Boto3 docs:      https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/sagemaker-runtime.html#SageMakerRuntime\n"
        "Other services:  https://pypi.org/project/boto3-stubs/\n"
        "Changelog:       https://github.com/vemel/mypy_boto3_builder/releases"
    )


def print_version() -> None:
    print("1.17.60.1")


def main() -> None:
    if "--version" in sys.argv:
        return print_version()
    print_info()


if __name__ == "__main__":
    main()
