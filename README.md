# Human-Language-Technology
# NLP Tasks: CoNLL-U Verb Analysis & Topic Visualization

## Overview
This repository contains solutions for two natural language processing (NLP) tasks:

1. **Analyzing Finnish Verb Forms** from the Universal Dependencies (UD) dataset.
2. **Topic Visualization** through Word Clouds generated from news articles.

---

## Task 1: Finnish Verb Form Analysis

### Description:
Finnish is renowned for its highly inflected verbs, which are said to have thousands of distinct morphological forms. This task involved analyzing the UD Finnish dataset (`fi_tdt-ud-train.conllu`) to identify:
- All unique verb forms present in the dataset.
- Their frequency of occurrence.

### Data Source:
- [Universal Dependencies - Finnish TDT](https://github.com/UniversalDependencies/UD_Finnish-TDT)

### Method:
- Downloaded and parsed the dataset in CoNLL-U format.
- Extracted and counted verb forms using morphological features provided by the dataset.
- Sorted verb forms by descending frequency.

### Results:
- Identified **408 unique verb forms**.
- Full verb form frequency list provided in the notebook/script.

---

## Task 2: Topic Identification with Word Clouds

### Description:
Analyzed two sets of news articles (`topic1.jsonl` and `topic2.jsonl`) to visually identify their main topics using word clouds.

### Data Sources:
- [Topic 1 News Data](http://dl.turkunlp.org/TKO_7095_2023/topic1.jsonl)
- [Topic 2 News Data](http://dl.turkunlp.org/TKO_7095_2023/topic2.jsonl)

### Method:
- Loaded and concatenated JSONL news articles.
- Generated word clouds to visualize the frequency and prominence of words.

### Results:
- Two clear and distinct word clouds were generated.
- Topics were inferred by examining the largest and most prominent words.

---

## Dependencies
- Python 3.x
- `wordcloud`
- `matplotlib`

Installation:
```bash
pip install wordcloud matplotlib
```

---

## Usage
Detailed steps and results can be found in the included Jupyter notebook(s) or Python scripts provided in this repository.

---

## Author
- Momina Iftikhar

---

