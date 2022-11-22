### Functions calculate gradient
import numpy as np



test_data= [[(1260, 277, 0.9320590645074844, 0),
  (319, 279, 0.9424398392438889, 0),
  (1097, 281, 0.8861296325922012, 0),
  (715, 282, 0.922205924987793, 0),
  (924, 287, 0.8656792491674423, 0),
  (1894, 291, 0.7527836412191391, 0),
  (1599, 301, 0.9368326216936111, 0),
  (1530, 303, 0.9114391356706619, 0),
  (542, 304, 0.9481390416622162, 0)],
 [(1242, 322, 0.753047913312912, 1),
  (317, 326, 0.8544386625289917, 1),
  (709, 326, 0.7316017001867294, 1),
  (1077, 326, 0.6437540650367737, 1),
  (1858, 326, 0.6873193085193634, 1),
  (902, 334, 0.7649941891431808, 1),
  (1490, 337, 0.767950639128685, 1),
  (1572, 338, 0.7793675661087036, 1),
  (533, 345, 0.8734769374132156, 1)],
 [(292, 325, 0.8250653296709061, 2),
  (1238, 329, 0.7833253890275955, 2),
  (1866, 329, 0.7912263423204422, 2),
  (1082, 330, 0.7113407999277115, 2),
  (698, 331, 0.8090753853321075, 2),
  (915, 339, 0.7913873493671417, 2),
  (1587, 343, 0.8643331378698349, 2),
  (514, 347, 0.8383287042379379, 2),
  (1497, 350, 0.651117742061615, 2)],
 [(326, 375, 0.4216989576816559, 3),
  (758, 376, 0.8987951576709747, 3),
  (1283, 379, 0.9403104484081268, 3),
  (970, 381, 0.8697373121976852, 3),
  (1143, 381, 0.7058737426996231, 3),
  (1634, 381, 0.8637414276599884, 3),
  (263, 387, 0.38892374373972416, 3),
  (1914, 389, 0.93159519135952, 3),
  (1554, 394, 0.8086288422346115, 3),
  (555, 396, 0.8864113092422485, 3)],
 [(1136, 313, 0.7159889340400696, 4),
  (347, 315, 0.4781347597017884, 4),
  (762, 319, 0.8633318692445755, 4),
  (965, 325, 0.7757578641176224, 4),
  (1297, 330, 0.8734845966100693, 4),
  (1933, 330, 0.9437475502490997, 4),
  (1633, 332, 0.7889433056116104, 4),
  (1555, 341, 0.6844360455870628, 4),
  (573, 344, 0.802033394575119, 4),
  (286, 371, 0.154358985950239, 4),
  (1759, 440, 0.2134254620759748, 4)],
 [(1248, 317, 0.5169245600700378, 5),
  (1067, 322, 0.4423528891056776, 5),
  (1851, 322, 0.5215321481227875, 5),
  (720, 324, 0.5604431182146072, 5),
  (1481, 324, 0.6283545345067978, 5),
  (343, 327, 0.7334063351154327, 5),
  (891, 330, 0.5502764880657196, 5),
  (1559, 333, 0.5003914833068848, 5),
  (552, 343, 0.7968787848949432, 5)],
 [(1435, 360, 0.45726205222308636, 6),
  (1267, 363, 0.10693401843309402, 6),
  (1120, 364, 0.11090758163481951, 6),
  (1896, 365, 0.10395606094971299, 6),
  (1897, 366, 0.1039862111210823, 6),
  (749, 372, 0.16990303015336394, 6),
  (1537, 376, 0.10302802920341492, 6),
  (348, 380, 0.6641469150781631, 6),
  (556, 394, 0.23378879763185978, 6)],
 [(757, 313, 0.27154092490673065, 7),
  (1130, 315, 0.14245658414438367, 7),
  (349, 318, 0.28838649298995733, 7),
  (958, 323, 0.17533467593602836, 7),
  (1288, 324, 0.19084834167733788, 7),
  (1929, 324, 0.22212159540504217, 7),
  (1622, 328, 0.1470886580646038, 7),
  (572, 337, 0.2917172908782959, 7),
  (1551, 339, 0.18804483115673065, 7),
  (528, 401, 0.1911509376950562, 7),
  (1759, 444, 0.23112975718686357, 7)],
 [(1179, 424, 0.6723505407571793, 8),
  (252, 437, 0.6843089163303375, 8),
  (642, 437, 0.7243667542934418, 8),
  (835, 438, 0.718565970659256, 8),
  (471, 444, 0.7409996688365936, 8),
  (1535, 447, 0.6913222372531891, 8),
  (1798, 448, 0.7001354992389679, 8),
  (1416, 451, 0.680016927421093, 8),
  (1016, 462, 0.6664675772190094, 8)],
 [(1177, 519, 0.7179494649171829, 9),
  (1589, 527, 0.7894521206617355, 9),
  (506, 528, 0.7372951656579971, 9),
  (884, 528, 0.7721498757600784, 9),
  (1474, 539, 0.822143629193306, 9),
  (264, 540, 0.882867231965065, 9),
  (669, 541, 0.8138717263936996, 9),
  (1853, 541, 0.7956452518701553, 9),
  (1075, 563, 0.6714834868907928, 9)],
 [(1180, 622, 0.7559709995985031, 10),
  (1568, 622, 0.7180686444044113, 10),
  (501, 627, 0.7555235028266907, 10),
  (851, 633, 0.7996207028627396, 10),
  (632, 637, 0.8148736506700516, 10),
  (234, 640, 0.8380218297243118, 10),
  (1806, 641, 0.7593495845794678, 10),
  (1481, 649, 0.602430559694767, 10),
  (1067, 680, 0.5030632689595222, 10)],
 [(1202, 429, 0.6237583756446838, 11),
  (836, 433, 0.4967755787074566, 11),
  (670, 442, 0.7211175560951233, 11),
  (1518, 442, 0.5826951414346695, 11),
  (1779, 442, 0.5744941383600235, 11),
  (299, 447, 0.7701146900653839, 11),
  (499, 447, 0.7608373463153839, 11),
  (1442, 451, 0.640153706073761, 11),
  (1038, 460, 0.5570063814520836, 11)],
 [(1228, 520, 0.8324708193540573, 12),
  (906, 521, 0.766789123415947, 12),
  (519, 529, 0.6726593375205994, 12),
  (1499, 533, 0.8199637085199356, 12),
  (1573, 534, 0.6100734025239944, 12),
  (696, 537, 0.8093263655900955, 12),
  (1840, 542, 0.6741794347763062, 12),
  (325, 544, 0.8504061847925186, 12),
  (1108, 555, 0.7458282560110092, 12)],
 [(1527, 591, 0.5173303335905075, 13),
  (1423, 606, 0.6972686722874641, 13),
  (839, 609, 0.6861284822225571, 13),
  (468, 610, 0.705693319439888, 13),
  (1207, 618, 0.7040615081787109, 13),
  (1784, 626, 0.6707060933113098, 13),
  (1027, 633, 0.6950665339827538, 13),
  (1469, 633, 0.1811701557599008, 13),
  (1473, 636, 0.18397036427631974, 13),
  (697, 637, 0.739371120929718, 13),
  (333, 642, 0.856922909617424, 13)],
 [(309, 274, 0.9230422824621201, 14),
  (1249, 274, 0.9427110254764557, 14),
  (704, 277, 0.9234891384840012, 14),
  (1085, 278, 0.8650520294904709, 14),
  (912, 283, 0.8848685175180435, 14),
  (1883, 286, 0.6860561072826385, 14),
  (1587, 296, 0.9363832026720047, 14),
  (1519, 298, 0.8692942559719086, 14),
  (533, 299, 0.9576709419488907, 14)],
 [(1263, 269, 0.9311244487762451, 15),
  (326, 271, 0.9320827275514603, 15),
  (1099, 271, 0.7650206983089447, 15),
  (719, 273, 0.9264536798000336, 15),
  (925, 279, 0.7793965488672256, 15),
  (1893, 281, 0.5357882753014565, 15),
  (1600, 293, 0.7813887298107147, 15),
  (1529, 294, 0.615262757986784, 15),
  (550, 298, 0.9638818502426147, 15)],
 [(299, 282, 0.5997577458620071, 16),
  (691, 286, 0.7368618845939636, 16),
  (1066, 286, 0.7493544518947601, 16),
  (1231, 287, 0.914355456829071, 16),
  (1864, 291, 0.6595870703458786, 16),
  (896, 295, 0.8027662634849548, 16),
  (1495, 305, 0.897755429148674, 16),
  (1566, 306, 0.8701214790344238, 16),
  (519, 310, 0.9154583364725113, 16)],
 [(338, 276, 0.7099217027425766, 17),
  (731, 277, 0.3601395785808563, 17),
  (558, 308, 0.522162102162838, 17)]]

test_data_2= [[(1231, 553, 0.7470061779022217, 0),
  (2008, 553, 0.9628499299287796, 1),
  (1634, 561, 0.9031820893287659, 2),
  (405, 566, 0.9154623299837112, 3),
  (1022, 574, 0.939346969127655, 4),
  (1737, 574, 0.9253786504268646, 5),
  (1384, 575, 0.9642678648233414, 6),
  (638, 588, 0.9191864430904388, 7),
  (824, 592, 0.9214871674776077, 8)],
 [(1222, 595, 0.6549539566040039, 9),
  (2005, 605, 0.9356071203947067, 10),
  (1745, 612, 0.8947285562753677, 11),
  (1627, 615, 0.7916442006826401, 12),
  (412, 617, 0.8084588646888733, 13),
  (1378, 618, 0.9175247699022293, 14),
  (1031, 628, 0.8512867391109467, 15),
  (652, 634, 0.9584159553050995, 16),
  (839, 637, 0.7987030744552612, 17)],
 [(1208, 591, 0.5313038006424904, 18),
  (1978, 601, 0.853596493601799, 19),
  (1350, 611, 0.8821698129177094, 20),
  (1723, 611, 0.8484141528606415, 21),
  (405, 612, 0.5870251879096031, 22),
  (1600, 616, 0.7298012971878052, 23),
  (1019, 629, 0.7266322076320648, 24),
  (636, 631, 0.8388900458812714, 25),
  (841, 636, 0.5855215042829514, 26)],
 [(1577, 579, 0.5385579094290733, 27),
  (1915, 586, 0.6240787655115128, 28),
  (352, 600, 0.505972683429718, 29),
  (1652, 602, 0.3228227198123932, 30),
  (1156, 607, 0.30555979162454605, 31),
  (1291, 612, 0.598194882273674, 32),
  (588, 629, 0.6793903112411499, 33),
  (954, 644, 0.5319601148366928, 34),
  (768, 659, 0.4596332535147667, 35),
  (1962, 683, 0.2674769349396229, 36)],
 [(1536, 535, 0.5254878997802734, 37),
  (303, 553, 0.5581148937344551, 38),
  (1612, 554, 0.1447592480108142, 39),
  (1613, 555, 0.14460560027509928, 40),
  (1848, 561, 0.6708478704094887, 41),
  (1626, 562, 0.14312854129821062, 42),
  (1627, 563, 0.14267850667238235, 43),
  (1629, 564, 0.14281325228512287, 44),
  (1101, 577, 0.2556716464459896, 45),
  (1658, 593, 0.25392594188451767, 46),
  (1270, 600, 0.34045545011758804, 47),
  (1154, 601, 0.2056911699473858, 48),
  (549, 606, 0.6504823565483093, 49),
  (1909, 612, 0.1675377602223307, 50),
  (711, 614, 0.34011950716376305, 51),
  (1710, 647, 0.1028221813030541, 52),
  (895, 659, 0.3694894462823868, 53),
  (1971, 675, 0.22943139262497425, 54)],
 [(1236, 594, 0.6944231167435646, 55),
  (2030, 607, 0.8987423926591873, 56),
  (1766, 613, 0.8613974153995514, 57),
  (1651, 615, 0.6694677621126175, 58),
  (413, 622, 0.8383355885744095, 59),
  (1039, 627, 0.7670992761850357, 60),
  (1405, 627, 0.9019343852996826, 61),
  (834, 633, 0.7949446737766266, 62),
  (667, 637, 0.8410669416189194, 63)],
 [(1583, 581, 0.32599024334922433, 64),
  (1629, 605, 0.28973300755023956, 65),
  (1976, 633, 0.7046880349516869, 66),
  (1171, 638, 0.7626121640205383, 67),
  (1717, 645, 0.5747985318303108, 68),
  (960, 646, 0.469705855473876, 69),
  (344, 649, 0.8255835324525833, 70),
  (836, 651, 0.10502984508639202, 71),
  (1288, 652, 0.1615577139891684, 72),
  (1289, 653, 0.16130724176764488, 73),
  (1343, 662, 0.7307037636637688, 74),
  (605, 665, 0.6777969971299171, 75),
  (766, 669, 0.734762504696846, 76)],
 [(1542, 540, 0.4191073286347091, 77),
  (1101, 578, 0.60184096544981, 78),
  (1244, 589, 0.19293148501310498, 79),
  (293, 614, 0.609507218003273, 80),
  (709, 615, 0.38440303038805723, 81),
  (1889, 632, 0.8270364701747894, 82),
  (562, 643, 0.6508771665394306, 83),
  (1286, 647, 0.5413890331983566, 84),
  (707, 652, 0.5604030564427376, 85),
  (1672, 656, 0.5205767303705215, 86),
  (896, 665, 0.46471553668379784, 87)],
 [(1711, 727, 0.8038259893655777, 88),
  (1988, 736, 0.8239908218383789, 89),
  (1224, 739, 0.6591808348894119, 90),
  (1354, 739, 0.8178819566965103, 91),
  (412, 751, 0.7363487780094147, 92),
  (648, 751, 0.8198198825120926, 93),
  (1022, 752, 0.8035532534122467, 94),
  (1616, 754, 0.7473087906837463, 95),
  (823, 765, 0.6801922619342804, 96)],
 [(1700, 823, 0.6786390468478203, 97),
  (1338, 829, 0.7686821669340134, 98),
  (626, 832, 0.7900020331144333, 99),
  (1588, 832, 0.6806431710720062, 100),
  (981, 833, 0.7078418731689453, 101),
  (379, 839, 0.8497574478387833, 102),
  (1986, 839, 0.904950276017189, 103),
  (773, 841, 0.6414894312620163, 104),
  (1208, 843, 0.7282819449901581, 105)],
 [(1725, 905, 0.6315771639347076, 106),
  (645, 910, 0.704120472073555, 107),
  (646, 911, 0.7039194256067276, 108),
  (1363, 916, 0.7885270416736603, 109),
  (1026, 918, 0.6304485648870468, 110),
  (833, 923, 0.5351277068257332, 111),
  (419, 927, 0.8194856196641922, 112),
  (1632, 930, 0.7108354866504669, 113),
  (2001, 939, 0.8816360533237457, 114),
  (1227, 954, 0.5826617702841759, 115)],
 [(1750, 733, 0.8306137174367905, 116),
  (1261, 739, 0.6928278207778931, 117),
  (2038, 739, 0.8270675837993622, 118),
  (1397, 744, 0.7919004410505295, 119),
  (448, 751, 0.7526635229587555, 120),
  (680, 753, 0.8128890544176102, 121),
  (1054, 754, 0.802046611905098, 122),
  (1652, 755, 0.724275067448616, 123),
  (849, 773, 0.7403119653463364, 124)],
 [(1716, 821, 0.9215629994869232, 125),
  (1359, 826, 0.894261971116066, 126),
  (1587, 830, 0.7075225859880447, 127),
  (644, 833, 0.8557437211275101, 128),
  (992, 833, 0.8596925139427185, 129),
  (401, 836, 0.9176097363233566, 130),
  (2028, 840, 0.9102430194616318, 131),
  (776, 842, 0.7996445298194885, 132),
  (1218, 843, 0.8003700077533722, 133)],
 [(1745, 905, 0.8409408926963806, 134),
  (1052, 914, 0.7679972499608994, 135),
  (1398, 915, 0.8396336287260056, 136),
  (667, 917, 0.7812326401472092, 137),
  (439, 929, 0.8494541198015213, 138),
  (831, 929, 0.7186395525932312, 139),
  (2032, 942, 0.8694037348031998, 140),
  (1609, 945, 0.47176322154700756, 141),
  (1228, 956, 0.607912614941597, 142)],
 [(1228, 543, 0.7471884768456221, 143),
  (2000, 547, 0.9594799727201462, 144),
  (1627, 555, 0.8199863433837891, 145),
  (402, 557, 0.8218569979071617, 146),
  (1379, 565, 0.9482653588056564, 147),
  (1018, 567, 0.8422738760709763, 148),
  (1730, 567, 0.9007173776626587, 149),
  (821, 583, 0.8365558087825775, 150),
  (635, 584, 0.727754071354866, 151)],
 [(2019, 549, 0.948710560798645, 152),
  (1244, 552, 0.7421944588422775, 153),
  (1645, 558, 0.8877136558294296, 154),
  (417, 563, 0.9187621623277664, 155),
  (1746, 566, 0.9189962446689606, 156),
  (1034, 569, 0.8997330516576767, 157),
  (1394, 570, 0.9235824644565582, 158),
  (648, 583, 0.913199707865715, 159),
  (837, 589, 0.9446563273668289, 160)],
 [(1215, 548, 0.34220631420612335, 161),
  (1988, 560, 0.6879286542534828, 162),
  (393, 564, 0.11932083498686552, 163),
  (1614, 571, 0.40992921590805054, 164),
  (1368, 572, 0.5645941570401192, 165),
  (1723, 577, 0.2643510773777962, 166),
  (1013, 587, 0.11809143610298634, 167)],
 [(2029, 564, 0.8219497799873352, 168),
  (1254, 568, 0.69173189625144, 169),
  (1764, 573, 0.8749134987592697, 170),
  (431, 576, 0.8029779642820358, 171),
  (1656, 578, 0.7371501475572586, 172),
  (1406, 582, 0.9124706834554672, 173),
  (1050, 587, 0.8221320807933807, 174),
  (666, 595, 0.9233274906873703, 175),
  (851, 605, 0.8649997562170029, 176)]]

test_data_3 = [[(252, 40, 0.9193818271160126, 0), (352, 56, 0.9153284132480621, 1)],
 [(251, 76, 0.8531261682510376, 2), (357, 88, 0.8221826702356339, 3)],
 [(220, 76, 0.7809132635593414, 4), (330, 84, 0.7232284396886826, 5)],
 [(321, 118, 0.8593774735927582, 6), (213, 124, 0.818839892745018, 7)],
 [(340, 88, 0.6837703660130501, 8), (214, 156, 0.807474672794342, 9)],
 [(283, 77, 0.7633949965238571, 10), (384, 90, 0.7800293117761612, 11)],
 [(291, 125, 0.7603770643472672, 12), (388, 137, 0.7540169358253479, 13)],
 [(288, 171, 0.8366356790065765, 14), (382, 181, 0.7432413324713707, 15)],
 [(232, 171, 0.5575926080346107, 16), (334, 178, 0.6368680819869041, 17)],
 [(232, 241, 0.7247243970632553, 18), (337, 249, 0.7384766042232513, 19)],
 [(350, 319, 0.5142094921320677, 20), (230, 322, 0.6512419134378433, 21)],
 [(269, 171, 0.5626600384712219, 22), (367, 181, 0.619416818022728, 23)],
 [(388, 248, 0.7864628732204437, 24), (265, 252, 0.547605786472559, 25)],
 [(371, 317, 0.5759240314364433, 26), (259, 326, 0.6682618856430054, 27)],
 [(245, 33, 0.9238940328359604, 28), (346, 51, 0.9164116233587265, 29)],
 [(258, 33, 0.9195215553045273, 30), (358, 50, 0.9301682263612747, 31)],
 [(236, 37, 0.8958051800727844, 32), (339, 56, 0.6556035727262497, 33)],
 [(265, 37, 0.8267908245325089, 34), (367, 53, 0.7593023777008057, 35)]]

test_data_4 = [[(252, 40, 0.9236832708120346, 0), (120, 57, 0.9238319098949432, 1)],
 [(251, 76, 0.8354469984769821, 2), (119, 86, 0.8830759972333908, 3)],
 [(220, 76, 0.7694465517997742, 4), (94, 86, 0.8313081413507462, 5)],
 [(88, 124, 0.8431820869445801, 6), (213, 124, 0.8244058340787888, 7)],
 [(90, 150, 0.8495210260152817, 8), (214, 157, 0.8241766095161438, 9)],
 [(283, 77, 0.751670241355896, 10), (144, 87, 0.8066177070140839, 11)],
 [(291, 125, 0.7421219646930695, 12), (151, 126, 0.8065313994884491, 13)],
 [(149, 162, 0.8623518347740173, 14), (288, 172, 0.8153683692216873, 15)],
 [(104, 162, 0.6374475434422493, 16), (232, 172, 0.5576830729842186, 17)],
 [(104, 220, 0.7456793040037155, 18), (232, 242, 0.7019675076007843, 19)],
 [(102, 281, 0.7432529032230377, 20), (230, 322, 0.6747846156358719, 21)],
 [(133, 163, 0.6370653435587883, 22), (269, 172, 0.5627307519316673, 23)],
 [(130, 227, 0.6819316893815994, 24), (265, 252, 0.546066414564848, 25)],
 [(126, 285, 0.7322840392589569, 26), (259, 326, 0.6633012518286705, 27)],
 [(245, 34, 0.9197878241539001, 28), (114, 52, 0.9177820384502411, 29)],
 [(258, 34, 0.9160163998603821, 30), (125, 52, 0.9131835997104645, 31)],
 [(236, 37, 0.8946171849966049, 32), (107, 55, 0.895718052983284, 33)],
 [(265, 37, 0.8413965702056885, 34), (131, 55, 0.7821370661258698, 35)]]

def calculate_angles(feature1_list, feature2_list):
    x1 , y1 = feature1_list[0:2]
    x2 , y2 = feature2_list[0:2]
    delta_x = x2-x1
    delta_y = y2-y1
    if delta_x ==0:
        if delta_y >0:
            return 90
        else:
            return 270
    elif delta_x >0 and delta_y>0:
        grad= (y2-y1)/(x2-x1)
        return np.arctan(grad)*180/np.pi
    elif delta_x  <0 and delta_y>0:
        grad = (y2-y1)/(x1-x2)
        return np.arctan(grad)*180/np.pi +90
    elif delta_x< 0 and delta_y< 0:

        grad = (y1-y2)/(x2-x1)
        return np.arctan(grad)*180/np.pi +180
    else:
        grad= (y2-y1)/(x2-x1)
        return np.arctan(grad)*180/np.pi +270







def return_angles(data):
    """Return array of lists with gradients of connecting body parts
    LEFT = LEFT FROM VIEWER
    connecting_body_parts= {"left eye to left ear":(15,17),
                             "left eye to nose":(15,0),
                             "nose to right eye":(0,14),
                             "right eye to right ear":(14,16),
                             "nose to chest":(0,1),
                             "chest to left shoulder":(1,5),
                             "left shoulder to left elbow":(5,6),
                             "left elbow to left wrist" :(6,7),
                             "chest to right shoulder":(1,2),
                             "right shoulder to right elbow":(2,3),
                             "right elbow to right wrist":(3,4),
                             "chest to left hip":(1,11),
                             "chest to right hip":(1,8),
                             "left hip to left knee":(11,12),
                             "left knee to left foot":(12,13),
                             "right hip to right knee":(8,9),
                             "right knee to right foot":(9,10)}
    """


    connecting_body_parts_id=[(16,14), (14,0),(0,15),(15,17),
                              (0,1),(1,2),(2,3),(3,4),(1,5),(5,6),
                              (6,7),(1,8),(1,11),(8,9),(9,10),
                              (11,12),(12,13)]
    output = []

    for connect in connecting_body_parts_id:
        feature1_list = data[connect[0]]
        feature2_list = data[connect[1]]
        # if len(feature1_list)!= 9 or len(feature2_list)!=9:
        #     continue
        output_mini=[(connect)]
        for i in range (min(len(feature1_list),len(feature2_list))):
            output_mini.append(calculate_angles(feature1_list[i],feature2_list[i]))

        output.append(output_mini)
    return output

angles= return_angles(test_data_4)
for angle in angles:
    print(angle)

# for angle in angles:
#     print(angle[2]-gradient[1]
#           , gradient[0])
