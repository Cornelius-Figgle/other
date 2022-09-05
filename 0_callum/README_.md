
# Setup

## Remember, to paste, you only need to right-click

- Open windows search, type `git` then select `git cmd`

## Adding files

- In here, type the following 3 commands

```shell
cd "c:\users\callum\source\repos\game test"
git init
notepad .gitignore
```

- This will open Notepad, in here write the following:

```text
.vs/
game test.pyproj
game test.sln
```

- Save the notepad file and then close it

## Creating initial commit

- Then go back to the `git cmd` window and type the following:

```shell
git add .
git status
git commit -m "initial commit"
```

## Creating GitHub repo

- Next, go to [GitHub](https://github.com/new) and name it `game-test`
- Make sure it is public, then choose `MIT License` off the license list
- Save the repo
- It will take you to the project page
- Click the `Code` button (next to `Add file`)
- Copy the https url displayed
- Will look like this: `https://github.com/TheLordJesusHimself/game-test.git`

## Pushing repo to GitHub

- Then go back to `git cmd` and type the following, replacing the url with the one you copied:

```shell
git branch -m main
git remote add origin https://github.com/TheLordJesusHimself/game-test.git
git push origin main
```

## Checking it uploaded fine

- Go back to the GitHub webpage, reload it and check the `game_test.py`, `LICENSE` and the `.gitignore` files are in there

## Setup in VS Code

- Open (or close and reopen) VS Code
- Check if game folder is open
- If not, press `Ctrl + K` then press `Ctrl + O` and select `c:\users\callum\source\repos\game test`
- In the sidebar (`Ctrl + B` if it isn't visible), press the button that looks like three connected dots with wiggly lines (Source Control), will probably be the third one down, underneath search
- In here, there should be a blank box labelled message, underneath a header that says `game-test`

## Commits And Pushing changes

- Open the `game_test.py` file in VS Code
- Add an extra comment or word or something, then save it (`Ctrl + S`)
- You should see the title turn orange
- Click the Source Control button (the button that looks like three connected dots)
- Then it will list the changes beneath it
- On the line that says `changes`, if you hover over it a plus icon will appear
- Press this and it will change to `Staged Changes`
- In the `Message` box, type a commit message like the following:

```Shell
Testing push from VS Code
```

- Make sure when typing commits you don't spell anything wrong as you can't undo them
- Then press `Commit` and then `Sync Changes` when the button changes
- Go back to GitHub, reload, and the message next to the file will change from `Initial Commit` to `Testing push from VS Code`
- Well done!
- Now if you want to upload changes, simply repeat the [Commits And Pushing changes](#commits-and-pushing-changes) section
