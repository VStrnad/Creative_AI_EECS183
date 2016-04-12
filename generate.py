#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('./language-models')
sys.path.append('./data')
sys.path.append('./pysynth')
import pysynth
import random
from dataLoader import *
from unigramModel import *
from bigramModel import *
from trigramModel import *
from musicData import *

# -----------------------------------------------------------------------------
# Core ------------------------------------------------------------------------
# Functions to implement: trainLyricsModels, selectNGramModel,
# generateSentence, and runLyricsGenerator

def trainLyricsModels(lyricsDirectory):
    """
        Requires: nothing
        Modifies: nothing
        Effects:  loads lyrics data from the data/lyrics/<lyricsDirectory> folder
        using the pre-written DataLoader class, then creates an
        instance of each of the NGramModel child classes and trains
        them using the text loaded from the data loader. The list
        should be in tri-, then bi-, then unigramModel order.
        
        Returns the list of trained models.
    """
    dataLoader = DataLoader()
    dataLoader.loadLyrics(lyricsDirectory) # lyrics stored in dataLoader.lyrics
    models = [TrigramModel(), BigramModel(), UnigramModel()]
    trigramModel = TrigramModel()
    bigramModel = BigramModel()
    unigramModel = UnigramModel()
    # train model
    trigramModel.trainModel(dataLoader.lyrics)
    bigramModel.trainModel(dataLoader.lyrics)
    unigramModel.trainModel(dataLoader.lyrics)
    
    models = [trigramModel, bigramModel, unigramModel]
    return models

def selectNGramModel(models, sentence):
    """
        Requires: models is a list of NGramModel objects sorted by descending
        priority: tri-, then bi-, then unigrams.
        Modifies: nothing
        Effects:  starting from the beginning of the models list, returns the
        first possible model that can be used for the current sentence
        based on the n-grams that the models know. (Remember that you
        wrote a function that checks if a model can be used to pick a
        word for a sentence!)
    """
    if models[0].trainingDataHasNGram(sentence):
        return models[0]
    elif models[1].trainingDataHasNGram(sentence):
        return models[1]
    else:
        return models[2]

def sentenceTooLong(desiredLength, currentLength):
    """
        Requires: nothing
        Modifies: nothing
        Effects:  returns a bool indicating whether or not this sentence should
        be ended based on its length. This function has been done for
        you.
    """
    STDEV = 1
    val = random.gauss(currentLength, STDEV)
    return val > desiredLength

def generateSentence(models, desiredLength):
    """
        Requires: models is a list of trained NGramModel objects sorted by
        descending priority: tri-, then bi-, then unigrams.
        desiredLength is the desired length of the sentence.
        Modifies: nothing
        Effects:  returns a list of strings where each string is a word in the
        generated sentence. The returned list should NOT include
        any of the special starting or ending symbols.
        
        For more details about generating a sentence using the
        NGramModels, see the spec.
    """
    sentence = ['^::^', '^:::^']
    grabbedToken = ''
    while sentenceTooLong(desiredLength, len(sentence) - 2) == False and grabbedToken !=  '$:::$':
        modelSelected = selectNGramModel(models, sentence)
        grabbedToken = modelSelected.getNextToken(sentence)
        sentence.append(grabbedToken)
    if grabbedToken == '$:::$':
        return sentence[2: - 1]
    else:
        return sentence[2: ]

def printSongLyrics(verseOne, verseTwo, chorus):
    """
        Requires: verseOne, verseTwo, and chorus are lists of lists of strings
        Modifies: nothing
        Effects:  prints the song. This function is done for you.
        """
    verses = [verseOne, chorus, verseTwo, chorus]
    print '\n',
    for verse in verses:
        for line in verse:
            print (' '.join(line)).capitalize()
        print '\n',

def runLyricsGenerator(models):
    """
        Requires: models is a list of a trained nGramModel child class objects
        Modifies: nothing
        Effects:  generates a verse one, a verse two, and a chorus, then
        calls printSongLyrics to print the song out.
        """
    verseOne = []
    verseTwo = []
    chorus = []
    i = 0
    for i in range(4):
        verseOne.append(generateSentence(models, 7))
        verseTwo.append(generateSentence(models, 7))
        chorus.append(generateSentence(models, 7))
        
    printSongLyrics(verseOne,verseTwo,chorus)




# -----------------------------------------------------------------------------
# Reach -----------------------------------------------------------------------
# Functions to implement: trainMusicModels, generateMusicalSentence, and
# runMusicGenerator

def trainMusicModels(musicDirectory):
    """
        Requires: nothing
        Modifies: nothing
        Effects:  works exactly as trainLyricsModels from the core, except
        now the dataLoader calls the DataLoader's loadMusic() function
        and takes a music directory name instead of an artist name.
        Returns a list of trained models in order of tri-, then bi-, then
        unigramModel objects.
        """
    dataLoader = DataLoader()
    dataLoader.loadMusic(musicDirectory) # music stored in dataLoader.songs
    models = [TrigramModel(), BigramModel(), UnigramModel()]
    dataLoader = DataLoader()
    trigramModel = TrigramModel()
    bigramModel = BigramModel()
    unigramModel = UnigramModel()
    # train model
    trigramModel.trainModel(dataLoader.songs)
    bigramModel.trainModel(dataLoader.songs)
    unigramModel.trainModel(dataLoader.songs)
    
    return models

def generateMusicalSentence(models, desiredLength, possiblePitches):
    """
        Requires: possiblePitches is a list of pitches for a musical key
        Modifies: nothing
        Effects:  works exactly like generateSentence from the core, except
        now we call the NGramModel child class' getNextNote()
        function instead of getNextToken(). Everything else
        should be exactly the same as the core.
        """
    sentence = ['^::^', '^:::^']

    # add rest of generateMusicalSentence implementation here
    while sentenceTooLong(desiredLength, len(sentence) - 2) == False and grabbedNote !=  '$:::$':
        modelSelected = selectNGramModel(models, sentence)
        grabbedNote = modelSelected.getNextNote(sentence, possiblePitches)
        sentence.append(grabbedNote)
    if grabbedNote == '$:::$':
        return sentence[2: - 1]
    else:
        return sentence[2: ]

    return sentence
    
    return sentence

def runMusicGenerator(models, songName):
    """
        Requires: models is a list of trained models
        Modifies: nothing
        Effects:  runs the music generator as following the details in the spec.
        
        Note: For the core, this should print "Under construction".
        """
    possiblePitches = KEY_SIGNATURES[random.choice(KEY_SIGNATURES.keys())]
    song = generateMusicalSentence(models,100, possiblePitches)
    pysynth.make_wav(song, fn = "TestSong")






# -----------------------------------------------------------------------------
# Main ------------------------------------------------------------------------

def getUserInput(teamName, lyricsSource, musicSource):
    """
        Requires: nothing
        Modifies: nothing
        Effects:  prints a welcome menu for the music generator and prints the
        options for the generator. Loops while the user does not input
        a valid option. When the user selects 1, 2, or 3, returns
        that choice.
        
        Note: this function is for the reach only. It is done for you.
        """
    print 'Welcome to the', teamName, 'music generator!\n'
    prompt = 'Here are the menu options:\n' + \
        '(1) Generate song lyrics by ' + lyricsSource + '\n' \
            '(2) Generate a song using data from ' + musicSource + '\n' \
                '(3) Quit the music generator\n'
    prompt = 'prompt'

    userInput = -1
    while userInput < 1 or userInput > 3:
        print prompt
        userInput = raw_input('Please enter a choice between 1 and 3: ')
        try:
            userInput = int(userInput)
        except ValueError:
            userInput = -1

    return userInput

def main():
    """
    Requires: nothing
    Modifies: nothing
    Effects:  this is your main function, which is done for you. It runs the
              entire generator program for both the reach and the core.
              It begins by loading the lyrics and music data, then asks the
              user to input a choice to generate either lyrics or music.

              Note that for the core, only choice 1 (the lyrics generating
              choice) needs to be completed; if the user inputs 2, you
              can just have the runMusicGenerator function print "Under
              construction."

              Also note that you can change the values of the first five
              variables based on your team's name, artist name, etc.
    """
    teamName = 'Team Name'
    lyricsSource = 'The Beatles'
    musicSource = 'Nintendo Gamecube'
    lyricsDirectory = 'the_beatles'
    musicDirectory = 'gamecube'

    print 'Starting program and loading data...'
    lyricsModels = trainLyricsModels(lyricsDirectory)
    musicModels = trainMusicModels(musicDirectory)
    print 'Data successfully loaded\n'

    userInput = getUserInput(teamName, lyricsSource, musicSource)

    while userInput != 3:
        print '\n',
        if userInput == 1:
            runLyricsGenerator(lyricsModels)
        elif userInput == 2:
            songName = raw_input('What would you like to name your song? ')
            runMusicGenerator(musicModels, 'wav/' + songName + '.wav')

        print '\n',
        userInput = getUserInput(teamName, lyricsSource, musicSource)

        print '\nThank you for using the', teamName, 'music generator!'



if __name__ == '__main__':
    main()
    # note that if you want to individually test functions from this file,
    # you can comment out main() and call those functions here. Just make
    # sure to call main() in your final submission of the project!
    """
    a = UnigramModel()
    runLyricsGenerator(a)
    """

