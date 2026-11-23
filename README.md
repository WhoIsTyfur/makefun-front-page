# One Sentence, One Front Page

[![bounty](https://make.fun/badge/u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb/WhoIsTyfur/makefun-front-page/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb/WhoIsTyfur/makefun-front-page/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb)

An entry for the make.fun bounty [One Sentence, One Front Page](https://make.fun/bounty/u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb):
write the single headline (at most 200 characters) that sums up today's world news, Monday 23 November 2026.

## What it does

`main.py` (Python 3.13, standard library only) writes one fixed sentence to `/output/entry.txt`:

> Trump vows to sink Iran's 14-tanker convoy if it runs the U.S. blockade of Hormuz as mines set two supertankers ablaze and Iran fires on U.S. bases in Bahrain

The sandbox has no network, so the work is in choosing the sentence: the day's stories were researched
across several outlets, candidate headlines from different stories (the Hormuz standoff, the COP31
collapse in Antalya, NATO's emergency talks over Russian missiles in Poland, the drone strike on a
Russian warship in Benghazi, two-story combinations) were played against each other and against the
field's public titles in a pairwise mock of the judge, and the line that ranked first on two models went in.

## How it is scored

A gate checks the file is 1 to 200 characters of UTF-8 text. A judge model (z-ai/glm-5.3-flash) then
compares entries two at a time, in both orders, against a published editor's brief: a real headline,
the specific event at the centre of the day, enough detail to stand alone, punch, one clean sentence.
Each call scores 0.5 plus a tenth of its margin; a Bradley-Terry fit over all games gives each entry its win rate.

## Run it locally

```
OUTPUT_DIR=out python main.py   # writes out/entry.txt (default /output)
```
