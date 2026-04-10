# README

I've only tested this on macOS 15.5 with OBS 32.1.0 64-bit.  The `capture.py` cleanup also needs `ffmpeg` installed and available in the path.

You also need to set up Profiles, Scene Collections, Scenes, and Sources in a certain way.

Profiles are for data that's capture in OBS->Preferences (Settings) - things like audio/video recording formats and resolution.

Scene Collections are a way to organize separate sets of Source rules in the same profile.

For this project, I set things up like this:

## Profile

The script currently expects the Profile name `dual-screencasts`, and you can make one from the top-level Profiles menu.

## Scene Collection

The script currently expects two named scene Collections - `collection-with-cursor` and `collection-no-cursor`.

## Scene

I left the scene name as the default `Scene`.

## Sources

The `with-cursor` scene needs a source named `with-cursor` that uses the macOS Screen Capture option with **Show cursor** turned **on** in the Properties dialog.

The `no-cursor` scene needs a source named `no-cursor` that uses the macOS Screen Capture option with **Show cursor** turned **off** in the Properties dialog.

## OBS WebSocket Server Settings

You also need to enable OBS' WebSocket Server from the menu OBS -> Tools -> WebSocket Server Settings by checking the **Enable WebSocket server** checkbox.  I believe you only need to do this once before running the scripts in any regular OBS instance.

# Running the scripts

1. `python -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt`
3. First, set up OBS Profiles, Scene Collections, Scenes, and Sources as described above.
4. `python start_instances.py` to open the two OBS instances.  Once they are open you can check if the right sources have loaded and if the settings look OK.
5. `python capture.py` to perform the recording.  Recording locations are currently set to `~/Movies/obs1` and `~/Movies/obs2`.