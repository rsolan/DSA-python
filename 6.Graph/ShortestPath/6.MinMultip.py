'''
https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbkpzZF8yakhIMHlRa2pzX2hFdW9BU2hIczczQXxBQ3Jtc0trY0lmc1B5WDRvbWF3ZVlveVI3QWVPRFJnV2xaR0h0VlVvNFJZXzU3bWxSNUJsTmFIdHlfTUkxZXp1V2hDMmpxRy03MmIyTlhYcl9JMktqNnB1TXFpaGo0MWZnQ3RsdnlFWEhYekRZeW5YWTJjRVN2cw&q=https%3A%2F%2Fbit.ly%2F3AugzNb&v=_BvEJ3VIDWw


min mult to reach from start to end

TC 1 
    star = 3
    end = 30
    arr[2,5,7]
    
    start = 3   ( 3 MULT WITH 2,5,7 AND REPEAT...), INC MULT WITH 1 AT EAH STEP
    -> 3x2 = 6
    6x5 = 30
    
    we can multiply by 2 5 7 any number of time 
    count of mult = 2 -> ans
    if a no>10^5 - take mod

tc2 -
    start =7 , end = 66175
    arr = 3 4 65
    start = 7 -> 7x3 = 21->1
    21x3= 63-> 2
    63x65 = 4095 -> 3
    4095x65 = 266175%10^5 = 66175 - end  -> 4
    stop AND RETURN WHENVER UGET ANS --- AS MIN DIST EARLIER -- APPLY DIJKSTRA
    ans = 4 mult
'''

'''
MIN HEAP - steps,num  - NO NEED OF PQ , USE Q 
dist arr - inf - STORE STPE SNOT DIST
node - 0 to 9999 as mdo with 100000
TC -  o (10^5 x n) , n arr size
