imp o r t pygame
imp o r t math
pygame . i n i t ( )
p i x e l _ s i z e = 1
# COLOR CODE
b l a c k = ( 0 , 0 , 0)
wh i t e = ( 2 5 5 , 255 , 255)
# SIZE PARAMETERS
27
s c r e e n _wi d t h = 800
s c r e e n _ h e i g h t = 600
# SET SCREEN SIZE
s c r e e n _ d i s p l a y = pygame . d i s p l a y . set_mode ( ( s c r e e n _wi d t h , s c r e e n _ h e i g h t ) )
s c r e e n _ d i s p l a y . f i l l ( b l a c k )
# TITLE
pygame . d i s p l a y . s e t _ c a p t i o n ( " Bresenham Ci r c l e " )
d e f b r e s e n h am_ c i r c l e (Cx , Cy , r a d ) :
s c r e e n _ c l o s e = F a l s e
wh i l e n o t s c r e e n _ c l o s e :
f o r e v e n t i n pygame . e v e n t . g e t ( ) :
i f e v e n t . t y p e == pygame .QUIT :
s c r e e n _ c l o s e = True
x = 0
y = r a d
d = 3 − 2* r a d
wh i l e x <= r a d / math . s q r t ( 2 ) :
# O* − 45*
pygame . draw . r e c t ( s c r e e n _ d i s p l a y , whi te ,
[Cx + y , Cy − x , p i x e l _ s i z e , p i x e l _ s i z e ] )
# 45* − 90*
pygame . draw . r e c t ( s c r e e n _ d i s p l a y , whi te ,
[Cx + x , Cy − y , p i x e l _ s i z e , p i x e l _ s i z e ] )
# 90* − 135*
pygame . draw . r e c t ( s c r e e n _ d i s p l a y , whi te ,
[Cx − x , Cy − y , p i x e l _ s i z e , p i x e l _ s i z e ] )
# 135* − 180*
pygame . draw . r e c t ( s c r e e n _ d i s p l a y , whi te ,
[Cx − y , Cy − x , p i x e l _ s i z e , p i x e l _ s i z e ] )
# 180* − 225*
pygame . draw . r e c t ( s c r e e n _ d i s p l a y , whi te ,
[Cx − y , Cy + x , p i x e l _ s i z e , p i x e l _ s i z e ] )
# 225* − 270*
pygame . draw . r e c t ( s c r e e n _ d i s p l a y , whi te ,
[Cx − x , Cy + y , p i x e l _ s i z e , p i x e l _ s i z e ] )
# 270* − 315*
pygame . draw . r e c t ( s c r e e n _ d i s p l a y , whi te ,
[Cx + x , Cy + y , p i x e l _ s i z e , p i x e l _ s i z e ] )
# 315* − 360*
pygame . draw . r e c t ( s c r e e n _ d i s p l a y , whi te ,
28
[Cx + y , Cy + x , p i x e l _ s i z e , p i x e l _ s i z e ] )
i f ( d < 0 ) :
d = d + 4 * x + 6
e l s e :
d = d + 4 * x − 4 * y + 10
y −= 1
x += 1
pygame . d i s p l a y . u p d a t e ( )
# d r i v e r code
x = 400
y = 300
r = 200
b r e s e n h am_ c i r c l e ( x , y , r )
pygame . q u i t ( )