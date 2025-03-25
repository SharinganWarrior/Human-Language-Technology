
# Required libraries
!pip install wordcloud matplotlib

import json
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# --------------------- Task 1: Finnish Verb Form Analysis ---------------------

# Download the Finnish dataset
!wget https://github.com/UniversalDependencies/UD_Finnish-TDT/raw/master/fi_tdt-ud-train.conllu

# Verb form counter
verb_forms = Counter()

# Process CoNLL-U file to count verb forms
with open('fi_tdt-ud-train.conllu', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        cols = line.split('\t')
        if len(cols) >= 6:
            upos, feats = cols[3], cols[5]
            if upos == 'VERB' and feats != '_':
                verb_forms[feats] += 1

# Display sorted verb forms
print("\n--- Finnish Verb Forms (Top 10) ---")
for form, count in verb_forms.most_common(10):
    print(f"{form}: {count}")

print(f"\nTotal unique verb forms: {len(verb_forms)}")

# --------------------- Task 2: News Topic Word Clouds ---------------------

# Download JSONL topic files
!wget http://dl.turkunlp.org/TKO_7095_2023/topic1.jsonl
!wget http://dl.turkunlp.org/TKO_7095_2023/topic2.jsonl

# Load texts from JSONL
def load_jsonl(filepath):
    texts = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            texts.append(data['text'])
    return " ".join(texts)

# Load datasets
topic1_text = load_jsonl('topic1.jsonl')
topic2_text = load_jsonl('topic2.jsonl')

# Generate word clouds
wordcloud1 = WordCloud(width=800, height=400, background_color='white').generate(topic1_text)
wordcloud2 = WordCloud(width=800, height=400, background_color='white').generate(topic2_text)

# Plot word clouds
plt.figure(figsize=(16, 10))

# Topic 1 Word Cloud
plt.subplot(2, 1, 1)
plt.imshow(wordcloud1, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Topic 1', fontsize=20)

# Topic 2 Word Cloud
plt.subplot(2, 1, 2)
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Topic 2', fontsize=20)

plt.tight_layout()
plt.show()
