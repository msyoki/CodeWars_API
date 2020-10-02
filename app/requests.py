import urllib.request,json
from .models import Challenge



#Getting the api_key
api_key = None

#Getting the base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['CODEWARS_API_KEY']
    base_url = app.config['CODEWARS_BASE_URL']

def get_challenges(slug):
    '''
    function that gets json response to our request
    '''
    get_challenges_url = base_url.format(slug,api_key)

    with urllib.request.urlopen(get_challenges_url)as url:
        get_challenges_data = url.read()
        get_challenges_response =json.loads(get_challenges_data)

        challenge_results=None

        if get_challenges_response['description']:
            challenge_results_list = get_challenges_response[{'id','slug','category','publishedAt','languages','description'}]
            challenge_results = process_results(challenge_results_list)

    return challenge_results

def process_results(challenge_list):
    challenge_results=[]
    for challenge_item in challenge_list:
        id= challenge_item.get('id')
        slug= challenge_item.get('slug')
        category= challenge_item.get('category')
        publishedAt=challenge_item.get('publishedAt')
        languages=challenge_item.get('languages')
        description = challenge_item.get('description')

        if description:
            challenge_object=Challenge(id,slug,category,publishedAt,languages,description)
            challenge_results.append(challenge_object)

    return challenge_results