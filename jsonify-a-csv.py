#!/bin/python2
import csv
import json

csvfile = open('movie.csv', 'r')
jsonfile = open('movie-comma.json', 'w')

fieldnames = ("id","Title","Plot","Tagline","RatingVotes","Rating","Writers","YearReleased","IMDBID","Runtime","MPAARating","Genre","Director","OriginalMovieTitle","Studio","TrailerURL","Country","FilePath")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    jsonfile.write('{"index":{"_index":"movies","_type":"test"}}\n')
    json.dump(row, jsonfile)
    jsonfile.write('\n')
