'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

imp - not only cheapest but with constraint -- K STOPS ONLY 
so if in 2 stops - price is 400
but k =1 stop
and in 1 stop price is 700
i will return 700

find min price but with k stops

1. src and dst are not stops - middle point ar considered as stops
2. PQ - dist,node,stops
PQ DOES NOT WORK AS IT WILL PRIORITIZE MIN PRICE OVER K CONSTRAINt - it will incld min price with greater k instead of 
more price with less k
use Q - stops, node , cost - 
check <=k , till k is allowed staring from 0 as k can be dest

TC = E as onlye q  = flight size
'''
