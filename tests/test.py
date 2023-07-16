import os, unittest
from src_sem_sum import parse_response, get_prompt_messages, get_summary_response, process_files, get_results
import pprint

class TestMethods(unittest.TestCase):
    def test_parse_response(self):
        # Test with provided JSON
        raw_text = """
```json
{
    "path": "tests/token-counter.ts",
    "file_purpose": "This file serves as a wrapper around the Tiktoken library, keeping tokenizers for all models in a cache and preloading the tokenizer for the default model.",
    "imported_symbols": ["encoding_for_model", "get_encoding", "Tiktoken", "TiktokenModel", "DLLMId", "findOpenAILlmRefOrThrow", "useModelsStore"],
    "exported_symbols": [
        {"countModelTokens": "It's a function that takes a text, a DLLMId, and debugFrom as parameters, and returns the number of tokens in the model corresponding to the given DLLMId."}
    ]
}
```
In this file, the `countModelTokens` function is the only symbol that is exported. It counts the number of tokens for a
.
        """
        expected_output = {
            "path": "tests/token-counter.ts",
            "file_purpose": "This file serves as a wrapper around the Tiktoken library, keeping tokenizers for all models in a cache and preloading the tokenizer for the default model.",
            "imported_symbols": [
                "encoding_for_model",
                "get_encoding",
                "Tiktoken",
                "TiktokenModel",
                "DLLMId",
                "findOpenAILlmRefOrThrow",
                "useModelsStore"
            ],
            "exported_symbols": [
                {
                    "countModelTokens": "It's a function that takes a text, a DLLMId, and debugFrom as parameters, and returns the number of tokens in the model corresponding to the given DLLMId."
                }
            ]
        }
        self.assertEqual(parse_response(raw_text), expected_output)

    def test_get_prompt_messages(self):
        expected_message = ""
        message = get_prompt_messages("tests/cases/sample.py")
        print(f"{message=}")
        self.assertEqual(message, expected_message)

    def test_get_summary_response(self):
        response = get_summary_response('tests/cases/sample.py')
        print(f'completion result: {response}')
        self.assertIsNotNone(response)

    def test_process_files(self):
        results = {}
        process_files("./tests/cases/", results)
        pprint.pprint(results)


if __name__ == '__main__':
    unittest.main()