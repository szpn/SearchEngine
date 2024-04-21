import wikipedia

wikipedia.set_lang("en")

visited = set()

def crawl_wikipedia(topic, max_depth=4, current_depth=0):
    if current_depth > max_depth or topic in visited:
        return


    try:
        page = wikipedia.page(topic)
        if page.title in visited:
            return
        visited.add(topic)
        visited.add(page.title)

        print(f"{'  ' * current_depth}{page.title}\t{topic}\t{page.url}")

        filename = f"tmp/{page.title}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(page.content)

        for new_topic in page.links:
            crawl_wikipedia(new_topic, max_depth, current_depth + 1)

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"{'  ' * current_depth}{topic} may refer to multiple pages. Try specifying further.")
        crawl_wikipedia(e.options[0], max_depth, current_depth + 1)
    except wikipedia.exceptions.PageError:
        print(f"{'  ' * current_depth}Page '{topic}' does not exist on Wikipedia.\n")


if __name__ == "__main__":
    crawl_wikipedia("World War Second")