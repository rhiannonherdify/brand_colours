from collections import namedtuple, OrderedDict
Colour = namedtuple('RGB','red, green, blue')

class RGB(Colour):
    def hex(self):
        return '#{:02X}{:02X}{:02X}'.format(self.red,self.green,self.blue)
    
    def rgb(self):
        return f'rgb({self.red}, {self.green}, {self.blue})'

    def rgba(self, alpha):
        return f'rgba({self.red}, {self.green}, {self.blue}, {alpha})'
      
# colour contants
# blues
blue = RGB(33, 87, 123)
blue1 = RGB(30, 78, 111)
blue2 = RGB(26, 70, 98)
blue3 = RGB(23, 61, 86)
blue4 = RGB(20, 52, 74)
blue5 = RGB(17, 44, 62)
# blue6 = RGB(13, 35, 49)
# blue7 = RGB(10, 26, 37)
blue0 = RGB(33, 87, 123)
bluel1 = RGB(55, 104, 136)
bluel2 = RGB(77, 121, 149)
bluel3 = RGB(100, 137, 163)
bluel4 = RGB(122, 154, 176)
bluel5 = RGB(144, 171, 189)
# bluel6 = RGB(166, 188, 202)
# bluel7 = RGB(188, 205, 210)

# yellows
yellow = RGB(245, 185, 88)
yellow1 = RGB(221, 167, 79)
yellow2 = RGB(196, 148, 70)
yellow3 = RGB(172, 130, 62)
yellow4 = RGB(147, 111, 53)
yellow5 = RGB(123, 93, 44)
# yellow6 = RGB(98, 74, 35)
# yellow7 = RGB(73, 55, 26)
yellow0 = RGB(245, 185, 88)
yellowl1 = RGB(246, 192, 105)
yellowl2 = RGB(247, 199, 121)
yellowl3 = RGB(248, 206, 138)
yellowl4 = RGB(249, 213, 155)
yellowl5 = RGB(250, 220, 172)
# yellowl6 = RGB(251, 227, 188)
# yellowl7 = RGB(252, 234, 205)

# greys
grey = RGB(211, 202, 191)
grey1 = RGB(211, 202, 191)
grey2 = RGB(190, 182, 172)
grey3 = RGB(148, 141, 134)
grey4 = RGB(127, 121, 115)
grey5 = RGB(106, 101, 96)
# grey6 = RGB(84, 81, 76)
# grey7 = RGB(63, 61, 57)
grey0 = RGB(211, 202, 191)
greyl1 = RGB(215, 207, 197)
greyl2 = RGB(220, 213, 204)
greyl3 = RGB(224, 218, 210)
greyl4 = RGB(229, 223, 217)
greyl5 = RGB(233, 229, 223)
# greyl6 = RGB(237, 234, 229)
# greyl7 = RGB(242, 239, 236)

# teals
teal = RGB(106, 170, 150)
teal1 = RGB(95, 153, 135)
teal2 = RGB(85, 136, 120)
teal3 = RGB(74, 119, 105)
teal4 = RGB(64, 102, 90)
teal5 = RGB(53, 85, 75)
# teal6 = RGB(42, 68, 60)
# teal7 = RGB(32, 51, 45)
teal0 = RGB(106, 170, 150)
teall1 = RGB(121, 179, 161)
teall2 = RGB(136, 187, 171)
teall3 = RGB(151, 196, 182)
teall4 = RGB(166, 204, 192)
teall5 = RGB(181, 213, 203)
# teall6 = RGB(195, 221, 213)
# teall7 = RGB(210, 230, 224)

# lightblues
lightblue = RGB(122, 166, 194)
lightblue1 = RGB(110, 149, 175)
lightblue2 = RGB(98, 133, 155)
lightblue3 = RGB(85, 116, 136)
lightblue4 = RGB(73, 100, 116)
lightblue5 = RGB(61, 83, 97)
# lightblue6 = RGB(49, 66, 78)
# lightblue7 = RGB(37, 50, 58)
lightblue0 = RGB(122, 166, 194)
lightbluel1 = RGB(135, 175, 200)
lightbluel2 = RGB(149, 184, 206)
lightbluel3 = RGB(162, 193, 212)
lightbluel4 = RGB(175, 202, 218)
lightbluel5 = RGB(189, 211, 225)
# lightbluel6 = RGB(202, 219, 231)
# lightbluel7 = RGB(215, 228, 237)
