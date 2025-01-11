#ChatRoutes.py

from flask import Blueprint, Flask, request, jsonify, Response, stream_with_context
from openai import OpenAI

import Agents.Agents

api_key=Agents.Agents.KIMI_API_KEY
base_url=Agents.Agents.KIMI_BASE_URL



chat_bp = Blueprint('chat', __name__)

#json格式输出接口
@chat_bp.route('/kimi/chat_with_json', methods=['POST'])
def chat_with_json():
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )
    user_input = request.json.get('message')
    messages = [
        {"role": "system", "content": "You are a helpful AI."},
        {"role": "user", "content": user_input}
    ]
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=messages,
        temperature=0.3,
    )
    response_content = completion.choices[0].message.content
    return jsonify({'reply':response_content})


#流式输出接口
@chat_bp.route('/kimi/chat_with_stream', methods=['POST'])
def chat_with_stream():
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )
    user_input = request.json.get('message')
    messages = [
        {"role": "system", "content": "You are a helpful AI."},
        {"role": "user", "content": user_input}
    ]
    stream = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=messages,
        temperature=0.3,
        stream=True#流式输出
    )

    def generate_response(stream):
        for chunk in stream:
            delta = chunk.choices[0].delta
            if hasattr(delta, 'content') and delta.content:
                yield f"data: {delta.content}\n\n"

    return Response(stream_with_context(generate_response(stream)), content_type='text/event-stream')

