#P = 18148148525895061883254460474894734506089518243573390311471625130391145646955552605907676262104969803401000011459982603291129842110214439800024132387527241371226196264554217486921255356478153859678675436049302765923005464271111581993885733158477251041116077570167723200583115997178695605052756784467564752529090025719148442134546603302595162189622279097249882560406317755150297446478696240036707272197845682544981011711745935059559738869726229895508734130144266442787879663249668989548485715987541994757458818700395901463238238183149300581379836399585601653759346189633028027462229026768399876005810959869755488343889
#S = 278307578365594447303553374319136214204595290024709911407663296891446891158652928413490376411270415264441277658990540695814884774678269220487151964625560657626422982058446618197590515356517366161707799530240971675976105526371994720455786850715814105504502451995467096696303232543885591787460881210785166594030
'''
n1 = 17102599847176672076700631995135018427382737286943928858873443625095649656322495730054828651175059657053221857162848547629647589616682663375890224554867919340248145766746400848944098609378232109671443027780190695156267250522921327864130481331818499479580603439674352424600030979547562647274685451776008566707358319589617222548480245608823385398933699387185380062774948282786359255895756531590184144677192883733976830974994402706254075484564475839363422289175180792584998490855993485178354446941404739616678463873117384516515663793563954118096218145691693449045697934758753545865521559316608665415989507490943345485939

n2 = 17102599847176672076700631995135018427382737286943928858873443625095649656322495730054828651175059657053221857162848547629647589616682663375890224554867919340248145766746400848944098609378232109671443027780190695156267250522921327864130481331818499479580603439674352424600030979547562647274685451776008566707884647571897771862868798190084436160719808986002251240259744478253829018142125053409044182469272387618653218533466430329449656869171169994661158935035522553363009062144456368647021094578859160569170378777247328605896508499659198109761776813651847412168613713670036774133597069624843027679007301910810705499343 
P = n1
S = (n2-n1-4)/2

import math
#from decimal import Decimal
#p = (S + (Decimal(pow((Decimal(pow(S,2)) - 4*P),(-2)))))/2
#q = (S - (Decimal(pow((Decimal(pow(S,2)) - 4*P),(-2)))))/2
#q =  (S - ((S**2 - 4*P)**(1/2)))/2

#print S
#print P
print (S**2-4*P)**(0.5)
#print "p = ",p
#print "q = ",q

#print "n = ", Decimal(p*q)
#print (Decimal(S**2) - 4*P)#**(-2)'''
from Crypto.Util.number import long_to_bytes 
m = 10907013987426429856879217337539489830276192613316631102146241420739731050743258519541320528992674585248859931389949921846797101357238668009428504586487786905018390220189787283581278327492232364572969701237431802918291488639085158328548690856569009602461483763557983057876880010402672941405769198538029425157465850175171180694463060943288542471052493092425881941193659208042562295601985294425296672406445439391278641470334312200252302791390871648994931470390143726383186811923601370028440499521838345796864590665273410598348110043670460160933863377009556012245461206093499606717323425126090496633256964470658430381221

print long_to_bytes(m)

