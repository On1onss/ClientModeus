import requests


class ModeusToken:

    def __init__(self, login, password, url):
        self.login = login
        self.password = password
        self.url = url

    def get_token(self):
        values = []

        with requests.Session() as getSAMLRequest:
            # URL example: https://foo-auth.modeus.org/oauth2/authorize?client_id=
            SAMLRequest = getSAMLRequest.get(self.url)

            with requests.Session() as getSAMLResponse:

                auth_payload = {"UserName": self.login,
                                "Password": self.password,
                                "AuthMethod": "FormsAuthentication"
                                }

                get_MSISAuth_coockie = getSAMLResponse.post(SAMLRequest.url, data=auth_payload)

                msis_auth_headers = {
                    "Cookie": get_MSISAuth_coockie.headers["Set-Cookie"].split(";")[0],
                }

                SAMLRespone = getSAMLResponse.get(SAMLRequest.url, headers=msis_auth_headers).text.split()

                get_commonauth_url = get_MSISAuth_coockie.text.split()

                for element in get_commonauth_url:
                    if "action" in element:
                        commonauth_url = element.split('"')[1]
                        break

                for value in SAMLRespone:
                    if "value" in value:
                        values.append(value)

                with requests.Session() as getToken:

                    data = {
                        "SAMLResponse": f'{values[0].split("=")[1][1:-1]}',
                        "RelayState": f'{values[1].split("=")[1][1:-1]}',
                        "submit": "Submit"
                    }

                    token = getToken.post(commonauth_url, data=data)

                    return f"Bearer {token.url.split("&")[0].split("=")[1]}"
