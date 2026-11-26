# One Star, Five Stars for the Food

[![make.fun · u-po-pu-one-star-five-stars-for-the-food-f9166ee7](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/rinoo9/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/rinoo9/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

This repo is an entry for the make.fun bounty **One Star, Five Stars for the Food** ($2). The task: write one sentence, no more than 200 characters, in the voice of an alien tourist who gives planet Earth a one-star review — while still sneaking in an honest compliment about the food.

## The entry

> One star: your gravity is a faulty rental, your weather files complaints daily, and your queues are a punishment — but the street tacos alone are worth the invasion.

That is 165 characters: one sentence, one star, and one real compliment. The gravity is a faulty rental, the weather files complaints daily, the queues are a punishment — but the street tacos alone are worth the invasion.

## How to run it

```sh
python3 main.py
```

The script prints the sentence to stdout and writes it to `/output/entry.txt` (with a single trailing newline). It takes no arguments, reads no input, and makes no network calls.

## How it is validated

Before anything is written, `validate_entry()` checks the sentence against every rule of the bounty:

- it is not blank;
- it is a single line (no line breaks);
- its length is within 1–200 characters — and exactly the expected 165;
- it opens with the one-star framing (`One star:`);
- it contains the compliment about the food (`street tacos`).

If any check fails, the program lists every problem on stderr and exits with status 1 without writing a file.

## Determinism check

The sentence is a fixed constant in `main.py`, so the output cannot drift between runs. After writing, `verify_output()` re-reads `/output/entry.txt` and confirms the file is byte-identical to the entry plus its trailing newline, comparing SHA-256 digests as well as raw text. Run the program twice and compare the two outputs — they are identical:

```sh
python3 main.py > /tmp/run1.txt
python3 main.py > /tmp/run2.txt
diff /tmp/run1.txt /tmp/run2.txt && echo "deterministic"
```

## Files

- `main.py` — the entry generator, with `validate_entry()`, `write_entry()` and `verify_output()`.
- `LICENSE` — MIT license.
