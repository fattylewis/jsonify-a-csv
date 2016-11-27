# jsonify-a-csv

A nasty little script that will JSON'ify a CSV to upload into elasticsearch.

At the moment it requires some really stupid manual steps, like setting the filename and the fieldnames. Id like to automate this in the future.

Once you have "JSON'ified" your CSV, you can fire it over to elasticsearch with `curl -s -XPOST localhost:9200/INDEXNAME/_bulk --data-binary @'PATH TO MY.json'`
