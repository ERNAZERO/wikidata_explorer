from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def search_wikidata(search_term):
    url = "https://query.wikidata.org/sparql"
    query = f"""
    SELECT ?item ?itemLabel ?itemDescription WHERE {{
      SERVICE wikibase:mwapi {{
        bd:serviceParam wikibase:endpoint "www.wikidata.org";
        wikibase:api "EntitySearch";
        mwapi:search "{search_term}";
        mwapi:language "de".
        ?item wikibase:apiOutputItem mwapi:item.
      }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "de". }}
    }}
    LIMIT 20
    """
    headers = {
        "Accept": "application/sparql-results+json"
    }
    response = requests.get(url, params={"query": query}, headers=headers)
    data = response.json()

    results = []
    for item in data["results"]["bindings"]:
        results.append({
            "id": item["item"]["value"].split("/")[-1],
            "label": item["itemLabel"]["value"],
            "description": item.get("itemDescription", {}).get("value", "")
        })
    return results


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        search_term = request.form.get("search")
        results = search_wikidata(search_term)
    # print(results)
    return render_template("index.html", results=results)


def get_entity_details(qid):
    url = "https://query.wikidata.org/sparql"
    query = f"""
    SELECT ?propertyLabel ?value ?valueLabel WHERE {{
      wd:{qid} ?prop ?value .
      ?property wikibase:directClaim ?prop .
      OPTIONAL {{ ?value rdfs:label ?valueLabel . FILTER(LANG(?valueLabel) = "de") }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "de". }}
    }}
    LIMIT 200
    """
    headers = {"Accept": "application/sparql-results+json"}
    response = requests.get(url, params={"query": query}, headers=headers)
    data = response.json()

    grouped = {}
    image_url = None

    for item in data.get("results", {}).get("bindings", []):
        prop = item.get("propertyLabel", {}).get("value", "Unbekannt")

        val = item.get("valueLabel", {}).get("value")
        if not val:
            val = item.get("value", {}).get("value", "—")

        if not image_url and prop.lower() in ["bild", "flagge (abbildung)", "wappenbild"]:
            image_url = val

        grouped.setdefault(prop, []).append(val)

    return grouped, image_url


def get_entity_label_and_description(qid):
    url = "https://query.wikidata.org/sparql"
    query = f"""
    SELECT ?itemLabel ?itemDescription WHERE {{
      wd:{qid} rdfs:label ?itemLabel.
      OPTIONAL {{ wd:{qid} schema:description ?itemDescription. }}
      FILTER(LANG(?itemLabel) = "de")
      FILTER(LANG(?itemDescription) = "de")
    }}
    LIMIT 1
    """
    headers = {"Accept": "application/sparql-results+json"}
    response = requests.get(url, params={"query": query}, headers=headers)
    data = response.json()
    bindings = data.get("results", {}).get("bindings", [])
    if bindings:
        item = bindings[0]
        label = item.get("itemLabel", {}).get("value", "")
        description = item.get("itemDescription", {}).get("value", "")
        return label, description
    return qid, ""


@app.route("/details/<qid>")
def details(qid):
    properties, image_url = get_entity_details(qid)
    label, description = get_entity_label_and_description(qid)
    return render_template("details.html", label=label, description=description, image_url=image_url, properties=properties)


if __name__ == '__main__':
    app.run()


