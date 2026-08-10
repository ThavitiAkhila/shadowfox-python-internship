import requests
from bs4 import BeautifulSoup
import csv


url = "https://quotes.toscrape.com/"

response = requests.get(url)


if response.status_code == 200:

    print("Website accessed successfully!")

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    with open(
        "scraped_data.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Quote",
            "Author",
            "Tags"
        ])

        for quote in quotes:

            quote_text = quote.find(
                "span",
                class_="text"
            ).get_text(strip=True)

            author = quote.find(
                "small",
                class_="author"
            ).get_text(strip=True)

            tag_elements = quote.find_all(
                "a",
                class_="tag"
            )

            tags = ", ".join(
                tag.get_text(strip=True)
                for tag in tag_elements
            )

            writer.writerow([
                quote_text,
                author,
                tags
            ])

            print("------------------------------")
            print("Quote:", quote_text)
            print("Author:", author)
            print("Tags:", tags)

    print()
    print("Scraping completed successfully!")
    print("Data saved to scraped_data.csv")

else:

    print("Unable to access website.")

    print(
        "Status code:",
        response.status_code
    )