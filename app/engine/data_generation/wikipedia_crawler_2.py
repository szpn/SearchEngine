import wikipedia
import logging
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
import threading

wikipedia.set_lang("simple")

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Global variables
visited = set()
executor = ThreadPoolExecutor(max_workers=100)
saved_topics_count = 0
start_time = time.time()

async def save_page_content(filename, content):
    global saved_topics_count
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        saved_topics_count += 1
        if saved_topics_count % 100 == 0:
            logger.info(f"Number of saved topics: {saved_topics_count}")
    except Exception as e:
        logger.exception(f"Error saving page content to file '{filename}': {e}")



def crawl_topic(topic):
    try:
        if topic in visited:
            logger.info(f"Skipping already visited topic: {topic}")
            return []

        page = wikipedia.page(topic)
        visited.add(topic)
        visited.add(page.title)

        logger.info(f"Crawled: {page.title}\t{topic}\t{page.url}")

        filename = f"tmp/{page.title}.txt"
        asyncio.run(save_page_content(filename, page.content))

        return [(link, page.title) for link in page.links]

    except wikipedia.exceptions.DisambiguationError as e:
        logger.debug(f"{topic} may refer to multiple pages. Try specifying further.")
    except wikipedia.exceptions.PageError:
        logger.debug(f"Page '{topic}' does not exist on Wikipedia.")
    except KeyError as e:
        logger.debug(f"KeyError occurred for topic '{topic}': {e}")
    except Exception as e:
        logger.exception(f"Error processing '{topic}': {e}")

    return []


def crawl_wikipedia(start_topic, max_depth=4):
    global executor

    futures = [executor.submit(crawl_topic, link) for link, _ in crawl_topic(start_topic)]

    for future in futures:
        result = future.result()
        if result and max_depth > 0:
            crawl_wikipedia(result[0][0], max_depth - 1)


def print_statistics():
    global saved_topics_count, start_time
    while True:
        end_time = time.time()
        elapsed_time = end_time - start_time
        crawled_pages_per_second = saved_topics_count / elapsed_time
        print(f"\rCrawled Pages: {saved_topics_count} | Elapsed Time: {elapsed_time:.2f} seconds | Crawled Pages Per Second: {crawled_pages_per_second:.2f}", end="", flush=True)
        time.sleep(1)


if __name__ == "__main__":
    try:
        statistics_thread = threading.Thread(target=print_statistics)
        statistics_thread.daemon = True
        statistics_thread.start()

        crawl_wikipedia("World War II")
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt detected. Exiting gracefully...")
    finally:
        logger.info("\nShutting down the executor.")
        executor.shutdown(wait=True)
