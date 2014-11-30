#!/usr/bin/env python
# coding: utf8

import urllib2, json, codecs

## Edit this section for your raid ##
server = 'Malganis'
region = 'us'
tanks = ['Tank1']
healers = ['Healer1']
rdps = ['Ranged1', 'Ranged2']
mdps = ['Melee1', 'Melee2']

# edit the path to the file you would like the output
f = codecs.open ('/tmp/raidgroup.txt', encoding='utf-8', mode='w+')

## Do not edit below this line ##

def getChar (name):
        url = 'http://' + region + '.battle.net/api/wow/character/' + server + '/' + name + '?fields=items'
        response = urllib2.urlopen(url)
        json_profile = json.load(response)
        print >> f, '%-20s ==> %20s' % (json_profile['name'], str(json_profile['items']['averageItemLevel']))

print >> f,  "Tanks\n"

for char in tanks:
        getChar(char)

print >> f, "\nHealers\n"

for char in healers:
        getChar(char)

print >> f, "\nRanged DPS\n"

for char in rdps:
        getChar(char)

print >> f,"\nMelee DPS\n"

for char in mdps:
        getChar(char)

f.close
