import openai
#
# # open ai에서 발급받은 api key를 등록합니다
import os
from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("sk-proj-iwRmhAVrCa50ha9vBVFHT3BlbkFJStglBteNx06FXfC0jXfm"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
# import sys
#
# print(sys.executable)