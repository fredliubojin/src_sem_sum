# src_sem_sum
# Semantic Source Code Summarizer

This project is a sophisticated Python application that utilizes OpenAI's GPT-4 model to generate semantic summaries of source code files. It can process individual files or entire directories, and supports a variety of programming languages including Java, Python, JavaScript, TypeScript, Golang, Rust, C and C++.

## Why do we need it
The generated yml file retains semantic information of the original source code, and description of the functionality and purpose of the files and its symbols (imported and exported).

While retaining major semantic of the original source code, the file itself is drastically smaller in token count, which could help explain the source code to LLM such as GPT4 less pressure on context window size (v.s. uploading entire source code to LLM).


## Features
- **Source Code Analysis:** The application reads the content of a source code file and uses GPT4 to generate a summary.
- **Multi-Language Support:** Supports Java, Python, JavaScript, TypeScript, Golang, Rust, C and C++.
- **Directory Scanning:** Can process an entire directory of source code files, recursively handling subdirectories.
- **YAML Output:** The summary for each file is returned in YAML format, providing a clear structure that is easy to parse and use in other applications.
- **Error Handling:** The application includes robust error handling, logging any issues that occur during processing.

## How to Use
1. Clone the repository to your local machine.
2. Install the required packages: `openai`, `os`, `json`, `unittest`, `re`, `yaml`, `argparse`, `logging`, `sys`, and `tqdm`.
3. Set your OpenAI API key as an environment variable: `export OPENAI_API_KEY=your-api-key`
4. Run the script with the desired arguments:
   - To process a single file: `python src_sem_sum.py --file your_file_path`
   - To process an entire directory: `python src_sem_sum.py --dir your_directory_path`
5. The script will output a YAML formatted string representing a dictionary where the keys are file paths and the values are the corresponding semantic summaries.

## Future Features
- **Improved Parsing:** More robust parsing of the GPT response, potentially with JSON schema.
- **Additional Language Support:** Extend the support to more programming languages.
- **Customizable Output Format:** Allow the user to specify the output format (e.g., JSON, XML, etc.).
- **Integration with Code Editors:** Develop plugins for popular code editors to use this tool directly from the editor.

Please note that this tool is reliant on the OpenAI GPT model, which may have usage costs associated with it. Be sure to understand the cost structure of the OpenAI API before using this tool extensively.
