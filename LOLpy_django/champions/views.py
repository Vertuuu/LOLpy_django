from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from LOLpy_Vertuuu.LOLpy import Champions, Champion, ChampionImages

def champions(request):
    all_champions = Champions().get_champions_keys()
    champions_list = []
    for champion in all_champions:
        champion = Champion(champion)
        key = champion.get_champion_key()
        name = champion.get_champion_name()
        title = champion.get_champion_title()
        source = ChampionImages(key,  region="en-US").get_icon_source()
        champion_data = {
            "key": key,
            "name": name,
            "title": title,
            "icon_path": source
            }
        champions_list.append(champion_data)
    context = {
        "champions": champions_list
    }
    template = loader.get_template('champions.html')
    return HttpResponse(template.render(context=context))
