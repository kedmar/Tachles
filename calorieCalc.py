import requests

import re

from recipe_scrapers import scrape_me


a = input('Insert a link for a recipe. Make sure it\'s in the verified website list\n')
a = a.replace("'", "")
scrape_me = scrape_me(a)

def get_ing(a):

    x = (scrape_me.ingredients())

    from pprint import pprint
    pprint(x)
    return x

ingList = get_ing(a)

def get_cals(ingList):
    calories_sum = 0
    for x in ingList :
        ingredient = x
        ingredient = ingredient.replace(' ', '+').replace('-', '+')

        url = 'https://www.google.co.il/search?q={}+calories'.format(ingredient)

        r = requests.get(url)
        content = r.content.decode('ANSI')

        pattern = ">*[0-9]+ [<b>]*[cC]alories"

        res = re.findall(pattern, content)
        if res:
            calorie_str = res[0]
            calorie_number = re.findall("[0-9]+", calorie_str)
            final = float(calorie_number[0])
            calories_sum += final
    if calories_sum == 0:
        return 50
    return calories_sum

print("\nthis recipe is ")
print(get_cals(ingList))
print("calories for all the servings\n")
print(scrape_me.instructions())