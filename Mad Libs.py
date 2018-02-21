story = '''
{}. But! {} only if ye be a {} of valor!
For {} is guarded by a {} so {},
so {}, that no {} has yet {}
with it... and {}!
'''

def main():
    command = input('Enter a command:')
    plural_noun = input('Enter a plural noun:')
    animal = input('Enter an animal:')
    location = input('Enter a location:')
    singular_noun = input('Enter a singular noun:')

    adjectives = []
    adjectives.append(input('Enter an adjective:'))
    adjectives.append(input('Enter another adjective:'))


    past_participles = []
    past_participles.append(input('Enter a past participle:'))
    past_participles.append(input('Enter another past participle:'))

    mad_lib = story.format(command,
                           command,
                           plural_noun,
                           location,
                           animal,
                           adjectives[0],
                           adjectives[1],
                           singular_noun,
                           past_participles[0],
                           past_participles[1])
    print(mad_lib)

    #print(past_participles[0], past_participles[1])


main()
