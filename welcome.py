from mastodon import Mastodon
from fastapi import FastAPI
from pydantic import BaseModel


class Account(BaseModel):
    # see AccountSerializer for the full list of properties: 
    #   https://github.com/mastodon/mastodon/blob/main/app/serializers/rest/admin/account_serializer.rb
    username: str


class AccountCreatedEvent(BaseModel):
    event: str
    created_at: str
    object: Account


app = FastAPI()


@app.post("/")
def root(event: AccountCreatedEvent):
    #   Set up Mastodon
    mastodon = Mastodon(
        access_token='HzmNln_8EgsEYhV1zTmDbLNrfnid2lJtaojn_B8olg8',
        api_base_url='https://dmv.community/'
    )

    account_id = f"@{event.object.username}"
    message = account_id + \
        "Welcome to DMV.Community! Glad to have you here! \n" \
        "Check out the About page at https://dmv.community/about, and the wiki at https://wiki.dmv.community! \n" \
        "If you are new to Mastodon, I recommend reading Roma's Mastodon Starter Pack: https://blog.kizu.dev/my-mastodon-starter-pack/ \n" \
        "Also check out my pinned posts on my profile for regional accounts to follow, and follow @FediFollows and @FediTips for more accounts to follow and tips on making the most of Mastodon and the fediverse!"

    mastodon.status_post(message, visibility='public')

    return {"message": f"Sent welcome message to {account_id}."}
