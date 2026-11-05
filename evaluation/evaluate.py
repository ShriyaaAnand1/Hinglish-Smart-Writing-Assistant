
import csv
from pathlib import Path

import jiwer


def character_error_rate(reference, hypothesis):

    return jiwer.cer(
        reference,
        hypothesis
    )


def word_accuracy(reference, hypothesis):

    ref_words = reference.split()
    hyp_words = hypothesis.split()

    if not ref_words:
        return 1.0 if not hyp_words else 0.0

    matches = 0

    for i, word in enumerate(ref_words):

        if i < len(hyp_words) and word == hyp_words[i]:
            matches += 1

    return matches / max(
        len(ref_words),
        len(hyp_words)
    )


def evaluate_file():

    input_file = Path("evaluation/test_cases.csv")
    output_file = Path("evaluation/results.csv")

    with input_file.open(
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        rows = list(csv.DictReader(file))

    results = []

    for row in rows:

        reference = row["expected_output"].strip()
        hypothesis = row["actual_output"].strip()

        cer = character_error_rate(
            reference,
            hypothesis
        )

        accuracy = word_accuracy(
            reference,
            hypothesis
        )

        results.append({
            "input_text": row["input_text"],
            "expected_output": reference,
            "actual_output": hypothesis,
            "cer": cer,
            "word_accuracy": accuracy
        })

    with output_file.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "input_text",
                "expected_output",
                "actual_output",
                "cer",
                "word_accuracy"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print("Evaluation completed.")
    print("Results saved to:", output_file)


if __name__ == "__main__":
    evaluate_file()
