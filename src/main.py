import request_api

content = input('Faça uma pergunta ao chatgpt: ')


def __init__():
    rs = request_api.chatgpt_answer(content)
    if 'error' in rs:
        res = {
            "statusCode": 400,
            "message": "Houve um Erro na sua consulta.",
            "error": f"{rs['error']['code']}"
        }
        return res
    else:
        message = rs["choices"][0]["message"]["content"]
        res = {
            "statusCode": 200,
            "message": f"{str(message)}"
        }
        return res


__init__()
