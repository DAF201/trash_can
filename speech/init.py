import speech

speech.say("Say something.")

print("You said " + speech.input())


def L1callback(phrase, listener):
    print(phrase)


def L2callback(phrase, listener):
    if phrase == "wow":
        listener.stoplistening()
    speech.say(phrase)


# callbacks are executed on a separate events thread.
L1 = speech.listenfor(["hello", "good bye"], L1callback)
L2 = speech.listenforanything(L2callback)

assert speech.islistening()
assert L2.islistening()

L1.stoplistening()
assert not L1.islistening()

speech.stoplistening()
