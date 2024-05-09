import win32com.client as win32
from typing import Tuple, Optional
from datetime import datetime
import requests
import bs4


def get_product_info(url: str) -> Tuple[Optional[str], Optional[float]]:
    try:
        if "amazon" not in url:
            print("Não há produtos da Amazon neste site.")
            return None, None

        response = requests.get(url)
        if response.status_code == 200:
            print("Conexão bem sucedida.")
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            title_element = soup.find("span", class_="a-size-large product-title-word-break")
            price_element = soup.find("span", class_="a-price-whole")

            if title_element and price_element:
                title = title_element.text.strip()
                price = float(price_element.text.strip().replace(',', '.'))
                return title, price
            else:
                print("\nNão foi possível encontrar informações sobre o produto.")
                print(f"No site: {url}")
                return None, None
        else:
            print("\033[31mFalha na conexão.\033[m")
            print(f"No site: {url}")
            return None, 0
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro de rede: {e}")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None, None


def add_product_to_file(product_name: str, price: float) -> None:
    try:
        with open("preco_do_produto", "a") as preco:
            if price is None:
                preco.write(f"{product_name}: R$ None\n")
            else:
                preco.write(f"{product_name}: R$ {price:.2f}\n")
    except Exception as e:
        print(f"Erro ao adicionar produto ao arquivo: {e}")


def show_all_products() -> None:
    try:
        with open('dados_de_compra', 'r') as file:
            urls = file.read().splitlines()
    except FileNotFoundError:
        print("Arquivo 'dados_de_compra' não encontrado.")
        return

    urls.sort()

    add_new_list = input("Gostaria de adicionar uma nova lista? (S/N)").upper()
    print("-=" * 50)

    if add_new_list == "S":
        with open("preco_do_produto", "a") as file:
            current_date = datetime.now()
            file.write(f"\n{current_date.strftime('%d/%m/%Y - %H:%M'):=^50}\n")

    print("Produtos encontrados nos dados de compra:")

    for index, url in enumerate(urls):
        product_name, _, product_url = url.partition(":")
        print(f"{index + 1:2} - {product_name}")
        title, price = get_product_info(product_url)

        if title and price or title is None and price is None:
            if price is None and title is None:
                price = 0
            add_product_to_file(product_name, price)

        if title is None or price is None:
            print("-=" * 50)
        else:
            print(f"Preço: R$ {price:.2f}")
            print(f"Site: {product_url}")
            print("=-" * 50)


def sort_purchase_data() -> None:
    try:
        with open('dados_de_compra', 'r') as dc:
            data = dc.read().splitlines()

        data.sort()

        with open('dados_de_compra', 'w') as ou:
            for item in data:
                ou.write(f"{item}\n")
    except FileNotFoundError:
        print("Arquivo 'dados_de_compra' não encontrado.")


def get_last_products_from_file(file_name: str, num_products: int) -> list:
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            last_lines = lines[-num_products:]
            return [line.strip() for line in last_lines]
    except FileNotFoundError:
        print(f"Arquivo '{file_name}' não encontrado.")
        return []


def format_products(products):
    return '\n'.join(products)


def enviar_email(products):
    current_time = datetime.now().strftime('%d/%m/%Y - %H:%M')

    # criar integração com o outlook
    outlook = win32.Dispatch('outlook.application')

    # criar um e-mail
    email = outlook.CreateItem(0)

    email_pessoal = input("Para quem você gostaria de enviar? ")
    assunto = input("Qual será o assunto? ")

    if email_pessoal.rfind("@gmail.com"):
        nome = email_pessoal.split("@")
        email_pessoal = nome[0] + "@gmail.com"

    # Para quem vai o e-mail // Assunto da mensagem
    email.To = f'{email_pessoal}'
    email.Subject = f'{assunto} - {current_time}'
    email.HTMLBody = f"""
<p>{format_products(products)}</p>
    """

    email.Send()
    print("Email enviado com sucesso")