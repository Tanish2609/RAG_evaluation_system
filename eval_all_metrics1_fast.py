import json
from deepeval.metrics import AnswerRelevancyMetric , FaithfulnessMetric , ContextualRelevancyMetric , GEval
from deepeval.test_case import LLMTestCase , SingleTurnParams
from deepeval.evaluate import CacheConfig

with open("results1.jsonl" , "r" , encoding="utf-8") as file:
    results = [json.loads(line) for line in file]