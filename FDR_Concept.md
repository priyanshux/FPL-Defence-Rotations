### Fixture Difficulty Ratings Concept For Defenders (Below FAQs)

#### Please note that this FDR Concept is specifically for defenders, so don't confuse or assume it to be an overall FDR. Difficulty against teams like SHU is considered to be pretty low since they don't score many goals (they scored 5th least number of goals last season, less than BOU who got relegated).

#### Frequently Asked Questions (FAQs)

##### 1. What do these numbers on ratings display?
The difficulty level to get a clean sheet in the specific match. It doesn't necessarily mean to tell you a lot about the overall defence of a team. The chances of these ratings increasing drastically would be much higher in the case of conceding 1 goal from no goals (costs you 4 points), when compared to the case of conceding 5 goals from 1 goals (costs you 2 points).

##### 2. Does it mean it doesn't consider the attacking returns?
Honestly, no. Since attacking returns can be very player specific (For eg; Joe Gomez won't get as many returns as TAA) and even though Liverpool defenders have a greater probability of gaining moer points than Fulham's, it is tough to allot them into numbers. More so since you rarely rotate defenders using their attacking returns.

##### 3. How do you justify Fulham's difficulty level against Chelsea at home (3.7) with Liverpool's difficulty level against Chelsea away (4.0)? Won't it be much more difficult for Fulham?
If you go through the code of this repo, you'll realise what this model does is sort the ratings of the combination in ascending order before discarding the higher ratings. And hence, I have focused more on the ratings < 3.5 since any rating higher than 3.5 would irrespective of the team be shifted to the bench and let the teams with lower ratings play in the starting 11. As long as you stick to the ratings in the upper half on the results (which I strongly recommend you to), you wouldn't see any 3.5+ being considered in most cases.

##### 5. The Google Sheets attached is confusing me, how am I supposed to read it?
There are a total of 14 sheets attached inside the worksheet, which you should be able to navigate through from the bottom left icon in Google Sheets. The names are assigned in the format of GWxx_y_z where xx denotes until which GW, y denotes the number of players you wish to rotate and z denotes the number of players in your starting 11. For eg; GW15_4_3 denotes the list of GW1-15 for rotating 4 players where 3 of them start in the playing 11.

##### 4. Will you be creating such combinations during mid-season as well?
Absolutely, I plan on doing this twice more before the season ends. 


#### Initial FDR "Against" Using Attack Record (Ascending)

##### CATEGORY 1: Home 1 Away 1.5
(Eg, Playing against FUL away from your home has 1.5 FDR. i.e Fulham plays on their home)

FUL
CRY
WBA

##### CATEGORY 2: Home 1.5 Away 2

LEE
NEW
SHU
BHA
AVL

##### CATEGORY 3: Home 2 Away 2.5

BUR
EVE

##### CATEGORY 4: Home 2.5 Away 3

WHU
SOU

##### CATEGORY 5: Home 3 Away 3.5

WOL
ARS
TOT
LEI

##### CATEGORY 6: Home 3.5 Away 4

CHE
MUN

##### CATEGORY 7: Home 4.5 Away 5 (Intentional 1 FDR difference from Category 6)

LIV
MCI


#### Post Initial FDR "For" Using Defence Record

##### CATEGORY A: -0.2 AGAINST CATEGORY 1,2,3,4 & -0.1 AGAINST CATEGORY 5

LIV
MCI

##### CATEGORY B: -0.2 AGAINST CATEGORY 1,2,3

MUN
SHU
WOL
LEI
LEE
CHE

##### CATEGORY C: -0.1 AGAINST CATEGORY 1,2,3 & +0.1 AGAINST CATEGORY 6

ARS
TOT
BUR
BHA
SOU
CRY

##### CATEGORY D: +0.1 AGAINST CATEGORY 5 & +0.2 AGAINST CATEGORY 6
EVE
NEW
WHU
AVL
WBA
FUL

