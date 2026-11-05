
import os
from functools import lru_cache


@lru_cache(maxsize=1)
def load_generator():

    model_id = os.getenv("PARAM1_MODEL_ID", "").strip()

    if not model_id:
        raise RuntimeError(
            "Set PARAM1_MODEL_ID to the correct Param1 model ID."
        )

    try:
        from transformers import pipeline

    except ImportError as e:
        raise RuntimeError(
            "Please install transformers and accelerate."
        ) from e

    generator = pipeline(
        "text-generation",
        model=model_id,
        trust_remote_code=True,
        device_map="auto"
    )

    return generator


def improve_sentence(text, language_name):

    if not text.strip():
        return text

    generator = load_generator()

    prompt = (
        f"Improve the following {language_name} sentence "
        "for grammar, spelling and clarity. "
        "Preserve the original meaning. "
        "Return only the improved sentence.\n\n"
        f"Sentence: {text}\n"
        "Improved sentence:"
    )

    result = generator(
        prompt,
        max_new_tokens=128,
        do_sample=False,
        return_full_text=False
    )

    if not result:
        raise RuntimeError("No output generated.")

    improved_text = result[0]["generated_text"].strip()

    return improved_text if improved_text else text
