Stamp Matching Solution
========

The solution I chose was to calculate the euclidean distances between each node on two graphs--one of the real stamp of one for the coordinates we're testing with--and then compare those distances. Some time was spent wrestling with the cairo library to get it to plot images of the graphs with the igraph library. After those were plotted (see [graph_samples.png](https://github.com/obimod/stamping/blob/master/graph_samples.png) for an example), I was able to see why my solution wasn't working. There was an error margin! After testing a few values (10, 15, and then 20) I discovered that an error margin of 20 was the sweet spot for the given dataset.

Euclidean distances on my MacBook Air (1.8GHz i7 & hosting locally):
  - 50,000 executions took 9.94717907906 seconds
  - 100,000 executions took 20.6022851467 seconds
  - 200,000 executions took 40.0098121166 seconds

I'd like to implement a stamp discovery process soon. But for now, here's some tests:
- [http://creativeroots.io/snowshoe?dots=733,1372,903,748,783,487,117,1209,335,358](http://creativeroots.io/snowshoe?dots=733,1372,903,748,783,487,117,1209,335,358) < match!
- [http://creativeroots.io/snowshoe?dots=833,1372,903,748,783,487,117,1209,335,358](http://creativeroots.io/snowshoe?dots=833,1372,903,748,783,487,117,1209,335,358) < no match

Service URL: http://creativeroots.io/snowshoe

Problem
========

We'd like you to write a toy SnowShoe tag recognizer program that can reliably identify the unique "dot pattern" of one of our standard SnowShoe developer tags. We'll provide you with a geometric tag definition and a small data set of potential tag matches.

Here's the tag definition:

  [[238,276],[698,324],[853,574],[148,1146],[786,1215]]

That's an array of five two-dimensional points expressed as a JSON string.

And here's what one potential match looks like:

  curl -g http://127.0.0.1:8086/?dots=795,1411,854,568,696,328,141,1138,238,276

So, also a list of five two-dimensional points, but rather than JSON, it's just CSV. The first two numbers are the X and Y coordinates of one point, the second two are the X and Y coordinates of another point, etc.

We'd like you to design and implement a tag recognition algorithm, then put your algorithm online as a live web service that we can make requests to Please feel free to use any languages or toolkits that you like. Your web service should accept an HTTP GET request of the following format:

  http://<your-service-url-and-path>?dots=<potential match line>

And return a single line in the body of the HTTP response. Either "A\n" for a match, or "_\n" for no match.

Don't worry too much about optimization or robustness. 
When we go over the completed exercise with you we'll talk about both topics. 
But we don't expect you to write production-quality code, here. 
Feel free to just comment any chunk of code that could be rewritten to be faster, or safer, or more secure. :)

When you're finished, please send us the URL for your web service and a link to download or browse all of the code you've written.

When you send us your URL, we'll do something like this from a command line ...

  cat potential-matches.csv | while read -r LINE ; do curl -g http://$YOUR_URL/?dots=$LINE ; done

We expect that command to return us a bunch of As and _s. Like this ...

  _
  A
  _
  _
  (etc...)

In all, you should find ten instances of the "A" tag. If you get really into this problem and have extra time, you might notice that most of the "unrecognized" lines in the potential-matches.csv file actually correspond to a single additional tag. 
If you want to, feel free to extend your web service to recognize that tag (the "B" tag) as well, and to provide us with a tag definition file for that tag. But don't feel that you need to do this extra work. We just stuck the other matches in for fun.

Here's the complete set of 30 potential matches:

--
795,1411,854,568,696,328,141,1138,238,276
733,1372,903,748,783,487,117,1209,335,358
430,1368,668,1134,558,547,794,779,312,894
870,937,628,692,64,801,275,565,386,1046
526,650,102,857,781,794,482,1648,1044,1374
728,1422,762,779,587,701,89,1389,133,508
116,889,126,1227,638,1547,300,1558,534,1127
320,888,339,1229,857,1537,517,1557,744,1121
817,1040,771,399,579,572,178,1078,108,205
874,1312,792,677,594,456,239,1394,130,513
890,1181,654,940,74,1064,303,831,423,1304
990,906,781,646,187,703,439,488,516,980
869,938,627,693,63,800,276,566,385,1047
785,160,335,110,951,413,241,985,883,1055
92,787,355,990,926,804,722,1065,541,610
41,776,286,976,855,767,652,1040,474,581
494,344,62,494,733,500,344,1327,947,1116
702,369,244,338,863,622,167,1207,810,1265
91,853,736,848,969,661,86,209,964,203
892,1047,879,700,364,400,703,375,470,809
64,1125,698,1149,934,980,86,474,956,514
464,318,1007,649,134,868,165,1157,569,1406
439,397,1009,680,128,983,233,1067,652,1471
301,137,935,266,180,779,316,1038,771,1128
64,605,661,416,211,1218,478,1345,924,1249
796,1360,740,1031,199,778,532,720,346,1177
193,1128,538,1083,806,551,852,877,402,682
0,1135,254,1343,822,1144,622,1418,441,953
119,719,363,937,943,792,724,1039,585,563
53,896,296,1103,870,913,662,1180,492,716
----

We're not trying to be tricky. It's very possible that the explanation above isn't as readable as it should be. We also understand that this class of problem might be new to you. Two of the skills we value are communication and teamwork. So if anything here isn't clear, or if you get stuck, please feel free to send mail asking for clarification or help. (We mean it!)
