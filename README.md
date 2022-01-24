## FastAPI PropelAuth Starter

This repo contains a forkable FastAPI backend which uses [PropelAuth](https://www.propelauth.com/?utm_campaign=github) to validate access tokens sent from your frontend.

[Here](https://www.propelauth.com/blog-categories/guide) are guides which will walk you through the code in this repo.

You can use this with any compatible frontend, like the [React PropelAuth Starter](https://github.com/PropelAuth/react-propelauth-starter)

### Using this repo

Make sure to update `.env` with your project's information. Then setup your venv, install, and run:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ uvicorn main:app --reload --port=3001
```
