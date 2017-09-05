# Extensions Research

## Task

This task was to understand how to design an electron project to be "hackable". This means that a third party can easily add extensions to the project to customize it. There are particular ways to develop and structure the project to achieve this goal.

## Why extensions?

A "Hackable" Aurora will allow our own users to add to Aurora and make it a better tool more suited for their specific needs.
Thus, the future generations can extend our work and carry on the spirit of
Aurora through those endless summer days and long, dark winter nights in the evanescent seasons that mark the vitality of the Tundra.

## Examples

### Atom
[Atom hackable guide](http://flight-manual.atom.io/hacking-atom/sections/tools-of-the-trade/). Atom is also an Electron program, so a good model for Aurora.

How to add a simple extension:
1. There is an `init.coffee` file in your `~/.atom` folder. It is run every time Atom is launched.  
  * [CoffeeScript](http://coffeescript.org/) is a language that compiles one-to-one in JS and just makes JS a little easier with nice simple features. If you don't want to use coffee, you can do the same in an `init.js` file.
2. For a simple extension, add code the `init.coffee` file. Example [here](http://flight-manual.atom.io/hacking-atom/sections/the-init-file/).
3. The entire [Atom API](https://atom.io/docs/api/v1.19.5/AtomEnvironment) is accessible from `init.coffee`. That's how you do magic Atom extensions.

How to add a more complicated extension:
1. Use the built in `Package Generator`.
2. It creates a default package for you wherever you specify and links that package to `~/.atom/packages`. All these packages will be loaded at runtime.
3. Modify your code in here just like any package.

To make custom keybindings:
1. Open `keymap.cson` in your `~/.atom` folder. This file is loaded lastly every time Atom is launched so it can override default keybindings.
  * [cson](https://github.com/bevry/cson) is the same as JSON but for `coffeescript`.
2. Add a new keymapping depending on context. Here's an [example](http://flight-manual.atom.io/using-atom/sections/basic-customization/#customizing-keybindings).

Takeaways:
- We need to write our API in a modular way. We also need clear API docs. We also need to define what will be in our publicly accessible API (if not everything).
- CoffeeScript is not required, but might be helpful. Something to look into I guess.
- We should have config files in a `~/.aurora` folder.
- We should definitely include a `package generator` if we want people to make use of this. It needs to be easy.


# Author
Kyle McCrohan, 2017.
