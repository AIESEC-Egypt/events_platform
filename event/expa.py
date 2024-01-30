import requests
import json
from graphqlclient import GraphQLClient
from datetime import datetime


def expa_sign_in_new(code_token):
    # URL TOKEN TO BE UPDATED
    r = requests.post(url="https://auth.aiesec.org/oauth/token?client_id=6a1dff3bc3c7fa6e1aea0b3d1e89683cfe1c9bf8517b82b26ecd0f34fa5c45db&client_secret=54460619eefb32285b26423a7e8c9cc903b8bb82c6efa394a08f261cfc8a1dbe&code=" +
                      code_token+"&grant_type=authorization_code&redirect_uri=https%3A%2F%2Faiesec.org.eg%2F")
    # print(r.content)
    token = json.loads(r.content.decode('utf-8'))['access_token']
    print('expa sign in ' + token)
    return token


def get_ep_info(access_token):
    client = GraphQLClient(
        'https://gis-api.aiesec.org/graphql?access_token=' + str(access_token))
    result = client.execute('''
            query Myquery {
                currentPerson {
                    id
                    first_name
                    last_name
                    full_name
                    gender
                    status
                    home_lc {
                        id
                        name
                        parent {
                            id
                            name
                        }
                    }
                    created_at
                    opportunity_applications_count
                    aiesec_email
                    email
                    contact_detail {
                        facebook
                        instagram
                        country_code
                        phone
                    }
                    member_positions {
                        role {
                            name
                        }
                        status
                    }
                }
            }

    ''')
    data = json.loads(result)
    data = data['data']['currentPerson']
    return data


def returndate(strdatetime):
    if strdatetime[0] == '-':
        strdatetime = strdatetime[1:]
    splitcreateddate = strdatetime.split('T')
    datecreated = splitcreateddate[0]
    datecreated = datecreated.split('-')
    createdat = datetime(int(datecreated[0]), int(
        datecreated[1]), int(datecreated[2]))
    # print createdat
    return createdat
