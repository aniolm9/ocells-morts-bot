#!/usr/bin/env python3
import settings
import game
import bot
import schedule
import time

def runnable(api):
    text = game.kill()
    print (text)
    bot.newTweet(api, text, settings.IMAGE)

def main():
    # Just run the first time.
    api = bot.createApi()

    # Run every day at 18:00.
    schedule.every().day.at("18:00").do(runnable, api=api)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
