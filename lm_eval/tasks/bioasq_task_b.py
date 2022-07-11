"""
Scitail: A textual entailment dataset from science question answering
https://arxiv.org/pdf/1910.14599.pdf

The SciTail dataset is an entailment dataset created from multiple-choice science exams and web sentences. Each question and the correct answer choice are converted into an assertive statement to form the hypothesis.

Homepage: "https://allenai.org/data/scitail"
"""
import numpy as np
from lm_eval.base import rf, BioTask
from lm_eval.metrics import mean


_CITATION = """

"""

class BioAsqBase(BioTask):
    VERSION = 0
    DATASET_PATH = "lm_eval/datasets/biomedical/bigbio/biodatasets/bioasq_task_b"
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
          
class BioAsqQA(BioAsqBase):
    DATASET_NAME = "bioasq_blurb_bigbio_qa"
