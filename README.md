# README

I've only tested this on macOS 15.5 with OBS 32.1.0 64-bit.

You also need to set up Profiles, Scene Collections, Scenes, and Sources in a certain way.

Profiles are for data that's capture in OBS->Preferences (Settings) - things like audio/video recording formats and resolution.

Scene Collections are a way to organize separate sets of Source rules in the same profile.

For this project, I set things up like this:

## Profile

The script currently expects the Profile name `dual-screencasts`, and you can make one from the top-level Profiles menu.

## Scene Collection

The script currently expects two named scene Collections - `with-cursor` and `no-cursor`.

## Scene

I left the scene name as the default `Scene`.

## Sources

The `with-cursor` scene needs a source named `with-cursor` that uses the macOS Screen Capture option with **Show cursor** turned **on** in the Properties dialog.

The `no-cursor` scene needs a source named `no-cursor` that uses the macOS Screen Capture option with **Show cursor** turned **off** in the Properties dialog.