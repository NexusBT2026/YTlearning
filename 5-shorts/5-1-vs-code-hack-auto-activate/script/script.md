## SHORT SCRIPT (± 50 sec)

“Quick VS Code hack for Python developers.

If you’re tired of manually activating your Conda environment every time you open VS Code, here’s a simple trick.

Create a file called settings.json inside your .vscode folder, and the copy paste this inside it:

```json
{
  "python.defaultInterpreterPath": "C:\\Users\\YOURNAME\\anaconda3\\envs\\bmad-python\\python.exe",
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "source": "PowerShell",
      "args": ["-NoExit", "-Command", "conda activate bmad-python"]
    }
  }
}
```

Just change your username to what your computer is called and your environment name to what environment you are using.

Now every new terminal in VS Code automatically activates your environment — no more typing conda activate.

I added an example file in the repo and a README section if you want to copy it.

More Python tips coming soon.”