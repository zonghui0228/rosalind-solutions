Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fp=open('C:\\Users\\sony\\Desktop\\rosalind_ini6.txt','r')
>>> str=fp.read()
>>> str
'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be\n'
>>> dict={}
>>> for word in str.split(' '):
	if dict.has_key(word):
		dict[word]+=1
	else:
		dict[word]=1

		
>>> for key,value in dict.items():
	print key
	print value

	
be

1
parted
1
right
1
they
2
For
1
be
40
there
2
is
4
There
4
When
1
it
36
an
4
see
1
in
4
hearted
1
shines
1
still
2
Mary
2
Speaking
3
standing
1
living
1
light
1
darkness
1
people
1
when
2
find
1
to
3
that
2
Let
6
answer
4
music
1
until
1
Shine
1
And
3
may
1
though
1
I
2
sound
1
night
1
wisdom
7
broken
1
chance
1
let
30
a
2
words
7
Mother
2
front
1
world
1
trouble
1
tomorrow
1
me
4
on
1
myself
1
hour
1
of
11
yeah
2
up
1
cloudy
1
times
1
will
5
she
1
Whisper
4
wake
1
the
4
my
1
agree
1
comes
2
>>> 
