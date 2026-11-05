
import os
from functools import lru_cache


@lru_cache(maxsize=1)
def load_translation_model():

    import torch

    from transformers import (
        AutoTokenizer,
        AutoModelForSeq2SeqLM
    )

    from IndicTransTokenizer import IndicProcessor

    model_name = os.getenv(
        "INDICTRANS_MODEL",
        "ai4bharat/indictrans2-indic-en-dist-200M"
    )

    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name,
        trust_remote_code=True
    )

    device = (
        "cuda" if torch.cuda.is_available()
        else "cpu"
    )

    model = model.to(device)

    processor = IndicProcessor(inference=True)

    return (
        torch,
        tokenizer,
        model,
        processor,
        device
    )


def translate_to_english(text, source_language_code):

    if not text.strip():
        return ""

    (
        torch,
        tokenizer,
        model,
        processor,
        device
    ) = load_translation_model()

    sentences = [text]

    batch = processor.preprocess_batch(
        sentences,
        src_lang=source_language_code,
        tgt_lang="eng_Latn"
    )

    inputs = tokenizer(
        batch,
        truncation=True,
        padding="longest",
        return_tensors="pt",
        return_attention_mask=True
    ).to(device)

    with torch.no_grad():

        generated_tokens = model.generate(
            **inputs,
            use_cache=True,
            max_length=256,
            num_beams=5,
            num_return_sequences=1
        )

    decoded = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True
    )

    translations = processor.postprocess_batch(
        decoded,
        tgt_lang="eng_Latn"
    )

    return translations[0] if translations else ""
