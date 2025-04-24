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

def champion(request, key):
    champion = Champion(key)
    name = champion.get_champion_name()
    title = champion.get_champion_title()
    bio = champion.get_champion_lore()
    lanes = champion.get_champion_lanes()
    resource = champion.get_champion_resource()
    range = champion.get_champion_range()

    abilites_names = champion.get_abilities_names()
    P_name = abilites_names["P"]
    Q_name = abilites_names["Q"]
    W_name = abilites_names["W"]
    E_name = abilites_names["E"]
    R_name = abilites_names["R"]

    abilites_sources = champion.get_abilities_sources()
    P_source = abilites_sources["P"]
    Q_source = abilites_sources["Q"]
    W_source = abilites_sources["W"]
    E_source = abilites_sources["E"]
    R_source = abilites_sources["R"]

    abilites_descs = champion.get_abilities_description()
    P_desc = abilites_descs["P"]
    Q_desc = abilites_descs["Q"]
    W_desc = abilites_descs["W"]
    E_desc = abilites_descs["E"]
    R_desc = abilites_descs["R"]

    
    images = ChampionImages(key)
    images = images.get_all_champion_images_sources()
    icon = images[0]
    loading = images[1]
    splash = images[2]

    context = {
        'key': key,
        'name': name,
        'title': title,
        'bio': bio,
        'lanes': lanes,
        'resource': resource,
        'range': range,
        'P_name': P_name,
        'Q_name': Q_name,
        'W_name': W_name,
        'E_name': E_name,
        'R_name': R_name,
        'P_source': P_source,
        'Q_source': Q_source,
        'W_source': W_source,
        'E_source': E_source,
        'R_source': R_source,
        'P_desc': P_desc,
        'Q_desc': Q_desc,
        'W_desc': W_desc,
        'E_desc': E_desc,
        'R_desc': R_desc,
        'icon': icon,
        'loading': loading,
        'splash': splash        
    }
    return render(request, template_name='champion.html', context=context)