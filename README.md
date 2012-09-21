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

* [Rails Related Files](https://github.com/luqman/SublimeText2RailsRelatedFiles) : lets imagine you "right clicked" on the following file/s (Screenshot 2) or by using the "CMD+Shift+O" shortcut (Screenshot 1)  it will search for files:

 `posts_controller.rb` under `app/controllers`

* See [Sublime Text 2 Guard Plugin](https://github.com/cyphactor/sublime_guard) usage

## Issues

if get an error message like "'https://github.com': Device not configured" then do,

```
git remote set-url origin git@github.com:username/repo.git
```
Here is the [stackoverflow answer](http://stackoverflow.com/questions/6565357/git-push-requires-username-and-password) for this issue.

