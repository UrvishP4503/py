import requests
import hashlib


def send_api_request(hashed_password: str):
    url = "https://api.pwnedpasswords.com/range/" + hashed_password
    result = requests.get(url)
    if result.status_code != 200:
        raise RuntimeError(f"{result.status_code}")
    return result


def get_password_data(api_response, tail_of_hash):
    hash_list = (line.split(":") for line in api_response.text.splitlines())
    number_of_passwords = 0
    for i, j in hash_list:
        # print(f"{i} {j}")
        if tail_of_hash in i:
            number_of_passwords += int(j)
    return number_of_passwords


def get_password_count(password: str):
    sha1_hash_of_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5char, tail = sha1_hash_of_password[:5], sha1_hash_of_password[5:]
    response = send_api_request(first5char)
    return get_password_data(response, tail)


def main():
    state = True
    while state:
        user_password = input("Enter your password: ")
        num = get_password_count(user_password)

        if num == 0:
            print(f"Use {user_password}.It is safe, your password was never in data breach")
        else:
            print(f"Your password was in {num} data breaches, you should not use it")

        ans = input("Do you want to enter another password[Y/n]")

        valid_yes_options = {'y', 'yes', 'yeah', 'yep'}

        if ans.lower() in valid_yes_options:
            state = True
        else:
            state = False


main()
