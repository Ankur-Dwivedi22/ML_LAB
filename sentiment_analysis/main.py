from sentiment_analysis.scraper import scrape_moneycontrol, scrape_yahoo_news
from sentiment_analysis.labeler import label_articles
from sentiment_analysis.utils import print_articles_with_labels


def main():
    # Scrape articles from both sources
    articles = scrape_moneycontrol() + scrape_yahoo_news()

    # Label the articles based on sentiment
    labels = label_articles(articles)

    # Print articles with their corresponding labels
    print_articles_with_labels(articles, labels)


if __name__ == "__main__":
    main()
