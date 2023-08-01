import logging
import random
import time
from typing import Union

import openai
from dotenv import load_dotenv
from fastapi import FastAPI, Header
from typing_extensions import Annotated

from models import Conversation

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(title='OpenAI ChatCompletion API PoC', version='0.0.1',
              contact={'name': 'Sameer', 'email': 'sam [at] sameerkumar.website'})


@app.post("/chat")
async def chat(conversation: Conversation, is_mock: bool = False,
               x_openai_api_key: Annotated[Union[str, None], Header(convert_underscores=True)] = None):
    logging.debug(conversation)

    logging.debug(f'is mock? => {is_mock}')
    # [ToDo] - Bad design, keeping it in the interest of time.
    if is_mock:
        time.sleep(random.randint(1, 2))
        return conversation
    logging.debug('calling openai')
    openai.api_key = x_openai_api_key
    # ToDo: throw 401 if api key is incorrect. 403 is quota is over.

    # bad design, keeping it for testing purposes
    chat_completion_resp = openai.ChatCompletion.create(
        model=conversation.llm_model,
        messages=conversation.model_dump()['messages'],
        temperature=1,  # can be taken as input
        n=1  # can be taken as input
    )
    return Conversation(messages=[r['message'] for r in chat_completion_resp['choices']],
                        llm_model='gpt-4').model_dump(by_alias=True)


@app.get("/test")
async def test(delay: int = 0):
    time.sleep(delay)
    return {'status': 'ok'}
