import boto3
import random
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

TABLE_NAME = os.environ['TABLE_NAME']
SNS_PHONE_NUMBER = os.environ['TELEFONE_SMS']

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)

    # Scan na tabela para pegar todos os IDs
    response = table.scan()
    itens = response.get('Items', [])

    if not itens:
        print("Tabela vazia.")
        return {"statusCode": 404, "body": "Nenhum item encontrado"}

    # Sorteia um item aleatório
    item_sorteado = random.choice(itens)
    id_sorteado = item_sorteado.get('id')

    print(f"ID sorteado: {id_sorteado}")
    print(f"Objeto completo: {item_sorteado}")

    # Monta mensagem para o SMS
    mensagem_sms = f"ID sorteado: {id_sorteado}\nDados: {item_sorteado}"

    # Envia SMS com SNS
    sns.publish(
        PhoneNumber=SNS_PHONE_NUMBER,
        Message=mensagem_sms
    )

    return {
        "statusCode": 200,
        "body": f"SMS enviado com dados do ID {id_sorteado}"
    }
