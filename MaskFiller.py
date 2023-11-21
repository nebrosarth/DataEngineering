from transformers import pipeline


class MaskFiller:
    def __init__(self):
        self.unmasker = pipeline('fill-mask', model='bert-base-uncased', device=0)

    def print_results(self, results):
        for i in range(len(results)):
            result = results[i]
            print(f"Variant #{i}, word={result['token_str']}: {result['sequence']}")

    def fill_mask(self, text):
        results = self.unmasker(text)
        self.print_results(results)
