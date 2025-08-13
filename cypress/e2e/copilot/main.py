import chainlit as cl

commands = [
    {"id": "Picture", "icon": "image", "description": "Use DALL-E"},
    {"id": "Search", "icon": "globe", "description": "Find on the web"},
    {
        "id": "Canvas",
        "icon": "pen-line",
        "description": "Collaborate on writing and code",
    },
]


@cl.on_chat_start
async def on_chat_start():
    await cl.context.emitter.set_commands(commands)
    await cl.Message(content="Hi from copilot!").send()


@cl.on_message
async def on_message(msg: cl.Message):
    if cl.context.session.client_type == "copilot":
        if msg.type == "system_message":
            await cl.Message(content=f"System message received: {msg.content}").send()
            return

        fn = cl.CopilotFunction(name="test", args={"msg": msg.content})
        res = await fn.acall()
        await cl.Message(content=res).send()
