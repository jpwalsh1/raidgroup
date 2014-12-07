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
        has_ring = json_profile['items']['finger1']['itemLevel'] == 680 or json_profile['items']['finger2']['itemLevel'] == 680
        has_ring = has_ring and 'Yes' or 'No'
        missing = ''

        try:
            neck = json_profile['items']['neck']['tooltipParams']['enchant']
        except KeyError:
            missing = missing + 'Neck, '

        try:
            back = json_profile['items']['back']['tooltipParams']['enchant']
        except KeyError:
            missing = missing + 'Cloak, '

        try:
            ring1 = json_profile['items']['finger1']['tooltipParams']['enchant']
        except KeyError:
            missing = missing + 'Ring 1, '

        try:
            ring2 = json_profile['items']['finger2']['tooltipParams']['enchant']
        except KeyError:
            missing = missing + 'Ring 2, '

        try:
            mh = json_profile['items']['mainHand']['tooltipParams']['enchant']
        except KeyError:
            missing = missing + 'Main Hand'

        if not missing:
           missing = 'None'

        print >>f, '%-20s ==> %10s; 680 Ring: %s; Missing Enchants: %s' % (json_profile['name'], str(json_profile['items']['averageItemLevelEquipped']), has_ring, missing)

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
