from deepsegment import DeepSegment
# The default language is 'en'
segmenter = DeepSegment('en')
a = """
would like to respond let me just ask
though why did you try to kill that bill
and successfully so that would have put
thousands of additional agents and
officers On the Border first let me
respond us to the rallies she said
people start leaving people don't go to
her rallies there's no reason to go and
the people that do go she's busing them
in and paying them to be there and then
showing them in a different light so she
can't talk about that people don't leave
my rallies we have the biggest rallies
the most incredible rallies in the
history of politics that's because people want to take their country back
our country is being lost we're a
failing nation and it happened three and
a half years ago and what what's going
on here you're going to end up in World
War II just to go into another subject
what they have done to our country by
allowing these millions and millions of
people to come into our country and look
at what's happening to the towns all
over the United States and a lot of
towns don't want to talk not going to be
Aurora or Springfield a lot of towns
don't want to talk about it because
they're so embarrassed by it in Spring
field they're eating the dogs the people
that came in they're eating the cats
they're eating they're eating the pets
of the people that live there and this
is what's happening in our country and
it's a shame as far as rallies are
concerned as far as the reason they go
is they like what I say they want to
bring our country back they want to make
America great again it's very simple
phrase make America great again she's
destroying this country and and if she
becomes president this country doesn't
have a chance of success not only
success will end up being Venezuela on
steroids I just want to clarify here you
rig up Springfield Ohio and ABC News did
reach out to the city manager there uh
he told us there have been no credible
reports of specific claims of pets being
harmed injured or abused by individuals
within the Immigrant Community all I've
seen people on televis let me just say
here this is people on television say my
dog was taken and used for food so maybe
he said that and maybe that's a good thing to say for a city manager I'm not 
taking this from Tel people television  say the dog was eaten by the people that went there
"""


b = """
would like to respond let me just ask
though why did you try to kill that bill
and successfully so that would have put
thousands of additional agents and
officers On the Border first let me
respond us to the rallies she said
people start leaving people don't go to
her rallies there's no reason to go and
the people that do go she's busing them
in and paying them to be there and then
showing them in a different light so she
can't talk about that people don't leave
my rallie"""
segmenter.segment(a)
# ['I am Batman', 'i live in gotham']


