# markov-server

Designed to be set up with a service like Heroku. Put the source text into source.txt and then when given the appropriate query, the webservice will return a sentence or sentences generated from the source. It is outputted in a JSON in thisformat:
```
{
  "content": [generated sentence(s)]
}
```

For example: `markov-server.herokuapp.com/chat` will output a JSON with `"content": [2 generated sentences]`

Tweet: `markov-server.herokuapp.com/chat?size=tweet` will output a JSON with `"content": [short sentence within tweet length (140 chars)]`

N-sentences: `markov-server.herokuapp.com/chat?size=N` will output a JSON with `"content": [N generated sentences]`
