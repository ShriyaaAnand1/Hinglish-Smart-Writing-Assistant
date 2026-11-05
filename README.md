
# Hinglish Smart Writing Assistant

## Project Overview

The Hinglish Smart Writing Assistant is an AI-powered application that converts text written in Roman-script Hinglish into native Indian-language scripts.

It allows users to type Indian-language words using English letters and obtain the corresponding text in Hindi, Kannada, or Tamil.

The application also provides optional sentence improvement and English translation features.

## Features

- Hinglish to native-script transliteration.
- Hindi, Kannada, and Tamil language support.
- Optional sentence improvement using BharatGen Param1.
- Optional English translation using AI4Bharat IndicTrans2.
- Interactive Streamlit interface.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Frontend |
| IndicXlit | Transliteration |
| Param1 | Sentence improvement |
| IndicTrans2 | Translation |
| PyTorch | Deep learning |
| Transformers | Pretrained model integration |

## Project Workflow

1. User selects an Indian language.
2. User enters Roman-script Hinglish text.
3. IndicXlit converts the input into the selected native script.
4. Param1 optionally improves the sentence.
5. IndicTrans2 optionally translates the output into English.
6. The application displays the results.

## Installation

```bash
python -m venv venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

Install IndicTransTokenizer separately as described in the project setup instructions.

## Run the Application

```bash
streamlit run app.py
```

## Evaluation

The project evaluates transliteration using:

- Character Error Rate (CER)
- Word Accuracy
- Manual output verification

The evaluation dataset contains 30–50 test cases covering different input sentences and spelling variations.

## Limitations

- Different Roman spellings can produce different transliterations.
- Context and ambiguous words may affect the output.
- Sentence improvement and translation depend on model availability and configuration.
- Model execution may require significant memory.

## References

- https://github.com/AI4Bharat/IndicXlit
- https://github.com/AI4Bharat/IndicTrans2
- https://github.com/VarunGumma/IndicTransTokenizer
- https://bharatgen.com/

## Contributors

Add team member names here.
