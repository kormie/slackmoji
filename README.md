# Slackmoji:
Life can be rough in the high stakes game of reactji novelty. The only way to survive is scripting and teaming up

> **Note**  
> This project is in its early stages, and currently, it only generates one type of Slack reactji.


## Contributions Welcome

We welcome and appreciate contributions. If you're interested in contributing, please take a look at the [redacted shell](bin/redacted) and [redacted python](lib/redacted.py) files. These files serve as examples of how to add new types of reactji generators.

The [shell](bin/redacted) file is the user entry point for generating new emoji with the "redacted" reactji generator. If you're creating a new type of reactji generator, you would create a similar file in the `bin/` directory. For example, if you were creating a generator for reactji that took an image as input and made a reactji of it exploding, you might create a `bin/explosion` file.

The [python](lib/redacted.py) file contains the image generation logic for the "redacted" reactji generator. If you're adding a new type of reactji generator, you would create a similar file in the `lib/` directory. Following the previous example, you might create a `lib/explosion.py` file for the image generation logic.
