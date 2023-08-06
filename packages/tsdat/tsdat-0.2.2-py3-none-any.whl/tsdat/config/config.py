import yaml
from yamllint import linter
from yamllint.config import YamlLintConfig
from typing import List, Dict
from .keys import Keys
from .pipeline_definition import PipelineDefinition
from .dataset_definition import DatasetDefinition
from .quality_test_definition import QualityTestDefinition


# TODO: add api method to download yaml templates or put them all
# in the examples folder.

class Config:
    """
    Wrapper for Dictionary of config values that provides helper functions for
    quick access.
    """

    def __init__(self, dictionary: Dict):
        pipeline_dict = dictionary.get(Keys.PIPELINE)
        dataset_dict = dictionary.get(Keys.DATASET_DEFINITION)
        qc_tests_dict = dictionary.get(Keys.QC_TESTS, {})

        self.pipeline_definition = PipelineDefinition(pipeline_dict)
        self.dataset_definition = DatasetDefinition(dataset_dict, self.pipeline_definition.output_datastream_name)

        self.qc_tests = self._parse_qc_tests(qc_tests_dict)

    def _parse_qc_tests(self, dictionary) -> Dict[str, QualityTestDefinition]:
        qc_tests: Dict[str, QualityTestDefinition] = {}
        for test_name, test_dict in dictionary.items():
            qc_tests[test_name] = QualityTestDefinition(test_name, test_dict)
        return qc_tests

    @classmethod
    def load(self, filepaths: List[str]):
        """-------------------------------------------------------------------
        Load one or more yaml config files which define data following 
        mhkit-cloud data standards.
        
        TODO: add a schema validation check on yaml so users can know if the 
        file is valid
        
        Args:
            filepaths (List[str]): The paths to the config files to load

        Returns:
            Config: A Config instance created from the filepaths.
        -------------------------------------------------------------------"""
        if isinstance(filepaths, str):
            filepaths = [filepaths]
        config = dict()
        for filepath in filepaths:
            Config.lint_yaml(filepath)
            with open(filepath, 'r') as file:
                dict_list = list(yaml.safe_load_all(file))
                for dictionary in dict_list:
                    config.update(dictionary)
        return Config(config)

    @staticmethod
    def lint_yaml(filename):
        # new-line-at-end-of-file
        conf = YamlLintConfig('{"extends": "relaxed", "rules": {"line-length": "disable", "trailing-spaces": "disable", "empty-lines": "disable"}}')
        with open(filename) as file:
            gen = linter.run(file, conf)
            errors = [error for error in gen if error.level == "error"]
            if errors:
                errors = "\n".join("\t\t" + str(error) for error in errors)
                raise Exception(f"Syntax errors found in yaml file {filename}: \n{errors}")
