import json
#Aritsts data: artists
artists =[
{'name': 'Robert Glasper',
 'description':"""Jazz pianist from Houston. 
  His pieces are influenced by a lot of different genres."""
},
{'name':'MF DOOM',
 'description':'Just remember ALL CAPS when you spell the man name. DOOM'
},
{'name':'Ryo Fukui',
 'description':'Jazz Pianist based in Sapporo (1948-2016)'}
]

#Albums data :albums
albums = [
{'al_title':'Black Radio',
 'al_description':'Best R&B Album at 55th Grammy Awards. Collab album with Shafiq Husayn, Eryka Babu, Lalah Hathaway, Lupe Fiasco, Bilal, Ledisi, We Are KING, Musiq Soulchild, Chrisette Michele,Meshell Ndegeocello, Stokley amd Yasiin Bey.',
 'year_released': 2012,
 'genre':'R&B'},
{'al_title':'ArtScience',
 'al_description':'Second Album released as Robert Glasper Experience ',
 'year_released': None,
 'genre':'Jazz'},
{'al_title':'Covered',
 'al_description':'His seventh Album recorded at Capitol Studio in Holywood and featuring song coverts of various artists.',
 'year_released':2015,
 'genre':'Jazz'},
{'al_title':'THE MOUSE & THE MASK',
 'al_description':"MF Doom's debut album as Danger Doom collaborating with Danger Mouse.",
 'year_released':2005,
 'genre':'Hiphop'},
{'al_title':'MM...FOOD',
 'al_description':'Fifth studio album as MF DOOM released by Rhymesayers. The title is anagram of MF DOOM.',
 'year_released':2004,
 'genre':'Hiphop'},
{'al_title':'Madvillainy',
 'al_description':'Prodcution with Madlib and this is the best sold album from his label, Stones Throw Records.',
 'year_released':2004,
 'genre':'Hiphop'},
{'al_title':'Scenery',
 'al_description':"Ryo Fukui's very first released album. Bass: Satoshi Denpo, Drums: Yoshinori Fukui.",
 'year_released':1976,
 'genre':'Jazz'},
{'al_title':'A Letter from Slowboat',
 'al_description':'Recorded at Sapporo jazz club, Slowboat on January 2015. Bass:Takumi Awaya, Drums: Ittetsu Takemura.',
 'year_released':2016,
 'genre':'Jazz'},
{'al_title':'Mellow Dream',
 'al_description':'Originally released in 1977. Bass: Satoshi Denpo, Drums: Yoshinori Fukui.',
 'year_released': None,
 'genre':'Jazz'}]

#songs data : songs 
songs=[] #adding converted data later on 
original_songs =[{'s_title':'Lift Off/ Mic Check','duration':'3:57','v_id':'LCK11o8EkJ4'},
{'s_title':'Afro Blue','duration':'5:07','v_id':'3-0JZlrk4xA'},
{'s_title':'Cherish The Day','duration':'5:51','v_id':'ZrL_SZjPclY'},
{'s_title':'Always Shine','duration':'5:22','v_id':'qOj_90wYK8Y'},
{'s_title':'Gonna Be Alright (F.T.B)','duration':'5:22','v_id':'nlWXsfjHeA8'},
{'s_title':'More Love','duration':'3:18','v_id':'-PPxEWkLiAs'},
{'s_title':'Ah Yeah','duration':'5:08','v_id':'oN0tFgLcp4g'},
{'s_title':'The Consequence Of Jealousy','duration':'6:07','v_id':'Q7lwMr6s-d0'},
{'s_title':'Why Do We Try','duration':'6:31','v_id':'GekMtAxxYj'},
{'s_title':'Black Radio','duration':'5:25','v_id':'IcIuGl1_3w8'},
{'s_title':'Letter To Hermione','duration':'4:51','v_id':'Yc0TmmmMlZs'},
{'s_title':'Smell Like Teen Spirit','duration':'7:24','v_id':'onXoreYFMhU'},
{'s_title':'This IS Not Fear','duration':'3:18','v_id':'HYSG3ieNIBg'},
{'s_title':'Thinkin Bout You','duration':'3:12','v_id':'d0WqdC0MUBU'},
{'s_title':'Day To Day','duration':'5:24','v_id':'1ljpTI6lJTA'},
{'s_title':'No One Like You','duration':'9:18','v_id':'z0yKuHIutLQ'},
{'s_title':'You And Me','duration':'4:38','v_id':'nqq3ZcjgNn4'},
{'s_title':'Tell Me A Bedtime Story','duration':'7:05','v_id':'LY_YflzoLUU'},
{'s_title':'Find You','duration':'6:46','v_id':'H4P_AeWFjI0'},
{'s_title':'In My Mind','duration':'6:07','v_id':'S4HIPl9OPQA'},
{'s_title':'Hurry Slowly','duration':'5:36','v_id':'4J-rDF-dK3E'},
{'s_title':'Written In Stone','duration':'5:01','v_id':'Zy3g2ryyQFU'},
{'s_title':"Let's Fall In Love",'duration':'7:33','v_id':'t3BHN0_HjTM'},
{'s_title':'Human','duration':'6:36','v_id':'W6ECLamZlAI'},
{'s_title':'Intro','duration':'2:12','v_id':'Kz8sEyalLa4'},
{'s_title':"I Don't Even Care",'duration':'7:42','v_id':'l9fJ97sF0qA'},
{'s_title':'Reckoner','duration':'5:07','v_id':'Lsl4TW3Hm1o'},
{'s_title':'Barangrill','duration':'7:06','v_id':'ibHN6_e8CNE'},
{'s_title':'In case You Forgot','duration':'13:01','v_id':'emIFOHMZiok'},
{'s_title':'So Beautiful','duration':'7:39','v_id':'GS2Y_CkaXP0'},
{'s_title':'The Worst','duration':'5:21','v_id':'2g6MsY8vD1A'},
{'s_title':'Good Morning','duration':'4:51','v_id':'_beYWQcDmN4'},
{'s_title':'Stella by Starlight','duration':'4:37','v_id':'I-VY-zs2eiY'},
{'s_title':'Levels','duration':'7:38','v_id':'jM3GvD3DKbw'},
{'s_title':'Got Over','duration':'2:07','v_id':'9qtMTr1q7l8'},
{'s_title':"I'm Dying of Thirst",'duration':'4:33','v_id':'QqJwk7GpYys'},
{'s_title':'El Chupa Nibre','duration':'2:36','v_id':'LpLW_g_Bj1w'},
{'s_title':'Sofa King','duration':'2:57','v_id':'z-wE-nYIgrw'},
{'s_title':'The Mask','duration':'3:12','v_id':'6L_JmYRGyBs'},
{'s_title':'Perfect Hair','duration':'2:03','v_id':'D0mEL2dp0RM'},
{'s_title':'Benzi Box','duration':'3:00','v_id':'DUaPECbl2rY'},
{'s_title':'Old School Rules','duration':'2:40','v_id':'gSWN0ZYVswY'},
{'s_title':'A.T.H.F(Aqua Teen Hunger Force)','duration':'3:03','v_id':'vA0z4Du00wM'},
{'s_title':'Basket Case','duration':'2:34','v_id':'kE-xDV3bmXU'},
{'s_title':'No Names','duration':'3:07','v_id':'XdNvVc3-3K0'},
{'s_title':'Crosshairs','duration':'2:26','v_id':'Eg_WWHBbkTI'},
{'s_title':'Mince Meat','duration':'2:32','v_id':'zP3lH3i1Xf4'},
{'s_title':'Vats of Urine','duration':'1:47','v_id':'aYXZcYP2JrI'},
{'s_title':'Space Hos','duration':'3:29','v_id':'FqXT7oOFFeA'},
{'s_title':'BaBa Bing','duration':'4:27','v_id':'PLTtmmefNxs'},
{'s_title':'Sofa King- Danger Mouse Remix','duration':'2:49','v_id':'EHqQSGlYiAE'},
{'s_title':"Space Ho's - Madlib Remix",'duration':'3:48','v_id':'qP14QTN4K-w'},
{'s_title':'Beef Rap','duration':'4:39','v_id':'WuxHWc-ZEXw'},
{'s_title':'Hoe Cakes','duration': '3:54','v_id':'MhND9Qqei8Y'},
{'s_title':'Potholderz feat.Count Bass D','duration':'3:20','v_id':'iU1L5dP2DhY'},
{'s_title':'One Beer','duration':'4:18','v_id':'6jd0VICL4og'},
{'s_title':'Deep Fried Frenz','duration':'4:59','v_id':'BoW0dZasOEE'},
{'s_title':'Poo-Putt Platter','duration':'1:13','v_id':'3gpabJMo0oE'},
{'s_title':'Filet-O-Rapper','duration':'1:03','v_id':'DUYWuYmXim'},
{'s_title':'Gumbo','duration':'0:49','v_id':'jaYO74GiLpY'},
{'s_title':'Fig Leaf Bi-Carbonate','duration':'3:19','v_id':'NqPK2bWZTOo'},
{'s_title':'Kon Karne','duration':'2:51','v_id':'E5s6jcuw6NM'},
{'s_title':'Guinesses feat.Angelika & 4ize','duration':'4:41','v_id':'erbJHWl2RkY'},
{'s_title':'Kon Quesco','duration':'4:00','v_id':'pGaAFLusB0M'},
{'s_title':'Rapp Snitch Knishes feat.Mr.Fantastik','duration':'2:52','v_id':'vPd5oLhCcpw'},
{'s_title':'Vomitspit','duration':'2:48','v_id':'LiOYkS877Xk'},
{'s_title':'Kookies','duration':'4:01','v_id':'DAYdO30Tcu4'},
{'s_title':'The Illest Villains','duration':'1:55','v_id':'zQ0yXh_ADlQ'},
{'s_title':'Accordion','duration':'1:58','v_id':'rpaonSDPw7Y'},
{'s_title':'Meat Grinder','duration':'2:11','v_id':'x8Ru8d0l_fU'},
{'s_title':'Bistro','duration':'1:07','v_id':'PRRMPtkmJjA'},
{'s_title':'Raid','duration':'2:30','v_id':'weWTuvdL-LQ'},
{'s_title':"America's Most Blunted",'duration':'3:54','v_id':'=jytxkJUM_7U'},
{'s_title':'Sickfit','duration':'1:21','v_id':'BTPRlerb1zQ'},
{'s_title':'Rainbows','duration':'2:51','v_id':'yDpaCiXJTEk'},
{'s_title':'Curls','duration':'1:35','v_id':'herNYSdJd0o'},
{'s_title':'Do Not Fire!','duration':'0:52','v_id':'iA2_XNCcygE'},
{'s_title':'Money Folder','duration':'3:02','v_id':'okYZpiuvQi4'},
{'s_title':'Shadows of Tomorrow','duration':'2:36','v_id':''},
{'s_title':'Operation Lifesaver aka Mint Test','duration':'1:30','v_id':''},
{'s_title':'Figaro','duration':'2:25','v_id':'A7_0vcjN-4c'},
{'s_title':'Hardcore Hustle','duration':'1:21','v_id':'PuaVf4f6lBM'},
{'s_title':'Strange Ways','duration':'1:51','v_id':'uSxlZQUqVPY'},
{'s_title':'Fancy Clown','duration':'1:55','v_id':'NYpXwlGT7XE'},
{'s_title':'Eye','duration':'1:57','v_id':'IbGLhsf1iLQ'},
{'s_title':'All Caps','duration':'2:10','v_id':'gSJeHDlhYls'},
{'s_title':'Great Day','duration':'2:16','v_id':'rS1cggllfig'},
{'s_title':'Rhinestone Cowboy','duration':'3:59','v_id':'s4iR668Ki3I'},
{'s_title':'It Could Happen To You','duration':'4:16','v_id':'-yX4S7exMtU'},
{'s_title':'I Want To Talk About Yout','duration':'6:32','v_id':'-T5jjfZtP5g'},
{'s_title':'Early Summer','duration':'10:44','v_id':'F5EFsUU7RRA'},
{'s_title':'Willow Weep For Me','duration':'7:43','v_id':'WiUzmWbDIFw'},
{'s_title':'Autumn Leaves','duration':'6:31','v_id':'XaAiNL-YJIs'},
{'s_title':'Scenery','duration':'5:31','v_id':'sr4vIBaumiM'},
{'s_title':'Sonora','duration':'7:34','v_id':'TdaJ3vpAXHs'},
{'s_title':'Stella by Stralight','duration':'3:45','v_id':'WHMDKKJbJlc'},
{'s_title':'Speak Low','duration':'5:35','v_id':'KlUI3sGWu7w'},
{'s_title':"Nobody Knows the Trouble I've seen",'duration':'6:38','v_id':'awsgBQaIcPg'},
{'s_title':'Old Coutry','duration':'7:03','v_id':'Yo6sbOixXF4'},
{'s_title':'Soltrane','duration':'6:42','v_id':'jcgXS21eS1Y'},
{'s_title':"Chasin'The Bird",'duration':'6:32','v_id':'awsgBQaIcPg'},
{'s_title':'Be My Love','duration':'3:39','v_id':'YAZEXBeMLPM'},
{'s_title':'Mellow Dream','duration':'9:51','v_id':'26Bv8WsV-0g'},
{'s_title':'My Foolish Heart','duration':'6:55','v_id':'UMDMcslei-8'},
{'s_title':'Baron Patato Blues','duration':'7:05','v_id':'15WuQ9N_7kg'},
{'s_title':"What's New",'duration':'5:59','v_id':'75OYtHZ-SeY'},
{'s_title':'Horizon','duration':'9:30','v_id':'hw5isR5yXT4'},
{'s_title':'My Funny Valentine','duration':'3:21','v_id':'gfJ0akPs3hk'}]
# with open ('songs.txt','r') as song_file:
#     songs_json = song_file.read()
#     imported_songs = json.loads(songs_json)

for song in original_songs:
    duration = song['duration']
    m,s = duration.split(':')
    converted_duration = int(m)*60 + int(s)
    converted_song ={
        's_title':song['s_title'],
        'duration':converted_duration, 
        'v_id' : song['v_id']}
    songs.append(converted_song)    
        
#cross table data
cross_table = []
#Making data for aritst X album X song cross table with for loop  

for i in range(1,37):
    if i in range (1,13): 
        cross_info  = {
        'artist_id' : 1,
        'album_id': 1, 
        'song_id': i
       }
        cross_table.append(cross_info)
    elif i in range(13,25):
        cross_info  = {
        'artist_id' : 1,
        'album_id': 2, 
        'song_id': i
       }
        cross_table.append(cross_info)
    elif i in range (25,38):
        cross_info  = {
        'artist_id' : 1,
        'album_id': 3, 
        'song_id': i
       }
        cross_table.append(cross_info)



for i in range(37,89):
    if i in range(37,53):
        cross_info  = {
        'artist_id' : 2,
        'album_id': 4, 
        'song_id': i
       }
        cross_table.append(cross_info)
    elif i in range(53,68):
        cross_info  = {
        'artist_id' : 2,
        'album_id': 5, 
        'song_id': i
       }
        cross_table.append(cross_info)
    elif i in range (68,89):
        cross_info  = {
        'artist_id' : 2,
        'album_id': 6, 
        'song_id': i
       }
        cross_table.append(cross_info)
 

artist3 = []
for i in range(89,109):
    if i in range(89,95):
        cross_info  = {
        'artist_id' : 3,
        'album_id': 7, 
        'song_id': i
       }
        cross_table.append(cross_info)
    elif i in range(95,103):
        cross_info  = {
        'artist_id' : 3,
        'album_id': 8, 
        'song_id': i
       }
        cross_table.append(cross_info)
    elif i in range (103,109):
        cross_info  = {
        'artist_id' : 3,
        'album_id': 9, 
        'song_id': i
       }
        cross_table.append(cross_info)

print (str(cross_table))
