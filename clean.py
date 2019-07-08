import json
with open('comuni.json') as json_file: 
    data = json.load(json_file)
    comuni_veneto = []
    # count = 0
    for p in data:
        if (p["regione"]["codice"] == "05"):
            comuni_veneto.append(p)
            # print('Name: ' + p["nome"])
            # count += 1
    # print(count)
    with open('comuni-veneto.json', 'w', encoding='utf-8') as f:
        json.dump(comuni_veneto, f, ensure_ascii=False, indent=4)