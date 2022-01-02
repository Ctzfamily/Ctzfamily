





@pgram.on_inline_query()
async def inline_query_handler(client, query):
    try:
        text = query.query.lower()
        answers = []
        if text.strip() == "":
            answerss = await inline_help_func(__HELP__)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
            return
        if text.split()[0] == "alive":
            answerss = await alive_function(answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
