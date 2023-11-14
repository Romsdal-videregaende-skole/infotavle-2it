import json, requests




def getJoke():

    request = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit')
    joke = json.loads(request.text)

    if joke.get('joke') is not None:

        print("joke", joke.get('joke'))

        return json.dumps({"Setup": None, "Punchline": joke.get('joke')})

    print(f"{joke.get('setup')}: ", f"\n{joke.get('delivery')}", "\n",)
    return json.dumps({"Setup": joke.get('setup'), "Punchline": joke.get('delivery')})

if __name__ == '__main__':
    print(getJoke())