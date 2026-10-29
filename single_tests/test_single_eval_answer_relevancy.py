from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase


test_case =  LLMTestCase(
    input = "What do penguins eat?",
    actual_output=("Penguins primarily feed on marine animals such as krill and tiny fish")
)

metric = AnswerRelevancyMetric(threshold=0.7) #true if >=0.7 else false

metric.measure(test_case)

print("Score :" , metric.score)
print("Reason :" , metric.reason)
print("Passed :" , metric.is_successful())
