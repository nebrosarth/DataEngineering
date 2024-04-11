from transformers import pipeline
from transformers.pipelines import PipelineException


class MaskFiller:
    """
    This class uses a BERT model to fill in the blank in a sentence.
    """

    def __init__(self):
        self.unmasker = pipeline('fill-mask', model='bert-base-uncased')

    def format_results(self, results, colorful=False):
        """
        Formats the results of the fill-mask operation.
        """
        formatted_results = []
        for i, result in enumerate(results):
            if colorful:
                formatted_results.append(f"Variant #{i}, word=**:violet[{result['token_str']}]**: {result['sequence']}")
            else:
                formatted_results.append(f"Variant #{i}, word={result['token_str']}: {result['sequence']}")
        return formatted_results

    def fill_mask(self, text, colorful=False):
        """
        Fills in the blank in the given text.
        """
        try:
            results = self.unmasker(text)
            return self.format_results(results, colorful)
        except PipelineException:
            raise
