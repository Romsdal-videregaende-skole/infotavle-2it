import json, requests

x = requests.get('https://v2.jokeapi.dev/joke/Any')


def getJoke():

    joke = json.loads(x.text)
    if joke.get('joke') is not None:
        print("joke", joke.get('joke'))
        return json.dumps({"Joke": joke.get('joke')})
    print(f"{joke.get('setup')}: ", f"\n{joke.get('delivery')}", "\n",)
    return json.dumps({"Setup": joke.get('setup'), "Punchline": joke.get('delivery')})
if __name__ == '__main__':
    print(getJoke())