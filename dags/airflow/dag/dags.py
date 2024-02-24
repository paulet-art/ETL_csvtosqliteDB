from airflow.decorators import dag, task
import pendulum 

import requests
import xmltodict

dag(
    dag_id = "podcast",
    schedule_interval = '@daily',
    start_date=pendulum.datetime(2023,6,11),
    catchup=False
)

def podcast():

    @task()
    def get_episodes():
        data = requests.get("https://www.marketplace.org/feed/podcast/marketplace/")
        feed = xmltodict(data.text)
        episodes = feed["rss"]["channel"]["item"]
        print(f"Found {len(episodes)} episodes")

    podcast_episodes = get_episodes()
summary = podcast()