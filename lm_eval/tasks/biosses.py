"""

"""
import numpy as np
from lm_eval.base import rf, BioTask
from lm_eval.metrics import mean


_CITATION = """

"""

class BiossesBase(BioTask):
    VERSION = 0
    DATASET_PATH = "lm_eval/datasets/biomedical/bigbio/biodatasets/biosses"
    DATASET_NAME = None
    SPLIT = None

    def has_training_docs(self):
        return True

    def has_validation_docs(self):
        return True

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():
            return self.dataset["train"]

    def validation_docs(self):
        if self.has_validation_docs():
            return self.dataset["validation"]

    def test_docs(self):
        if self.has_test_docs():
            return self.dataset["test"]
          
class BiossesPAIRS(BiossesBase):
    DATASET_NAME = "biosses_bigbio_pairs"