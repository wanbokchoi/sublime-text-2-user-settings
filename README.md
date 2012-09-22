# My Sublime Text 2 settings

These are the settings I use based on [@brynary's "Running RSpec from Sublime Text 2" posting](http://blog.codeclimate.com/blog/2012/06/21/sublime-text-2-for-ruby/)

## Install

Go to your Packages directory:

```
cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
```

Clone as your `User` packages:

```
git clone https://github.com/kellyredding/sublime-text-2-user-settings.git User
```

## Updating

Go to your User Packages directory:

```
cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/User
```

Pull on the repo:

```
git pull
```

## Usage

* you can bind ⌘R to run the current file and ⌘⇧R to run the current test. The tests will run in Terminal.

* ⌘ P
  - ⌘ P and then type ”@”, that gives you a list of all the methods in this file.
  - ⌘ P and then type ”:” followed by a number, that jumps to the specified line number in this file.

*  ^ Space, also you can explore classes and methods by clicking on them while holding the Alt key.

* Shift+Ctrl+space To trigger manual codeintel autocompletion use .

* Make a selection, then command + option + control + ] an alignment tool and not a full-blown beautifier. It works best when there's one assignment per line

* [Rails Related Files](https://github.com/luqman/SublimeText2RailsRelatedFiles) : lets imagine you "right clicked" on the following file/s (Screenshot 2) or by using the "⌘⇧O" shortcut (Screenshot 1)  it will search for files:

 `posts_controller.rb` under `app/controllers`

* See [Sublime Text 2 Guard Plugin](https://github.com/cyphactor/sublime_guard) usage

RubyMotionBuilder Usage
-----

### RubyMotion syntax

1. Open \*.rb or Rakefile in your RubyMotion project
2. You can see the "RubyMotion" on status bar in right bottom corner. Otherwise, it's not working. If Sublime Text 2 cache keep syntax as "Ruby", please close and open the file.

**note:** RubyMotion detection rule is projtect's Rakefile contains "Motion", or not.

### Code completion

1. Inside your RubyMotion project just start typing the name of a method and the autocomplete window will pop up.
2. Press enter/return to trigger the completion.

### Build

1. Open \*.rb or Rakefile in your RubyMotion project and enter **[command + b]**.
2. Wait for the console to notify you the message "[Finished]".
3. If you get a error, you can jump to it with press **[F4]**

**note:** Default target is Simulator. If you want to change the target, please edit "RubyMotion.sublime-build".

### Clean

1. Open the Command Palette using **[command + shift + p]** and enter "clean".
2. Select `RubyMotionBuilder: Clean` from the popup menu and press **[return]**
3. Wait for the console to notify you the message "[Finished]".

### Run

1. Open *\.rb or Rakefile in your RubyMotion project and enter **[command + r]**. If you want to enable retina, please enter **[shift + command + r]**.
2. Wait for the Terminal.app will kick Simulator.
3. If you want to modify code and to try again, just re-enter **[command + r]**.
Then, automatically post "quit" to Terminal.app and re-execute "rake".

**note:** `Goto symbol` was assigned to **[control + r]**

### Deploy

1. Open \*.rb or Rakefile in your RubyMotion project and enter **[command + option + b]**.
2. Wait for the console to notify you the message "[Finished]".

### Syntax/Completions generator

These two commands also supported in Command Pallet.

* `RubyMotionBuilder: Generate syntax` will generate syntax and snippets from Ruby syntax.
* `RubyMotionBuilder: Generate completions` will generate completions from BridgeSupport files of RubyMotion.

## Issues

if get an error message like "'https://github.com': Device not configured" then do,

```
git remote set-url origin git@github.com:username/repo.git
```
Here is the [stackoverflow answer](http://stackoverflow.com/questions/6565357/git-push-requires-username-and-password) for this issue.

