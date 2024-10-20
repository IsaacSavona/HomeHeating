# from pathlib import Path

# import pytest


# @pytest.fixture(scope="session")
# def test_directory() -> Path:
#     path = Path(__file__).parent
#     assert path.exists()
#     return path


# @pytest.fixture(scope="session")
# def repository_directory(test_directory) -> Path:
#     path = test_directory.parent
#     assert path.exists()
#     return path


# @pytest.fixture(scope="session")
# def module_directory(repository_directory) -> Path:
#     path = repository_directory / "homeheating"
#     assert path.exists()

#     # Add the module directory to sys.path so pytest can find the package
#     sys.path.append(str(path))

#     return path

