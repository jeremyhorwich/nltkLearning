#Determine if a sentence can be parsed more than one way

#Import the grammar

def importGrammar(fileName):
    grammarFile = open("grammars/" + fileName,"r")
    grammar = dict()
    for line in grammarFile:
        rule = parseGrammarRule(line)
        grammar.update(rule)
    return grammar


def parseGrammarRule(lineOfGrammar):
    splitLHSandRHS = lineOfGrammar.split("->")
    if len(splitLHSandRHS) != 2:
        raise Exception("Grammar in unexpected format")
    
    grammarRule = dict()
    combinationResult = splitLHSandRHS[0].strip()
    combinations = splitLHSandRHS[1].split("|")

    for combination in combinations:
        grammarRule[combination.strip("' \n")] = combinationResult
    return grammarRule    
     

def detectAmbiguity(sentence, grammar):
    sentence = sentence.strip(" .!").lower()
    phraseList = sentence.split()

    rulesByPhraseType = dict()
    for i in range(len(phraseList)):
        phraseList[i] = grammar[phraseList[i]]
        if phraseList[i] not in rulesByPhraseType:
            rulesByPhraseType[phraseList[i]] = findRulesByPhraseType(grammar, phraseList[i])
    print(rulesByPhraseType["NP"])

def findRulesByPhraseType(grammar, phrase):
    rulesAppliedToPhrase = list()
    for rule in grammar:
        if phrase in rule.split():
            rulesAppliedToPhrase.append(rule)
    return rulesAppliedToPhrase

grammar = importGrammar("grouchoGrammar.txt")
detectAmbiguity("I shot an elephant in my pajamas",grammar)



#Step 1: Check each element of the list
#Step 2: Check how many combinations it has
#   If it has 1 combination, combine.
#   If it has 2 available combinations, break and fail
#   If it has "1.5" an available combination and a currently unavailable combination, add it to another list (1.5 list)
#Step 3: Make new list (send grammar rules to be executed to a function which handles it)
#   If this new list is the same as the one before, then check your "1.5 list"
#       If there are no elements in the list (nothing can be changed) return an exception (unsolveable with current grammar, etc.)
#       If your 1.5 list has only one element, execute the available grammar rule for that element and make a new list
#       If this list has more than one element, we copy the sentence and perform the algorithm for each copied sentence (via recursion)
#Step 4: Return the result of the same function with the new argument of the new sentence (recursion)

