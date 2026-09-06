import re


def answer_question(text, question):
    if not text.strip():
        return "No document text is available."

    if not question.strip():
        return "Please enter a question."

    # Split document into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    question_words = set(
        word.lower()
        for word in re.findall(r'\b\w+\b', question)
        if len(word) > 2
    )

    best_sentences = []

    for sentence in sentences:
        sentence_words = set(
            word.lower()
            for word in re.findall(r'\b\w+\b', sentence)
        )

        common_words = question_words.intersection(sentence_words)

        if common_words:
            best_sentences.append(
                (len(common_words), sentence.strip())
            )

    # Sort sentences according to relevance
    best_sentences.sort(reverse=True)

    if best_sentences:
        return " ".join(
            sentence for _, sentence in best_sentences[:3]
        )

    return "I could not find an answer to that question in the document."