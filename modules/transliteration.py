
import re
from functools import lru_cache


@lru_cache(maxsize=3)
def load_engine(language_code):

    try:
        from ai4bharat.transliteration import XlitEngine

    except ImportError as e:
        raise RuntimeError(
            "Please install ai4bharat-transliteration."
        ) from e

    engine = XlitEngine(
        language_code,
        beam_width=5,
        rescore=True
    )

    return engine


def get_best_candidate(result, language_code):

    if isinstance(result, dict):

        candidates = result.get(language_code)

        if candidates is None and result:
            candidates = next(iter(result.values()))

    else:
        candidates = result

    if isinstance(candidates, (list, tuple)):
        return str(candidates[0]) if candidates else ""

    if candidates is None:
        return ""

    return str(candidates)


def transliterate(text, language_code):

    if not text or not text.strip():
        return ""

    engine = load_engine(language_code)

    tokens = re.findall(
        r"\w+|[^\w\s]+|\s+",
        text,
        flags=re.UNICODE
    )

    output = []

    for token in tokens:

        # Preserve spaces and punctuation
        if token.isspace():
            output.append(token)
            continue

        if re.fullmatch(r"[^\w\s]+", token):
            output.append(token)
            continue

        try:

            result = engine.translit_word(
                token,
                topk=1
            )

            candidate = get_best_candidate(
                result,
                language_code
            )

            output.append(
                candidate if candidate else token
            )

        except Exception:
            output.append(token)

    return "".join(output)
