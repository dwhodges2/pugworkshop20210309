import requests
import time

# MET WEB API: https://metmuseum.github.io/

MET_BASE_URL = 'https://collectionapi.metmuseum.org/public/collection/v1'


def api_requester(base_url, endpoint):
    req = base_url + '/' + endpoint
    response = requests.get(req)
    # time.sleep(.05)
    return response.json()


def get_ids(begin_date, end_date, query):
    # Return ids for a date range and keyword
    query = 'search?dateBegin=' + \
        str(begin_date) + '&dateEnd=' + str(end_date) + '&' + query
    x = api_requester(MET_BASE_URL, query)
    the_ids = x['objectIDs']  # a list
    return the_ids


def get_item(id):
    return api_requester(MET_BASE_URL, 'objects/' + str(id))


def get_data(id_list):
    # Get a set of data for a list of IDs. Columns configured below.

    # Sort ids numerically
    id_list = list(map(int, id_list))
    id_list.sort()
    print(str(len(id_list)) + ' items found.')

    heads = ['objectID', 'title', 'objectWikidata_URL', 'objectBeginDate', 'objectEndDate', 'primaryImageSmall', 'artistDisplayName', 'artistWikidata_URL',
             'objectName', 'medium', 'accessionYear', 'terms', 'EXCLUDE?']
    the_data = [heads]
    for id in id_list:
        print(str(id))
        obj = get_item(id)
        # extract particular info from the item
        obj_info = [obj['objectID'], obj['title'], obj['objectWikidata_URL'],
                    obj['objectBeginDate'], obj['objectEndDate'], obj['primaryImageSmall'],
                    obj['artistDisplayName'], obj['artistWikidata_URL'],
                    obj['objectName'], obj['medium'], obj['accessionYear'],
                    parse_tags(obj['tags'])
                    ]
        the_data.append(obj_info)
    return the_data


def list_to_array(list):
    return [[x] for x in list]


def parse_tags(taglist):
    try:
        terms = [t['term'] for t in taglist]
    except TypeError:
        terms = []
    return '; '.join(terms)


def main():

    x = get_ids(1800, 1900, 'q=animals')
    print(len(x))
    y = get_item(241318)

    print(y)

    quit()


if __name__ == "__main__":
    main()
