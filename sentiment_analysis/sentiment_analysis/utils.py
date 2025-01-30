def print_articles_with_labels(articles, labels):
    for article, label in zip(articles, labels):
        print(f"Article: {article}\nLabel: {label}\n")