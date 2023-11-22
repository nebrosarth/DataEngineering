from transformers import pipeline


class MaskFiller:
    def __init__(self):
        self.unmasker = pipeline('fill-mask', model='bert-base-uncased', device=0)

    def format_results(self, results, colorful=False):
        formatted_results = []
        for i in range(len(results)):
            result = results[i]
            if colorful:
                formatted_results.append(f"Variant #{i}, word=**:violet[{result['token_str']}]**: {result['sequence']}")
            else:
                formatted_results.append(f"Variant #{i}, word={result['token_str']}: {result['sequence']}")
        return formatted_results

    def fill_mask(self, text, colorful=False):
        results = self.unmasker(text)
        return self.format_results(results, colorful)
