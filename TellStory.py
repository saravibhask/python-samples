storyFormat = '''
Once upon a time, deep in an ancient jungle, 
there lived a {animal}. This {animal} 
liked to eat {food}, but the jungle had 
very little {food} to offer. One day, an 
{explorer} found the {animal} and discovered 
it liked {food}. The explorer {explorer} took the 
{animal} back to {city}, where it could 
eat as much {food} as it wanted. However, 
the {animal} became homesick, so the 
explorer {explorer} brought it back to the jungle, 
leaving a large supply of {food}. 

The End 
'''

def tellStory():
    userPicks = dict()
    addPicks('explorer', userPicks)
    addPicks('animal', userPicks)
    addPicks('food', userPicks)
    addPicks('city', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)

def addPicks(cue, dictionary):
    prompt = 'Enter your choice for ' + cue + ' : '
    response = input(prompt)
    dictionary[cue] = response
    
tellStory()
