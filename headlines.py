from flask import Flask, render_template, request, redirect, url_for
import feedparser

app = Flask(__name__)

pubs = {"bbc"		: "http://feeds.bbci.co.uk/news/rss.xml",
		"cnn"		: "http://rss.cnn.com/rss/edition.rss",
		"fox"		: "http://feeds.foxnews.com/foxnews/latest",
		"iol"		: "http://rss.iol.io/iol/all-content-feed"
		}
		
app.jinja_env.globals["pubs"] = pubs

@app.route("/")
def get_news():
	query = request.args.get("publication")
	if not query:
		query = "bbc"
	elif query.lower() not in pubs:
		return redirect(url_for("get_news", publication="bbc"))
	else:
		query = query.lower()
		
	url = pubs[query]
	entries = feedparser.parse(url)["entries"]
	return render_template("home.html", entries=entries,
		query=query)


if __name__ == "__main__":
	app.run(debug=True)
